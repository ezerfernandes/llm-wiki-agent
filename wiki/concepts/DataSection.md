---
title: "Data Section (C Program Memory)"
type: concept
tags: [c-language, memory, globals, address-space]
sources: [dis-2-1-scope-memory]
last_updated: 2026-05-17
---

# Data Section

The **data section** is the region of a [[CLanguage|C]] program's [[ProcessMemory|address space]] that stores [[GlobalVariable|global variables]]. Per [[dis-2-1-scope-memory|DIS Ch 2.1]]:

> "Global variables are stored in the *data* section."

This is the region whose existence makes the *"remain permanently in scope"* promise for [[GlobalVariable|globals]] mechanical: data-section storage is allocated at program load and persists until exit — it never gets pushed onto a [[StackFrame|frame]] (so it does not vanish on [[ReturnStatement|return]]) and it never sits on the [[HeapSection|heap]] (so the programmer does not [[Free|free]] it).

## Properties

- **Program-lifetime storage** — every [[GlobalVariable|global]] occupies a fixed address in this region for the program's entire run.
- **Initialized at load time** — a global declared `int g_x = 7;` arrives at its initial value before [[MainFunction|`main`]] runs, because the data section's contents come from the executable file. A global declared without an initializer (`int g_x;`) is zero-initialized by the OS (the *BSS* sub-region).
- **Writable** — unlike the [[CodeSection|code section]], the data section is writable; that's the whole point.
- **Bounded in size at compile time** — the count of globals (and their `sizeof`) is fixed at link time; the data section is not dynamic.

## .data vs .bss (under the hood)

Modern toolchains actually split the data region in two: `.data` for explicitly-initialized globals (their initial bytes live in the binary) and `.bss` for zero-initialized globals (the binary only records the *size*, not the zeros — the OS supplies them at load). [[dis-2-1-scope-memory|Ch 2.1]] does not draw this distinction; it treats both as *"the data section."*

## Pedagogical placement

Ch 2.1 introduces the data section as the storage region for [[GlobalVariable|globals]]; it's the second of the four [[ProcessMemory|program-memory]] regions. Later chapters will revisit it when introducing `static` (which extends data-section storage to function-local variables) and when discussing executable file formats.

## Connections

- [[dis-2-1-scope-memory]] — introducing source.
- [[ProcessMemory]] / [[AddressSpace]] — the container.
- [[CodeSection]] / [[HeapSection]] / [[StackSection]] — the other three regions.
- [[GlobalVariable]] — the variable class that lives here.
- [[CompilationProcess]] / [[BinaryExecutable]] — produce the initial bytes that populate this region at load.
- [[OperatingSystem]] — zero-initializes the BSS sub-region at process launch.
- [[CLanguage]] / [[DiveIntoSystems]].
