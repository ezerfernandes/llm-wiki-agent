---
title: "Ascending primes (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, primes, combinatorics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Ascending_primes
---

## Summary
Generate and display every prime number whose decimal digits are in strictly ascending order (no repeated digits, each digit larger than the one before). The naive approach filters all primes below 123,456,789, but the key insight is that ascending-digit numbers form a tiny set: they are exactly the combinations of the digits 1–9, so one only needs to generate those candidates and run roughly 511 primality tests rather than sieving millions of numbers.

## Task Requirements
- Generate all primes with strictly ascending decimal digits.
- Show the complete list (digits must increase from left to right, so each candidate uses a subset of {1..9} in sorted order).

## Language Coverage
66 languages implement this task, spanning systems and scripting languages as well as several BASIC and Lisp dialects. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Perl, Raku, and Wren.

## Connections
- [[PrimeNumbers]] — the core objects being filtered and tested
- [[PrimalityTest]] — each candidate must be checked for primality
- [[Combinatorics]] — candidates are subsets/combinations of the digits 1–9 in sorted order
- [[DigitManipulation]] — the ascending-order constraint is a property of the decimal digits
- [[Sieve of Eratosthenes]] — the naive baseline approach this task improves upon

## Contradictions
- None — reference task page.
