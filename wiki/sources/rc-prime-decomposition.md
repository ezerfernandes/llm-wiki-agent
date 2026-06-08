---
title: "Prime decomposition (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, factorization, arbitrary-precision]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Prime_decomposition
---

## Summary
The task asks the programmer to write a function that returns the prime factorization of an integer n greater than 1 — the list (with multiplicity) of primes whose product equals n. For example, 12 decomposes to {2, 2, 3}. A key constraint is that the solution must not be bound by the machine word size; it should handle arbitrarily large numbers given enough RAM, which steers implementations toward big-integer arithmetic.

## Task Requirements
- Implement a function returning an array or collection holding the prime factors of a given n > 1.
- Repeated prime factors must appear once per occurrence (e.g. 12 → {2, 2, 3}).
- The implementation must work for arbitrarily large numbers, not limited by the computer's word size.
- An isPrime-like primality test may be assumed; one may reuse trial division or a Sieve of Eratosthenes.

## Language Coverage
117 languages implement this task, reflecting very broad coverage spanning systems, scripting, functional, and assembly languages — including C, C++, Rust, Go, Java, Python, Haskell, Common Lisp, Perl, and 360 Assembly.

## Connections
- [[PrimeFactorization]] — the core operation the task computes
- [[TrialDivision]] — the simplest algorithm for finding factors
- [[SieveOfEratosthenes]] — an alternative source of candidate primes
- [[NumberTheory]] — the mathematical domain (fundamental theorem of arithmetic)
- [[ArbitraryPrecisionArithmetic]] — required to lift the word-size limit

## Contradictions
- None — reference task page.
