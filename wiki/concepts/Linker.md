---
title: "Linker (ld)"
type: concept
tags: [toolchain, linker, build, c-language]
sources: [dis-2-9-5-libraries]
last_updated: 2026-05-17
---

# Linker (`ld`)

The **linker** is the toolchain stage that **resolves symbol references across [[ObjectFile|object files]] and [[CLibrary|libraries]]** to produce a final [[BinaryExecutable|executable]] (or a [[DynamicLibrary|shared object]]). On hosted Linux it is conventionally `/usr/bin/ld` (GNU `ld` or LLVM `lld`); [[GCC|`gcc`]] invokes it implicitly as **stage 4** of the [[CompilationProcess|compile-then-run pipeline]] per [[dis-2-9-5-libraries|DIS Ch 2.9.5]].

## What it does

Each [[ObjectFile|`.o` file]] coming out of the [[AssemblyStage|assembler]] contains:

- **Defined symbols** — names of functions and globals this object provides.
- **Undefined references** — names this object **uses** but doesn't define (e.g., a call to `printf` from a `main.o`).

The linker's job is to **match every undefined reference to a defined symbol** somewhere — either in another `.o` file on the command line, or in a [[StaticLibrary|`.a`]] archive (whose `.o` members are pulled in selectively), or in a [[DynamicLibrary|`.so`]] shared object (whose presence is **recorded** as a deferred dynamic reference rather than resolved immediately). A failure to find a match surfaces as [[UndefinedReferenceError|*"undefined reference to `foo`"*]] — *"the linker (`ld`)"* per Ch 2.9.5 is the source of this signature error.

## Static vs dynamic resolution

| Source | Stage 4 behavior | Stage 5 behavior |
|---|---|---|
| `.o` files | Symbols inlined, references resolved | (done) |
| `.a` archive | Used members' symbols inlined | (done) |
| `.so` shared object | Reference recorded, name preserved | [[DynamicLinker|`ld.so`]] resolves at launch |

## The `-l<name>` lookup

The linker consumes `-lfoo` by searching its **library search path** (built-in defaults plus `-L<path>` additions) for `libfoo.so` *then* `libfoo.a`, preferring the shared object. Per [[dis-2-9-5-libraries|Ch 2.9.5]]: *"the compiler can choose to dynamically link when both a shared object (`.so`) and an archive (`.a`) version of a library are available."*

## Distinction from the dynamic linker

The build-time **`ld`** is invoked once at compile/link time. The runtime **[[DynamicLinker|`ld.so`]] / `ld-linux.so`** is a separate program loaded into every dynamic process at launch — it resolves the references `ld` left for it. Different programs, related names, complementary roles.

## Connections

- [[dis-2-9-5-libraries]] — introducing source.
- [[LinkingStage]] — stage 4 of the pipeline.
- [[ObjectFile]] — what the linker consumes.
- [[StaticLibrary]] / [[DynamicLibrary]] — the two library formats it handles.
- [[StaticLinking]] / [[DynamicLinking]] — the two resolution modes.
- [[UndefinedReferenceError]] — its signature error.
- [[CompilerVsLinker]] — the diagnostic-stage split.
- [[DynamicLinker]] — the runtime counterpart at stage 5.
- [[CompilationProcess]] — the surrounding five-stage pipeline.
- [[GCC]] — drives `ld` implicitly.
- [[LinkerScript]] — the configuration file consumed in [[BareMetalProgramming|bare-metal]] contexts (in hosted Linux it's implicit / system-default).
