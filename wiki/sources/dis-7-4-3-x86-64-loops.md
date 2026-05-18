---
title: "Dive into Systems — Ch 7.4.3 Loops in Assembly (x86-64)"
type: source
tags: [dive-into-systems, x86_64, assembly, control-flow, loops, while, for, do-while]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C7-x86_64/loops.html
sources: []
last_updated: 2026-05-17
---

# Dive into Systems — Ch 7.4.3 Loops in Assembly (x86-64)

## Summary

**Third and final leaf** of [[dis-7-4-x86-64-conditional-loops|Ch 7.4]] of *[[DiveIntoSystems]]*. Operationalizes the [[dis-7-4-1-x86-64-preliminaries|Ch 7.4.1]] mechanism families ([[X86FlagsRegister|FLAGS]] + [[CmpInstruction|`cmp`]] + [[X86JumpInstructions|conditional jumps]]) into the **canonical compilation pattern** for [[CLanguage|C]]'s [[WhileLoop|`while`]] / [[ForLoop|`for`]] / [[DoWhileLoop|`do`–`while`]] constructs at the [[X86_64|x86-64]] [[AssemblyLanguage|assembly]] surface, via a single worked example — `sumUp(int n)`. Headline rules: (1) the **canonical `while`/`for` pattern** is **jump-to-test** — an unconditional `jmp` skips the body, lands at the condition check, and a conditional jump on the **un-negated** loop condition branches **back** to the body (the inverse of [[AsmIfThenElse|Ch 7.4.2]]'s if-pattern, which jumps on the **negated** condition forward over the body); (2) `for` and `while` produce **identical assembly** — *"every `for` loop can be represented by a `while` loop"* — the three-clause `for` mechanically decomposes into init / `while (cond) { body; step; }`.

## Key Claims

- **Loops at the assembly level are jumps that branch backward.** The architecture has no dedicated loop construct — *"loops in [[AssemblyLanguage|assembly]] rely on [[X86JumpInstructions|jump instructions]] to revisit code blocks based on condition evaluation."* The structural shape is: jump-target label → body → condition → conditional jump back to label.
- **The canonical `while` pattern is jump-to-test.** The compiler emits an **unconditional [[X86JumpInstructions|`jmp`]] to the condition check** first, falls through into the **condition + conditional jump back to the body label** at the bottom. The conditional jump uses the **un-negated** loop condition — opposite of [[AsmIfThenElse|Ch 7.4.2]]'s if-pattern (which jumps on the **negated** condition forward to skip the then-branch). The `sumUp` trace lands `jmp 0x400547` → body at `0x40053d` → `cmp` at `0x400547`-`0x40054a` → `jle 0x40053d` (branch back if `i ≤ n` still holds).
- **`for` and `while` compile to identical assembly.** *"Every `for` loop can be represented by a `while` loop."* The three-clause `for (init; cond; step) { body; }` decomposes mechanically to `init; while (cond) { body; step; }` — same loop variable, same condition, same termination, same emitted instructions. The optimizer sees only the post-decomposition form.
- **`do`–`while` skips the leading `jmp`.** Because the body executes unconditionally on first entry (the [[DoWhileLoop|always-at-least-once]] property), the do-while pattern is **simpler** than `while`/`for` — no jump-to-test prologue, just **body → condition + conditional jump back to body**. This is the **structural difference** between the two loop families at the assembly surface.
- **Test-before-body vs. test-after-body is preserved by codegen.** *"Test conditions typically execute before the body (except do-while)."* `while`/`for` always check the condition before executing the body even on first iteration (hence the leading `jmp` to the test); `do`–`while` always runs the body once before checking.
- **Stack-resident loop variables; `%eax` as the comparison shuttle.** In the unoptimized `sumUp` trace, `total` lives at `%rbp-0x8` and `i` at `%rbp-0x4`; the `%eax` register loads `i` into the [[CmpInstruction|`cmp`]] producer and writes the updated `total` back. The body's `add` / `mov` instructions modify the stack-resident locals, then the loop control sequence (`mov i, %eax` + `cmp %eax, n` + `jle body`) decides whether to branch back.
- **Loop continuation hinges on a single [[X86FlagsRegister|FLAGS]] read after [[CmpInstruction|`cmp`]].** The conditional jump that closes the loop consumes the same SF/OF/ZF/CF set by the trailing `cmp` — same mechanism as the if-pattern of [[AsmIfThenElse|Ch 7.4.2]], but with the **direction of the jump reversed** (backward to the body label rather than forward over an else-branch) and the **polarity un-negated** (jump *while* the condition holds, rather than *unless* it holds).

