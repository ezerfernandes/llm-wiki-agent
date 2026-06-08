---
title: "Roots of a quadratic function (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, numerical-methods, floating-point]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Roots_of_a_quadratic_function
---

## Summary
The task asks for a program that solves the quadratic equation ax² + bx + c = 0, returning both roots and correctly handling the non-real (complex) case. The key insight is that the textbook quadratic formula is numerically unstable: when one root is far closer to zero than the other, the subtraction in (-b ± √(b²-4ac)) suffers catastrophic cancellation. The challenge is to use a more careful algorithm — such as computing one root via the stable formula and deriving the other from the product-of-roots relation c/a — so both roots stay accurate even for inputs like a=1, b=-10⁹, c=1.

## Task Requirements
- Find the two roots of ax² + bx + c = 0; need not verify a ≠ 0.
- Correctly handle non-real (complex) roots when the discriminant is negative.
- Use a numerically stable method: for a=1, b=-10⁹, c=1 (double precision), both returned roots must exceed 10⁻¹¹.
- For single-precision-only languages, handle b=-10⁶ instead.
- Display the computed roots for that test case.

## Language Coverage
71 languages implement this task, spanning systems languages, functional languages, scientific/array tools, and BASIC dialects. Representative implementations include C, C++, C#, Java, Python, Haskell, OCaml, Fortran, Ada, Julia, MATLAB / Octave, and Wren.

## Connections
- [[QuadraticFormula]] — the closed-form solution being implemented
- [[FloatingPointArithmetic]] — the source of the accuracy hazard
- [[CatastrophicCancellation]] — the specific numerical failure mode being avoided
- [[ComplexNumbers]] — required to represent non-real roots
- [[NumericalStability]] — the property the improved algorithm must preserve

## Contradictions
- None — reference task page.
