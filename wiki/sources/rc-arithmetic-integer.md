---
title: "Arithmetic/Integer (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, arithmetic, integer-arithmetic]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Arithmetic/Integer
---

## Summary
A basic language-learning task that reads two integers from the user and displays the results of the standard integer arithmetic operations on them. The key subtlety is not the arithmetic itself but documenting how each language handles edge cases: the rounding direction of integer division (toward zero vs. toward negative infinity) and whether the remainder/modulo takes the sign of the dividend or the divisor.

## Task Requirements
- Read two integers from user input (no error handling required).
- Display their sum, difference, product, integer quotient, and remainder.
- Display exponentiation if the language provides such an operator.
- State how the integer quotient rounds (e.g., toward zero or toward negative infinity).
- State whether the remainder's sign follows the first operand (dividend) or the second operand (divisor) when they differ.
- Bonus: demonstrate an integer `divmod` operator that returns quotient and remainder together (as in Haskell, Python, and ALGOL 68).

## Language Coverage
241 languages implement this task, reflecting its status as a fundamental, near-universal exercise. Representative implementations span systems languages (C, C++, Rust, Go, Zig), functional languages (Haskell, OCaml, F#, Scheme), scripting languages (Python, Ruby, Perl, JavaScript, Lua), and low-level assembly targets (x86, ARM, 6502, RISC-V).

## Connections
- [[IntegerArithmetic]] — the core operations this task exercises
- [[EuclideanDivision]] — defines the quotient/remainder relationship and its rounding conventions
- [[ModuloOperation]] — the source of sign-convention differences across languages
- [[Exponentiation]] — the optional power operation
- [[Divmod]] — the bonus combined quotient-and-remainder operator

## Contradictions
- None — reference task page.
