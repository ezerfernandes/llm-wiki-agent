---
title: "Dive into Systems — Ch 7.3 Additional Arithmetic Instructions (x86-64)"
type: source
tags: [dive-into-systems, x86-64, assembly, arithmetic, bitwise, shift, lea]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C7-x86_64/arithmetic.html
sources: []
last_updated: 2026-05-17
---

## Summary

Chapter 7.3 of *[[DiveIntoSystems]]* — **third leaf** of Ch 7 *x86-64 Assembly*, follows [[dis-7-2-x86-64-common|Ch 7.2]]'s data-movement / stack / `add`-`sub` primitives. **Expands the [[X86_64|x86-64]] arithmetic surface** with three new instruction families — **extended integer arithmetic** ([[X86NegInstruction|`neg`]], [[X86IncDecInstructions|`inc` / `dec`]], [[X86MulInstruction|`imul`]], [[X86DivInstruction|`idiv`]]), **[[X86ShiftInstructions|bit-shift instructions]]** (`shl` / `sal` / `shr` / `sar`), and **[[X86BitwiseInstructions|bitwise logic instructions]]** (`and` / `or` / `xor` / `not`) — plus the **[[LeaInstruction|`lea` (load effective address)]] instruction**, the [[dis-7-2-x86-64-common|Ch 7.2]] forward-reference now delivered. The two headline pedagogical points: the `idiv` / multi-bit-shift hidden-operand conventions (`%rax` dividend, `%cl` shift count), and `lea` as an **address-arithmetic instruction that performs no memory access** — exploited by compilers as a multi-operation arithmetic shortcut.

## Key Claims

