---
title: "Debug Symbols"
type: concept
tags: [debugging, compilation, c-language, gcc, elf, dwarf]
sources: [dis-3-1-gdb]
last_updated: 2026-05-17
---

# Debug Symbols

**Debug symbols** are the metadata a compiler embeds in an executable that lets a [[Debugger|debugger]] map machine-level addresses back to **source-level constructs** — line numbers, variable names, function names, type information, [[StackFrame|stack-frame]] layout. Without them, a debugger sees only addresses and bytes; with them, the debugger can offer source-line breakpoints, named variable inspection, and meaningful [[GdbBacktrace|backtraces]].

[[dis-3-1-gdb|DIS Ch 3.1]] introduces them implicitly through the [[GccDashG|`gcc -g`]] flag — the *load-bearing precondition* for source-level [[GDB]] use.

## What's encoded

The standard format on ELF-using Unix systems is **DWARF** (Debugging With Arbitrary Record Formats). For each compilation unit, DWARF records:

- **Line-number tables** mapping `(file, line) ↔ instruction address` ranges.
- **Symbol tables** mapping `variable name ↔ memory location` (stack offset, register, or static address) per [[VariableScope|scope]].
- **Type definitions** — the full type tree (primitives, [[CStruct|structs]], [[CArray|arrays]], [[Pointer|pointers]], [[Typedef|typedefs]]).
- **Function descriptors** — entry address, [[FunctionParameter|parameter]] list with locations, return-type, frame-layout info for unwinding.
- **Macros** (with [[GccDashG|`-g3`]] only).

## How GDB uses them

When the user runs [[GdbPrint|`print x`]] at a halt point, GDB:
1. Looks up the current instruction address in the DWARF line table → finds the active source line and scope.
2. Looks up `x` in that scope's symbol table → finds the location (e.g., `rbp - 16`) and type (e.g., `int`).
3. Reads the bytes at that location from the debuggee's memory.
4. Formats the bytes per the type and prints them.

Without DWARF entries, step 2 fails — GDB can read the raw bytes but doesn't know they live at `rbp - 16`, what type they are, or even that the variable `x` exists.

## The `gcc -g` family

| Flag | Effect |
|---|---|
| `-g` | Generate standard DWARF debug info (default level 2 on most platforms). |
| `-g0` | No debug info. |
| `-g1` | Minimal — function names and external variables only. Enough for backtraces, not for variable inspection. |
| `-g2` | Default `-g`. Full source-line and variable info. |
| `-g3` | Adds macro definitions (so GDB's `info macro` works). |

## Why **off** during release builds

Debug symbols can **double or triple the binary size**. Production binaries typically strip symbols (`strip a.out` or compile with `-g0`). The conventional split: ship the stripped binary, archive a separate `.debug` file (`objcopy --only-keep-debug a.out a.out.debug`) for use in post-mortem debugging.

## Interaction with optimization

[[dis-3-1-gdb|Ch 3.1]]'s warning: *"compiler-optimized code is often very difficult to debug because sequences of optimized machine code often do not clearly map back to C source code."* The DWARF line table is *still produced* with `-O2 -g`, but it points to instructions that have been reordered, inlined, eliminated, or vectorized — single-stepping jumps around the source unpredictably and *"variable optimized out"* messages appear when a value never landed in memory.

Conventional rule during debugging: **`-O0 -g`**.

## Connections

- [[dis-3-1-gdb]] — introducing source.
- [[GccDashG]] — the build flag that emits debug symbols.
- [[GDB]] / [[Debugger]] — the consumer.
- [[CompilerOptimization]] — the build setting that degrades symbol↔source mapping.
- [[GCC]] — the compiler whose `-g` flag this concept centers on.
- [[Objdump]] — also consumes symbols for disassembly listing.
- [[VariableScope]] — the lexical structure DWARF records mirror.
- [[StackFrame]] — DWARF unwind info describes frame layout per function.
- [[CompilationProcess]] — debug symbols are produced at the [[CompilationStage|compile stage]] and preserved through [[LinkingStage|link]].
- [[CoreFile]] — useful only when matching debug symbols are available.
