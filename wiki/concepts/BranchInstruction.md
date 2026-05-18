---
title: "Branch Instruction"
type: concept
tags: [assembly, control-flow, branch, isa, microarchitecture]
sources: [dis-7-4-2-x86-64-if-statements]
last_updated: 2026-05-17
---

# Branch Instruction

A **branch instruction** is any [[AssemblyLanguage|assembly]] instruction whose purpose is to **alter the sequential flow of execution** — either by redirecting the [[InstructionPointer|instruction pointer]] (a *taken branch*) or by **conditionally gating** the effect of another instruction (a *predicated* or *branch-free* realization). Per [[dis-7-4-2-x86-64-if-statements|Ch 7.4.2 of *[[DiveIntoSystems]]*]], the [[X86_64|x86-64]] [[ISA]] exposes branch behavior through two structurally distinct families:

- **[[X86JumpInstructions|Conditional and unconditional jumps]]** — the **classic branch family**: write a new value into [[InstructionPointer|`%rip`]] (always, or conditioned on [[X86FlagsRegister|FLAGS]]). The default realization of [[CLanguage|C]]'s [[IfStatement|`if`]] / [[WhileLoop|`while`]] / [[ForLoop|`for`]] / [[SwitchStatement|`switch`]] constructs.
- **[[X86ConditionalMove|Conditional moves (`cmov`)]]** — the **predicated / branch-free family**: leave `%rip` untouched but conditionally gate a register write on the same [[X86FlagsRegister|FLAGS]] codes the jump family consumes. Introduced at `-O1` and above as a [[CompilerOptimization|compiler optimization]] of side-effect-free if-then-else patterns.

This page promotes the **branch-instruction concept** to first-class status — previously a forward-reference from [[dis-7-4-x86-64-conditional-loops|Ch 7.4]]'s framing as *"branch-driven non-sequential execution"* and from [[dis-5-8-pipelining-advanced|Ch 5.8]]'s [[ControlHazard|control-hazard]] / [[BranchPrediction|branch-prediction]] discussion. Both forward references now resolve here.

## Two realizations of the same control intent

The if-then-else pattern *"pick value A if condition, else value B"* admits both realizations:

| Aspect | Branch (jump-based) | Branch-free (cmov-based) |
|---|---|---|
| **`%rip`** modification | Yes (taken branch redirects) | No (sequential fetch continues) |
| **Both arms evaluated?** | No — only the chosen arm | Yes — both arms always |
| **Microarchitecture** | Predicted by [[BranchPredictor|branch predictor]]; misprediction → [[PipelineStall|pipeline stall]] | No prediction needed; no [[ControlHazard|control hazard]] |
| **Safety side-condition** | None — any if-then-else compiles | Both arms must be safely pre-evaluable (no faults, no side effects) |
| **Typical use** | All if/while/for; any side-effect-bearing arm | `-O1`+ side-effect-free value selection |

See [[AsmIfThenElse]] for the worked compilation pattern showing both forms side by side.

## Why two families?

The branch-free family exists to **eliminate** (not merely mitigate) the [[ControlHazard|control hazard]] that [[dis-5-8-pipelining-advanced|Ch 5.8]] introduced: a taken-branch redirect to `%rip` cannot be resolved until late in the pipeline, so the predictor has to **guess** which target to fetch from in the meantime — a wrong guess flushes the speculative work. A predicated instruction has **no branch to guess** — both arms are evaluated; the result is selected after-the-fact — so no [[BranchPrediction|branch prediction]] is required and no flush can occur.

The trade is that **both arms always run**: this is the safety side-condition. Pre-evaluating a possibly-faulting expression (the classic [[NullPointerSafety|null-pointer]] dereference case) on the *wrong* arm would crash the program, so the compiler must verify side-effect-freedom before substituting `cmov` for a branch. When verification fails, the compiler falls back to the jump-based family — *"the compiler takes the safe road and uses jumps."*

## On other ISAs

The branch-vs-branch-free split is universal across modern [[ISA|ISAs]]:

- **[[X86_64|x86-64]]**: [[X86JumpInstructions|`j*`]] (branch) vs [[X86ConditionalMove|`cmov`]] (predicated).
- **[[ARM|ARM (AArch64)]]**: `B.cond` (branch) vs `CSEL` / `CSET` / `CINC` (conditional-select family — predicated). Earlier AArch32 had **full instruction predication** (every instruction carried an optional condition code).
- **[[RISCV|RISC-V]]**: `BEQ`/`BNE`/... (branch); no in-ISA predicated-move (compilers synthesize via shifts + masks, or use the optional **Zicond** extension's `CZERO.EQZ` / `CZERO.NEZ`).

The split reflects the **same** microarchitecture pressure ([[ControlHazard|control hazards]] in deep pipelines) across all three ISAs; the dialect-specific differences live in the predicated-instruction encoding and breadth.

## Connections

- [[X86JumpInstructions]] — the branch-based family on [[X86_64|x86-64]].
- [[X86ConditionalMove]] — the predicated / branch-free family on [[X86_64|x86-64]].
- [[AsmIfThenElse]] — the compilation pattern that uses one or the other.
- [[InstructionPointer]] — what branches write and `cmov` does not.
- [[CmpInstruction]] / [[TestInstruction]] — the flag-setters that precede a branch or a `cmov`.
- [[X86FlagsRegister]] / [[ConditionCode]] — the flags branches and `cmov` both consume.
- [[ControlHazard]] / [[BranchPrediction]] / [[BranchPredictor]] / [[PipelineStall]] — the [[dis-5-8-pipelining-advanced|Ch 5.8]] microarchitecture story branches participate in and `cmov` short-circuits.
- [[CompilerOptimization]] — `-O1`+ substitutes branch-free for branch where safe.
- [[NullPointerSafety]] / [[SegmentationFault]] — the safety side-condition gating branch-free substitution.
- [[ControlFlow]] — the umbrella term; branch instructions are the assembly-surface realization.
- [[IfStatement]] / [[WhileLoop]] / [[ForLoop]] / [[DoWhileLoop]] / [[SwitchStatement]] — the [[CLanguage|C]] constructs branch instructions compile.
- [[ARM]] / [[RISCV]] — sister ISAs with their own branch-vs-predicated splits.
