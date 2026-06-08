---
title: "Least common multiple (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Least_common_multiple
---

## Summary
This Rosetta Code task asks the programmer to compute the least common multiple (LCM) of two integers — the smallest positive integer that has both inputs as factors (e.g., LCM(12, 18) = 36). The key insight is that LCM relates directly to the greatest common divisor via the identity lcm(m, n) = |m × n| / gcd(m, n), so once GCD is available (e.g., by the Euclidean algorithm) the LCM is a one-line computation.

## Task Requirements
- Compute the least common multiple of two integers m and n.
- Return the smallest positive integer that has both m and n as factors.
- Handle the special case where either m or n is zero by returning zero.
- Acceptable approaches include iterating multiples of m until one is divisible by n, applying the gcd-based formula, or merging the prime decompositions of m and n.

## Language Coverage
157 languages implement this task, reflecting that it is a small, fundamental number-theory exercise with near-universal coverage. Representative implementations include C, C++, Python, Java, Haskell, Rust, Go, Ruby, Lisp, and APL, alongside many BASIC dialects and assembly variants.

## Connections
- [[LeastCommonMultiple]] — the core number-theoretic quantity being computed
- [[GreatestCommonDivisor]] — supplies the gcd used in the lcm = |m·n|/gcd formula
- [[EuclideanAlgorithm]] — standard method for obtaining the gcd
- [[PrimeFactorization]] — alternative approach via merging prime decompositions
- [[NumberTheory]] — the mathematical domain this task belongs to

## Contradictions
- None — reference task page.
