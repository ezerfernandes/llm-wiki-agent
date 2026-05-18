---
title: "Dive into Systems — Ch 8.3 Additional Arithmetic Instructions (IA32)"
type: source
tags: [dive-into-systems, ia32, assembly, arithmetic, mul, div, neg, shift, bitwise, lea, 32-bit]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C8-IA32/arithmetic.html
---

## Summary

[[SuzanneJMatthews|Matthews]] / [[TiaNewhall|Newhall]] / [[KevinCWebb|Webb]]'s **Ch 8.3** of *[[DiveIntoSystems]]* — the **third leaf** of Ch 8 *32-bit IA32 Assembly* and the **32-bit structural twin** of [[dis-7-3-x86-64-arithmetic|Ch 7.3]]. Re-presents the same extended-arithmetic surface — extended integer arithmetic ([[X86NegInstruction|`neg`]] / `inc` / `dec`, [[X86MulInstruction|`imul`]] / `mul`, [[X86DivInstruction|`idiv`]] / `div`), [[X86ShiftInstructions|bit-shift instructions]] (`shl` / `sal` / `shr` / `sar`), [[X86BitwiseInstructions|bitwise logic instructions]] (`and` / `or` / `xor` / `not`), and the [[LeaInstruction|`lea` (load effective address)]] instruction — but at the **[[IA32]] 32-bit register width**. **Headline 32-vs-64 deltas**: (1) operands default to **32-bit (`l`) width** — there is no `q` 64-bit form; (2) the [[X86MulInstruction|`mul` / `imul`]] one-operand form uses the **`%edx:%eax` register pair** (not `%rdx:%rax`) — `%eax` holds the multiplicand, the 64-bit product lands in `%edx:%eax` (high 32 bits in `%edx`, low 32 in `%eax`); (3) the [[X86DivInstruction|`idiv` / `div`]] instruction uses the **`%edx:%eax` pair as the 64-bit dividend** — *"requiring the dividend in `%eax` and storing quotient in `%eax` with remainder in `%edx`"* — and the IA32 dividend-setup idiom is `cltd` (sign-extend `%eax` into `%edx`); (4) the multi-bit-shift count still lives in `%cl` (the bottom byte of `%ecx`) — same convention as [[dis-7-3-x86-64-arithmetic|Ch 7.3]] at the byte-granularity level. The two headline pedagogical points from [[dis-7-3-x86-64-arithmetic|Ch 7.3]] **carry over unchanged**: (a) **`not` ≠ `neg`** — *"the `not` instruction flips the bits but does not add 1"* — pinning the `~x = -x - 1` identity to the IA32 instruction surface; (b) the [[CompilerOptimization|strength-reduction]] *shift-as-multiply* claim — *"to compute `77 * 4`, most compilers will translate this operation to `77 << 2` to avoid the use of an `imul` instruction"*. The [[LeaInstruction|`lea`]] instruction *"performs arithmetic on the operand specified by the source S and places the result in the destination operand D"* without a memory access — same compiler-strength-reduction role as on [[X86_64|x86-64]]. **79th ingested DIS chapter — third leaf of Ch 8.** **No new concept pages** — reuses [[X86MulInstruction]], [[X86DivInstruction]], [[X86NegInstruction]], [[X86ShiftInstructions]], [[X86BitwiseInstructions]], [[LeaInstruction]] from [[dis-7-3-x86-64-arithmetic|Ch 7.3]]; IA32-specific deltas (`%edx:%eax` pair, `cltd` sign-extension idiom, 32-bit operand width) are noted on those concept pages and on the [[IA32]] entity page.

## Key Claims

