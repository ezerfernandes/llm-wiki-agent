---
title: "Dive into Systems — Ch 7.4.2 If Statements in Assembly (x86-64)"
type: source
tags: [book, dive-into-systems, x86-64, assembly, control-flow, if-statement, branch, cmov]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C7-x86_64/if_statements.html
sources: []
last_updated: 2026-05-17
---

## Summary

**Second leaf** of [[dis-7-4-x86-64-conditional-loops|Ch 7.4]] of *[[DiveIntoSystems]]*. Operationalizes the [[dis-7-4-1-x86-64-preliminaries|Ch 7.4.1]] mechanism families ([[X86FlagsRegister|FLAGS]] + [[CmpInstruction|`cmp`]] + [[X86JumpInstructions|conditional jumps]]) into the **canonical compilation pattern** for [[CLanguage|C]]'s [[IfStatement|`if`]] / [[ElseStatement|`else`]] construct via a single worked example — `getSmallest(int x, int y)` — traced through both unoptimized (branch-based) and `-O1`-optimized (branch-free, [[X86ConditionalMove|`cmov`]]-based) [[X86_64|x86-64]] assembly. Introduces a **second branch-free idiom** ([[X86ConditionalMove|`cmov`]]) alongside the existing branch-based jump pattern, plus the **safety side-condition** that gates it — the [[NullPointerSafety|null-pointer / side-effect]] caveat forcing the compiler back to jumps when both arms cannot be safely pre-evaluated. **68th ingested DIS chapter.**

## Key Claims

- **The `if (cond) { then } else { else }` compilation pattern uses inverted-condition jumps**: the compiler converts to goto form *"if (NOT cond) goto else; then; goto done; else: ...; done: ..."* — *"a standard if statement [is] where a jump occurs when conditions are **not** true."* In the `getSmallest` trace, the source-level `if (x > y)` compiles to **`jle else_branch`** — the jump fires when `x ≤ y` (the **negation** of the source condition), falling through to the then-branch when `x > y`. Realizes the [[BranchInstruction|forward-branch-skips-then]] structural pattern.
- **The Ch 7.4.1 `cmp` + conditional-jump building blocks are exactly what shows up here.** [[CmpInstruction|`cmp -0x18(%rbp), %eax`]] sets [[X86FlagsRegister|FLAGS]] *"as if computing `%eax − -0x18(%rbp)`"* (the [[AtAndTSyntax|AT&T source-first]] order); [[X86JumpInstructions|`jle`]] consumes SF + OF to decide whether to take the branch. The two unconditional jumps (`jmp done`, label `done:`) form the **fall-through path** structuring the diamond.
- **The `-O1` optimization replaces branches with [[X86ConditionalMove|conditional moves]]** whenever the equivalent ternary form is **side-effect-free** — *"when both branches of an `if-else` statement simply assign different values to a single variable, the compiler may use `cmov` to remove the branch entirely."* The `getSmallest_cmov` trace shows the same logic as **three branchless instructions**: `cmp %esi, %edi` (set flags) → `mov %esi, %eax` (tentatively place `y` in return) → **`cmovle %edi, %eax`** (overwrite with `x` iff `x ≤ y`). No `j*` instructions; no labels.
- **The `cmov` family mirrors the [[X86JumpInstructions|conditional-jump family]] one-to-one.** Same mnemonic suffix vocabulary (`e`/`ne`/`g`/`ge`/`l`/`le` signed; `a`/`ae`/`b`/`be` unsigned; `s`/`ns`) — *"each cmov variant pairs with its sibling jump"*. Twelve named variants: signed (`cmove`, `cmovne`, `cmovs`, `cmovns`, `cmovg`, `cmovge`, `cmovl`, `cmovle`); unsigned (`cmova`, `cmovae`, `cmovb`, `cmovbe`).
- **`cmov` evaluates both arms unconditionally and selects after-the-fact**, *"avoiding branch misprediction penalties"* — the branch-prediction motivation surfaced in [[dis-5-8-pipelining-advanced|Ch 5.8]]'s [[ControlHazard|control hazards]] / [[BranchPrediction|branch prediction]] discussion. This is `cmov`'s payoff: no [[PipelineStall|pipeline stall]] from a misprediction, because there is no branch to predict.
- **The safety side-condition**: *"the compiler takes the safe road and uses jumps"* whenever pre-evaluating both arms could **cause a fault or visible side effect** — the canonical example is `if (x != NULL) return (*x)++; else return 1;` where unconditionally pre-evaluating `(*x)++` on the `x == NULL` path would [[SegmentationFault|segfault]]. **`cmov` cannot guard a [[NullPointerSafety|null pointer]]** — the dereference happens regardless of which arm "wins" — so the compiler falls back to the [[BranchInstruction|branch-based]] pattern.

