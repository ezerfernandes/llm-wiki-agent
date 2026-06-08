---
title: "Giuga numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-factorization]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Giuga_numbers
---

## Summary
A Giuga number is a composite number n such that for each of its distinct prime factors f, the quantity (n/f - 1) is divisible by f. The task asks the programmer to find and display the first four Giuga numbers, with an optional stretch goal of finding the fifth and beyond. The key insight is that the search requires factoring candidate composites and checking a divisibility condition against each distinct prime factor; all known Giuga numbers happen to be even, though no odd example has been proven impossible.

## Task Requirements
- Determine and display the first four Giuga numbers.
- A number qualifies if it is composite and every distinct prime factor f divides (n/f - 1) exactly.
- Stretch: find the fifth Giuga number (and more if feasible) — these grow large quickly.

## Language Coverage
49 languages implement this task, spanning systems, scripting, functional, and array-oriented styles. Representative examples include C++, Rust, Go, Java, Python, Haskell, Julia, Perl, Raku, J, and PARI/GP, with several BigInt-capable implementations needed to reach the larger Giuga numbers in the stretch goal.

## Connections
- [[NumberTheory]] — the task is a pure number-theoretic property of integers.
- [[PrimeFactorization]] — each candidate must be factored into its distinct primes.
- [[Divisibility]] — the defining condition is a modular divisibility test on (n/f - 1).
- [[CompositeNumbers]] — Giuga numbers are by definition composite.
- [[BigIntegerArithmetic]] — higher Giuga numbers exceed native integer ranges.

## Contradictions
- None — reference task page.
