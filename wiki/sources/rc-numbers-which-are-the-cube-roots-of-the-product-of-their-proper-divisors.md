---
title: "Numbers which are the cube roots of the product of their proper divisors (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, divisors]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Numbers_which_are_the_cube_roots_of_the_product_of_their_proper_divisors
---

## Summary
Find positive integers n such that n equals the cube root of the product of n's proper divisors. For example, 24 has proper divisors 1, 2, 3, 4, 6, 8, 12 whose product is 13,824, and the cube root of 13,824 is 24. The key insight is that the product of all divisors of n equals n^(d(n)/2), so the proper-divisor product is n^(d(n)/2 - 1); this equals n^3 exactly when n has 8 divisors (or trivially when n = 1), making divisor-count testing far cheaper than computing huge products.

## Task Requirements
- Compute and show the first 50 such positive integers.
- Also show the 500th and 5,000th such numbers.
- Stretch goal: compute and show the 50,000th such number.
- Treat 1 as the first member of the sequence (per OEIS A111398), even though 1 has no proper divisors.

## Language Coverage
40 languages implement this task, spanning systems, scripting, functional, and array languages. Representative implementations include C, C++, C#, Go, Java, Python, Haskell, Julia, Perl, Raku, Ruby, Fortran, and J.

## Connections
- [[NumberTheory]] — the task is rooted in divisor properties of integers.
- [[Divisors]] — relies on enumerating and counting proper divisors.
- [[DivisorFunction]] — uses the divisor-count function d(n) and the product-of-divisors identity n^(d(n)/2).
- [[IntegerSequences]] — corresponds to OEIS sequence A111398.

## Contradictions
- None — reference task page.
