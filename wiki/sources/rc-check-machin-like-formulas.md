---
title: "Check Machin-like formulas (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, exact-arithmetic, pi]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Check_Machin-like_formulas
---

## Summary
Machin-like formulas express pi/4 as an integer-weighted sum of arctangents of rationals, and are used to compute pi efficiently. The task is to verify a list of 16 such formulas by computing the tangent of the right-hand side with exact (rational) arithmetic and confirming it equals exactly 1, then to show that one near-identical formula is incorrect because its tangent differs from 1. The key insight is that the tangent addition identity lets you collapse the whole sum of arctangents into a single exact rational tangent value without ever evaluating any transcendental function.

## Task Requirements
- For 16 given Machin-like formulas, compute tan(right-hand side) using exact arithmetic and show each equals 1.
- Show that a final, deliberately altered formula yields a tangent that is not 1, confirming it is incorrect.
- Use the identities tan(a+b) = (tan a + tan b)/(1 − tan a tan b), tan(arctan(a/b)) = a/b, and tan(−a) = −tan(a).
- Equations may be stored in any data structure; extra credit for parsing them from human-readable text input.
- Note: a full proof would also require bounding the right-hand side within (−3pi/4, 5pi/4) due to tangent periodicity.

## Language Coverage
31 languages implement this task. Coverage is broad, spanning functional, imperative, and math-oriented systems, including Python, Haskell, Go, Java, Julia, Perl, Raku, OCaml, Mathematica / Wolfram Language, and PARI/GP.

## Connections
- [[MachinLikeFormula]] — the family of arctangent identities for pi being verified
- [[Pi]] — the constant these formulas approximate
- [[TangentAdditionFormula]] — the recurrence used to fold the sum exactly
- [[RationalArithmetic]] — exact fraction arithmetic that avoids floating-point error
- [[Arctangent]] — the inverse trigonometric function appearing in each term

## Contradictions
- None — reference task page.
