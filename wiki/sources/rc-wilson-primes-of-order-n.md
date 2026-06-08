---
title: "Wilson primes of order n (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, primes]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Wilson_primes_of_order_n
---

## Summary
A Wilson prime of order n is a prime p whose square exactly divides the expression (n − 1)! × (p − n)! − (−1)^n. The task generalizes the classic Wilson prime definition: for n = 1 it reduces to the familiar test where p² divides (p − 1)! + 1, whose only known examples are 5, 13, and 563. The key insight is that the factorials only need to be tracked modulo p² to keep the arithmetic tractable.

## Task Requirements
- For each order n from 1 to 11 inclusive, find the primes p satisfying the divisibility condition.
- If the language lacks big integers, search primes p < 18; if it supports big integers, search primes p < 11,000.
- Display the resulting Wilson primes for each order on the page.

## Language Coverage
38 languages implement this task, spanning systems and scripting languages as well as math-oriented and BASIC dialects. Representative implementations include C, C++, Rust, Go, Java, Python, Perl, Raku, Julia, Mathematica/Wolfram Language, and REXX.

## Connections
- [[WilsonsTheorem]] — the n = 1 case is the squared form of Wilson's theorem
- [[PrimeNumbers]] — the search domain is restricted to primes p
- [[Factorial]] — the core expression is built from products of factorials
- [[ModularArithmetic]] — factorials are reduced modulo p² to bound the computation
- [[NumberTheory]] — the task is a generalization within elementary number theory

## Contradictions
- None — reference task page.
