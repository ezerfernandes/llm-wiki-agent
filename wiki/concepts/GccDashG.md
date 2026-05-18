---
title: "`gcc -g` (Debug-Info Flag)"
type: concept
tags: [debugging, compilation, gcc, c-language, debug-symbols]
sources: [dis-3-1-gdb]
last_updated: 2026-05-17
---

# `gcc -g` (Debug-Info Flag)

The [[GCC|`gcc`]] compiler flag that **embeds [[DebugSymbol|debug symbols]]** in the produced executable so a source-level [[Debugger|debugger]] like [[GDB]] can map binary addresses back to source lines, variable names, and types. [[dis-3-1-gdb|DIS Ch 3.1]] elevates `-g` to the chapter's **load-bearing precondition** — without it, GDB sees only machine code.

## Canonical invocation

```bash
gcc -g -o buggy buggy.c        # compile with full DWARF debug info
gdb ./buggy                    # GDB can now resolve line:42 ↔ machine address
```

## Levels

| Variant | Effect |
|---|---|
| `-g` | Default — full DWARF (line tables, symbol tables, type info). |
| `-g0` | **No** debug info. Equivalent to omitting `-g`. |
| `-g1` | Minimal — function names and externals; enough for [[GdbBacktrace|`bt`]] but not [[GdbPrint|`print var`]]. |
| `-g3` | Adds macro information; required for `info macro` in GDB. |
| `-ggdb` | Use the format GDB likes best on this platform (DWARF-with-GNU-extensions on most targets). |

## The optimization tradeoff

[[dis-3-1-gdb|Ch 3.1]]'s warning is the chapter's load-bearing rule:

> *"Compiler-optimized code is often very difficult to debug because sequences of optimized machine code often do not clearly map back to C source code."*

The DWARF line table *is still emitted* with `-O2 -g`, but [[CompilerOptimization|optimization]] reorders / inlines / eliminates instructions, so single-stepping jumps around the source non-monotonically and variables show as `<optimized out>` in [[GdbPrint|`print`]] when they never landed in memory.

**Standard debug build flags**: `-O0 -g`. The conventional release vs. debug split:

```bash
gcc -O2          -o release   prog.c   # production: optimized, no symbols
gcc -O0 -g       -o debug     prog.c   # development: unoptimized, full symbols
gcc -O2 -g       -o profile   prog.c   # profiling: optimized but with symbols (perf, gprof)
```

## Build-system integration

In [[Makefile|`make`]] / [[Cargo|`cargo`]] / [[CMake|`cmake`]] / [[Meson|`meson`]] workflows the debug-symbol flag is the default for debug profiles:

- **CMake** — `cmake -DCMAKE_BUILD_TYPE=Debug` → `-O0 -g`.
- **Make** — conventional `CFLAGS = -O0 -g` in the debug target.
- **Cargo** — `cargo build` (debug profile) implies `[profile.dev] debug = true` which is `-g`-equivalent for the Rust toolchain.

## Size cost

Debug symbols typically **double or triple binary size**. Standard practice:
- Build with `-g`.
- Strip for distribution: `strip ./buggy` removes the DWARF sections from the on-disk binary.
- Archive the symbols separately: `objcopy --only-keep-debug ./buggy ./buggy.debug` — match up later when investigating a [[CoreFile|core file]] from a stripped binary.

## Connections

- [[dis-3-1-gdb]] — introducing source.
- [[DebugSymbol]] — what `-g` emits.
- [[GDB]] / [[Debugger]] — the consumer of the symbols.
- [[CompilerOptimization]] — the orthogonal axis (`-O0` … `-O3` / `-Os` / `-Oz`) `-g` interacts with.
- [[GCC]] — the compiler this flag belongs to.
- [[Objdump]] — also consumes the symbols (for annotated disassembly listing).
- [[CompilationProcess]] — `-g` affects the [[CompilationStage|compile]] and [[AssemblyStage|assemble]] stages; symbols survive through [[LinkingStage|link]] into the final ELF.
- [[CoreFile]] — useful only when the matching `-g` build is available to overlay onto the dump.
