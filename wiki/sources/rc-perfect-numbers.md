---
title: "Perfect numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, divisors]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Perfect_numbers
---

## Summary
The task asks the programmer to write a function that decides whether a given positive integer is a perfect number — that is, a number equal to the sum of its proper positive divisors (all divisors excluding the number itself), such as 6 = 1 + 2 + 3. The key insight is that perfectness can be tested either by summing proper divisors directly or by checking that the number equals half the sum of all of its divisors. Known perfect numbers connect to Mersenne primes via the formula (2^n − 1) × 2^(n−1), and it remains unknown whether any odd perfect numbers exist.

## Task Requirements
- Implement a predicate function that returns whether an input number is perfect.
- A perfect number is a positive integer equal to the sum of its proper positive divisors (excluding itself).
- Equivalently, it is a number that is half the sum of all its positive divisors (including itself).

## Language Coverage
135 languages implement this task, giving very broad coverage across functional, imperative, and esoteric paradigms. Representative implementations include Python, C, C++, Java, Haskell, Rust, Go, Ruby, Scheme, and REXX.

## Connections
- [[NumberTheory]] — perfect numbers are a classic topic in elementary number theory.
- [[Divisors]] — the test centers on enumerating and summing proper divisors.
- [[MersennePrime]] — even perfect numbers correspond one-to-one with Mersenne primes.
- [[LucasLehmerTest]] — the referenced primality test used to find the Mersenne primes that generate perfect numbers.

## Contradictions
- None — reference task page.
