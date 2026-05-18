---
title: "C Source File (.c)"
type: concept
tags: [c-language, build, toolchain]
sources: [dis-2-9-5-libraries]
last_updated: 2026-05-17
---

# C Source File (`.c`)

A **C source file** (conventionally `.c`) holds the **implementation half** of a [[CLanguage|C]] program or library — function bodies, global definitions, and `#include` directives for the [[HeaderFile|`.h` files]] declaring the API surface it implements or consumes. The `.c` / `.h` split is the conventional library-author discipline: per [[dis-2-9-5-libraries|DIS Ch 2.9.5]], the **header is the API the user `#include`s**, the **`.c` is the implementation the library author compiles** into a [[StaticLibrary|`.a`]] or [[DynamicLibrary|`.so`]] and ships as binary. Users of a library never see the original `.c`.

## Translation unit boundary

Each `.c` file is one **translation unit** — the compiler's atomic processing chunk. The [[PreprocessingStage|preprocessor]] expands all `#include`s into the `.c`, producing a self-contained source for the [[CompilationStage|compile]] stage. One `.c` → one `.o` ([[ObjectFile|object file]]) → linked into the final executable. Cross-`.c` symbol visibility goes through the [[Linker|linker]] at stage 4 ([[LinkingStage|link-edit]]).

## Convention vs syntax

The `.c` extension is **convention**, not C-language syntax — [[GCC|`gcc`]] uses the extension to decide what tool to invoke (`.c` → C compiler, `.cpp`/`.cc` → C++, `.s` → assembler, `.o` → linker only). The `-x c` flag overrides the auto-detection.

## Forward reference

[[dis-2-9-5-libraries|Ch 2.9.5]] names-and-defers the **library-author side** of the `.c`/`.h` split — writing your own libraries — to the next subsection [[dis-2-9-6-writing-libraries|Ch 2.9.6]] *Writing and Using Your Own C Libraries*, now ingested. Ch 2.9.6 codifies the three-step recipe ([[HeaderGuard|`#ifndef` guard]] in `.h` / [[StaticFunction|`static`]] helpers in `.c` / [[ArCommand|`ar`]] or `gcc -fPIC -shared` for the binary) and surfaces the **scaling claim** that the same `.h`/`.c` split is the canonical multi-file C program organization, not a library-specific construct.

## Connections

- [[dis-2-9-5-libraries]] — introducing source (the library-consumer view).
- [[HeaderFile]] — the API counterpart shipped alongside.
- [[CLibrary]] — the artifact this file gets compiled into.
- [[ObjectFile]] — the per-`.c` compiled output.
- [[CompilationProcess]] — the pipeline that consumes it.
- [[PreprocessingStage]] / [[CompilationStage]] / [[AssemblyStage]] — the first three stages this file traverses.
- [[GCC]] — the compiler driver.
- [[CLanguage]] — the language served.
