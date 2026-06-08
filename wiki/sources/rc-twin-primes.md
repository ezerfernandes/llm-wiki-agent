---
title: "Twin primes (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-numbers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Twin_primes
---

## Summary
Twin primes are pairs of prime numbers (P1, P2) where P2 = P1 + 2, such as (3, 5), (5, 7), and (11, 13). The task asks for a program that counts how many twin prime pairs exist below a user-specified bound. The key efficiency insight is that generating primes once via a sieve and then scanning for adjacent primes differing by 2 is far cheaper than testing each candidate independently.

## Task Requirements
- Display the count of twin prime pairs found under a user-specified number, with both P1 and P2 below that bound.
- Extension: find all twin prime pairs under 100000, 10000000, and 1000000000.
- Extension: discuss the time complexity and possible ways to reduce computation time.
- Match the given examples: 8 pairs under 100, and 35 pairs under 1000.

## Language Coverage
42 languages implement this task, spanning systems languages, scripting languages, functional languages, and many BASIC dialects. Representative implementations include C, C++, Rust, Go, Java, Python, Perl, Raku, Julia, Haskell-adjacent F#, and Mathematica.

## Connections
- [[PrimeNumbers]] — the underlying objects being paired
- [[SieveOfEratosthenes]] — the standard efficient way to generate the prime candidates
- [[NumberTheory]] — twin primes are a classic open problem (the twin prime conjecture)
- [[PrimalityTesting]] — naive approaches test each candidate individually

## Contradictions
- None — reference task page.
