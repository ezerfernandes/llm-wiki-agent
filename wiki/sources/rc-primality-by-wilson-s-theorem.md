---
title: "Primality by Wilson's theorem (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, primality-test]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Primality_by_Wilson's_theorem
---

## Summary
This task asks the programmer to write a boolean function that determines whether a given integer is prime using Wilson's theorem. The key insight is that a number p is prime if and only if p evenly divides (p − 1)! + 1. While mathematically elegant, the approach is computationally impractical for large inputs because it requires evaluating a factorial that grows extremely fast.

## Task Requirements
- Write a boolean function returning whether an integer is prime.
- Use Wilson's theorem as the test: p is prime iff p divides (p − 1)! + 1.
- Correctly treat 1 and all non-positive integers as not prime.

## Language Coverage
76 languages implement this task, spanning low-level assembly through modern functional and scripting languages. Representative examples include C, C++, Rust, Java, Python, Haskell, Julia, Perl, Raku, Go, and historical or niche entries such as ALGOL 68, EDSAC order code, and PARI/GP.

## Connections
- [[WilsonsTheorem]] — the number-theoretic identity underlying the test
- [[PrimalityTest]] — the broader class of algorithms this task belongs to
- [[Factorial]] — the core computation, (p − 1)!, required by the theorem
- [[ModularArithmetic]] — divisibility of (p − 1)! + 1 by p is naturally expressed mod p

## Contradictions
- None — reference task page.
