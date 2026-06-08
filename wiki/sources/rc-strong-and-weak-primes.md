---
title: "Strong and weak primes (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-numbers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Strong_and_weak_primes
---

## Summary
The task asks the programmer to classify primes by comparing each prime to the average of its two neighboring primes. A prime is "strong" when it is greater than the mean of the prime before and the prime after it, and "weak" when it is less than that mean. The key insight is that this requires generating a sequence of primes and examining sliding triples of consecutive primes, distinct from the cryptographic notion of a strong prime.

## Task Requirements
- Display the first 36 strong primes on one line (where prime(p) > [prime(p-1) + prime(p+1)] / 2).
- Display the count of strong primes below 1,000,000.
- Display the count of strong primes below 10,000,000.
- Display the first 37 weak primes on one line (where prime(p) < [prime(p-1) + prime(p+1)] / 2).
- Display the count of weak primes below 1,000,000 and below 10,000,000.
- Optionally format counts and threshold numbers with comma separators.

## Language Coverage
41 languages implement this task, spanning systems languages, scripting languages, functional languages, and computer-algebra systems. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Julia, Perl, Raku, REXX, and Wolfram Language.

## Connections
- [[PrimeNumbers]] — the task operates entirely on the prime sequence
- [[SieveOfEratosthenes]] — a common way to generate primes up to the bounds
- [[NumberTheory]] — strong/weak primes are a number-theoretic classification
- [[OEIS]] — corresponds to sequences A051634 (strong) and A051635 (weak)

## Contradictions
- None — reference task page.
