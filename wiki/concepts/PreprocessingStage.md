---
title: "Preprocessing Stage"
type: concept
tags: [c-language, preprocessor, toolchain, compilation-process]
sources: [dis-2-9-5-libraries]
last_updated: 2026-05-17
---

# Preprocessing Stage

The **preprocessing stage** is stage 1 of the five-stage [[CompilationProcess|compile pipeline]] [[dis-2-9-5-libraries|DIS Ch 2.9.5]] codifies. The C preprocessor (a textual pass that doesn't understand C syntax) interprets `#`-prefixed [[PreprocessorDirective|preprocessor directives]] — splicing in [[HeaderFile|headers]] via `#include`, substituting [[CConstant|`#define`]] macros, and resolving `#if` / `#ifdef` conditional compilation.

## Output

An **expanded translation unit** — pure C with every directive resolved. [[GCC|`gcc -E foo.c`]] stops after preprocessing and emits the result to stdout (typically thousands of lines once `<stdio.h>` has been spliced in).

## `-I<path>` extends the header search path

The default `<header.h>` search path on Linux is `/usr/include`, `/usr/local/include`, and compiler-internal paths. `-I<path>` prepends a directory: `gcc -I./vendor/include foo.c` makes `#include <vendor/foo.h>` find the local copy first. The `"header.h"` (quotes) form additionally searches the current directory before the system paths.

## Errors at this stage

- **Header not on disk** — *"foo.h: No such file or directory"* — distinct from the **header not `#include`d** error which surfaces at stage 2 ([[CompilationStage|compile]]) as *"implicit declaration of function `foo`"*. Per [[dis-2-9-5-libraries|Ch 2.9.5]] these two are stage-distinct failure modes.

## Connections

- [[dis-2-9-5-libraries]] — introducing source.
- [[CompilationProcess]] — the surrounding five-stage pipeline.
- [[PreprocessorDirective]] — the syntax this stage interprets.
- [[HeaderFile]] — what `#include` consumes.
- [[CConstant]] — `#define` macros.
- [[GCC]] — `-E` and `-I<path>` flags.
- [[CompilationStage]] — the next stage (stage 2).
- [[CompilerVsLinker]] — error-stage taxonomy.
