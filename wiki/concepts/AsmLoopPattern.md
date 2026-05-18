---
title: "Loop Compilation Pattern (x86-64 Assembly)"
type: concept
tags: [x86_64, assembly, control-flow, loop, compiler, codegen]
sources: [dis-7-4-3-x86-64-loops]
last_updated: 2026-05-17
---

# Loop Compilation Pattern (x86-64 Assembly)

The **canonical [[X86_64|x86-64]] [[AssemblyLanguage|assembly]] compilation pattern** for [[CLanguage|C]]'s three loop constructs — [[WhileLoop|`while`]], [[ForLoop|`for`]], [[DoWhileLoop|`do`–`while`]] — per [[dis-7-4-3-x86-64-loops|DiS Ch 7.4.3]]. The [[X86_64|x86-64]] [[InstructionSet|ISA]] has **no dedicated loop instruction**; the compiler synthesizes loop semantics out of the [[dis-7-4-1-x86-64-preliminaries|Ch 7.4.1]] primitives — [[CmpInstruction|`cmp`]] + the [[X86JumpInstructions|jump-instruction family]] reading [[X86FlagsRegister|FLAGS]] — with the **direction of the jump reversed** vs. [[AsmIfThenElse|the if-pattern]] (backward to a body label rather than forward over an else-branch) and **the polarity un-negated** (jump *while* the loop condition holds, rather than *unless* it holds).

## Two structural forms

### Form 1 — Test-first (`while` / `for`)

The compiler emits an **unconditional [[X86JumpInstructions|`jmp`]] to the condition check** first, so the body is skipped on first entry. Pseudocode:

```
        jmp test
body:   <loop body>
test:   cmp <loop condition operands>
        j<cond> body        ; backward conditional jump, un-negated condition
```

The conditional jump uses the **un-negated** loop condition — `jle` for `i <= n`, `jl` for `i < n`, `jne` for `x != y`, etc. — mirroring the source-level `while (cond)` directly.

### Form 2 — Test-last (`do`–`while`)

Because the body executes unconditionally on first entry (the [[DoWhileLoop|always-at-least-once]] property), the do-while pattern **drops the leading `jmp`**:

```
body:   <loop body>
        cmp <loop condition operands>
        j<cond> body        ; backward conditional jump, un-negated condition
```

The do-while pattern is **strictly simpler** than the while/for pattern at the assembly surface — one fewer jump instruction, no leading jump-to-test prologue.

## `for` and `while` compile to the same assembly

*"Every `for` loop can be represented by a `while` loop."* The three-clause `for (init; cond; step) { body; }` decomposes mechanically to `init; while (cond) { body; step; }` — same loop variable, same condition, same termination, same emitted instructions. The optimizer sees only the post-decomposition form, so the choice between `for` and `while` in source is **purely stylistic** at the assembly surface.

## The `sumUp` worked trace

From [[dis-7-4-3-x86-64-loops|Ch 7.4.3]]'s running example (`while (i <= n) { total += i; i++; }`, locals at `%rbp-0x8` / `%rbp-0x4`):

| Address    | Instruction               | Role                                                        |
|------------|---------------------------|-------------------------------------------------------------|
| `0x40053b` | `jmp 0x400547`            | Jump-to-test prologue (Form 1's leading `jmp`)              |
| `0x40053d` | body                      | `add` and `mov` operations updating `total` and `i`         |
| `0x400547` | `mov -0x4(%rbp), %eax`    | Load `i` into the comparison shuttle                        |
| `0x40054a` | `cmp %eax, ...`           | Set [[X86FlagsRegister|FLAGS]] from `n − i`                  |
| `0x40054d` | `jle 0x40053d`            | Backward conditional jump, un-negated `i ≤ n` condition     |

## Contrast with the if-pattern

[[AsmIfThenElse|Ch 7.4.2]]'s if-pattern jumps **forward** over the then-branch on the **negated** condition (`x > y` → `jle else`). This section's loop pattern jumps **backward** to the body label on the **un-negated** condition (`i <= n` → `jle body`). **Same mechanism, opposite direction, opposite polarity** — two ends of the same [[X86JumpInstructions|jump-family]] surface.

## Connections

- [[dis-7-4-3-x86-64-loops]] — source.
- [[WhileLoop]] / [[ForLoop]] / [[DoWhileLoop]] — source-language constructs this pattern translates.
- [[X86JumpInstructions]] / [[CmpInstruction]] / [[X86FlagsRegister]] — mechanism layer.
- [[AsmIfThenElse]] — sibling control-flow compilation pattern (forward-jump-on-negated-condition).
- [[BranchInstruction]] — the family-level abstraction over loop and if patterns.
- [[InstructionPointer]] — the register the backward jump writes to indirectly.
- [[ControlFlow]] / [[CLanguage]] / [[X86_64]] / [[AssemblyLanguage]] / [[DiveIntoSystems]].
