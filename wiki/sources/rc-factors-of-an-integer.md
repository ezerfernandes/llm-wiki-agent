---
title: "Factors of an integer (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Factors_of_an_integer
---

## Summary
Compute the factors (divisors) of a positive integer — the positive integers that divide the number evenly, leaving no remainder. The key insight is that divisors come in pairs: if `d` divides `n`, then so does `n/d`, so a solution only needs to trial-divide up to the square root of `n` and emit both members of each pair. Every prime number has exactly two factors, 1 and itself.

## Task Requirements
- Given a positive integer, output all of its positive divisors (the integers that divide it with no remainder).
- Handling of zero and negative integers is explicitly out of scope.
- Note that the result always includes both 1 and the number itself.

## Language Coverage
173 languages implement this task, making it one of the most broadly covered entries on the site, spanning assembly, functional, scripting, and esoteric families. Representative implementations include C, C++, Python, Java, Haskell, Rust, Go, Ruby, Scheme, and APL.

## Connections
- [[DivisorFunction]] — factors are the divisors counted/summed by sigma functions
- [[TrialDivision]] — the standard approach of testing candidate divisors up to sqrt(n)
- [[PrimeNumber]] — a number is prime iff it has exactly two factors
- [[NumberTheory]] — divisibility is a foundational concept in this field
- [[PrimeDecomposition]] — related task that factors into prime powers rather than all divisors

## Contradictions
- None — reference task page.
