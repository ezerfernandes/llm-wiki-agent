---
title: "Dive into Systems — Ch 9.4.1 Preliminaries (ARM64 Conditional Control)"
type: source
tags: [book, dive-into-systems, arm64, armv8, assembly, control-flow, condition-codes, flags, nzcv]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C9-ARM64/preliminaries.html
sources: []
last_updated: 2026-05-17
---

## Summary

**First leaf** of [[dis-9-4-arm64-conditional-loops|Ch 9.4]] of *[[DiveIntoSystems]]*. Introduces the four mechanisms every conditional construct at the [[ARM64|AArch64]] assembly level rests on: the **[[ARM64FlagsRegister|NZCV condition-flag register]]** (the ALU side-channel that records *what just happened* — N / Z / C / V stored in the `PSTATE` processor-state register), the **[[ARM64Cmp|comparison instructions `cmp` / `cmn` / `tst`]]** (set flags **without writing a destination**), the **[[ARM64ConditionalBranch|`b.cond` conditional-branch family]]** (`b.eq` / `b.ne` / `b.lt` / `b.gt` / `b.le` / `b.ge` / `b.hi` / `b.lo` / ...), and the **[[ARM64ConditionalSelect|`csel` conditional-select instruction]]** (branch-free data conditional, the [[ARM64]] analog of [[X86ConditionalMove|x86 `cmov`]]). Together they encode [[CLanguage|C]]'s comparison operators (`==` / `!=` / `<` / `<=` / `>` / `>=`) into branch-driven [[ARM64]] [[AssemblyLanguage|assembly]]. **95th ingested DIS chapter — first leaf of Ch 9.4.**

## Key Claims

- **The NZCV register stores four single-bit ALU side-effects** as part of `PSTATE` (the [[ARM64]] processor-state register): **N (Negative)** = result is negative (MSB = 1 under [[TwosComplement|two's complement]]); **Z (Zero)** = result equals 0; **C (Carry)** = unsigned-arithmetic carry-out / borrow-out of the MSB; **V (Overflow)** = signed-integer overflow. **Structural analog** of [[X86FlagsRegister|x86 FLAGS]]'s ZF/SF/OF/CF — same four ALU side-effects, different register layout and naming convention.
- **Flag-setting is opt-in via the `s` suffix.** Per [[dis-9-3-arm64-arithmetic|Ch 9.3]]'s headline rule, ordinary [[ARM64]] arithmetic does **not** modify flags — only the **`s`-suffixed variants** (`adds` / `subs` / `ands`) update NZCV. The [[ARM64Cmp|`cmp` / `cmn` / `tst`]] instructions are the **flag-only siblings** (their entire purpose is to set NZCV — they discard the arithmetic result).
- **`cmp O1, O2` subtracts O2 from O1** to set flags — *"the `cmp` instruction subtracts O2 from O1"* — without modifying either register. **`cmn` (compare negative)** adds instead (useful for comparing against a negative immediate without rewriting it). **`tst R1, R2`** performs bitwise AND for similar purposes; the canonical idiom is **`tst x0, x0`** which tests whether `x0` is zero (`x AND x = 0` iff `x = 0`).
- **Condition codes are mnemonic suffixes** consumed by `b.cond` / `csel` / `cset` etc.: **`eq`** (equal — Z=1), **`ne`** (not equal — Z=0), **`lt` / `le` / `gt` / `ge`** (signed less / less-or-equal / greater / greater-or-equal — consume N + V), **`lo` / `ls` / `hi` / `hs`** (unsigned lower / lower-or-same / higher / higher-or-same — consume C). The signed/unsigned split is **encoded in the suffix**, not in the comparison that preceded it — the same `cmp` instruction sets all four flags, and the consumer chooses interpretation.
- **`b.cond` has a limited range.** *"Conditional branch instructions have a much more limited range (1 MB) than the `b` instruction."* The compiler uses a **conditional branch + unconditional `b`** chain for long-distance conditional jumps.

## Key Quotes

> "The `cmp` instruction subtracts O2 from O1" — sets NZCV without modifying either operand.

> "A common usage of the `tst` instruction is to test whether a register value is 0."

> "Conditional branch instructions have a much more limited range (1 MB) than the `b` instruction."

## Connections

- [[DiveIntoSystems]] — host textbook; this is Ch 9.4.1, the **first leaf of [[dis-9-4-arm64-conditional-loops|Ch 9.4]]**.
- [[ARM64FlagsRegister]] — the NZCV condition-flag register inside `PSTATE`.
- [[ARM64Cmp]] — the flag-only `cmp` / `cmn` / `tst` family.
- [[ARM64ConditionalBranch]] — the `b.cond` family that consumes NZCV.
- [[ARM64ConditionalSelect]] — the `csel` branch-free data conditional.
- [[dis-7-4-1-x86-64-preliminaries]] / [[dis-8-4-1-ia32-preliminaries]] — structural siblings (non-twins) — same three-mechanism scaffolding ([[X86FlagsRegister|FLAGS]] + [[CmpInstruction|`cmp`/`test`]] + [[X86JumpInstructions|`jXX`]]) on a different ISA.
- [[dis-9-3-arm64-arithmetic]] — where the `s`-suffix flag-setting opt-in was introduced.
- [[ARM64]] / [[ControlFlow]] / [[ConditionCode]] / [[TwosComplement]] — supporting concepts.

## Contradictions

None. Ch 9.4.1 introduces a **structurally distinct flag-register scheme** ([[ARM64FlagsRegister|NZCV]] vs [[X86FlagsRegister|FLAGS]]) rather than revising prior claims — alternative ISA-design answer.
