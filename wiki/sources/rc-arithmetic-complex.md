---
title: "Arithmetic/Complex (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, complex-numbers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Arithmetic/Complex
---

## Summary
This task asks the programmer to implement the basic arithmetic of complex numbers — numbers of the form a + b·i where i = √-1 — typically stored as a pair of real numbers (real and imaginary parts). The required operations are addition, multiplication, negation, and inversion, each shown as a separate function, with subtraction and division derivable from these. The key insight is that many languages ship a native complex type or library, but where one is absent the solver must define the type and its operations from scratch.

## Task Requirements
- Implement addition, multiplication, negation, and inversion of complex numbers as separate functions.
- Print the result of each operation tested.
- (Optional) Show complex conjugation: the conjugate of a + bi is a - bi.
- If the language has a complex-number library, demonstrate using it; otherwise, define the complex type itself.

## Language Coverage
131 languages implement this task, spanning a very broad range from numeric/math-oriented languages with built-in complex support to general-purpose and low-level languages that must define the type manually. Representative examples include Python, Haskell, C, C++, Java, Julia, Fortran, Common Lisp, Rust, and Mathematica / Wolfram Language.

## Connections
- [[ComplexNumbers]] — the core mathematical object the task models
- [[ImaginaryUnit]] — the value i = √-1 underlying the imaginary part
- [[ComplexConjugate]] — the optional conjugation operation (a + bi → a - bi)
- [[OperatorOverloading]] — common technique for expressing these operations on a user-defined type
- [[FieldArithmetic]] — the algebraic structure of complex numbers as a field

## Contradictions
- None — reference task page.
