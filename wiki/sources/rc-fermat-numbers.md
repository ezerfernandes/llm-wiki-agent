---
title: "Fermat numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-numbers, bignum]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Fermat_numbers
---

## Summary
Fermat numbers are positive integers of the form F_n = 2^(2^n) + 1 for non-negative n, named after Pierre de Fermat. The task asks the programmer to generate them and to factor as many as feasible. The key insight is how rapidly these numbers grow (the exponent itself is a power of two), so the larger members quickly exceed native integer ranges and demand arbitrary-precision arithmetic; factoring them is also famously hard, with only the first five (F0–F4) known to be prime and only the first twelve fully factored.

## Task Requirements
- Write a routine to generate Fermat numbers F_n = 2^(2^n) + 1.
- Display the first 10 Fermat numbers, F0 through F9.
- Find and display the prime factors of as many Fermat numbers as patience (or roughly five minutes of processing) allows.

## Language Coverage
44 languages implement this task, spanning systems, functional, scripting, and array languages — most relying on a bignum library for the larger terms. Representative implementations include C, C++, Rust, Go, Java, Haskell, Python, Julia, Raku, and J.

## Connections
- [[NumberTheory]] — Fermat numbers are a classic number-theoretic sequence.
- [[PrimeNumbers]] — the task hinges on Fermat primes and prime factorization.
- [[ArbitraryPrecisionArithmetic]] — the doubly-exponential growth forces bignum support.
- [[IntegerFactorization]] — finding the prime factors of each F_n.
- [[PierreDeFermat]] — the mathematician these numbers are named after.

## Contradictions
- None — reference task page.
