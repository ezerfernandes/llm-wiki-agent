---
title: "Dive into Systems — Ch 9.3 Arithmetic Instructions (ARMv8)"
type: source
tags: [assembly, arm64, aarch64, armv8, isa, risc, arithmetic, shift, bitwise, dive-into-systems]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C9-ARM64/arithmetic.html
---

## Summary

Chapter 9.3 *Arithmetic Instructions* is the **third leaf of Ch 9 *64-bit ARM Assembly*** of *[[DiveIntoSystems]]* and the **third-ISA structural sibling** of [[dis-7-3-x86-64-arithmetic|Ch 7.3]] (x86-64) and [[dis-8-3-ia32-arithmetic|Ch 8.3]] (IA32). It extends [[dis-9-2-arm64-common|Ch 9.2]]'s data-movement primitives with the three pure-register instruction families that the [[LoadStoreArchitecture|load/store rule]] reserves for register-only operands: **integer arithmetic** ([[ARM64ArithmeticInstructions|`add` / `sub` / `neg`]], the carry forms `adc` / `sbc` / `ngc`, the multiplication family `mul` / `madd` / `msub` / `mneg`, and division `udiv` / `sdiv`), **bit-shift** ([[ARM64ShiftInstructions|`lsl` / `lsr` / `asr` / `ror`]]), and **bitwise logic** ([[ARM64BitwiseInstructions|`and` / `orr` / `eor` / `mvn`]] plus the inverted-operand composites `bic` / `orn` / `eon`). Two cross-cutting observations distinguish [[ARM64]] from [[X86_64|x86-64]] / [[IA32]] at this surface: (1) the **`s` suffix** (`adds`, `subs`, `ands`, ...) toggles **flag-setting** at the instruction level rather than requiring a separate [[CmpInstruction|`cmp`]] / [[TestInstruction|`test`]] instruction, and (2) [[ARM64]] mints the **composite multiply-accumulate family** (`madd D, O1, O2, O3` → `D = O3 + (O1 × O2)`) and the **inverted-operand bitwise composites** (`bic` = `A & ~B`, `orn` = `A | ~B`, `eon` = `A ^ ~B`) that have **no [[CISC]] analog** — these are [[RISC]]-style three-operand fused instructions that compress common compiler-generated patterns. The chapter closes with the textbook's standard caveat: *"modern compilers automatically optimize arithmetic with bitwise operations when beneficial, so premature optimization in source code is discouraged."*

## Key Claims

