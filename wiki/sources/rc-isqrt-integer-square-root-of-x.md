---
title: "Isqrt (integer square root) of X (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, integer-arithmetic]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Isqrt_(integer_square_root)_of_X
---

## Summary
The task asks the programmer to compute the integer square root of a non-negative number X — that is, the largest integer R such that R² ≤ X. The key insight is to do this without floating point: while `floor(sqrt(X))` works for small values, it loses accuracy on large integers, so the task specifies a quadratic-residue (digit-by-digit) algorithm using only integer arithmetic, where the two divisions are by 4 and 2 (bit shifts) and the lone multiplication is also shiftable. A useful side effect is that the leftover Z equals X − R², revealing whether X is a perfect square.

## Task Requirements
- Implement Isqrt(X) returning floor of the square root of a non-negative X using integer-only arithmetic (per the given pseudo-code), not floating point.
- Display Isqrt of the integers from 0 through 65 inclusive in a horizontal format.
- Display Isqrt of the odd powers 7¹ through 7⁷³ inclusive in a vertical format.
- Use comma separators when displaying larger numbers.
- If the language supports only smaller integers, show as many values as it can.

## Language Coverage
84 languages implement this task, spanning systems and functional languages, scripting tongues, and many BASIC dialects, which makes it a good test of arbitrary-precision (bignum) support. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, OCaml, Julia, Raku, and REXX.

## Connections
- [[IntegerSquareRoot]] — the core function being implemented
- [[QuadraticResidue]] — the integer-only algorithm specified by the task
- [[BitwiseOperations]] — divisions by 4 and 2 reduce to bit shifts
- [[ArbitraryPrecisionArithmetic]] — needed to reach 7⁷³ without overflow
- [[PrimalityTest]] — a primary use case, trial division up to √X

## Contradictions
- None — reference task page.
