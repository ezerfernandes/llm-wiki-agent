---
title: "Prime reciprocal sum (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, big-integers, greedy-algorithm]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Prime_reciprocal_sum
---

## Summary
The task is to greedily build a sequence of primes where each new term is the smallest prime whose reciprocal can be added to a running cumulative sum while keeping that sum strictly below 1. Starting from a sum of 0, the first term is 2 (sum 1/2), then 3 (sum 5/6), and so on. The key insight is that the reciprocals grow rapidly: terms quickly become enormous primes with hundreds or thousands of digits, so exact rational arithmetic and big-integer primality testing are required.

## Task Requirements
- Generate the sequence: each term is the smallest prime whose reciprocal keeps the cumulative reciprocal sum strictly below 1.
- Find and display the first 10 terms; for any value with more than 40 digits, show the first and last 20 digits plus the total digit count.
- If primality testing is probabilistic, indicate so.
- Stretch goal: find the next 5 terms (or as many as patience allows), again showing only the first/last 20 digits and digit count.

## Language Coverage
24 languages implement this task, spanning systems and scripting languages with strong big-number support. Representative implementations include C, C#, Java, Rust, Python, Julia, Perl, Raku, Mathematica/Wolfram Language, PARI/GP, and Wren.

## Connections
- [[PrimeNumbers]] — each sequence term must be prime
- [[PrimalityTesting]] — large candidates require deterministic or probabilistic primality checks
- [[BigInteger]] — exact arbitrary-precision arithmetic for huge primes and fractions
- [[GreedyAlgorithm]] — smallest-valid-prime choice at each step
- [[NumberTheory]] — relates to OEIS A075442, the slowest-growing prime reciprocal sum to 1

## Contradictions
- None — reference task page.
