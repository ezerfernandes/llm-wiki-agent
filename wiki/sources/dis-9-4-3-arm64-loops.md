---
title: "Dive into Systems — Ch 9.4.3 Loops in Assembly (ARM64)"
type: source
tags: [book, dive-into-systems, arm64, armv8, assembly, control-flow, loops, while-loop, for-loop]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C9-ARM64/loops.html
sources: []
last_updated: 2026-05-17
---

## Summary

**Third leaf** of [[dis-9-4-arm64-conditional-loops|Ch 9.4]] of *[[DiveIntoSystems]]*. Re-composes the [[dis-9-4-1-arm64-preliminaries|Ch 9.4.1]] mechanism set ([[ARM64Cmp|`cmp`]] + [[ARM64ConditionalBranch|`b.cond`]]) into the **backward-branching shape** that implements [[CLanguage|C]]'s three loop forms — [[WhileLoop|`while`]] / [[ForLoop|`for`]] / [[DoWhileLoop|`do`–`while`]] — on [[ARM64|AArch64]]. **Non-twin structural sibling** of [[dis-7-4-3-x86-64-loops|Ch 7.4.3]] / [[dis-8-4-3-ia32-loops|Ch 8.4.3]] — same loop-as-conditional-backward-branch primitive, [[ARM64]] mnemonics. **97th ingested DIS chapter — third leaf of Ch 9.4.**

## Key Claims

- **Loops = backward-branch composition.** *"Like if statements, loops in assembly are also implemented using branch instructions. However, loops enable instructions to be revisited based on the result of an evaluated condition."* The compiler emits a [[ARM64Cmp|`cmp`]] followed by a [[ARM64ConditionalBranch|`b.cond`]] whose target address is **earlier** in the instruction stream than the branch itself — backward control transfer realizes the iteration.
- **`while` / `for` collapse to the same shape.** *"Every `for` loop can be represented by a while loop."* The `for` loop's **initialization**, **condition test**, and **step** are emitted as ordinary sequential instructions surrounding a `while`-shaped condition + body + backward-branch. The text demonstrates `for (i = 1; i <= n; i++) { total += i; }` compiles to **identical assembly** as the corresponding `while` loop.
- **Worked example: `sumUp()`.** The `sumUp(int n)` function (sum of 1..n) demonstrates the canonical loop assembly:
  ```assembly
  0x0758: ldr   w1, [sp, #28]    // load i
  0x075c: ldr   w0, [sp, #12]    // load n
  0x0760: cmp   w1, w0           // compare i and n (sets NZCV)
  0x0764: b.le  0x73c            // branch back if i <= n
  ```
  The [[LoadStoreArchitecture|load/store discipline]] is visible — operands are pulled from stack slots into registers, compared, and the conditional branch consumes the resulting NZCV state.
- **`do`–`while` reuses the same primitive.** A `do`–`while` is the **degenerate case** where the condition test + backward branch appear at the **end** of the body — no entry-test branch needed because the body is unconditionally entered once.

## Key Quotes

> "Like if statements, loops in assembly are also implemented using branch instructions. However, loops enable instructions to be revisited based on the result of an evaluated condition."

> "Every for loop can be represented by a while loop."

## Connections

- [[DiveIntoSystems]] — host textbook; third leaf of [[dis-9-4-arm64-conditional-loops|Ch 9.4]].
- [[dis-9-4-1-arm64-preliminaries]] — supplies [[ARM64Cmp|`cmp`]] + [[ARM64ConditionalBranch|`b.cond`]] composed here.
- [[dis-9-4-2-arm64-if-statements]] — sibling leaf; same primitive, forward-branch shape vs this leaf's backward-branch shape.
- [[dis-7-4-3-x86-64-loops]] / [[dis-8-4-3-ia32-loops]] — non-twin structural siblings.
- [[WhileLoop]] / [[ForLoop]] / [[DoWhileLoop]] / [[LoadStoreArchitecture]] / [[ARM64]] — supporting concepts.

## Contradictions

None. Re-confirms the [[dis-1-3-conditionals-loops|Ch 1.3]] source-level claim that all three [[CLanguage|C]] loop forms reduce to the same control-flow primitive — operationalized at the [[ARM64]] [[AssemblyLanguage|assembly]] surface.
