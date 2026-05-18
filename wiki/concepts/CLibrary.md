---
title: "C Library"
type: concept
tags: [c-language, libraries, build, toolchain]
sources: [dis-2-9-5-libraries]
last_updated: 2026-05-17
---

# C Library

A **C library** is a reusable, precompiled bundle of [[CLanguage|C]] functionality distributed in **two halves**, per [[dis-2-9-5-libraries|DIS Ch 2.9.5]]: *"a C library consists of two parts: an API (header files) and the implementation (precompiled binary code)."*

1. **API half** — one or more [[HeaderFile|`.h`]] files declaring function prototypes, types, and macros. Consumed at preprocess time via [[PreprocessorDirective|`#include`]]. Lives under `/usr/include` / `/usr/local/include` or custom locations reached via `-I<path>`.
2. **Implementation half** — precompiled binary code in either a [[StaticLibrary|static archive `lib<name>.a`]] (linked at build time) or a [[DynamicLibrary|shared object `lib<name>.so`]] (linked at runtime). Lives under `/usr/lib` / `/usr/local/lib` or custom locations reached via `-L<path>`.

The two halves are decoupled: the library author ships the `.h` + `.{a,so}` pair (often with a `-dev` package gating the headers); consumers never see the original `.c` sources. This split is why a [[CCompiler|C compiler]] can typecheck a call against the prototype at compile time while leaving symbol resolution to the [[Linker|linker]].

## The `-l<name>` abstraction

[[GCC|`gcc`]] uses `-l<name>` (not the literal filename) at link time: `-lm` finds `libm.{so,a}`, `-lpthread` finds `libpthread.{so,a}`. Per Ch 2.9.5: *"this level of abstraction enables programmers to be flexible about the desired linking type (e.g., static or shared) without having to specify a specific filename."* The compiler can *"choose to dynamically link when both a shared object (`.so`) and an archive (`.a`) version of a library are available."*

## Canonical examples (from earlier DIS chapters)

- **[[StandardCLibrary|`libc`]]** — linked implicitly; `<stdio.h>`, `<stdlib.h>`, `<string.h>`.
- **`libm`** — math; `#include <math.h>` plus `-lm` (the [[dis-1-1-getting-started|Ch 1.1]] example).
- **`libpthread`** — threads; `-pthread` is the preferred form (not `-lpthread`).

## Connections

- [[dis-2-9-5-libraries]] — introducing source.
- [[HeaderFile]] — the API half.
- [[StaticLibrary]] / [[DynamicLibrary]] — the two implementation-half formats.
- [[StaticLinking]] / [[DynamicLinking]] — the two consumption modes.
- [[Linker]] — what resolves `-l<name>` to a binary.
- [[CompilationProcess]] — five-stage pipeline; libraries are consumed at stages 1 (headers) and 4–5 (binaries).
- [[GCC]] — the toolchain driving `-l` / `-L` / `-I` resolution.
- [[UndefinedReferenceError]] — the signature error when a library is forgotten.
- [[CSourceFile]] — the `.c` author-side half (covered in [[dis-2-9-6-writing-libraries|Ch 2.9.6]] — named-and-deferred).
- [[CStandardLibrary]] — the libraries shipped with every hosted [[CLanguage|C]] toolchain.