## Key Quotes

> "A standard if statement [is] where a jump occurs when conditions are **not** true."

> "When both branches of an if-else statement simply assign different values to a single variable, the compiler may use `cmov` to remove the branch entirely."

> "The compiler takes the safe road and uses jumps."

> "cmov executes both conditional branches in hardware, selecting the result afterward."

## Connections

- [[DiveIntoSystems]] — host textbook; this is Ch 7.4.2, the **second leaf** of [[dis-7-4-x86-64-conditional-loops|Ch 7.4]] (after [[dis-7-4-1-x86-64-preliminaries|7.4.1]] and before 7.4.3 *Loops*).
- [[dis-7-4-1-x86-64-preliminaries]] — supplies the [[X86FlagsRegister|FLAGS]] / [[CmpInstruction|`cmp`]] / [[X86JumpInstructions|conditional jump]] vocabulary this chapter composes into the if-then-else pattern.
- [[X86ConditionalMove]] — the `cmov` family minted here; the branch-free alternative to the [[X86JumpInstructions|`j*` family]].
- [[AsmIfThenElse]] — the canonical compilation pattern for [[IfStatement|`if`]] / [[ElseStatement|`else`]] in [[X86_64|x86-64]] assembly minted here.
- [[BranchInstruction]] — control-flow primitive promoted from forward reference here; covers both branch-based ([[X86JumpInstructions|conditional jumps]]) and branch-free ([[X86ConditionalMove|`cmov`]]) realizations.
- [[X86JumpInstructions]] — `jle` / `jg` / `je` etc. used in the branch-based pattern.
- [[CmpInstruction]] — sets flags consumed by both `j*` and `cmov` instructions.
- [[IfStatement]] / [[ElseStatement]] — the [[CLanguage|C]] constructs being compiled.
- [[TernaryOperator|C ternary `? :`]] — the side-effect-free expression form that maps cleanly onto `cmov`.
- [[BranchPrediction]] / [[ControlHazard]] — the [[dis-5-8-pipelining-advanced|Ch 5.8]] microarchitecture story that motivates `cmov` as a branch-misprediction-elimination tool.
- [[PipelineStall]] — what `cmov` avoids by removing the branch.
- [[InstructionPointer]] — `cmov` does **not** modify `%rip`; jumps do.
- [[NullPointerSafety]] / [[SegmentationFault]] — the safety side-condition that gates `cmov` use.
- [[CompilerOptimization]] — `cmov`-substitution is enabled at `-O1` and above; the page's third concrete `-O*` payoff after [[X86ShiftInstructions|`shl`-as-multiply]] and [[LeaInstruction|`lea`-as-arithmetic]].

## Contradictions

None. Extends prior coverage:

- **Operationalizes [[dis-7-4-1-x86-64-preliminaries|Ch 7.4.1]]** — the `cmp` + conditional-jump primitives are now composed into the diamond-shaped if-then-else control-flow pattern.
- **Confirms [[dis-5-8-pipelining-advanced|Ch 5.8]]'s** [[BranchPrediction|branch-prediction]] / [[ControlHazard|control-hazard]] motivation by showing the **compiler-side response** — `cmov` is a branch-free realization that **eliminates** the hazard rather than mitigating it.
- **Confirms [[dis-7-3-x86-64-arithmetic|Ch 7.3]]'s [[CompilerOptimization|compiler-optimization]] theme** — `-O1` substitution of `cmov` for branches is structurally identical to the `shl`-for-`imul` and `lea`-for-multi-op-arithmetic strength reductions, just at the control-flow surface rather than the arithmetic surface.
