---
title: "GCC (GNU Compiler Collection)"
type: concept
tags: [compiler, toolchain, gcc, c-language]
sources: [dis-1-1-getting-started, dis-2-9-5-libraries]
last_updated: 2026-05-17
---

# GCC (GNU Compiler Collection)

**GCC** is the canonical [[CCompiler|C compiler]] used throughout [[DiveIntoSystems]]. It translates [[CLanguage|C]] source files into a [[BinaryExecutable|binary executable]] the [[ComputerHardware|hardware]] can directly run.

## Basic usage (per [[dis-1-1-getting-started|Ch 1.1]])

```
$ gcc hello.c              # produces ./a.out by default
$ ./a.out
$ gcc -o hello hello.c     # -o names the output binary
$ ./hello
```

## Common flags introduced in Ch 1.1

- `-o <name>` — name the output executable instead of the default `a.out`.
- `-Wall` — enable all common warnings (the recommended default).
- `-g` — include debug symbols so [[GDB|`gdb`]] / other debuggers can show source-level info.
- `-lm` — **link the math library**. `#include <math.h>` alone is not enough — `libm` must be linked explicitly when the program uses `sqrt`, `sin`, `pow`, etc.

## Compile-pipeline flags ([[dis-2-9-5-libraries|Ch 2.9.5]])

| Flag | Stage | Purpose |
|---|---|---|
| `-E` | 1 [[PreprocessingStage|preprocess]] | Stop after preprocessing — emit expanded source. |
| `-S` | 2 [[CompilationStage|compile]] | Stop after compilation — emit `.s` [[AssemblyLanguage|assembly]]. |
| `-c` | 3 [[AssemblyStage|assemble]] | Stop after assembly — emit `.o` [[ObjectFile|object file]]. |
| `-l<name>` | 4 [[LinkingStage|link]] | Link `lib<name>.{so,a}` from the library search path. |
| `-L<path>` | 4 link | Add `<path>` to the library search path. |
| `-I<path>` | 1 preprocess | Add `<path>` to the header search path. |
| `--static` | 4 link | Force [[StaticLinking|static linking]] (archive only — no `.so`). |
| `-pthread` | 1+4 | Enable [[PThreads|pthreads]] (preferred over `-lpthread` — also defines `_REENTRANT`). |
| `-shared -fPIC` | 4 link | Build a [[DynamicLibrary|`.so`]] shared object instead of an executable. |

Per [[dis-2-9-5-libraries|Ch 2.9.5]], `-l<name>` is an abstraction over the literal `lib<name>.{so,a}` filename — *"this level of abstraction enables programmers to be flexible about the desired linking type."* The compiler chooses [[DynamicLinking|dynamic]] when both `.so` and `.a` exist.

## Position in the toolchain

GCC sits at the source→binary step of the [[CompilationProcess]] — the five-stage pipeline [[PreprocessingStage|preprocess]] → [[CompilationStage|compile]] → [[AssemblyStage|assemble]] → [[LinkingStage|link-edit]] → [[RuntimeLinking|runtime link]] per [[dis-2-9-5-libraries|Ch 2.9.5]]. On the Rust side of the wiki, the analogous role is filled by [[Rustc|`rustc`]] driven by [[Cargo]].

## Connections

- [[CLanguage]] — the language GCC compiles.
- [[CCompiler]] — the role GCC plays.
- [[CompilationProcess]] — the multi-stage pipeline GCC orchestrates.
- [[BinaryExecutable]] — its output.
- [[DiveIntoSystems]] / [[dis-1-1-getting-started]] — the textbook context.
- [[Rustc]] — the parallel role on the Rust side of the wiki.
