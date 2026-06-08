---
title: "Continued fraction/Arithmetic/Construct from rational number (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, continued-fractions, lazy-evaluation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Continued_fraction/Arithmetic/Construct_from_rational_number
---

## Summary
The task asks for a function `r2cf(N1, N2)` (or `r2cf(Fraction N)`) that converts a rational number given as a numerator/denominator pair into its continued-fraction representation. The function emits one term at a time in a lazy fashion: it computes the integer quotient and remainder of N1 divided by N2, outputs the quotient, then sets N1 to N2 and N2 to the remainder, repeating until the denominator is zero. This is essentially the Euclidean algorithm reframed to produce successive continued-fraction coefficients.

## Task Requirements
- Implement `r2cf` that determines the integer part and remainder of N1/N2.
- After outputting the integer part, set N1 to N2 and N2 to the remainder, looping until abs(N2) is zero (lazy, one term per call).
- Demonstrate on the rationals: 1/2, 3, 23/8, 13/11, 22/7, -151/77.
- Feed increasingly accurate decimal approximations of sqrt(2) (14142/10000 ... 14142136/10000000) and observe the result approaching [1; 2, 2, 2, ...].
- Feed approximations of 22/7 (31/10 ... 314285714/100000000) and contrast their behavior with sqrt(2).
- Note the representational subtlety that [3;7] equals [3;7,infinity] when an extra term is required (analogous to 3.7 = 3.70).

## Language Coverage
55 languages implement this task, giving broad coverage across functional, imperative, and stack-based paradigms. Representative implementations include C, C++, C#, Python, Haskell, Java, JavaScript, Go, Rust, Ruby, Scheme, and Forth.

## Connections
- [[ContinuedFraction]] — the numeric representation being constructed
- [[EuclideanAlgorithm]] — the repeated quotient/remainder step is exactly Euclid's GCD process
- [[LazyEvaluation]] — terms are produced one at a time on demand
- [[NumberTheory]] — rational and irrational number approximation underpins the task
- [[RationalNumber]] — input is a numerator/denominator pair

## Contradictions
- None — reference task page.
