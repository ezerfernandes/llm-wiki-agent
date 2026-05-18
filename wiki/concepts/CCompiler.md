---
title: "C Compiler"
type: concept
tags: [compiler, c-language, toolchain]
sources: [dis-1-1-getting-started]
last_updated: 2026-05-17
---

# C Compiler

A **C compiler** is a program that translates [[CLanguage|C]] source code into a [[BinaryExecutable|binary executable]] form that the [[ComputerHardware|hardware]] can directly execute ([[dis-1-1-getting-started|DIS Ch 1.1]]). It is the role; [[GCC|`gcc`]] is the canonical instance used throughout [[DiveIntoSystems]]; `clang` and MSVC's `cl.exe` are other instances.

## Why C needs a compiler

Unlike [[Python]], which ships with an interpreter that reads and executes source directly, C requires a compile-then-run cycle:

1. Edit `hello.c`.
2. Run the compiler: `gcc hello.c`.
3. Execute the produced binary: `./a.out`.

This separation lets C programs run at hardware speed without an interpreter in the loop, at the cost of the extra build step every time the source changes.

## Connections

- [[CLanguage]] — what it compiles.
- [[GCC]] — the canonical instance.
- [[CompilationProcess]] — the multi-stage pipeline it orchestrates.
- [[BinaryExecutable]] — its output artifact.
- [[Python]] — the interpreted contrast.
- [[Rustc]] — the parallel role on the Rust side of the wiki.
