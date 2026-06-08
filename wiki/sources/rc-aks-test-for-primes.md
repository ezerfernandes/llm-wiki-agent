---
title: "AKS test for primes (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, combinatorics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/AKS_test_for_primes
---

## Summary
This task implements the elementary primality lemma used as a stepping stone in the AKS primality test (but not the AKS test itself). The key insight: a number p is prime if and only if every coefficient of the polynomial (x−1)^p − (x^p − 1) is divisible by p. Equivalently, p is prime when all the interior binomial coefficients of the expansion of (x−1)^p are divisible by p. The page warns this is an inefficient exponential-time algorithm, not the actual polynomial-time AKS test.

## Task Requirements
- Write a function that, given p, generates the coefficients of the expanded polynomial (x−1)^p.
- Display the polynomial expansions of (x−1)^p for p from 0 to at least 7 inclusive.
- Use that function to build a primality test that returns whether p is prime via the divisibility theorem.
- Generate a list of all primes under 35.
- Stretch goal: generate all primes under 50, which requires integers wider than 31 bits.

## Language Coverage
86 languages implement this task, giving very broad coverage across paradigms. Representative implementations include C, C++, Python, Java, Haskell, Rust, Go, Julia, Common Lisp, and Raku.

## Connections
- [[BinomialCoefficients]] — the polynomial coefficients of (x−1)^p are signed binomial coefficients.
- [[PrimalityTesting]] — the task is a divisibility-based primality criterion.
- [[NumberTheory]] — based on a number-theoretic theorem about prime divisibility.
- [[PascalsTriangle]] — the coefficient rows correspond to Pascal's triangle entries.
- [[ArbitraryPrecisionArithmetic]] — the stretch goal needs integers beyond 31 bits.

## Contradictions
- None — reference task page.