- **Same extended-arithmetic surface as [[dis-7-3-x86-64-arithmetic|Ch 7.3]] at 32-bit width.** [[X86NegInstruction|`neg`]] / `inc` / `dec`, [[X86MulInstruction|`imul`]] / `mul`, [[X86DivInstruction|`idiv`]] / `div`, [[X86ShiftInstructions|`shl` / `sal` / `shr` / `sar`]], [[X86BitwiseInstructions|`and` / `or` / `xor` / `not`]], and [[LeaInstruction|`lea`]] all apply; only the default operand width (32 vs 64) and the dividend / product register pair (`%edx:%eax` vs `%rdx:%rax`) differ.
- **`%edx:%eax` is the IA32 register pair for [[X86MulInstruction|`mul` / `imul`]] (one-operand form) and [[X86DivInstruction|`div` / `idiv`]].** For multiplication, the 64-bit product of two 32-bit operands lands with high 32 bits in `%edx`, low 32 bits in `%eax`. For division, the 64-bit dividend is read from `%edx:%eax`; the quotient lands in `%eax`, the remainder in `%edx`. The IA32 dividend-setup idiom is `cltd` (sign-extend `%eax` into `%edx`).
- **Shift-as-multiply is the canonical [[CompilerOptimization|compiler optimization]].** *"To compute `77 * 4`, most compilers will translate this operation to `77 << 2` to avoid the use of an `imul` instruction"* — same rule as [[dis-7-3-x86-64-arithmetic|Ch 7.3]]; the shift count still lives in `%cl` (the bottom byte of `%ecx`) for multi-bit shifts.
- **Arithmetic vs logical right shift split survives the ISA change.** [[X86ShiftInstructions|`sar`]] (arithmetic, sign-replicating) and `shr` (logical, zero-filling) are **separate instructions** because the IA32 instruction surface — like x86-64 — does not carry [[SignedInteger|signed]]-vs-[[UnsignedInteger|unsigned]] type information at the operand level; the consumer mnemonic decides.
- **`not` ≠ `neg` — the [[BitwiseOperator|bitwise-NOT]] vs [[TwosComplement|two's-complement-negate]] distinction.** *"The `not` instruction flips the bits but does not add 1"* — pins the `~x = -x - 1` identity to the IA32 instruction surface (same rule as on [[X86_64|x86-64]]).
- **[[LeaInstruction|`lea`]] performs arithmetic without memory access.** *"The `lea` instruction performs arithmetic on the operand specified by the source S and places the result in the destination operand D"* — encodes `D ← B + I*S + C` in one op, used by compilers as a general-arithmetic [[CompilerOptimization|strength-reduction]] shortcut, not just for address calculation. Same role as in [[dis-7-3-x86-64-arithmetic|Ch 7.3]].
- **Readability over premature optimization.** *"Programmers should prioritize code readability whenever possible and avoid premature optimization"* — the compiler does shift-substitution and `lea`-based strength-reduction automatically; hand-rolled bit tricks at C-source level are no longer justified.

## Key Quotes

> "The `lea` instruction performs arithmetic on the operand specified by the source S and places the result in the destination operand D." — `lea` as the no-memory-access arithmetic shortcut at IA32 width.

> "Multiplication and division instructions typically take a long time to execute. Bit shifting offers the compiler a shortcut for multiplicands and divisors that are powers of 2." — motivation for the *shift-as-multiply* [[CompilerOptimization|strength-reduction]] pattern.

> "Programmers should prioritize code readability whenever possible and avoid premature optimization." — the chapter's headline guidance against hand-rolled bit tricks.

## Connections

- [[DiveIntoSystems]] — book; **79th ingested chapter**, third leaf of Ch 8 *32-bit IA32 Assembly*.
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — authors.
- [[dis-8-1-ia32-basics]] — Ch 8.1; supplies the [[IA32]] register set ([[GeneralPurposeRegister|8 GPRs]] — `%eax`/`%ebx`/`%ecx`/`%edx`/`%edi`/`%esi`/`%esp`/`%ebp`) that the `%edx:%eax` mul/div pair sits on.
- [[dis-8-2-ia32-common]] — Ch 8.2; direct predecessor (the `mov` / `add` / `sub` / `push` / `pop` primitives Ch 8.3 extends).
- [[dis-7-3-x86-64-arithmetic]] — **structural twin** at x86-64 width.
- [[IA32]] — the 32-bit ISA whose instruction set Ch 8.3 extends.
- [[X86MulInstruction]] — reused; IA32 delta: 64-bit product lands in `%edx:%eax`.
- [[X86DivInstruction]] — reused; IA32 delta: 64-bit dividend read from `%edx:%eax`, quotient in `%eax`, remainder in `%edx`; `cltd` is the dividend-setup idiom.
- [[X86NegInstruction]] — reused; same `neg` / `inc` / `dec` semantics at 32-bit width.
- [[X86ShiftInstructions]] — reused; same `shl` / `sal` / `shr` / `sar` 2x2 grid; multi-bit count in `%cl`.
- [[X86BitwiseInstructions]] — reused; same `and` / `or` / `xor` / `not` quartet, direct hardware home of the gate-level primitives from [[dis-5-3-gates|Ch 5.3]].
- [[LeaInstruction]] — reused; same address-arithmetic-without-memory-access role.
- [[CompilerOptimization]] — *shift-as-multiply* and `lea`-based strength reduction.
- [[TwosComplement]] — the `~x = -x - 1` identity (`not` vs `neg` split) at IA32 width.
- [[AtAndTSyntax]] — source-first AT&T operand order, same as [[dis-7-3-x86-64-arithmetic|Ch 7.3]].

## Contradictions

None. Ch 8.3 is a **consistent 32-bit re-presentation** of [[dis-7-3-x86-64-arithmetic|Ch 7.3]] — instruction semantics, operand rules, and hidden-operand conventions are structurally identical; only the register-pair width (`%edx:%eax` vs `%rdx:%rax`), default operand suffix (`l` vs `q`), and dividend-setup idiom (`cltd` vs `cqto`) differ.
