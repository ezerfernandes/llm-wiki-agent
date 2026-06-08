---
title: "Mertens function (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Mertens_function
---

## Summary
The task asks the programmer to compute the Mertens function M(x), defined as the running sum of the Möbius function μ(n) from n = 1 to x. Equivalently it counts square-free integers up to x with an even number of prime factors minus those with an odd number. The key insight is that implementing M(x) reduces to summing Möbius values, so a Möbius routine is the natural building block.

## Task Requirements
- Write a routine that returns the Mertens number M(x) for any positive integer x.
- Display at least the first 99 terms in a grid layout (not a single line or column).
- Report how many times M(n) equals zero for n in the range M(1) through M(1000).
- Report how many times the sequence crosses zero (current term equals zero but the preceding term does not) in M(1) through M(1000).

## Language Coverage
58 languages implement this task, spanning low-level assembly through high-level array and functional languages. Representative implementations include C, C++, Go, Rust-adjacent Swift, Python, Haskell, Julia, J, APL, Raku, and 8080/8086 Assembly.

## Connections
- [[MobiusFunction]] — Mertens is the cumulative sum of the Möbius function.
- [[NumberTheory]] — the task is a classic multiplicative number-theory exercise.
- [[PrimeFactorization]] — Möbius values depend on counting distinct prime factors and detecting square-free numbers.
- [[MertensConjecture]] — the famous (disproven) bound |M(x)| < √x motivates the function.

## Contradictions
- None — reference task page.
