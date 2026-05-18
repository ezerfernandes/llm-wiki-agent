---
title: "Binary Executable"
type: concept
tags: [c-language, compiler, build, systems]
sources: [dis-1-1-getting-started]
last_updated: 2026-05-17
---

# Binary Executable

A **binary executable** is a file containing machine-code instructions the [[ComputerHardware|hardware]] can directly execute. It is the output of the [[CompilationProcess]] driven by a [[CCompiler|C compiler]] such as [[GCC]].

By default [[GCC|`gcc`]] writes the binary to `./a.out`; the `-o <name>` flag names it explicitly (`gcc -o hello hello.c` → `./hello`) ([[dis-1-1-getting-started|DIS Ch 1.1]]).

On a hosted [[OperatingSystem|OS]] the executable is typically in a platform-specific container format (ELF on Linux, Mach-O on macOS, PE on Windows) that the kernel loader maps into a fresh process's address space before jumping into the program's entry point — which on a C program is the runtime startup code that ultimately calls [[MainFunction|`main`]].

## Connections

- [[CompilationProcess]] — produces it.
- [[CCompiler]] / [[GCC]] — the tools that produce it.
- [[CLanguage]] — the source language.
- [[MainFunction]] — the entry point the loader hands control to (via runtime startup).
- [[ExitStatus]] — the integer it returns to the OS when it terminates.
- [[OperatingSystem]] — the loader and process manager that runs it.
