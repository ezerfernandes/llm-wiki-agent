---
title: "Almost prime (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Almost_prime
---

## Summary
A k-almost-prime is a natural number that is the product of exactly k (possibly repeated) prime factors, counted with multiplicity. The task asks the programmer to write a routine that generates k-almost-primes and uses it to print the first ten members for each k from 1 to 5. The key insight is that 1-almost-primes are just the primes themselves and 2-almost-primes are the semiprimes, so the general test reduces to counting prime factors with multiplicity.

## Task Requirements
- Implement a function/method that generates k-almost-primes.
- Build a table of the first ten k-almost-primes for each k in the range 1 ≤ k ≤ 5.

## Language Coverage
106 languages implement this task, giving very broad coverage across mainstream, functional, assembly, and esoteric ecosystems. Representative implementations include C, C++, Python, Java, JavaScript, Haskell, Rust, Go, Ruby, and Raku.

## Connections
- [[NumberTheory]] — the task is grounded in factorization of natural numbers.
- [[PrimeFactorization]] — counting prime factors with multiplicity is the core operation.
- [[Semiprime]] — the 2-almost-prime special case is exactly the set of semiprimes.
- [[PrimeNumbers]] — 1-almost-primes are the primes themselves.

## Contradictions
- None — reference task page.
