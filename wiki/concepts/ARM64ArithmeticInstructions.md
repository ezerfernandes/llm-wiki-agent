---
title: "ARM64 Arithmetic Instructions"
type: concept
tags: [arm64, aarch64, assembly, arithmetic, add, sub, mul, div, neg, madd, risc]
sources: [dis-9-3-arm64-arithmetic]
last_updated: 2026-05-17
---

# ARM64 Arithmetic Instructions

The **arithmetic instruction family** on [[ARM64]] operates **exclusively on registers and immediate constants** per the [[LoadStoreArchitecture|load/store rule]] from [[dis-9-1-arm64-basics|Ch 9.1]]. Per [[dis-9-3-arm64-arithmetic|Ch 9.3]] it splits into **three sub-families**: basic three-operand arithmetic (`add` / `sub` / `neg`), **carry-variant** instructions for extended-precision arithmetic (`adc` / `sbc` / `ngc`), and the **multiplication / division** family including the composite multiply-accumulate operations.

## Basic arithmetic

| Instruction | Effect |
|---|---|
| `add D, O1, O2` | `D = O1 + O2` |
| `sub D, O1, O2` | `D = O1 - O2` |
| `neg D, O1` | `D = -(O1)` — arithmetic negation (two's-complement) |

`O2` may be a register or an `#imm` immediate; `O1` and `D` are registers.

## Carry variants (extended-precision)

| Instruction | Effect |
|---|---|
| `adc D, O1, O2` | `D = O1 + O2 + C` |
| `sbc D, O1, O2` | `D = O1 - O2 - ~C` |
| `ngc D, O1` | `D = -(O1) - ~C` |

`C` is the carry flag in the condition-flag register. The complement (`~C`) appears in subtraction-derived variants because [[ARM64]] sets `C` as **`borrow == 0`** rather than `borrow == 1`.

## The `s` suffix — opt-in flag-setting

Appending `s` to any of these mnemonics (`adds`, `subs`, `negs`, `adcs`, `sbcs`, `ngcs`) makes the instruction **set the condition flags** (N / Z / C / V) as a side effect. Without the suffix, the instruction does **not** touch the flags.

This is the **single most ISA-distinctive feature** of [[ARM64]] arithmetic relative to [[X86_64|x86-64]] / [[IA32]]: where x86 requires a separate [[CmpInstruction|`cmp`]] / [[TestInstruction|`test`]] instruction to generate flags, [[ARM64]] folds it into the **same instruction** that produces the value — at the option of the assembler / compiler.

## Multiplication

| Instruction | Effect |
|---|---|
| `mul D, O1, O2` | `D = O1 × O2` |
| `madd D, O1, O2, O3` | `D = O3 + (O1 × O2)` — fused multiply-accumulate |
| `msub D, O1, O2, O3` | `D = O3 - (O1 × O2)` — fused multiply-subtract |
| `mneg D, O1, O2` | `D = -(O1 × O2)` — multiply-negate |

**No hidden operands.** Contrast [[X86MulInstruction|x86-64 `imul`]] which uses `%rax` / `%rdx` as the implicit destination. [[ARM64]] keeps every operand explicit — the [[RISC]] discipline of *fully visible operand state*.

`madd` / `msub` are **four-operand fused instructions** with **no [[CISC]] equivalent**. They compress loop accumulators, dot products, and address calculations into a single instruction.

## Division

| Instruction | Effect |
|---|---|
| `udiv D, O1, O2` | `D = O1 / O2` — **unsigned** division |
| `sdiv D, O1, O2` | `D = O1 / O2` — **signed** division |

Again **no hidden operands** (contrast [[X86DivInstruction|x86 `idiv`]] which reads dividend from `%rdx:%rax` and writes quotient to `%rax`, remainder to `%rdx`). To compute the remainder on [[ARM64]], use the `msub` composite: `udiv q, a, b ; msub r, q, b, a` yields `r = a - (q × b) = a mod b`.

## Worked example — `adder2`'s addition step

Per [[dis-9-1-arm64-basics|Ch 9.1]] and [[dis-9-3-arm64-arithmetic|Ch 9.3]]:

```
add w0, w0, #0x2
```

Three-operand destination-first form: `D = w0`, `O1 = w0`, `O2 = #0x2`. The structural opposite of [[X86_64]]'s `addl $0x2, %eax` (AT&T two-operand, source-first).

## Connections

- [[dis-9-3-arm64-arithmetic]] — promoting source; lists the full instruction set.
- [[ARM64]] — the [[ISA]].
- [[LoadStoreArchitecture]] — the policy that confines these instructions to register operands.
- [[X86ArithmeticInstructions]] — the contrasting [[CISC]] family.
- [[X86MulInstruction]] — contrasting hidden-operand multiplication.
- [[X86DivInstruction]] — contrasting hidden-operand division.
- [[X86NegInstruction]] — contrasting [[CISC]] negation.
- [[X86FlagsRegister]] — the [[CISC]] condition-flag register; [[ARM64]] has the analogous N / Z / C / V flags, set by the **`s`-suffixed** instructions only.
- [[CmpInstruction]] / [[TestInstruction]] — the [[X86_64|x86-64]] mechanism for separating flag-generation from value-production. [[ARM64]] uses the `s`-suffix instead.
- [[TwosComplement]] — the underlying signed-integer encoding; `neg` and `sdiv` interpret operands in two's-complement.
- [[ARM64ShiftInstructions]] — sibling family.
- [[ARM64BitwiseInstructions]] — sibling family.
- [[AssemblyLanguage]] — umbrella concept.
