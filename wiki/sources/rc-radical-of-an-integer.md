---
title: "Radical of an integer (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-factorization]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Radical_of_an_integer
---

## Summary
The radical of a positive integer is the product of its distinct prime factors (with the radical of 1 defined as 1 by convention). For example, 504 = 2³ × 3² × 7 has radical 2 × 3 × 7 = 42. The key insight is that the radical strips away the exponents in a prime factorization, so a number's radical depends only on which primes divide it, not how many times.

## Task Requirements
- Compute and display the radicals of the first 50 positive integers.
- Compute the radicals of 99999, 499999, and 999999.
- Tabulate the distribution of the first one million integers by their count of distinct prime factors (max is 7 in this range).
- Bonus: by an independent method, count the primes and prime powers up to one million and verify the count of integers with exactly one distinct prime factor.

## Language Coverage
32 languages implement this task, spanning systems languages, scripting languages, and array/functional languages. Representative implementations include ALGOL 68, C, C++, Java, Python, Julia, Perl, Raku, Ruby, J, Phix, and Wren.

## Connections
- [[PrimeFactorization]] — the radical is derived directly from the prime factorization
- [[NumberTheory]] — radicals underpin square-free numbers and the abc conjecture
- [[SquareFreeIntegers]] — a number equals its own radical iff it is square-free
- [[SieveOfEratosthenes]] — an efficient way to factor or count primes over a range up to one million

## Contradictions
- None — reference task page.