- **Three basic arithmetic instructions**: [[ARM64ArithmeticInstructions|`add D, O1, O2`]] (`D = O1 + O2`), [[ARM64ArithmeticInstructions|`sub D, O1, O2`]] (`D = O1 - O2`), [[ARM64ArithmeticInstructions|`neg D, O1`]] (`D = -(O1)`). All three accept **register or immediate** for `O2`; **no memory operand** at this surface per the [[LoadStoreArchitecture|load/store rule]].
- **Carry-variants** for extended-precision arithmetic: [[ARM64ArithmeticInstructions|`adc D, O1, O2`]] (`D = O1 + O2 + C`), [[ARM64ArithmeticInstructions|`sbc D, O1, O2`]] (`D = O1 - O2 - ~C`), [[ARM64ArithmeticInstructions|`ngc D, O1`]] (`D = -(O1) - ~C`). The carry flag `C` is the [[ARM64]] equivalent of [[X86FlagsRegister|x86's CF]]; the *complement* of `C` (`~C`) appears in `sbc` / `ngc` because [[ARM64]]'s subtractor sets `C` as **`borrow == 0`** rather than `borrow == 1`.
- **`s` suffix toggles flag-setting at the instruction level**: `adds` / `subs` / `ands` / etc. set the condition flags (N / Z / C / V) as a side effect, while the bare mnemonic does not. This **inlines** the [[CmpInstruction|`cmp`]] / [[TestInstruction|`test`]]-style flag generation that [[X86_64|x86-64]] and [[IA32]] require as separate instructions — and is the [[ARM64]] mechanism for *flags-as-needed* without polluting every arithmetic op with flag updates.
- **Multiplication and division**: [[ARM64ArithmeticInstructions|`mul D, O1, O2`]] (`D = O1 × O2`), [[ARM64ArithmeticInstructions|`udiv D, O1, O2`]] (unsigned, 32-bit width), [[ARM64ArithmeticInstructions|`sdiv D, O1, O2`]] (signed, 64-bit width). **No hidden `%rax` / `%rdx` operands** as in [[X86MulInstruction|x86 `imul`]] / [[X86DivInstruction|x86 `idiv`]] — all operands are explicit, in keeping with [[RISC]] regular form.
- **Composite multiply-accumulate family**: [[ARM64ArithmeticInstructions|`madd D, O1, O2, O3`]] (`D = O3 + (O1 × O2)`), [[ARM64ArithmeticInstructions|`msub D, O1, O2, O3`]] (`D = O3 - (O1 × O2)`), [[ARM64ArithmeticInstructions|`mneg D, O1, O2`]] (`D = -(O1 × O2)`). These **four-operand fused instructions** compress common compiler-generated patterns (loop accumulators, dot products) — a [[RISC]] feature with **no direct [[CISC]] equivalent** at this surface.
- **Four bit-shift instructions**: [[ARM64ShiftInstructions|`lsl D, R, #v`]] (logical/arithmetic left shift — same for both), [[ARM64ShiftInstructions|`lsr D, R, #v`]] (logical right shift — zero-fill upper bits), [[ARM64ShiftInstructions|`asr D, R, #v`]] (arithmetic right shift — sign-extend upper bits — preserves signedness for negative values), [[ARM64ShiftInstructions|`ror D, R, #v`]] (rotate right — wrap low bits to high positions, no fill). The shift value `v` is a **6-bit constant** (range `0`–`63` on 64-bit ops) or a register operand.
- **Four basic bitwise instructions**: [[ARM64BitwiseInstructions|`and D, O1, O2`]] (`D = O1 & O2`), [[ARM64BitwiseInstructions|`orr D, O1, O2`]] (`D = O1 | O2` — **note the doubled `r`** distinguishing from a hypothetical `or` that does not exist on [[ARM64]]), [[ARM64BitwiseInstructions|`eor D, O1, O2`]] (`D = O1 ^ O2` — *exclusive or* in [[ARM64]] vocabulary; [[X86BitwiseInstructions|x86 calls it `xor`]]), [[ARM64BitwiseInstructions|`mvn D, O`]] (bitwise NOT — *"flips bits without adding 1"*; structurally analogous to [[X86_64|x86-64]] `not`, *not* `neg` which is the arithmetic negation).
- **Inverted-operand bitwise composites**: [[ARM64BitwiseInstructions|`bic D, O1, O2`]] (`D = O1 & ~O2` — *"bit clear"*; useful for masking off bits without a separate `mvn` instruction), [[ARM64BitwiseInstructions|`orn D, O1, O2`]] (`D = O1 | ~O2`), [[ARM64BitwiseInstructions|`eon D, O1, O2`]] (`D = O1 ^ ~O2`). These three are **[[ARM64]]-specific composites** with no [[CISC]] equivalent — they compress the very common `mask & ~clear_bits` pattern into a single instruction.
- **Cross-cutting compiler-optimization caveat**: *"modern compilers automatically optimize arithmetic with bitwise operations when beneficial, so premature optimization in source code is discouraged."* Restates the canonical [[DiveIntoSystems]] anti-premature-optimization claim — first seen as the `77 * 4` → `77 << 2` example in [[dis-7-3-x86-64-arithmetic|Ch 7.3]]; the [[ARM64]] equivalent is the same shift-instead-of-multiply substitution carried out by the compiler.

## Key Quotes

> "Modern compilers automatically optimize arithmetic with bitwise operations when beneficial, so premature optimization in source code is discouraged." — the canonical [[DiveIntoSystems]] anti-premature-optimization restatement; appears across all three per-ISA chapters.

> "An optional `s` suffix (like `adds`) indicates the operation sets condition flags." — the **single most ISA-distinctive feature** of [[ARM64]] arithmetic at the surface: flag-setting is **opt-in per-instruction** rather than tied to specific [[CmpInstruction|comparison]] / [[TestInstruction|test]] mnemonics.

## Connections

- [[DiveIntoSystems]] — the host textbook; this is its **93rd ingested chapter** and the **third leaf of Ch 9 *64-bit ARM Assembly***.
- [[dis-9-1-arm64-basics]] — established the [[LoadStoreArchitecture|load/store rule]] that confines arithmetic to register operands.
- [[dis-9-2-arm64-common]] — **prior sibling at Ch 9.2**; delivered the data-movement instructions that move operands into the registers Ch 9.3 then operates on.
- [[dis-7-3-x86-64-arithmetic]] — **non-twin structural sibling at Ch 7.3** (x86-64). Same instruction-family taxonomy (arithmetic / shift / bitwise), **structurally distinct** at every individual instruction (no `madd` / `bic` / `orn` / `eon` on x86-64; no `s`-suffix flag-toggle; explicit operands on `mul` / `div` rather than hidden `%rax` / `%rdx`).
- [[dis-8-3-ia32-arithmetic]] — **non-twin structural sibling at Ch 8.3** (IA32 32-bit). Same observations.
- [[ARM64ArithmeticInstructions]] — **minted** by this ingest; covers `add` / `sub` / `neg` / `adc` / `sbc` / `ngc` / `mul` / `madd` / `msub` / `mneg` / `udiv` / `sdiv`.
- [[ARM64ShiftInstructions]] — **minted** by this ingest; covers `lsl` / `lsr` / `asr` / `ror`.
- [[ARM64BitwiseInstructions]] — **minted** by this ingest; covers `and` / `orr` / `eor` / `mvn` / `bic` / `orn` / `eon`.
- [[ARM64]] — extended concept; this ingest fills in the arithmetic / shift / bitwise instruction tables.
- [[LoadStoreArchitecture]] — restated; all Ch 9.3 instructions are **register-only**, consistent with the load/store discipline.
- [[X86ArithmeticInstructions]] — contrasting [[CISC]] family.
- [[X86MulInstruction]] / [[X86DivInstruction]] — contrasting hidden-operand multiplication / division; [[ARM64]] uses fully explicit operands.
- [[X86ShiftInstructions]] — contrasting shift family; [[ARM64]] adds `ror` (rotate) as a peer of the three shift forms.
- [[X86BitwiseInstructions]] — contrasting bitwise family; [[ARM64]] uses `eor` (where [[X86_64|x86]] uses `xor`), and adds the three inverted-operand composites `bic` / `orn` / `eon`.
- [[X86FlagsRegister]] — contrasting condition-code architecture; [[ARM64]] uses an analogous N / Z / C / V flag set, but **opt-in per instruction** via the `s` suffix.
- [[CmpInstruction]] / [[TestInstruction]] — the [[X86_64|x86-64]] mechanism for separating flag-generation from value-production; the [[ARM64]] `s`-suffix mechanism is an **alternative answer** to the same flag-management question.
- [[AssemblyLanguage]] — umbrella concept.

## Contradictions

None. Ch 9.3 introduces a **third instruction-family vocabulary** distinct from [[dis-7-3-x86-64-arithmetic|Ch 7.3]] and [[dis-8-3-ia32-arithmetic|Ch 8.3]] but consistent with the wiki's [[ISA]] / [[RISC]] / [[CISC]] framing. The [[ARM64]] `s`-suffix flag-toggle and the [[X86_64|x86-64]] dedicated `cmp` / `test` instructions are **alternative ISA-design answers** to the same *flag-generation when needed* question, both fully described.
