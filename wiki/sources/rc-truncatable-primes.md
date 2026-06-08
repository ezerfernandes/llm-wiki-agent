---
title: "Truncatable primes (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, primes]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Truncatable_primes
---

## Summary
A truncatable prime is a prime that remains prime as you repeatedly strip digits off one end. A left-truncatable prime stays prime as leading digits are removed (e.g. 997 → 97 → 7), and a right-truncatable prime stays prime as trailing digits are removed (e.g. 7393 → 739 → 73 → 7). The task is to find the largest left-truncatable and right-truncatable primes below one million in base 10. A key constraint is that no digit may be zero, since a zero would leave a number with a leading zero or a non-prime truncation.

## Task Requirements
- Find the largest left-truncatable prime less than one million (base 10).
- Find the largest right-truncatable prime less than one million (base 10).
- A number qualifies only if every truncation from the relevant end is also prime.
- No zeroes are permitted anywhere in the number.

## Language Coverage
69 languages implement this task, giving very broad coverage across functional, imperative, and array-oriented paradigms. Representative implementations include C, C++, C#, Python, Java, Haskell, Julia, Rust, Go, Perl, and Raku.

## Connections
- [[PrimeNumbers]] — the core objects being tested and truncated
- [[PrimalityTest]] — each truncation requires a primality check
- [[SieveOfEratosthenes]] — a common way to precompute primes under one million
- [[NumberTheory]] — the broader domain this task belongs to

## Contradictions
- None — reference task page.
