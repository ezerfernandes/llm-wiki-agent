---
title: "If-Then-Else Compilation Pattern (x86-64 Assembly)"
type: concept
tags: [x86-64, assembly, control-flow, if-statement, compilation-pattern, branch]
sources: [dis-7-4-2-x86-64-if-statements]
last_updated: 2026-05-17
---

# If-Then-Else Compilation Pattern (x86-64)

The **if-then-else pattern** is the canonical [[X86_64|x86-64]] [[AssemblyLanguage|assembly]] compilation pattern for [[CLanguage|C]]'s [[IfStatement|`if`]] / [[ElseStatement|`else`]] construct. Per [[dis-7-4-2-x86-64-if-statements|Ch 7.4.2 of *[[DiveIntoSystems]]*]], the compiler realizes it in **two structural forms** depending on safety side-conditions: a **branch-based** form (always available) using [[X86JumpInstructions|conditional jumps]] + labels, and a **branch-free** form (gated on side-effect-freedom) using [[X86ConditionalMove|`cmov`]] instructions.

## Form 1: branch-based (always works)

The compiler converts the source-level `if`/`else` to **goto form with the condition inverted** — *"a standard if statement [is] where a jump occurs when conditions are **not** true."*

Source:

```c
if (x > y) {
    smallest = y;          // then-branch
} else {
    smallest = x;          // else-branch
}
```

Goto form:

```c
if (x <= y) goto assign_x;     // jump on NEGATED condition
smallest = y;                   // then-branch falls through
goto done;
assign_x:
    smallest = x;               // else-branch (labeled)
done:
    /* fall through */
```

Assembly:

```
    cmp  -0x18(%rbp), %eax     ; flags ← (x - y)  (AT&T source-first)
    jle  L_else                ; jump if x <= y (NEGATION of x > y)
    mov  %edx, -0x4(%rbp)      ; then: smallest = y
    jmp  L_done
L_else:
    mov  %eax, -0x4(%rbp)      ; else: smallest = x
L_done:
    ...
```

Structural shape — a **diamond**: a flag-setting instruction (almost always [[CmpInstruction|`cmp`]] or [[TestInstruction|`test`]]) → a **conditional jump on the negated source condition** that skips the then-branch when the source condition is **false** → the then-branch falling through → an **unconditional jump** to the join point → the else-branch labeled at the conditional jump's target → the join label. **Two labels, one [[CmpInstruction|`cmp`]], one [[X86JumpInstructions|conditional jump]], one [[X86JumpInstructions|unconditional jump]]** in the canonical layout.

## Form 2: branch-free with [[X86ConditionalMove|`cmov`]] (`-O1`+, side-effect-free only)

When the if-then-else is **structurally a value-selection** (both arms assign different values to the same variable) **and** both candidate values are safely pre-evaluable, the compiler at `-O1` and above substitutes the entire diamond with **three branchless instructions**:

```c
return x > y ? y : x;     // structurally identical to the if/else above
```

```
cmp    %esi, %edi          ; flags ← (x - y)
mov    %esi, %eax          ; tentatively place y in return
cmovle %edi, %eax          ; if (x <= y), overwrite with x
retq
```

**No labels, no `j*` instructions.** The control-flow diamond is gone; the [[InstructionPointer|`%rip`]] never redirects. This is structurally a [[CompilerOptimization|compiler optimization]] sibling to [[dis-7-3-x86-64-arithmetic|Ch 7.3]]'s [[X86ShiftInstructions|`shl`-as-multiply]] and [[LeaInstruction|`lea`-as-arithmetic]] strength reductions — applied at the control-flow surface rather than the arithmetic surface.

## When the compiler picks which form

| If the if-then-else is... | The compiler emits... |
|---|---|
| simple value-selection, side-effect-free, both arms safely pre-evaluable | [[X86ConditionalMove|`cmov`]] (Form 2) — branch-free |
| has side effects, function calls, possible faults, or asymmetric work | [[X86JumpInstructions|conditional jumps]] (Form 1) — branch-based |
| compiled at `-O0` (unoptimized) | [[X86JumpInstructions|conditional jumps]] (Form 1) — always |

Headline rule: *"the compiler takes the safe road and uses jumps"* whenever pre-evaluating both arms could fault (e.g. dereferencing a possibly-null pointer) or produce visible side effects. See [[NullPointerSafety]] for the canonical example.

## The inverted-condition rule

In Form 1, **the jump tests the negation of the source condition** so the **then**-branch falls through. The mnemonic mapping is the [[X86JumpInstructions|jump-family]] negation table:

| Source C condition | Conditional jump skipping the then-branch |
|---|---|
| `x > y`  (signed) | `jle` |
| `x >= y` (signed) | `jl`  |
| `x < y`  (signed) | `jge` |
| `x <= y` (signed) | `jg`  |
| `x == y`          | `jne` |
| `x != y`          | `je`  |
| `x > y`  (unsigned) | `jbe` |
| `x < y`  (unsigned) | `jae` |

The same negation rule applies symmetrically — the compiler may also emit the **non-negated** form and put the then-branch at the labeled target. Both layouts are correct; modern compilers pick based on branch-prediction heuristics (forward branches are predicted not-taken).

## Connections

- [[IfStatement]] / [[ElseStatement]] — the [[CLanguage|C]] constructs this pattern compiles.
- [[X86JumpInstructions]] — the conditional-jump family used in Form 1.
- [[X86ConditionalMove]] — the `cmov` family used in Form 2.
- [[BranchInstruction]] — the generic control-flow-transfer primitive both forms realize.
- [[CmpInstruction]] / [[TestInstruction]] — the flag-setters that precede the conditional jump (Form 1) or `cmov` (Form 2).
- [[X86FlagsRegister]] / [[ConditionCode]] — the flags both forms consume.
- [[InstructionPointer]] — Form 1 redirects `%rip`; Form 2 does not.
- [[TernaryOperator|C `? :` operator]] — the source-level form that most cleanly maps onto Form 2.
- [[NullPointerSafety]] / [[SegmentationFault]] — the safety side-condition that forces the compiler back to Form 1.
- [[CompilerOptimization]] — Form 2 is enabled at `-O1` and above.
- [[BranchPrediction]] / [[BranchPredictor]] / [[ControlHazard]] / [[PipelineStall]] — the [[dis-5-8-pipelining-advanced|Ch 5.8]] microarchitecture story that makes Form 2 a measurable win when applicable.
- [[dis-7-4-1-x86-64-preliminaries|Ch 7.4.1]] — supplies the [[CmpInstruction|`cmp`]] / [[X86JumpInstructions|conditional-jump]] vocabulary Form 1 uses.
