---
title: "GDB `stepi` / `nexti` (Single-Instruction Stepping)"
type: concept
tags: [gdb, debugging, assembly, low-level, stepping]
sources: [dis-3-5-gdb-assembly]
last_updated: 2026-05-17
---

# GDB `stepi` / `nexti` (Single-Instruction Stepping)

**`stepi`** (abbreviated **`si`**) and **`nexti`** (**`ni`**) are the [[AssemblyLanguage|assembly]]-level duals of [[StepDebug|`step` / `next`]]: each advances the debuggee by **exactly one machine instruction** rather than one source line. The pair is the granular *execution-control* primitive that the [[dis-3-5-gdb-assembly|Ch 3.5]] [[GDB]] block introduces.

## The step-into vs step-over distinction, restated

The [[dis-3-2-gdb-commands|Ch 3.2]] rule — *"to inspect the function's behavior, use `step` instead of `next`"* — applies again, one abstraction level lower:

- **`stepi`** advances one instruction and **steps into `call` instructions**, halting at the first instruction of the called function. *"The `si` command steps into function calls, meaning that GDB will pause the program at the first instruction of the called function."*
- **`nexti`** advances one instruction but treats `call` as **atomic** — the entire callee runs to completion (at debugger speed) before [[GDB]] returns control.

So `stepi` is the assembly equivalent of [[StepDebug|`step`]] and `nexti` is the assembly equivalent of [[StepDebug|`next`]] — same call-handling distinction, instruction-grained instead of line-grained.

## When to reach for it

Whenever you need to observe each instruction's effect on the [[CpuRegister|register file]] or memory — verifying a [[CompilerOptimization|compiler-optimized]] sequence, debugging hand-written [[AssemblyLanguage|assembly]] ([[dis-2-9-7-c-to-assembly|Ch 2.9.7]]), walking through a stripped binary, or tracing a [[SegmentationFault|crash]] inside library code where no source is available. Source-level [[StepDebug|`step`]] is too coarse when one source line expands into a dozen instructions; `stepi` is the only command that gives the per-instruction view.

## Pairs with

- [[GdbDisassemble|`disass`]] — print the map you are walking with `stepi`.
- [[GdbDisplay|`display/i $pc`]] — auto-print the next instruction at every halt, the standard companion display.
- [[CpuRegister|`info registers`]] — inspect the register file between each step.
- [[InstructionPointer|`%rip` / `%eip`]] — advances by the instruction's byte width on each `stepi`.
- [[StepDebug|`step` / `next`]] — the source-level analogs; same call-handling distinction.
