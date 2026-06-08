---
title: "Compile-time calculation (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, metaprogramming, compilers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Compile-time_calculation
---

## Summary
This task asks the programmer to compute 10! (ten factorial = 3,628,800) entirely at compile time rather than at runtime, then print the precomputed result when the program runs. The key insight is demonstrating each language's mechanism for moving computation out of runtime — constant folding, constant expressions, template metaprogramming, or macros — and discussing the limits of what a given compiler will evaluate ahead of time.

## Task Requirements
- Calculate 10! (ten factorial) at compile time, not at runtime.
- Print the resulting value when the program is run.
- Discuss the limitations that apply to compile-time calculation in the chosen language.

## Language Coverage
78 languages implement this task, spanning systems languages with explicit compile-time facilities, functional languages, scripting languages, and even several assembly dialects. Representative entries include C, C++, Rust, Ada, D, Zig, Nim, Haskell, OCaml, Forth, and Python.

## Connections
- [[ConstantFolding]] — compiler optimization that evaluates constant expressions at compile time
- [[TemplateMetaprogramming]] — technique (notably in C++) used to compute values during compilation
- [[Factorial]] — the specific computation being performed
- [[Macros]] — preprocessor/macro expansion as a compile-time evaluation strategy
- [[Compiler]] — the component responsible for ahead-of-time evaluation

## Contradictions
- None — reference task page.
