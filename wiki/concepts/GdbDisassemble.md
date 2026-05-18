---
title: "GDB `disassemble` (`disass`)"
type: concept
tags: [gdb, debugging, assembly, low-level]
sources: [dis-3-5-gdb-assembly]
last_updated: 2026-05-17
---

# GDB `disassemble` (`disass`)

**`disassemble`** (typically abbreviated **`disass`**) is the [[GDB]] command that **prints the [[AssemblyLanguage|assembly]] instructions** for a function or an address range — the entry point to **assembly-level debugging** when the [[CLanguage|C]] source view runs out.

Three canonical forms ([[dis-3-5-gdb-assembly|DIS Ch 3.5]]):

- `disass main` — print the full assembly for the named function (resolved via [[DebugSymbol|symbol table]]).
- `disass 0x1234 0x1248` — print instructions in the address range `[start, end)`.
- `disass` (bare) — print assembly for the **current** function (the one containing `%rip` / `%eip`).

The output is the [[AssemblyLanguage|assembly]] dialect for the binary's target [[ISA]] — AT&T-syntax x86-64 / [[IA32|IA-32]] under default GNU [[GCC|`gcc`]] builds, ARM / RISC-V if the binary was cross-compiled. Each line shows the instruction address, opcode mnemonic, and operands; the **current [[InstructionPointer|PC]]** is marked with `=>` so you can see where execution is paused relative to the surrounding code.

## When to reach for it

The [[dis-3-2-gdb-commands|Ch 3.2]] rule — *"compiler-optimized code is often very difficult to debug because sequences of optimized machine code often do not clearly map back to C source code"* — is the headline use case: under [[CompilerOptimization|`-O2`]], [[StepDebug|`step` / `next`]] jumps around the source file in ways that defeat source-level reasoning, and `disass` is the escape hatch. Other canonical situations: stripped binaries with no [[DebugSymbol|symbols]], crashes inside [[CLibrary|libc]] / vendor blobs, hand-written `.s` files ([[dis-2-9-7-c-to-assembly|Ch 2.9.7]]), reverse-engineering, and verifying that the compiler emitted the instruction sequence you expected.

## Companion: `x/i $pc`

The [[GdbExamineMemory|`x` examine-memory]] primitive in **instruction format** — `x/i $pc` — prints the **single next instruction** at the [[InstructionPointer|program counter]]. The two-command pair `disass` (whole function context) + `x/i $pc` (live one-line view) is the standard assembly-level inspection loop, often paired with [[GdbDisplay|`display/i $pc`]] to auto-print at every [[GdbStepi|`stepi`]] halt.

## Pairs with

- [[GdbStepi|`stepi` / `nexti`]] — single-instruction stepping; `disass` shows the map, `stepi` walks it.
- [[CpuRegister|`info registers`]] — register-file inspection at each step.
- [[InstructionPointer|`%rip` / `%eip`]] — the *"you are here"* marker in the disassembly.
- [[Breakpoint|`break *0x...`]] — address-based breakpoint at an instruction `disass` revealed.
- [[DataDisplayDebugger|DDD]] — its separate disassembly window is `disass` made always-on.
