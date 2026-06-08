---
title: "Primorial numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, primes, bignum]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Primorial_numbers
---

## Summary
A primorial number is the product of the first n successive prime numbers, with primorial(0) defined as 1. The task asks the programmer to generate this sequence (OEIS A002110), which grows even faster than factorials. The key practical insight is that the numbers explode in size, so exact arbitrary-precision integer arithmetic is required rather than floating-point approximations.

## Task Requirements
- Show the first ten primorial numbers (indices 0 through 9 inclusive).
- Show the length (number of decimal digits) of the primorial numbers whose index is 10, 100, 1,000, 10,000, and 100,000.
- Optionally show the length of the one-millionth primorial number.
- Use exact integers, not approximations.

## Language Coverage
49 languages implement this task, spanning bignum-friendly scripting languages and lower-level languages that need explicit big-integer libraries. Representative examples include Python, Haskell, Julia, Java, C++, Rust, Go, Perl, Raku, and REXX.

## Connections
- [[PrimeNumbers]] — the sequence is built from successive primes
- [[NumberTheory]] — primorials are a classic number-theoretic sequence
- [[ArbitraryPrecisionArithmetic]] — exact bignum integers are mandatory as values grow rapidly
- [[Factorial]] — analogous cumulative-product construction
- [[SieveOfEratosthenes]] — common technique for generating the required primes

## Contradictions
- None — reference task page.
