---
title: "Dive into Systems — Ch 9.4 Conditional Control and Loops (ARMv8)"
type: source
tags: [book, dive-into-systems, arm64, armv8, assembly, control-flow, conditionals, loops, hub]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C9-ARM64/conditional_control_loops.html
sources: []
last_updated: 2026-05-17
---

## Summary

**Fourth leaf** of Ch 9 *64-bit ARM Assembly* of *[[DiveIntoSystems]]* and the **hub page** opening the three-subsection treatment of [[ControlFlow|control flow]] at the [[ARM64|AArch64]] [[AssemblyLanguage|assembly]] level. **Non-twin structural sibling** of [[dis-7-4-x86-64-conditional-loops|Ch 7.4]] / [[dis-8-4-ia32-conditional-loops|Ch 8.4]] — pivots from [[dis-9-3-arm64-arithmetic|Ch 9.3]]'s **straight-line arithmetic / shift / bitwise surface** to **branch-driven non-sequential execution**. The chapter explains how compilers translate [[CLanguage|C]]'s [[IfStatement|`if` / `else`]] and [[WhileLoop|`while`]] / [[ForLoop|`for`]] / [[DoWhileLoop|`do`–`while`]] constructs into [[ARM64]] instructions that **modify the `pc` program counter** based on evaluated conditions. Hub-only — three subsections (9.4.1 Preliminaries, 9.4.2 If Statements, 9.4.3 Loops) deliver the mechanisms.

## Key Claims

- **Conditional control as `pc` modification.** The compiler translates [[CLanguage|C]] conditionals into instructions that **conditionally overwrite `pc`** rather than letting it advance to the next sequential instruction — same primitive structure as [[dis-7-4-x86-64-conditional-loops|Ch 7.4]]'s `%rip` modification, but with the [[ARM64]] **[[ARM64FlagsRegister|NZCV flag register]]** and the **`b.cond`** conditional-branch family ([[ARM64ConditionalBranch|`b.eq` / `b.ne` / `b.lt` / `b.gt` / ...]]) in place of [[X86FlagsRegister|x86 FLAGS]] and the [[X86JumpInstructions|`jXX`]] family.
- **Three-subsection partition.** Ch 9.4 splits the control-flow surface into:
  - **9.4.1 Preliminaries** — the [[ARM64FlagsRegister|NZCV condition-flag register]], the [[ARM64Cmp|`cmp` / `cmn` / `tst`]] comparison instructions, the [[ARM64ConditionalBranch|`b.cond`]] family, and the [[ARM64ConditionalSelect|`csel`]] conditional-select instruction — the mechanism set 9.4.2 and 9.4.3 compose.
  - **9.4.2 If Statements in Assembly** — the [[IfStatement|`if`]] / [[ElseStatement|`else`]] compilation pattern — `cmp` + `b.cond`-on-negated-condition, plus the **branch-free `csel`** alternative.
  - **9.4.3 Loops in Assembly** — the [[WhileLoop|`while`]] / [[ForLoop|`for`]] / [[DoWhileLoop|`do`–`while`]] compilation patterns — same `cmp` + `b.cond` primitive re-composed into a **backward-branching shape**.
- **[[CCompiler|Compiler]] view of control flow.** Same compiler-mechanic framing as [[dis-7-4-x86-64-conditional-loops|Ch 7.4]] / [[dis-8-4-ia32-conditional-loops|Ch 8.4]] — given a [[CLanguage|C]] `if` or loop, what [[ARM64]] instruction sequence does the compiler emit?

## Key Quotes

> "Modify the program counter to alter program flow based on evaluated conditions." — the structural definition of conditional control at the [[ARM64]] ISA level.

## Connections

- [[DiveIntoSystems]] — parent textbook; this is the **94th ingested chapter** / **fourth leaf of Ch 9**.
- [[dis-9-3-arm64-arithmetic]] — immediate predecessor; closed the [[ARM64]] arithmetic / shift / bitwise instruction surface.
- [[dis-9-2-arm64-common]] / [[dis-9-1-arm64-basics]] — Ch 9.4 builds atop the [[ARM64DataMovement|data-movement]] primitives and the [[ARM64|register / addressing-mode]] framework.
- [[dis-7-4-x86-64-conditional-loops]] / [[dis-8-4-ia32-conditional-loops]] — structural siblings (non-twins): same three-subsection split, different ISA mechanism set.
- [[ARM64FlagsRegister]] / [[ARM64ConditionalBranch]] / [[ARM64Cmp]] / [[ARM64ConditionalSelect]] — the four mechanism pages 9.4 introduces.
- [[ControlFlow]] / [[ARM64]] — the umbrella concept and host ISA.

## Subsections (delivered as separate leaf ingests)

- **9.4.1 Preliminaries** ([[dis-9-4-1-arm64-preliminaries]]) — NZCV flags + `cmp` / `cmn` / `tst` + `b.cond` + `csel`.
- **9.4.2 If Statements in Assembly** ([[dis-9-4-2-arm64-if-statements]]) — `if` / `else` compilation pattern + `csel` branch-free form.
- **9.4.3 Loops in Assembly** ([[dis-9-4-3-arm64-loops]]) — `while` / `for` / `do`–`while` backward-branch pattern.

## Contradictions

None. Ch 9.4 **extends** the Ch 9 instruction-family tour with the control-flow category — adds rather than revises. The [[ARM64FlagsRegister|NZCV]] flag scheme is an **alternative ISA-design answer** to [[X86FlagsRegister|x86 FLAGS]] (ZF/SF/OF/CF), not a contradiction; the **`b.cond`** branch family and **`csel`** conditional-select are the [[ARM64]] analogs of [[X86JumpInstructions|`jXX`]] and [[X86ConditionalMove|`cmov`]].
