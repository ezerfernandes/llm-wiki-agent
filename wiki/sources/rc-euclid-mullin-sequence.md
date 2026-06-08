---
title: "Euclid-Mullin sequence (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-numbers, bignum]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Euclid-Mullin_sequence
---

## Summary
The Euclid-Mullin sequence is an infinite sequence of distinct primes where each term is the smallest prime factor of one plus the product of all preceding terms. Starting from 2, the next term is 2+1=3, then 2x3+1=7, and so on. The key insight is that this echoes Euclid's proof of the infinitude of primes; terms can grow very large very quickly, so factoring the accumulated product demands arbitrary-precision arithmetic and a capable integer factorization routine.

## Task Requirements
- Generate terms by taking, at each step, the least prime factor of (product of all earlier terms) + 1.
- Seed the sequence with the first element equal to 2.
- Compute and display the first 16 elements (or as many as the language supports without arbitrary precision).
- Stretch goal: compute the next 11 elements, for 27 total.
- Reference: OEIS sequence A000945.

## Language Coverage
39 languages implement this task, showing broad coverage across general-purpose and niche languages, with success largely gated by access to bignum and factorization support. Representative implementations include Python, Go, Java, C++, Raku, Julia, Perl, J, Mathematica/Wolfram Language, and PARI/GP.

## Connections
- [[PrimeNumbers]] — every term is a distinct prime
- [[IntegerFactorization]] — each step requires finding the least prime factor of a large integer
- [[EuclidsTheorem]] — the construction mirrors Euclid's proof of infinitely many primes
- [[ArbitraryPrecisionArithmetic]] — accumulated products quickly exceed native integer ranges
- [[OEIS]] — catalogued as sequence A000945

## Contradictions
- None — reference task page.
