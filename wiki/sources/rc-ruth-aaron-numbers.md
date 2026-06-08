---
title: "Ruth-Aaron numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-factorization]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Ruth-Aaron_numbers
---

## Summary
A Ruth-Aaron pair is two consecutive integers whose sums of prime divisors are equal — named after Babe Ruth's 714 home run record and Hank Aaron's record-breaking 715th, the canonical example. The task explores two variants: one summing distinct prime divisors, the other summing prime factors with multiplicity. The key insight is that "Ruth-Aaron numbers" reduce to comparing the prime-factor-sum of n against that of n+1 across a sequence.

## Task Requirements
- Find and show the first 30 Ruth-Aaron numbers using prime factors (counted with multiplicity).
- Find and show the first 30 Ruth-Aaron numbers using prime divisors (distinct).
- Each group is referred to by its first (smaller) number.
- Stretch: find the first Ruth-Aaron triple (three consecutive integers) for the factors variant.
- Stretch: find the first Ruth-Aaron triple for the divisors variant.

## Language Coverage
25 languages implement this task, showing broad coverage across functional, systems, and array-oriented styles. Representative implementations include C++, Go, Haskell, Java, Julia, Python, Perl, Raku, Nim, and J.

## Connections
- [[PrimeFactorization]] — core operation: decomposing each integer into primes.
- [[NumberTheory]] — the task is a recreational number-theory sequence.
- [[SieveOfEratosthenes]] — common technique for generating primes to factorize efficiently.
- [[IntegerSequences]] — corresponds to OEIS sequences A006145 and A039752.

## Contradictions
- None — reference task page.