## Key Quotes

> "Loops in assembly rely on jump instructions to revisit code blocks based on condition evaluation. The architecture doesn't have dedicated loop constructs; instead, conditional and unconditional jumps implement loop logic."

> "Every `for` loop can be represented by a `while` loop." — `for` and `while` compile to identical assembly.

> "Test conditions typically execute before the body (except do-while)." — preserves the source-language semantics across the codegen layer.

## The `sumUp` worked example

The chapter's running example sums `1..n`:

```c
int sumUp(int n) {
    int total = 0;
    int i = 1;
    while (i <= n) {
        total += i;
        i++;
    }
    return total;
}
```

Compiled to unoptimized [[X86_64|x86-64]] [[AssemblyLanguage|assembly]] (locals at `%rbp-0x8` for `total` and `%rbp-0x4` for `i`), the loop body sits at `0x40053d` and the structure is:

| Address    | Instruction               | Role                                                        |
|------------|---------------------------|-------------------------------------------------------------|
| `0x40053b` | `jmp 0x400547`            | **Jump-to-test** prologue — skip body on first entry         |
| `0x40053d` | body (`add` / `mov` ops)  | Update `total`, increment `i`                                |
| `0x400547` | `mov -0x4(%rbp), %eax`    | Load `i` into the comparison shuttle                        |
| `0x40054a` | `cmp %eax, ...`           | Set [[X86FlagsRegister|FLAGS]] from `n − i`                  |
| `0x40054d` | `jle 0x40053d`            | **Branch back** to body while `i ≤ n`                        |

The shape — *unconditional `jmp` forward to the test, conditional jump backward from the test to the body* — is the canonical [[AsmLoopPattern|loop compilation pattern]] for [[WhileLoop|`while`]] and [[ForLoop|`for`]].

## Connections

- [[DiveIntoSystems]] — source book. **69th ingested chapter — third leaf of Ch 7.4.**
- [[dis-7-4-x86-64-conditional-loops]] — parent hub.
- [[dis-7-4-1-x86-64-preliminaries]] — the [[X86FlagsRegister|FLAGS]] + [[CmpInstruction|`cmp`]] + [[X86JumpInstructions|jump-family]] mechanism layer this section operationalizes.
- [[dis-7-4-2-x86-64-if-statements]] — **sibling leaf**; same mechanism families compiled into the **forward-jump-on-negated-condition** if-pattern, contrasting with this section's **backward-jump-on-un-negated-condition** loop pattern.
- [[X86_64]] / [[AssemblyLanguage]] / [[X86JumpInstructions]] / [[CmpInstruction]] / [[X86FlagsRegister]] — mechanism layer.
- [[WhileLoop]] / [[ForLoop]] / [[DoWhileLoop]] — source-language constructs this section translates.
- [[ControlFlow]] / [[CLanguage]] — abstraction layer.
- [[InstructionPointer]] — the register the jump-family writes to indirectly.
- [[AsmIfThenElse]] — the if-statement compilation pattern from the sibling leaf, contrasted in pattern direction (forward vs. backward) and polarity (negated vs. un-negated).
- New concept page minted by this ingest:
  - [[AsmLoopPattern]] — the canonical jump-to-test loop compilation pattern, covering all three of [[WhileLoop|`while`]] / [[ForLoop|`for`]] / [[DoWhileLoop|`do`–`while`]] with the structural distinction between test-first and test-last forms.

## Contradictions

None — extends the [[dis-7-4-1-x86-64-preliminaries|Ch 7.4.1]] / [[dis-7-4-2-x86-64-if-statements|Ch 7.4.2]] picture along the loop axis without revising it.
