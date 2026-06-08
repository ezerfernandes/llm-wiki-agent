---
title: "Call a function in a shared library (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, foreign-function-interface, dynamic-linking]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Call_a_function_in_a_shared_library
---

## Summary
This task asks the programmer to invoke a function residing in a shared library (a `.so`, `.dll`, or `.dylib`) without statically linking against it at compile time. The library must be loaded and resolved at runtime, and if the library is unavailable the program should fall back to an internal equivalent function. The key insight is that this operates close to the platform ABI level rather than the usual high-level API, exercising dynamic loading mechanisms like `dlopen`/`dlsym` or `LoadLibrary`/`GetProcAddress`.

## Task Requirements
- Call a function located in a shared library at runtime.
- Do not dynamically link to the library at compile time (resolve symbols dynamically instead).
- If the shared library is available, use its function; otherwise fall back to an internal equivalent implementation.
- Work at the ABI level, not the normal API level.

## Language Coverage
61 languages implement this task, spanning systems languages with native FFI, scripting languages with runtime loaders, and even assembly. Representative examples include C, Rust, Go, D, Ada, Fortran, Python, Perl, Ruby, Haskell, OCaml, and X86-64 Assembly.

## Connections
- [[ForeignFunctionInterface]] — calling library code across language/ABI boundaries
- [[DynamicLinking]] — runtime resolution of shared library symbols
- [[ApplicationBinaryInterface]] — the ABI level at which this operates
- [[SharedLibrary]] — the `.so`/`.dll`/`.dylib` artifact being loaded
- [[GracefulDegradation]] — falling back to an internal function when the library is absent

## Contradictions
- None — reference task page.
