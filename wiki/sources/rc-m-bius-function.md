---
title: "Möbius function (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Möbius_function
---

## Summary
The task is to implement the classical Möbius function μ(n), a multiplicative function central to number theory and combinatorics. The key insight is that μ(n) is determined entirely by the prime factorization of n: it returns 1 for n = 1, 0 whenever n has a squared prime factor, and otherwise ±1 according to whether the number of distinct prime factors of a square-free n is even (+1) or odd (−1).

## Task Requirements
- Write a routine μ(n) that computes the Möbius number for a positive integer n.
- Define μ(1) = 1.
- Return 1 for a square-free n with an even number of prime factors.
- Return −1 for a square-free n with an odd number of prime factors.
- Return 0 when n has a squared (repeated) prime factor.
- Use the routine to display at least the first 99 terms in a grid layout (not a single long row or column).

## Language Coverage
59 languages implement this task, spanning systems, functional, scripting, and array languages. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Julia, Perl, Raku, J, and Wren.

## Connections
- [[NumberTheory]] — μ(n) is a foundational arithmetic function in this field.
- [[PrimeFactorization]] — computing μ requires factoring n into primes and detecting repeated factors.
- [[MultiplicativeFunction]] — the Möbius function is multiplicative for coprime arguments.
- [[MertensFunction]] — the related task summing μ(k) over k from 1 to n.
- [[SquareFreeIntegers]] — μ(n) is nonzero exactly for square-free n.

## Contradictions
- None — reference task page.
