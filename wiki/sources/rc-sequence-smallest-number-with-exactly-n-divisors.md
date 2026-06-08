---
title: "Sequence: smallest number with exactly n divisors (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, divisors]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sequence:_smallest_number_with_exactly_n_divisors
---

## Summary
The task asks the programmer to generate the integer sequence whose nth term is the smallest natural number having exactly n divisors. At least the first 15 terms must be shown. The key insight is that the count of divisors is determined by the exponents in a number's prime factorization (the divisor-counting function), so for prime n the answer is 2^(n-1), while composite n often yields smaller values via mixed factorizations.

## Task Requirements
- For each n, find the smallest natural number that has exactly n divisors.
- Display at least the first 15 terms of the resulting sequence.
- Corresponds to OEIS A005179.

## Language Coverage
55 languages implement this task, spanning a broad mix of systems, functional, scripting, and array languages. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Julia, Perl, Raku, and APL.

## Connections
- [[NumberTheory]] — the task is fundamentally about properties of integers.
- [[PrimeFactorization]] — divisor counts derive from prime exponent structure.
- [[DivisorFunction]] — computing the number of divisors (tau) drives the search.
- [[IntegerSequences]] — produces an OEIS catalogued sequence (A005179).
- [[BruteForceSearch]] — a common straightforward implementation scans integers until the divisor count matches.

## Contradictions
- None — reference task page.
