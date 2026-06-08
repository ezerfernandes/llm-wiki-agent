---
title: "Extensible prime generator (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, generators]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Extensible_prime_generator
---

## Summary
The task asks for a prime number generator that yields primes in order without a fixed upper bound, automatically adjusting to produce arbitrarily large primes within system limits. The key insight is extensibility: rather than sieving up to a known ceiling, the generator must either count open-endedly or grow its working limit on demand (e.g., a segmented or incremental sieve, or lazy infinite sequences).

## Task Requirements
- Implement a generator producing primes in ascending order with no predetermined upper limit.
- Demonstrate extensibility by one of: an open-ended counter (state where it lives), an automatically extended limit (start small so it must grow), or another clearly explained unbounded method.
- Use the generator to show the first twenty primes.
- Show the primes between 100 and 150.
- Show the count of primes between 7,700 and 8,000.
- Show the 10,000th prime.

## Language Coverage
61 languages implement this task, a broad cross-section spanning systems, functional, and scripting paradigms. Representative entries include C, C++, Rust, Go, Java, Haskell, Python, Ruby, Perl, Raku, Julia, and Wren, with lazy infinite sequences common in the functional languages and incremental/segmented sieves in the imperative ones.

## Connections
- [[PrimeNumber]] — the mathematical objects being generated
- [[SieveOfEratosthenes]] — the classic algorithm, here made incremental or segmented for extensibility
- [[Generators]] — lazy/on-demand production of an unbounded sequence
- [[NumberTheory]] — the domain the task belongs to
- [[EmirpPrimes]] — a related task this generator is designed to support

## Contradictions
- None — reference task page.
