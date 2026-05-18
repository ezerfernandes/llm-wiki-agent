---
title: "ARM64 csel (Conditional Select)"
type: concept
tags: [arm64, armv8, assembly, control-flow, csel, conditional-select, branch-free, cmov]
sources: [dis-9-4-1-arm64-preliminaries, dis-9-4-2-arm64-if-statements]
last_updated: 2026-05-17
---

# ARM64 Conditional Select (`csel`)

The **`csel`** instruction is [[ARM64|AArch64]]'s **conditional-data-transfer** primitive — the [[ARM64]] analog of [[X86ConditionalMove|x86 `cmov`]]. It performs the if/else of a small expression **without emitting any branch instruction**, eliminating the [[ControlHazard|control hazard]] / [[BranchPrediction|branch-prediction]] cost that an [[ARM64ConditionalBranch|`b.cond`]]-based [[IfStatement|`if`]]-compilation would otherwise incur. Per [[dis-9-4-2-arm64-if-statements|Ch 9.4.2 of *[[DiveIntoSystems]]*]].

## Instruction shape

```
csel D, R1, R2, <cond>     ;  if (cond) D = R1 else D = R2
```

The CPU reads the [[ARM64FlagsRegister|NZCV flags]] just as a [[ARM64ConditionalBranch|`b.cond`]] would, then commits **either R1 or R2** into the destination `D`. **Both source registers are read unconditionally**; only the writeback is gated by the condition. No branch instruction is emitted — `pc` advances sequentially, so the pipeline never stalls on a misprediction.

## Condition suffixes

Same suffix vocabulary as [[ARM64ConditionalBranch|`b.cond`]] — `eq` / `ne` / `lt` / `le` / `gt` / `ge` / `lo` / `ls` / `hi` / `hs` / `mi` / `pl` / `vs` / `vc`. The signed/unsigned split is encoded in the suffix, exactly as for [[ARM64ConditionalBranch|`b.cond`]].

## The `csel` family (related instructions)

Per the ARMv8 ARM, the conditional-select family includes:

- **`csel D, R1, R2, cond`** — base form: `D = cond ? R1 : R2`.
- **`csinc D, R1, R2, cond`** — `D = cond ? R1 : R2 + 1`. Useful for the `cond ? x : x+1` pattern and for **`cset`** (alias `csinc D, xzr, xzr, !cond` → `D = cond ? 0 : 1`; commonly written `cset D, cond` → `D = cond ? 1 : 0`).
- **`csinv D, R1, R2, cond`** — `D = cond ? R1 : ~R2`. Underpins **`csetm`** (set-mask: `D = cond ? -1 : 0`).
- **`csneg D, R1, R2, cond`** — `D = cond ? R1 : -R2`.

The `cset` / `csetm` / `cinc` / `cinv` / `cneg` mnemonics are **assembler aliases** for specific `csel` family encodings — the [[ARM64]] analog of [[X86_64|x86]] `setCC`.

## Performance motivation

*"Branch instructions can disrupt instruction pipelines, making them expensive."* The `csel` form pre-evaluates both candidate values into registers and commits one — **no branch-prediction cost, no pipeline flush** on misprediction. For a small `if/else` selecting between two register-resident values, `csel` is strictly faster.

## Compiler caution caveat

*"The compiler is very cautious about optimizing branch instructions into `csel` instructions, especially in cases where side effects and pointer values are involved."*

Both arms of the source `if/else` must be **safely pre-evaluable** — `csel` reads R1 *and* R2 unconditionally, so if computing R2 requires:

- **Dereferencing a possibly-[[NullPointerSafety|null]] pointer** (segfault on the not-taken arm) — compiler refuses to substitute.
- **A side-effecting call** (`printf`, file I/O, store to memory) — compiler refuses to substitute.
- **A division that could trap** — compiler refuses to substitute.

In any of these cases the compiler emits the [[ARM64ConditionalBranch|`b.cond`]]-based form so the unsafe arm only executes when actually selected. Same caveat as [[X86ConditionalMove|x86 `cmov`]] in [[dis-7-4-2-x86-64-if-statements|Ch 7.4.2]].

## Worked example pattern

C:
```c
int max = (a > b) ? a : b;
```

[[ARM64]] (with `a` in `w0`, `b` in `w1`):
```asm
cmp   w0, w1
csel  w2, w0, w1, gt    ; w2 = (a > b) ? a : b
```

Two instructions, **no branch** — vs the [[ARM64ConditionalBranch|`b.cond`]]-based form which would require a forward branch plus an unconditional branch over the else-arm.

## Comparison to x86 `cmov`

| | [[X86ConditionalMove|x86 `cmov`]] | [[ARM64ConditionalSelect|ARM64 `csel`]] |
|---|---|---|
| Operands | 2 (`cmovCC src, dst`) | 3 (`csel D, R1, R2, cond`) |
| Selects between | `dst` (unchanged) and `src` (conditionally loaded) | **R1 and R2 explicitly** |
| Condition vocabulary | x86 condition codes (`e`/`ne`/`g`/`l`/`a`/`b`/...) | [[ARM64]] condition codes (`eq`/`ne`/`gt`/`lt`/`hi`/`lo`/...) |
| Family members | `cmov*`, `set*` | `csel`, `csinc`, `csinv`, `csneg` (+ aliases `cset`, `csetm`, ...) |

[[ARM64]]'s **3-operand** `csel` is more expressive than [[X86_64|x86]]'s 2-operand `cmov` — the destination is independent of both sources, so neither source register need be tied to the destination.

## Connections

- [[ARM64FlagsRegister]] — supplies NZCV bits this instruction consumes.
- [[ARM64Cmp]] — the typical flag-producer paired with `csel`.
- [[ARM64ConditionalBranch]] — the branch-based alternative `csel` replaces.
- [[X86ConditionalMove]] — x86 analog (`cmov`).
- [[NullPointerSafety]] / [[BranchPrediction]] / [[ControlHazard]] — supporting concepts behind the caveat / motivation.
- [[ARM64]] / [[ConditionCode]] / [[ControlFlow]] — supporting concepts.
- [[dis-9-4-1-arm64-preliminaries]] / [[dis-9-4-2-arm64-if-statements]] — sources.
