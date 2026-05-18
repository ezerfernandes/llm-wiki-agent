---
title: "x86-64 Conditional Move Instructions (`cmov`)"
type: concept
tags: [x86-64, assembly, control-flow, branch-free, optimization, condition-codes]
sources: [dis-7-4-2-x86-64-if-statements]
last_updated: 2026-05-17
---

# x86-64 Conditional Move Instructions

The **`cmov` family** is [[X86_64|x86-64]]'s **branch-free conditional-assignment primitive** — a [[X86MovInstruction|`mov`]]-shaped instruction whose write to the destination is **gated** on the same [[X86FlagsRegister|FLAGS]] condition codes that a [[X86JumpInstructions|conditional jump]] consumes. Per [[dis-7-4-2-x86-64-if-statements|Ch 7.4.2 of *[[DiveIntoSystems]]*]], `cmov` is the optimized (`-O1`+) realization of side-effect-free if-then-else patterns — the [[CompilerOptimization|compiler-optimization]] alternative to the [[BranchInstruction|branch-based]] [[AsmIfThenElse|`j*`-and-label]] pattern.

## Form

```
cmovCC S, D
```

If condition `CC` holds (encoded in the [[X86FlagsRegister|FLAGS]] left by the most recent flag-setting instruction — typically [[CmpInstruction|`cmp`]]), then `D ← S`. Otherwise `D` is unchanged. **Both operands are read unconditionally**; only the *write* is gated.

## The family

`cmov` mnemonic suffixes mirror the [[X86JumpInstructions|conditional-jump family]] one-to-one — same flag tests, same signed/unsigned split lives in the mnemonic:

### Equality / sign (sign-agnostic)

| Mnemonic | Flag test | Meaning |
|---|---|---|
| `cmove`  / `cmovz`  | ZF = 1 | equal / zero |
| `cmovne` / `cmovnz` | ZF = 0 | not equal / nonzero |
| `cmovs`  | SF = 1 | negative |
| `cmovns` | SF = 0 | non-negative |

### Signed ordering (consume SF + OF)

| Mnemonic | C operator |
|---|---|
| `cmovg`  | `>`  (signed) |
| `cmovge` | `>=` (signed) |
| `cmovl`  | `<`  (signed) |
| `cmovle` | `<=` (signed) |

### Unsigned ordering (consume CF)

| Mnemonic | C operator |
|---|---|
| `cmova`  | `>`  (unsigned) |
| `cmovae` | `>=` (unsigned) |
| `cmovb`  | `<`  (unsigned) |
| `cmovbe` | `<=` (unsigned) |

## Canonical pattern

Ch 7.4.2's `getSmallest_cmov` trace:

```c
int getSmallest_cmov(int x, int y) {
    return x > y ? y : x;
}
```

```
cmp  %esi, %edi      ; set flags from (x - y)  (AT&T source-first)
mov  %esi, %eax      ; tentatively place y in return register
cmovle %edi, %eax    ; if (x <= y), overwrite eax with x
retq
```

**No `j*` instructions; no labels.** The structural shape — *"tentatively place one arm, conditionally overwrite with the other"* — is the universal idiom.

## Payoff: no branch to mispredict

`cmov` executes both arms unconditionally and selects the destination value after-the-fact — *"avoiding branch misprediction penalties"*. There is no [[ControlHazard|control hazard]] (the [[InstructionPointer|`%rip`]] is never redirected), so the [[BranchPredictor|branch predictor]] is bypassed entirely. Where the [[BranchInstruction|branch-based]] pattern relies on the [[BranchPrediction|branch predictor]] guessing correctly to avoid a [[PipelineStall|pipeline stall]], `cmov` is **deterministically branch-free**.

This is the same [[dis-5-8-pipelining-advanced|Ch 5.8]] *control-hazard* story seen from the compiler side: the [[BranchPrediction|branch-prediction]] mitigation is replaced by **elimination**.

## The safety side-condition

`cmov` requires both arms to be **safely pre-evaluable**: both source operands must already be in registers (or readable memory locations) at the point of the `cmov`, because they are read whether or not the condition holds.

This **rules out** any if-then-else where one arm has a side effect or could fault:

```c
int incrementX(int *x) {
    if (x != NULL) {
        return (*x)++;       // dereference + write — cannot be unconditionally pre-evaluated
    } else {
        return 1;
    }
}
```

Here `(*x)++` would [[SegmentationFault|segfault]] on the `x == NULL` path if executed unconditionally. The compiler falls back to the [[BranchInstruction|jump-based]] pattern — *"the compiler takes the safe road and uses jumps"*. See [[NullPointerSafety]].

## Connections

- [[X86MovInstruction]] — `cmov` is the conditional version; same source / destination operand structure.
- [[X86JumpInstructions]] — one-to-one mnemonic-suffix mirror; the [[BranchInstruction|branching]] alternative.
- [[CmpInstruction]] / [[TestInstruction]] — flag-setters that almost always precede a `cmov`.
- [[X86FlagsRegister]] / [[ConditionCode]] — the flags `cmov` consumes.
- [[AsmIfThenElse]] — the if-then-else compilation pattern `cmov` is the branch-free realization of.
- [[BranchInstruction]] — generic control-flow-transfer primitive of which both jumps and `cmov` are instances (`cmov` is **predicated** rather than branching).
- [[CompilerOptimization]] — `-O1` introduces `cmov` substitution; structural sibling of [[dis-7-3-x86-64-arithmetic|Ch 7.3]]'s [[X86ShiftInstructions|`shl`-as-multiply]] and [[LeaInstruction|`lea`-as-arithmetic]] strength reductions.
- [[BranchPrediction]] / [[BranchPredictor]] / [[ControlHazard]] / [[PipelineStall]] — the [[dis-5-8-pipelining-advanced|Ch 5.8]] microarchitecture story `cmov` short-circuits.
- [[NullPointerSafety]] / [[SegmentationFault]] — the safety side-condition that gates `cmov` substitution.
- [[TernaryOperator|C `? :` operator]] — the [[CLanguage|C]] expression form that maps cleanly onto `cmov`.
- [[X86_64]] / [[AtAndTSyntax]] — host ISA / syntax.
