---
title: "Chowla numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-numbers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Chowla_numbers
---

## Summary
The task asks the programmer to implement Chowla's function, where chowla(n) is the sum of the proper divisors of a positive integer n excluding both 1 and n itself (equivalently sigma(n) - 1 - n). The key insight is that this single function doubles as a primality and perfectness test: chowla(n) = 0 (for n > 1) means n is prime, while chowla(n) = n - 1 means n is a perfect number.

## Task Requirements
- Create a `chowla` function returning the chowla number for a positive integer n.
- Display, one per line, the integer index and its chowla number for the first 37 integers.
- Use chowla(n) = 0 to detect primes; count primes up to 100, 1,000, 10,000, 100,000, 1,000,000, and 10,000,000.
- Use chowla(n) = n - 1 to detect perfect numbers; find and display all perfect numbers up to 35,000,000.
- Format large numbers with commas and show all output.

## Language Coverage
64 languages implement this task, showing broad coverage across system, scripting, functional, and math-oriented languages. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Julia, Perl, Raku, REXX, and Wolfram Language.

## Connections
- [[NumberTheory]] — the task belongs to the prime-numbers / number-theory category.
- [[DivisorFunction]] — chowla is a variant of the sigma (sum-of-divisors) function.
- [[PrimeNumber]] — chowla(n) = 0 serves as a primality test.
- [[PerfectNumber]] — chowla(n) = n - 1 identifies perfect numbers.
- [[ProperDivisors]] — the chowla number sums proper divisors minus one.

## Contradictions
- None — reference task page.
