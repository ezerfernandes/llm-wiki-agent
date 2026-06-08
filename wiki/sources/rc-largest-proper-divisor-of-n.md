---
title: "Largest proper divisor of n (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Largest_proper_divisor_of_n
---

## Summary
The task is to compute the largest proper divisor of each integer n for n < 101, where a proper divisor is a divisor strictly less than n itself. By definition a(1) = 1, and for n > 1, a(n) is the greatest divisor of n that is not n. The key insight is that the largest proper divisor equals n divided by the smallest prime factor of n, so for prime n the answer is always 1, and for even n it is n/2.

## Task Requirements
- Define a(1) = 1.
- For n > 1, compute a(n) = the largest proper divisor of n (the greatest divisor strictly less than n).
- Produce the sequence for all n in the range n < 101.

## Language Coverage
78 languages implement this task, reflecting very broad coverage across mainstream, functional, and esoteric languages. Representative implementations include Python, C, C++, Java, JavaScript, Go, Rust, Haskell, Julia, Raku, and assembly variants such as X86 Assembly.

## Connections
- [[Divisor]] — the task centers on finding divisors of an integer.
- [[NumberTheory]] — proper divisors are a foundational number-theory concept.
- [[PrimeFactorization]] — the largest proper divisor is n divided by its smallest prime factor.
- [[Trial Division]] — a common brute-force approach iterates candidate divisors downward.

## Contradictions
- None — reference task page.
