---
title: "Greatest prime dividing the n-th cubefree number (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-factorization]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Greatest_prime_dividing_the_n-th_cubefree_number
---

## Summary
The task asks the programmer to generate the sequence a[n] (OEIS A370833), where a[n] is the largest prime factor of the n-th cubefree number. A cubefree number is a positive integer whose prime factorization contains no factor raised to the third (or higher) power; all primes are trivially cubefree, and 1 is the first such number by convention with a[1] = 1. The key insight is that solving the stretch goals efficiently requires counting cubefree numbers up to a bound via inclusion-exclusion over cubes rather than sieving each candidate.

## Task Requirements
- Compute and display the first 100 terms of a[n].
- Compute and display the 1,000th, 10,000th, and 100,000th members of the sequence.
- Stretch: compute and display the 1 millionth and 10 millionth terms.

## Language Coverage
21 languages implement this task, offering moderate breadth across compiled, interpreted, and array-oriented styles. Representative implementations include C++, Java, Rust, Nim, Pascal, Python, Julia, Perl, Raku, Wren, and Mathematica / Wolfram Language.

## Connections
- [[CubefreeNumber]] — the defining property filtering the integers
- [[PrimeFactorization]] — needed to find the greatest prime factor of each term
- [[InclusionExclusionPrinciple]] — used to count cubefree numbers below a bound for large n
- [[NumberTheory]] — the broader domain of the task
- [[OEIS]] — sequence A370833 is the reference definition

## Contradictions
- None — reference task page.
