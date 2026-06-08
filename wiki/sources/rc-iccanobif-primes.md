---
title: "Iccanobif primes (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-numbers, fibonacci]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Iccanobif_primes
---

## Summary
An iccanobif prime is a prime number that becomes a Fibonacci number when its decimal digits are reversed ("iccanobif" is "fibonacci" spelled backwards). The task is to find these by testing reversed Fibonacci numbers for primality. The key insight is to generate Fibonacci numbers, reverse each one's digits, and check whether the result is prime, since this is far cheaper than scanning all primes and reversing each.

## Task Requirements
- Find and display the first 10 iccanobif primes.
- Stretch: find and display the digit count of the next 15 iccanobif primes (these grow large, so only the digit length is reported).
- Reference is OEIS A036797.

## Language Coverage
31 languages implement this task, giving broad coverage across systems, scripting, array, and big-integer-capable languages. Representative implementations include Ada, ALGOL 68, C, C++, Java, Python, Julia, Perl, Raku, Phix, Nim, and Wren.

## Connections
- [[PrimeNumbers]] — core primality test driving the task
- [[FibonacciSequence]] — the source numbers that are reversed and tested
- [[DigitReversal]] — the transformation applied to each Fibonacci number
- [[BigIntegerArithmetic]] — needed because later Fibonacci numbers exceed native integer ranges
- [[NumberTheory]] — the mathematical domain of the problem

## Contradictions
- None — reference task page.
