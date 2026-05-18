---
title: "Dive into Systems — Ch 3.5 Debugging Assembly Code"
type: source
tags: [book, textbook, dive-into-systems, debugging, gdb, assembly, low-level]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C3-C_debug/gdb_assembly.html
---

## Summary

Chapter 3.5 of *[[DiveIntoSystems]]* extends the [[dis-3-1-gdb|Ch 3.1]] / [[dis-3-2-gdb-commands|Ch 3.2]] / [[dis-3-4-gdb-advanced|Ch 3.4]] [[GDB]] block to **debugging at the [[AssemblyLanguage|assembly-instruction]] level** — the workflow you need when the [[CLanguage|C]] source view runs out (stripped binaries, [[CompilerOptimization|`-O2`]] code that does not map cleanly back to source, hand-written `.s` files, or [[SegmentationFault|crashes]] inside [[CLibrary|library]] code). Introduces four primitives layered on the existing [[GDB]] vocabulary: [[GdbDisassemble|`disass`]] to print the assembly for a function or address range, [[GdbStepi|`stepi` / `nexti`]] for single-instruction stepping (the assembly-level dual of [[StepDebug|`step` / `next`]]), `info registers` / `print $rax` for [[CpuRegister|CPU-register]] inspection, and `break *0x...` for **address-based [[Breakpoint|breakpoints]]**. Names the [[InstructionPointer|instruction pointer]] (`%rip` / `%eip`) as the register that ties all of this together — the source-of-truth for *"where am I executing right now"* once you leave the source view. Closes by recommending [[DataDisplayDebugger|DDD]]'s separate disassembly / register / command windows for assembly-level work.

## Key Claims

- **Assembly-level debugging is necessary** when there is no source (stripped binaries, libc internals), when compiler optimizations break the source-to-instruction mapping, or when debugging hand-written assembly.
- **[[GdbDisassemble|`disass` / `disassemble`]]** prints the assembly instructions for a function or address range: `disass main` (whole function), `disass 0x1234 0x1248` (address-range slice). The companion `x/i $pc` form ([[GdbExamineMemory|`x` examine memory]] in instruction format) shows the next instruction at the current [[InstructionPointer|PC]].
- **[[GdbStepi|`stepi` / `si`]] and `nexti` / `ni`** are the assembly-level duals of [[StepDebug|`step` / `next`]]: `stepi` advances **one machine instruction** and steps **into** call instructions; `nexti` advances one instruction but treats `call` as atomic (runs the called function to completion at debugger speed). Re-establishes the [[dis-3-2-gdb-commands|Ch 3.2]] *"to inspect the function's behavior, use `step` instead of `next`"* rule, one abstraction level lower.
- **`info registers`** dumps the entire [[CpuRegister|register file]] (`%rax` / `%rbx` / `%rcx` / `%rdx` / `%rsi` / `%rdi` / `%rbp` / `%rsp` / `%rip` / `%eflags` on x86-64); **`print $rax`** prints a single register; **`display $rax`** ([[GdbDisplay]]) re-prints after every halt.
- **The [[InstructionPointer|instruction pointer]] register** (`%rip` on x86-64, `%eip` on [[IA32|IA-32]]) **holds the address of the next instruction to execute** — it is the assembly-level analog of the [[StepDebug|`step`]] cursor in source view.
- **Address-based [[Breakpoint|breakpoints]]** via `break *0x080483c1` halt at a specific machine-code address (no source-line equivalent needed) — the primitive you use when [[GdbDisassemble|`disass`]] reveals an interesting instruction.
- **Memory examination** with `x/d 0x40062d` / `x/s 0x40062d` / `x/4c 0x40062d` reads bytes at an absolute address in decimal / string / character form ([[GdbExamineMemory|`x` examine memory]] revisited at the assembly level).
- **[[DataDisplayDebugger|DDD]] for assembly work** provides separate windows for the disassembly view, the register file, and the command prompt — easier than the all-in-one [[GDB]] CLI when single-stepping through dozens of instructions.

## Key Quotes

> *"The `si` command steps into function calls, meaning that GDB will pause the program at the first instruction of the called function."*

> *"`disass main`"* — *"shows assembly for the main function"*; *"`disass 0x1234 0x1248`"* — *"displays instructions between specified addresses"*.

## Connections

- [[DiveIntoSystems]] — Ch 3.5 of the book; closes Ch 3's GDB workflow block (Ch 3.1 narrative + Ch 3.2 reference + Ch 3.3 [[Valgrind]] + Ch 3.4 advanced + Ch 3.5 assembly-level).
- [[dis-3-1-gdb]] / [[dis-3-2-gdb-commands]] — the source-level [[GDB]] foundation this section drops down from.
- [[dis-3-4-gdb-advanced]] — the immediately preceding section; Ch 3.4 covered process / signal / fork features, Ch 3.5 covers assembly / register / instruction features.
- [[dis-2-9-7-c-to-assembly]] — the corpus's first assembly-language section; provides the [[IA32]] / [[AssemblyLanguage]] / [[Objdump]] vocabulary that Ch 3.5 now lets you observe at **runtime** rather than just inspect statically.
- [[GDB]] — the tool whose vocabulary is being extended.
- [[AssemblyLanguage]] / [[IA32]] — the target abstraction level.
- [[GdbDisassemble]] — new concept; the entry point to assembly-level debugging.
- [[GdbStepi]] — new concept; the assembly-level dual of [[StepDebug|`step` / `next`]].
- [[CpuRegister]] — new concept; the register file `info registers` reflects over.
- [[InstructionPointer]] — new concept; `%rip` / `%eip`, the *where-am-I* register.
- [[GdbExamineMemory]] — Ch 3.2's `x/nfu addr` primitive, now applied to instruction-format reads (`x/i $pc`).
- [[GdbPrint]] / [[GdbDisplay]] / [[GdbInfo]] — extended to take `$reg`-prefixed register references.
- [[Breakpoint]] — extended with the `break *0x...` address-based form.
- [[DataDisplayDebugger]] — recommended GUI for the multi-pane assembly workflow.
- [[CompilerOptimization]] — the [[dis-3-2-gdb-commands|Ch 3.2]] *"compiler-optimized code is often very difficult to debug because sequences of optimized machine code often do not clearly map back to C source code"* warning is exactly the situation Ch 3.5 addresses.

## Contradictions

None. Ch 3.5 strictly extends the [[GDB]] vocabulary from Ch 3.1 / 3.2 / 3.4 — every command added here is **new**, not a revision of an existing one.
