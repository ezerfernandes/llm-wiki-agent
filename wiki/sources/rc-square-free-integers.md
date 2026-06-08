---
title: "Square-free integers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Square-free_integers
---

## Summary
The task asks for a function that tests whether a positive integer is square-free, meaning it is divisible by no perfect square other than 1. Equivalently, a number is square-free if no prime appears more than once in its factorization. The key practical insight is that you only need to check divisibility by squares of primes up to the square root of the candidate, which keeps the test efficient even at the trillion scale.

## Task Requirements
- Write a function that tests whether a positive integer is square-free.
- List all square-free integers between 1 and 145 (inclusive) in a horizontal format.
- List all square-free integers between 1 trillion and 1 trillion + 145 (inclusive).
- Report the count of square-free integers in the ranges 1–100, 1–1,000, 1–10,000, 1–100,000, and 1–1,000,000.

## Language Coverage
58 languages implement this task, giving broad coverage across functional, imperative, and array-oriented paradigms, with several requiring big-integer support for the trillion-range check. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Julia, Raku, J, and REXX.

## Connections
- [[NumberTheory]] — square-free integers are a classic topic in elementary number theory.
- [[PrimeFactorization]] — the property is defined by no repeated prime factor.
- [[TrialDivision]] — the straightforward test divides by squares of candidate factors.
- [[Squarefree]] — the specific named property and its asymptotic density (6/π²).

## Contradictions
- None — reference task page.
