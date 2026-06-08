---
title: "Use another language to call a function (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, foreign-function-interface, interoperability]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Use_another_language_to_call_a_function
---

## Summary
This task is the inverse of calling a foreign function: instead of your language calling into C, a given C `main` program must call a `Query` function that you implement in your language. The key insight is exposing your language's code with a C-compatible ABI (matching calling convention, name, and the `(char *Data, size_t *Length)` signature) so the host C program can link against and invoke it.

## Task Requirements
- Implement the missing `Query` function so the supplied C `main` can call it.
- `Query` receives a buffer pointer `Data` and a `size_t *Length` holding the buffer size in bytes.
- Place the string `Here am I` into the buffer.
- If the buffer is too small, return 0.
- Otherwise write to the start of the buffer, set `Length` to the number of bytes written, and return 1.

## Language Coverage
39 languages implement this task, spanning native systems languages, managed/VM languages, and scripting languages that expose C-callable entry points. Representative implementations include C, C++, Ada, D, Rust, Go, Fortran, Haskell, OCaml, Python, and X86-64 Assembly.

## Connections
- [[ForeignFunctionInterface]] — the mechanism for cross-language calls
- [[CallingConvention]] — ABI rules that make the C `main` able to invoke `Query`
- [[ApplicationBinaryInterface]] — binary contract for symbol names and argument passing
- [[Pointers]] — `Data` and `Length` are passed by pointer for in/out semantics

## Contradictions
- None — reference task page.
