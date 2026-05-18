---
title: "ARM64 cmp / cmn / tst (Flag-Only Comparison)"
type: concept
tags: [arm64, armv8, assembly, comparison, flags, condition-codes, cmp, cmn, tst]
sources: [dis-9-4-1-arm64-preliminaries]
last_updated: 2026-05-17
---

# ARM64 Comparison Instructions

The **`cmp` / `cmn` / `tst`** instruction family is the [[ARM64|AArch64]] **flag-only** comparison family — each one performs an arithmetic / logical operation **purely to set the [[ARM64FlagsRegister|NZCV flags]]** and discards the result. They are the [[ARM64]] analogs of [[CmpInstruction|x86 `cmp`]] / [[TestInstruction|x86 `test`]] and the dedicated comparison vocabulary that [[ARM64ConditionalBranch|`b.cond`]] and [[ARM64ConditionalSelect|`csel`]] consume. Per [[dis-9-4-1-arm64-preliminaries|Ch 9.4.1 of *[[DiveIntoSystems]]*]].

## The three instructions

- **`cmp O1, O2`** — *subtracts O2 from O1* and sets NZCV based on the result. Equivalent to **`subs xzr, O1, O2`** (write the result to the zero register `xzr`, discarding it). *"The `cmp` instruction subtracts O2 from O1"* without modifying either operand.
- **`cmn O1, O2`** — **compare negative**: *adds O1 + O2* and sets NZCV. Equivalent to **`adds xzr, O1, O2`**. Useful for comparing against a negative immediate without rewriting the constant (`cmn x0, #1` tests `x0 == -1`).
- **`tst O1, O2`** — **test**: bitwise `O1 AND O2` and sets NZCV. Equivalent to **`ands xzr, O1, O2`**. The canonical idiom is **`tst x0, x0`** (or `tst w0, w0`) which tests whether the register equals zero — `x AND x = 0` iff `x = 0`, so the Z flag becomes a direct zero-test.

## Operand-order convention

[[ARM64]]'s **destination-first** operand order from [[dis-9-1-arm64-basics|Ch 9.1]] is preserved — but the comparison family has **no destination** (the discard slot is implicit `xzr`), so the operand order reads **naturally left-to-right**: `cmp x0, x1` evaluates `x0 - x1` (read as *compare x0 against x1*). Contrast [[CmpInstruction|x86 AT&T `cmp`]] which evaluates `src2 - src1` because of the [[AtAndTSyntax|AT&T source-first quirk]].

## Operand types

- `cmp xN, xM` / `cmp xN, #imm` — register-register or register-immediate (12-bit immediate; larger requires a `mov` first).
- `cmp xN, xM, LSL #s` / `cmp xN, xM, ASR #s` / ... — second operand can have an **inline shift** baked in, no separate shift instruction needed.
- Same operand variants apply to `cmn` and `tst`.

## What each flag means after `cmp O1, O2`

Per [[dis-9-4-1-arm64-preliminaries|Ch 9.4.1]] (`cmp` = `O1 - O2`):

- **Z == 1** → operands are **equal**.
- **N == 1** → `O1 - O2` is negative under [[TwosComplement|two's complement]] → signed `O1 < O2` (combined with V).
- **C == 1** → no unsigned borrow → unsigned `O1 >= O2`. *Note the inverted-borrow convention from [[X86FlagsRegister|x86]]: on [[ARM64]], `cmp` sets `C == 1` when the subtraction does **not** borrow.*
- **V == 1** → signed overflow occurred during the subtraction.

The [[ARM64ConditionalBranch|`b.cond`]] suffix table maps flag combinations back to the source-level comparison operator.

## Comparison to x86

| | [[CmpInstruction|x86 `cmp`]] / [[TestInstruction|x86 `test`]] | [[ARM64Cmp|ARM64 `cmp` / `cmn` / `tst`]] |
|---|---|---|
| Subtract-and-discard | `cmp` (AT&T: source-first → `src2 - src1`) | `cmp` (destination-first reading → `O1 - O2`) |
| Add-and-discard | — (no dedicated mnemonic) | **`cmn`** (compare negative) |
| Bitwise-AND-and-discard | `test` | `tst` |
| Underlying ops | Just-set-flags variants of `sub` / `and` | Aliases of `subs xzr` / `adds xzr` / `ands xzr` |
| Zero-test idiom | `test %rax, %rax` | `tst x0, x0` (or `cbz x0, <label>`) |

## Connections

- [[ARM64FlagsRegister]] — the NZCV flags this family sets.
- [[ARM64ConditionalBranch]] — `b.cond` consumes the NZCV state set here.
- [[ARM64ConditionalSelect]] — `csel` also consumes the NZCV state set here.
- [[ARM64ArithmeticInstructions]] — these are flag-only aliases of `subs` / `adds` / `ands`.
- [[CmpInstruction]] / [[TestInstruction]] — x86 analogs.
- [[ARM64]] / [[ConditionCode]] / [[TwosComplement]] — supporting concepts.
- [[dis-9-4-1-arm64-preliminaries]] — source.
