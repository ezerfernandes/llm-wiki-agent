---
title: "Object File (.o)"
type: concept
tags: [c-language, toolchain, build, linker]
sources: [dis-2-9-5-libraries]
last_updated: 2026-05-17
---

# Object File (`.o`)

An **object file** is the binary output of stage 3 ([[AssemblyStage|assemble]]) of the [[CompilationProcess|compile pipeline]] — machine code for one translation unit, with **unresolved external symbol references** still pending [[Linker|linker]] resolution at stage 4. Per [[dis-2-9-5-libraries|DIS Ch 2.9.5]], `gcc -c foo.c` produces `foo.o`.

## Anatomy

On Linux the format is **[[ELF|ELF]]** (Executable and Linkable Format). The relevant sections:

- **`.text`** — machine instructions.
- **`.data`** — initialized [[GlobalVariable|globals]].
- **`.bss`** — zero-initialized globals (no on-disk bytes, just a size).
- **`.rodata`** — read-only constants (string literals, `const` data).
- **Symbol table** — names and addresses of defined symbols, names and placeholder relocations for undefined references.
- **Relocation entries** — instructions to the [[Linker|linker]] for patching addresses once final positions are known.

## How it differs from an executable

An [[BinaryExecutable|executable]] (also ELF on Linux) has:

- All external references resolved (statically) or recorded as `NEEDED` `.so` dependencies (dynamically).
- A `.dynamic` section listing required shared objects.
- An entry-point address (`_start`) the kernel jumps to.
- A program header table describing how to map segments into a process's [[AddressSpace|address space]].

An object file has **none of these** — it is an incomplete fragment.

## How it differs from a static library

A [[StaticLibrary|`.a` archive]] is a **bundle** of `.o` files plus an index — `ar` is the tool, not a separate format. The [[Linker|linker]] pulls individual `.o` members out of an archive on demand.

## Why this stage exists

Splitting compile (`gcc -c foo.c → foo.o`) from link (`gcc *.o -o prog`) enables:

- **Incremental builds** — touching one `.c` recompiles only that translation unit; the link step is cheap.
- **Mixed-language linking** — a [[Rust|Rust]] `.o` (via [[Rustc|`rustc --emit=obj`]]) and a [[CLanguage|C]] `.o` can be linked together (see [[ExternC]] / [[NoMangle]] from the [[TheEmbeddedRustBook|Embedded Rust]] corpus).
- **Library distribution** — ship `.o`s in `.a` archives or as `.so` shared objects without releasing `.c` sources.

## Connections

- [[dis-2-9-5-libraries]] — introducing source.
- [[AssemblyStage]] — the stage that produces `.o` files.
- [[CompilationProcess]] — the surrounding pipeline.
- [[Linker]] — what consumes `.o` files at stage 4.
- [[LinkingStage]] — the consuming stage.
- [[StaticLibrary]] — archive bundle of `.o` files.
- [[BinaryExecutable]] — the final stage-4 product (linked).
- [[GCC]] — `-c` flag stops at `.o` generation.
- [[ELF]] — the file format on Linux.
- [[ExternC]] / [[NoMangle]] — the Rust-side `.o`-producing attributes covered in [[rust-embedded-book-interoperability-rust-with-c]].
