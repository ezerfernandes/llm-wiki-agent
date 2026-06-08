---
title: "Quaternion (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, linear-algebra]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Quaternion
---

## Summary
The task asks the programmer to implement a quaternion type and the basic arithmetic that operates on it. Quaternions extend complex numbers with one real and three imaginary parts (a + bi + cj + dk), governed by the rules i² = j² = k² = ijk = −1. The key insight is that quaternion multiplication is non-commutative: in general q1·q2 ≠ q2·q1, which the task explicitly requires the solution to demonstrate.

## Task Requirements
- Represent a quaternion (real part plus three imaginary components, e.g. the tuple (1, 2, 3, 4)).
- Compute the norm: sqrt(a² + b² + c² + d²).
- Compute the negative: (−a, −b, −c, −d).
- Compute the conjugate: (a, −b, −c, −d).
- Add a real number r to a quaternion: r + q = (a+r, b, c, d).
- Add two quaternions component-wise.
- Multiply a real number by a quaternion (scalar multiplication).
- Multiply two quaternions using the Hamilton product formula.
- Demonstrate that q1·q2 ≠ q2·q1 (non-commutativity).
- If the language has built-in quaternion support, use it.

## Language Coverage
86 languages implement this task, giving very broad coverage across functional, imperative, and array-oriented paradigms, including C, C++, Python, Haskell, Java, Rust, Julia, Mathematica/Wolfram Language, Perl, and Racket.

## Connections
- [[Quaternions]] — the four-dimensional number system being modeled
- [[ComplexNumbers]] — quaternions generalize complex numbers
- [[HamiltonProduct]] — the non-commutative multiplication rule
- [[NoncommutativeAlgebra]] — why q1·q2 ≠ q2·q1
- [[LinearAlgebra]] — norms, conjugates, and rotation applications

## Contradictions
- None — reference task page.
