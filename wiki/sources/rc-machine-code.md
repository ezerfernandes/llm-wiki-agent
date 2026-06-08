---
title: "Machine code (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, low-level, assembly, memory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Machine_code
---

## Summary
This task asks the programmer to write raw architecture-specific opcode bytes into a memory location and then execute them directly from a high-level language. The reference example is an x86 (32-bit) routine that adds two unsigned bytes and returns the sum. The key insight is that doing this safely requires obtaining executable memory (e.g. via `mmap`/`VirtualAlloc` with execute permission) and calling into it through a function pointer.

## Task Requirements
- Poke the necessary machine-code opcodes into a memory location.
- Provide a means to pass two values into the machine code.
- Execute the code with unsigned-byte arguments 7 and 12, yielding the result 19.
- Perform appropriate cleanup (free the pointer or release the memory allocation).
- If the architecture differs from 32-bit x86, specify it; optionally include an assembly listing alongside the opcodes.

## Language Coverage
47 languages implement this task, ranging from systems languages and assembly dialects to scripting and Lisp-family languages. Representative examples include C, Rust, Go, D, Swift, Python, Perl, Common Lisp, Racket, and X86-64 Assembly.

## Connections
- [[MachineCode]] — the raw opcode bytes being executed
- [[AssemblyLanguage]] — the human-readable form the opcodes correspond to
- [[ExecutableMemory]] — allocating memory with execute permission to run injected code
- [[FunctionPointer]] — the mechanism used to invoke the poked-in code
- [[CallingConvention]] — how the two byte arguments are passed to the routine

## Contradictions
- None — reference task page.
