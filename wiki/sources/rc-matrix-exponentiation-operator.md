---
title: "Matrix-exponentiation operator (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, linear-algebra, operator-overloading]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Matrix-exponentiation_operator
---

## Summary
This task asks the programmer to implement matrix exponentiation — raising a square matrix to an integer power — and to expose it as an operator rather than a plain function. Since most languages provide built-in exponentiation only for integers and reals, the exercise demonstrates extending that notation to matrices, typically by overloading the power operator (e.g. `^`, `**`) on a matrix type. The key insight is that matrix powers reduce to repeated matrix multiplication, with the identity matrix as the base case for the zeroth power.

## Task Requirements
- Implement matrix exponentiation (a square matrix raised to a non-negative integer power).
- Expose the operation as an operator, not just a named function, where the language permits.

## Language Coverage
68 languages implement this task, giving broad coverage across functional, object-oriented, array, and computer-algebra languages. Representative examples include C, C++, C#, Java, Python, Haskell, J, Julia, Rust, Perl, Raku, and Mathematica/Wolfram Language.

## Connections
- [[MatrixMultiplication]] — the underlying operation that exponentiation iterates.
- [[OperatorOverloading]] — the language feature used to bind the power operator to matrices.
- [[ExponentiationBySquaring]] — an efficient algorithm some implementations use for the power loop.
- [[IdentityMatrix]] — the multiplicative identity serving as the base case for exponent zero.
- [[LinearAlgebra]] — the mathematical domain of square matrices and their powers.

## Contradictions
- None — reference task page.
