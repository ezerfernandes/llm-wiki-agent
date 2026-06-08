---
title: "Variadic function (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, functions, language-features]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Variadic_function
---

## Summary
This Rosetta Code task asks the programmer to create a function that accepts a variable number of arguments and prints each one on its own line. The key insight is demonstrating how a language expresses variadic parameters and, where supported, how to "spread" or apply such a function to a list of arguments assembled at runtime.

## Task Requirements
- Define a function that takes a variable number of arguments.
- Print each argument on its own line.
- If the language supports it, show how to call the function by unpacking/applying a runtime-constructed list of arguments.

## Language Coverage
123 languages implement this task, reflecting that variadic functions are a near-universal language feature with widely varying syntax — from C's `stdarg.h` and `...`, to Python's `*args`, JavaScript's rest parameters and `apply`, and Lisp-family `&rest`. Representative implementations include C, C++, Java, JavaScript, Python, Ruby, Perl, Haskell, Common Lisp, Go, and Rust.

## Connections
- [[VariadicFunction]] — the language feature being demonstrated
- [[FunctionApplication]] — applying a function to a runtime list of arguments
- [[ArgumentUnpacking]] — spreading a collection into positional arguments
- [[CallAFunction]] — the related Rosetta Code task on basic function invocation

## Contradictions
- None — reference task page.