- **Six arithmetic primitives** beyond [[X86ArithmeticInstructions|`add` / `sub`]]: `inc D` (`D ← D + 1`), `dec D` (`D ← D − 1`), `neg D` (`D ← −D` — full [[TwosComplement|two's-complement]] negation), `imul S, D` (`D ← S × D` — *"truncates the result to 64 bits in the case of overflow"*), `idiv S` (signed integer division — `%rax / S` → quotient in `%rax`, remainder in `%rdx`).
- **`idiv`'s hidden-operand convention**: *"prior to the execution of the `idiv` instruction, it is assumed that register `%rax` contains the dividend."* Single explicit operand `S` is the divisor; the two implicit operands are `%rax` (dividend, also written as the quotient destination) and `%rdx` (remainder destination). Pattern conflicts with the otherwise uniform two-explicit-operand structure of the rest of the arithmetic instructions — caller must set up `%rax` (and typically `%rdx`) before `idiv`.
- **Four [[X86ShiftInstructions|bit-shift instructions]]** split along two axes — **direction** (left vs right) × **arithmetic vs logical** (signed-preserving vs unsigned-zero-fill): `sal v, D` and `shl v, D` (left shifts — `D ← D << v` — *arithmetic left shift = logical left shift* since the low-bit fill is `0` either way), `sar v, D` (arithmetic right shift — `D ← D >> v` with [[SignExtension|sign-bit replication]] for signed integers), `shr v, D` (logical right shift — `D ← D >> v` with zero-fill for unsigned integers).
- **Shift-count constraint**: *"the shift value `v` must either be a constant or stored in register `%cl`"* — `%cl` is the low byte of `%rcx`. Second hidden-operand convention in the chapter (after `idiv`'s `%rax`/`%rdx`) — both leverage specific GPRs for instruction-specific operands.
- **[[CompilerOptimization|Compiler-optimization]] payoff for shifts**: *"to compute `77 * 4`, most compilers will translate this operation to `77 << 2` to avoid the use of an `imul` instruction"* — the *[[BitShift|shift-as-multiply-by-power-of-two]]* [[dis-4-6-bitwise|Ch 4.6]] flagged at the C level now resurfaces as a [[CompilerOptimization|strength-reduction]] move at the assembly level. Shifts execute in fewer cycles than `imul` on most microarchitectures.
- **Four [[X86BitwiseInstructions|bitwise logic instructions]]**: `and S, D` (`D ← S & D`), `or S, D` (`D ← S | D`), `xor S, D` (`D ← S ^ D`), `not D` (`D ← ~D` — single operand). These map one-to-one onto the [[BitwiseOperator|C bitwise operators]] [[dis-4-6-bitwise|Ch 4.6]] codified.
- **`not` ≠ `neg` — the canonical confusion**: *"remember that bitwise `not` is distinct from negation (`neg`). The `not` instruction flips the bits but does not add 1."* The wiki's central [[TwosComplement|two's-complement]] negation recipe (*"flip all the bits and add one"* — [[dis-4-3-signed|Ch 4.3]]) splits across exactly these two instructions: `not` does the flip; only `neg` does the flip-and-add-one. Hence `~x = -x - 1` at the bit-pattern level — the [[BitwiseNot|`~` identity]] [[dis-4-6-bitwise|Ch 4.6]] supplied at the C level.
- **[[LeaInstruction|Load-effective-address (`lea`)]] — the headline new instruction**: `lea S, D` computes the address that the [[X86AddressingMode|addressing-mode expression]] `S` would resolve to, and writes that **computed address** into `D` — **without** actually accessing memory at that address. Functionally identical to [[X86MovInstruction|`mov`]] **except** for the memory-access semantics: `mov 8(%rax), %rax` reads 8 bytes from address `%rax + 8`; `lea 8(%rax), %rax` writes `%rax + 8` itself into `%rax`. *"The `lea` instruction performs the same (sometimes complicated) operand arithmetic without the memory lookup."*
- **`lea`'s compiler use is arithmetic, not addressing**: because the [[X86AddressingMode|`disp(base, index, scale)`]] expression evaluates `disp + base + index*scale` in one instruction, `lea` is a **three-operand arithmetic instruction in disguise** — it can encode `D ← B + I*S + C` with a single fast instruction, replacing what would otherwise be a sequence of `mov` + `add` + `imul` / `shl`. Five worked examples cover the full operand-form space: `lea 8(%rax), %rax` (add constant), `lea (%rax, %rdx), %rax` (add two registers), `lea (, %rax, 4), %rax` (multiply by power of two via `scale`), `lea -0x8(%rcx), %rax` (subtract constant — using negative displacement), `lea -0x4(%rcx, %rdx, 2), %rax` (full form — `%rcx + %rdx*2 - 4`).

## Key Quotes

> "Prior to the execution of the `idiv` instruction, it is assumed that register `%rax` contains the dividend." — formal statement of `idiv`'s hidden-operand convention; the dividend / divisor / quotient / remainder discipline that distinguishes integer division from the symmetric `add`/`sub`/`imul` instructions.

> "The shift value `v` must either be a constant or stored in register `%cl`." — the shift-count constraint; ties [[X86ShiftInstructions|all four bit-shift instructions]] to `%cl` (low byte of `%rcx`) as the canonical variable-shift register.

> "To compute `77 * 4`, most compilers will translate this operation to `77 << 2` to avoid the use of an `imul` instruction." — the explicit compiler-shortcut quote that turns [[BitShift|bit-shift]] into the canonical [[CompilerOptimization|strength-reduction]] for power-of-two multiplication.

> "Remember that bitwise `not` is distinct from negation (`neg`). The `not` instruction flips the bits but does not add 1." — the surgical clarification of the `not` vs `neg` boundary; pin-codes the `~x = -x - 1` identity from [[dis-4-6-bitwise|Ch 4.6]] into the assembly-level instruction surface.

> "The `lea` instruction performs the same (sometimes complicated) operand arithmetic without the memory lookup." — the headline `lea` semantic distinction from [[X86MovInstruction|`mov`]] — the no-memory-access property that turns address arithmetic into general arithmetic.

## Worked Examples (LEA)

Assume initial register state `%rax = 0x5`, `%rdx = 0x4`, `%rcx = 0x808`. Each row shows the [[X86AddressingMode|addressing-mode]] expansion and the result that `lea` writes into `%rax`:

| Instruction | Computed expression | Result |
|---|---|---|
| `lea 8(%rax), %rax` | `8 + %rax` | `0x5 + 8 = 13` |
| `lea (%rax, %rdx), %rax` | `%rax + %rdx` | `0x5 + 0x4 = 9` |
| `lea (, %rax, 4), %rax` | `%rax * 4` | `0x5 * 4 = 20` |
| `lea -0x8(%rcx), %rax` | `%rcx - 8` | `0x808 - 8 = 0x800` |
| `lea -0x4(%rcx, %rdx, 2), %rax` | `%rcx + %rdx*2 - 4` | `0x808 + 0x4*2 - 4 = 0x80c` |

## Connections

- [[DiveIntoSystems]] — the parent textbook; this is the **65th ingested chapter**.
- [[dis-7-2-x86-64-common]] — immediate predecessor; the [[X86MovInstruction|`mov`]] + [[X86ArithmeticInstructions|`add` / `sub`]] + [[X86StackInstructions|`push` / `pop`]] primitives Ch 7.3 extends. [[LeaInstruction|`lea`]] is **the deferred instruction** Ch 7.2 flagged.
- [[dis-7-1-x86-64-basics]] — [[X86AddressingMode|addressing-mode]] / [[OperandSize|operand-size]] / [[AtAndTSyntax|AT&T syntax]] framework that constrains every instruction in this chapter.
- [[X86_64]] — the ISA; **16 new instructions** added to its wiki-cataloged surface.
- [[X86MulInstruction]] — new — `imul S, D` (signed multiplication; truncates to 64 bits on overflow).
- [[X86DivInstruction]] — new — `idiv S` (signed division; `%rax` dividend / `%rdx` remainder hidden-operand convention).
- [[X86NegInstruction]] — new — bundles `neg D` (two's-complement negation) with `inc D` / `dec D` (the two single-operand arithmetic shortcuts).
- [[X86ShiftInstructions]] — new — bundles `shl` / `sal` / `shr` / `sar` (left / right × arithmetic / logical).
- [[X86BitwiseInstructions]] — new — bundles `and` / `or` / `xor` / `not` (the assembly-level [[BitwiseOperator|bitwise-operator]] surface).
- [[LeaInstruction]] — new — **promoted from forward-reference to first-class concept**; the address-arithmetic-without-memory-access instruction.
- [[dis-4-3-signed]] — the [[TwosComplement|two's-complement]] / [[SignExtension|sign-extension]] foundations behind `neg` and `sar`.
- [[dis-4-4-3-mult-div]] — the [[BinaryMultiplication|multiplication]] / [[BinaryDivision|division]] algorithms behind `imul` / `idiv`.
- [[dis-4-6-bitwise]] — the [[BitwiseOperator|C bitwise operators]] and [[BitShift|shifts]] that map one-to-one onto Ch 7.3's `and`/`or`/`xor`/`not` and `shl`/`sar`/`shr`/`sal`.
- [[CompilerOptimization]] — the *shift-as-power-of-two-multiply* and `lea`-as-multi-op-arithmetic patterns are canonical [[CompilerOptimization|strength-reduction]] moves.

## Contradictions

None. Ch 7.3 **extends** rather than revises prior wiki content — it delivers the [[LeaInstruction|`lea`]] forward reference [[dis-7-2-x86-64-common|Ch 7.2]] flagged, instantiates the [[dis-4-6-bitwise|Ch 4.6]] [[BitwiseOperator|C bitwise operators]] at the assembly level, and operationalizes the [[dis-4-4-3-mult-div|Ch 4.4.3]] integer multiplication / division algorithms as named ISA instructions.
