---
title: "Product of min and max prime factors (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-factorization]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Product_of_min_and_max_prime_factors
---

## Summary
The task asks the programmer to compute, for each integer from 1 to 100, the product of its smallest and largest prime factors and display the results. The core operation is factoring each term and multiplying the minimum prime factor by the maximum prime factor. By convention the result for 1 is defined as 1 (since 1 has no prime factors), and for a prime p the answer is simply p×p; this corresponds to OEIS sequence A066048.

## Task Requirements
- Find and display the product of the minimum and maximum prime factors for the terms 1 through 100, inclusive.
- Treat the term for 1 as a special case whose result is defined to be 1.

## Language Coverage
48 languages implement this task, spanning systems languages, functional languages, array languages, and esoteric or historical languages. Representative examples include C, C++, Java, Python, Go, Haskell, Julia, Perl, Raku, APL, and J.

## Connections
- [[PrimeFactorization]] — the task hinges on factoring each integer into primes.
- [[NumberTheory]] — prime factors and multiplicative structure of integers.
- [[TrialDivision]] — the typical method for finding smallest and largest prime factors.
- [[OEIS]] — corresponds to sequence A066048.

## Contradictions
- None — reference task page.
