---
title: "Code Section (C Program Memory)"
type: concept
tags: [c-language, memory, compilation, address-space]
sources: [dis-2-1-scope-memory]
last_updated: 2026-05-17
---

# Code Section

The **code section** (a.k.a. **text section**) is the region of a [[CLanguage|C]] program's [[ProcessMemory|address space]] that holds the program's compiled instructions. Per [[dis-2-1-scope-memory|DIS Ch 2.1]]:

> "The program's instructions are stored in the *code* section of the memory."

This is the runtime side of [[dis-1-1-getting-started|Ch 1.1]]'s [[CompilationProcess|compile-then-run]] model: the bytes [[GCC|`gcc`]] produced in the [[BinaryExecutable|binary]] end up in this region when the [[OperatingSystem|OS]] loads the program into memory.

## Properties

- **Read-only** on modern OSes — the OS maps the code-section pages without write permission so a stray write cannot self-modify the program. Attempting to write to a code-section address typically segfaults.
- **Executable** — distinguishing it from the [[DataSection|data]] / [[HeapSection|heap]] / [[StackSection|stack]] regions, which on hardened systems are mapped non-executable (the W^X discipline).
- **Program-lifetime** — code-section bytes are present for the program's entire run; they do not get pushed/popped or allocated/freed.

## Pedagogical placement

[[dis-2-1-scope-memory|Ch 2.1]] introduces the code section *nominally* — it's the first of the four [[ProcessMemory|program-memory]] regions, and it's where the [[CompilationProcess|compiled]] [[BinaryExecutable|binary]]'s `.text` segment ends up at load time. Later [[DiveIntoSystems]] chapters (assembly, OS) open up:

- The instruction-fetch path from the code section into the CPU's pipeline.
- The role of the executable-file format (ELF on Linux) in describing which bytes go where.
- Read-only mapping enforcement via the MMU's page protections.

## Connections

- [[dis-2-1-scope-memory]] — introducing source.
- [[ProcessMemory]] / [[AddressSpace]] — the container.
- [[DataSection]] / [[HeapSection]] / [[StackSection]] — the other three regions.
- [[CompilationProcess]] / [[BinaryExecutable]] / [[GCC]] — produce the bytes that populate this region.
- [[OperatingSystem]] — loads the binary's code into this region at process launch.
- [[CLanguage]] / [[DiveIntoSystems]].
