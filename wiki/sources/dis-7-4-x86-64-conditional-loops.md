---
title: "Dive into Systems — Ch 7.4 Conditional Control and Loops (x86-64)"
type: source
tags: [dive-into-systems, x86-64, assembly, control-flow, conditionals, loops, hub]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C7-x86_64/conditional_control_loops.html
sources: []
last_updated: 2026-05-17
---

## Summary

Chapter 7.4 of *[[DiveIntoSystems]]* — **fourth leaf** of Ch 7 *x86-64 Assembly* and the **hub page** opening the three-subsection treatment of [[ControlFlow|control flow]] at the [[X86_64|x86-64]] [[AssemblyLanguage|assembly]] level. Follows [[dis-7-3-x86-64-arithmetic|Ch 7.3]]'s extended-arithmetic / bit-shift / bitwise / `lea` surface and pivots from **straight-line code** to **branch-driven non-sequential execution** — how the compiler translates [[CLanguage|C]]'s [[IfStatement|`if` / `else`]] and [[WhileLoop|`while`]] / [[ForLoop|`for`]] / [[DoWhileLoop|`do`–`while`]] constructs into instructions that **modify the [[InstructionPointer|`%rip`]] instruction pointer** based on evaluated conditions. Hub-only — three subsections deliver the mechanisms.

## Key Claims

- **Conditional control as `%rip` modification.** *"The material explains how compilers translate conditional expressions into assembly instructions that modify the [[InstructionPointer|instruction pointer]] to alter program flow based on evaluated conditions"* — every [[IfStatement|`if`]] / loop / [[SwitchStatement|`switch`]] in the source language compiles down to an instruction sequence that **conditionally overwrites `%rip`** rather than letting it advance to the next sequential instruction. The control-flow primitive at the ISA level is *"modify `%rip` if condition holds"*, not *"jump to label"*.
- **Three-subsection partition.** Ch 7.4 splits the control-flow surface into:
  - **7.4.1 Preliminaries** — the condition-evaluation machinery (condition codes / flag bits / comparison instructions / conditional-jump instructions) that 7.4.2 and 7.4.3 will compose into higher-level constructs.
  - **7.4.2 If Statements in Assembly** — the **[[IfStatement|`if`]] / [[ElseStatement|`else`]] / [[ElseStatement|`else if`]] family** — branch-on-condition with a fall-through path and an unconditional-jump-to-skip-the-else pattern.
  - **7.4.3 Loops in Assembly** — the **three [[CLanguage|C]] loop forms** ([[WhileLoop|`while`]] / [[ForLoop|`for`]] / [[DoWhileLoop|`do`–`while`]]) — same primitive (conditional jump) re-composed into a backward-branching shape.
- **[[CCompiler|Compiler]] view of control flow.** The chapter framing is **compiler-mechanic**, not assembly-programmer: the question is *"given a [[CLanguage|C]] `if` / loop, what instruction sequence does the compiler emit?"* — operationalizing the [[dis-6-asm-intro|Ch 6]] *"closest a programmer gets to coding at the machine level"* claim by exposing the gap between high-level [[ControlFlow|control-flow]] syntax and the low-level **conditional-jump primitive** the hardware actually executes.
- **Continuity with prior x86-64 chapters.** Hub builds on the **register / operand / addressing-mode** scaffolding from [[dis-7-1-x86-64-basics|Ch 7.1]], the **data-movement / stack** primitives from [[dis-7-2-x86-64-common|Ch 7.2]], and the **arithmetic / bitwise / shift** surface from [[dis-7-3-x86-64-arithmetic|Ch 7.3]] — adds the **fourth instruction-family category** ([[dis-6-asm-intro|Ch 6]]'s four-category partition: arithmetic/logic, data movement, stack, **control flow**) that completes the per-ISA tour.

## Key Quotes

> "Modify the [[InstructionPointer|instruction pointer]] to alter program flow based on evaluated conditions." — the chapter's structural definition of conditional control at the ISA level; the **`%rip`-as-control-flow-variable** abstraction every subsection elaborates.

## Connections

- [[DiveIntoSystems]] — parent textbook; this is the **66th ingested chapter**.
- [[dis-7-3-x86-64-arithmetic]] — immediate predecessor; Ch 7.3 closed the **arithmetic / bit-shift / bitwise / `lea`** instruction families. Ch 7.4 pivots to the **control-flow** family.
- [[dis-7-2-x86-64-common]] — Ch 7.2's [[X86MovInstruction|`mov`]] / [[X86ArithmeticInstructions|`add` / `sub`]] / [[X86StackInstructions|`push` / `pop`]] primitives remain in use; Ch 7.4 adds branches over the same operands.
- [[dis-7-1-x86-64-basics]] — register / operand / addressing-mode framework; the conditional-jump instructions Ch 7.4.1 introduces are constrained by the same operand grammar.
- [[dis-1-3-conditionals-loops]] — **the [[CLanguage|C]]-level original** of the constructs Ch 7.4 compiles down — [[IfStatement|`if`]] / [[ElseStatement|`else`]], [[WhileLoop|`while`]] / [[DoWhileLoop|`do`–`while`]] / [[ForLoop|`for`]], [[BreakStatement|`break`]] / [[ContinueStatement|`continue`]]. Ch 7.4 = the assembly-side complement.
- [[InstructionPointer]] — the **`%rip` register** that conditional control modifies; the control-flow primitive at the [[X86_64|x86-64]] ISA level.
- [[ControlFlow]] — the umbrella concept; Ch 7.4 delivers its [[X86_64|x86-64]] assembly realization.
- [[X86_64]] — the ISA; Ch 7.4 adds the control-flow instruction family to its wiki-cataloged surface.

## Subsections (deferred to leaf ingests)

- **7.4.1 Preliminaries** — condition codes / comparison + conditional-jump instructions.
- **7.4.2 If Statements in Assembly** — [[IfStatement|`if`]] / [[ElseStatement|`else`]] compilation pattern.
- **7.4.3 Loops in Assembly** — [[WhileLoop|`while`]] / [[ForLoop|`for`]] / [[DoWhileLoop|`do`–`while`]] compilation patterns.

## Contradictions

None. Ch 7.4 **extends** the Ch 7 instruction-family tour with the control-flow category — adds rather than revises.
