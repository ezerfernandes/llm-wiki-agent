---
title: "Compiler vs Linker (Error-Stage Taxonomy)"
type: concept
tags: [toolchain, compiler, linker, build-error, c-language]
sources: [dis-2-9-5-libraries]
last_updated: 2026-05-17
---

# Compiler vs Linker (Error-Stage Taxonomy)

[[dis-2-9-5-libraries|DIS Ch 2.9.5]]'s headline diagnostic insight: **error messages from a C build come from one of four tools at four distinct stages**, and the message identifies which one to blame.

## The four-tool table

| Tool | Stage | Sees | Reports |
|---|---|---|---|
| **Preprocessor** | 1 [[PreprocessingStage|preprocess]] | `#include` paths | *"No such file or directory"* (header not on disk) |
| **[[CCompiler|Compiler]]** | 2 [[CompilationStage|compile]] | C semantics, prototypes | *"implicit declaration"*, *"undeclared identifier"*, type errors |
| **[[Linker|Linker]] (`ld`)** | 4 [[LinkingStage|link-edit]] | Symbol tables across `.o` / `.a` / `.so` | [[UndefinedReferenceError|*"undefined reference"*]], *"multiple definition"* |
| **[[DynamicLinker|Dynamic linker]] (`ld.so`)** | 5 [[RuntimeLinking|launch]] | `NEEDED` `.so` entries, runtime search path | *"cannot open shared object file"* |

The [[AssemblyStage|assembler]] (stage 3) almost never produces errors in normal compile-from-C workflows — its job is mechanical translation.

## Why this taxonomy matters

A **missing header** and a **missing library** are different problems with different fixes — but both look like *"my program doesn't build"* to a novice. The error message names the tool, the tool names the stage, the stage names the fix:

- **Compiler error → C source problem** (forgot `#include`, typo in function name, wrong arg count).
- **Linker error → build-graph problem** (forgot `-l<name>`, wrong link order, missing `.o` file).
- **Runtime loader error → deployment problem** (missing `.so` on target host, [[LDLibraryPath|`LD_LIBRARY_PATH`]] not set).

## The `pow` example (canonical)

```c
#include <math.h>
int main(void) { return pow(2, 10); }
```

- `gcc -c prog.c` → `prog.o` (compile succeeds — prototype visible).
- `gcc prog.o -o prog` → ***"undefined reference to `pow`"*** (link fails — no `libm`).
- `gcc prog.o -lm -o prog` → success.

Remove the `#include <math.h>` line and run `gcc -c prog.c`:
- ***"implicit declaration of function 'pow'"*** (compile fails — prototype missing).

Same `pow` call, two distinct errors, two distinct fixes — the **stage-taxonomy is the lookup key**.

## Connections

- [[dis-2-9-5-libraries]] — introducing source.
- [[CompilationProcess]] — the five-stage pipeline this taxonomy partitions.
- [[CCompiler]] / [[Linker]] / [[DynamicLinker]] — the three main tools.
- [[PreprocessingStage]] / [[CompilationStage]] / [[AssemblyStage]] / [[LinkingStage]] / [[RuntimeLinking]] — the five stages.
- [[UndefinedReferenceError]] — the load-bearing linker-stage error.
- [[HeaderFile]] / [[CLibrary]] — the two artifacts whose absence causes the two main errors.
- [[GCC]] — the driver that invokes all four tools.
