---
title: "Combinations and permutations (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, combinatorics, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Combinations_and_permutations
---

## Summary
This task asks the programmer to implement the combination operator (nCk, "n choose k") and the permutation operator (nPk) in the target language. The key insight is that both can be computed without forming full factorials by using the falling-product forms — nPk = n(n-1)...(n-k+1) and nCk = nPk / k! — which keeps intermediate values small enough for exact integer arithmetic, while very large arguments require a floating-point approximation (e.g., via the gamma/log-gamma function) to avoid overflow.

## Task Requirements
- Implement the combination operator nCk = n! / (k!(n-k)!), expressible as the falling product n(n-1)...(n-k+1) divided by k!.
- Implement the permutation operator nPk = n(n-1)(n-2)...(n-k+1).
- Demonstrate exact integer arithmetic: a sample of permutations from 1 to 12 and combinations from 10 to 60.
- Demonstrate approximate floating-point arithmetic: permutations from 5 to 15000 and combinations from 100 to 1000, where the magnitudes exceed exact integer range and an approximation (such as calling the gamma function) is appropriate.

## Language Coverage
53 languages implement this task, spanning systems languages, functional languages, scripting languages, and math-oriented environments. Representative implementations include C, C++, Rust, Go, Java, Haskell, Python, Julia, Perl, Raku, Mathematica / Wolfram Language, and R.

## Connections
- [[Combinatorics]] — the task directly implements counting of combinations and permutations
- [[BinomialCoefficient]] — nCk is the binomial coefficient, linked to the related "Evaluate binomial coefficients" task
- [[Factorial]] — both operators derive from factorial ratios
- [[GammaFunction]] — used for the floating-point approximation of large arguments
- [[ArbitraryPrecisionArithmetic]] — exact integer results for large n require bignum support

## Contradictions
- None — reference task page.
