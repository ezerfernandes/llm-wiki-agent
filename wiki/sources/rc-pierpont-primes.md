---
title: "Pierpont primes (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-numbers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Pierpont_primes
---

## Summary
A Pierpont prime is a prime of the form 2^u · 3^v + 1 for non-negative integers u and v (the "first kind"); the "second kind" uses 2^u · 3^v − 1. The task asks for a routine that generates both kinds. The key insight is that candidates are exactly the numbers whose only prime factors are 2 and 3 (3-smooth numbers), shifted by ±1, so one enumerates these "smooth" candidates in increasing order and primality-tests each rather than scanning all integers.

## Task Requirements
- Write a routine to find Pierpont primes of the first and second kinds.
- Find and display the first 50 Pierpont primes of the first kind.
- Find and display the first 50 Pierpont primes of the second kind.
- If the language supports big integers, find and display the 250th Pierpont prime of each kind.

## Language Coverage
36 languages implement this task, spanning systems, scripting, functional, and array-oriented styles. Representative implementations include C, C++, C#, Go, Rust-adjacent FreeBASIC, Haskell, F#, Julia, Python, Perl, Raku, Ruby, J, and Wren.

## Connections
- [[PrimeNumbers]] — Pierpont primes are a constrained subset of primes.
- [[SmoothNumbers]] — candidates are 3-smooth numbers (only factors 2 and 3) plus or minus one.
- [[PrimalityTest]] — each generated candidate must be tested for primality.
- [[NumberTheory]] — the task sits within the study of special prime forms.
- [[BigInteger]] — the 250th terms require arbitrary-precision arithmetic.

## Contradictions
- None — reference task page.
