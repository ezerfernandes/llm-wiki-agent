---
title: "ARM64 Bitwise Instructions"
type: concept
tags: [arm64, aarch64, assembly, bitwise, and, orr, eor, mvn, bic, orn, eon]
sources: [dis-9-3-arm64-arithmetic]
last_updated: 2026-05-17
---

# ARM64 Bitwise Instructions

The **bitwise instruction family** on [[ARM64]] consists of **four basic instructions** plus **three inverted-operand composites** per [[dis-9-3-arm64-arithmetic|Ch 9.3]]. Like all [[ARM64]] computational instructions, these operate **only on registers and immediates** per the [[LoadStoreArchitecture|load/store rule]].

## Basic bitwise instructions

| Instruction | Effect | x86 equivalent |
|---|---|---|
| `and D, O1, O2` | `D = O1 & O2` | `andq` |
| `orr D, O1, O2` | `D = O1 \| O2` | `orq` |
| `eor D, O1, O2` | `D = O1 ^ O2` — *exclusive or* | `xorq` |
| `mvn D, O` | `D = ~O` — bitwise NOT | `notq` |

Two **naming differences** distinguish [[ARM64]] from [[X86_64|x86]]:

- **`orr`** has a doubled `r` (no `or` mnemonic on [[ARM64]] — historically reserved at the encoding level).
- **`eor`** is *exclusive or* — [[ARM64]]'s vocabulary; [[X86_64|x86]] calls the same operation `xor`.

## `mvn` vs `neg`

[[dis-9-3-arm64-arithmetic|Ch 9.3]] makes the distinction explicit: `mvn` performs **bitwise NOT** (*"flips bits without adding 1"*) — it is the [[ARM64]] equivalent of [[X86_64]]'s `not`. The arithmetic negation `-x` is [[ARM64ArithmeticInstructions|`neg`]] (= `not + 1`), which is the equivalent of [[X86_64]]'s `neg`. Confusing the two yields off-by-one errors at the bit-pattern level.

## Inverted-operand composites — `bic` / `orn` / `eon`

| Instruction | Effect |
|---|---|
| `bic D, O1, O2` | `D = O1 & ~O2` — *bit clear*: mask off bits set in `O2` |
| `orn D, O1, O2` | `D = O1 \| ~O2` — OR with NOT-of-`O2` |
| `eon D, O1, O2` | `D = O1 ^ ~O2` — XOR with NOT-of-`O2` |

These three are **[[ARM64]]-specific composites** with **no [[CISC]] equivalent**. They compress the common `mask & ~clear_bits` and `value | ~mask` patterns into a single instruction — for example, **clearing the low 4 bits** of a register on [[X86_64]] requires `and $0xFFFFFFFFFFFFFFF0, %rax` (two instructions if the mask needs loading from immediate); on [[ARM64]] it is `bic x0, x0, #0xF`.

## The `s` suffix

`ands` sets the condition flags (N / Z) as a side effect — the bitwise analog of [[ARM64ArithmeticInstructions|`adds` / `subs`]]. This **inlines** the [[TestInstruction|`test`]] instruction that [[X86_64|x86-64]] requires as a separate operation, and is the standard idiom for *test-if-zero* / *test-if-bit-set* compound checks. `mvn` does not have an `s` variant (no flags meaningfully set by bitwise inversion in isolation); `orr` / `eor` likewise lack `s` variants at the user-mode surface.

## Connections

- [[dis-9-3-arm64-arithmetic]] — promoting source.
- [[ARM64]] — the [[ISA]].
- [[LoadStoreArchitecture]] — the rule that confines these to register operands.
- [[ARM64ArithmeticInstructions]] — sibling family; `neg` (arithmetic negation) is the close cousin of `mvn` (bitwise NOT).
- [[ARM64ShiftInstructions]] — sibling family.
- [[X86BitwiseInstructions]] — contrasting [[CISC]] family; [[ARM64]] adds the three inverted-operand composites (`bic` / `orn` / `eon`) and uses different mnemonic spellings (`orr` / `eor` vs `or` / `xor`).
- [[TestInstruction]] — the [[X86_64|x86-64]] flag-only-AND equivalent; [[ARM64]] uses `ands` instead.
- [[BitwiseOperator]] — the cross-ISA concept; [[ARM64]] is the [[RISC]] instance.
- [[AssemblyLanguage]] — umbrella concept.
