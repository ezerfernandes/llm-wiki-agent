---
title: "Penta-power prime seeds (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, primes]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Penta-power_prime_seeds
---

## Summary
Find positive integers n (the "seeds") for which all five expressions n^0 + n + 1, n^1 + n + 1, n^2 + n + 1, n^3 + n + 1, and n^4 + n + 1 evaluate to prime numbers simultaneously. Note that n^0 + n + 1 = n + 2 and n^1 + n + 1 = 2n + 1, so two of the five conditions reduce to simple linear forms; the higher powers grow quickly, so each candidate requires testing increasingly large numbers for primality. The author notes the sequence appears to be original.

## Task Requirements
- Find and display the first thirty penta-power prime seeds (or as many as a language's math capability reasonably supports if fewer).
- Stretch goal: find and display the position and value of the first seed whose value exceeds ten million.

## Language Coverage
25 languages implement this task, a moderate spread across compiled, functional, scripting, and math-oriented languages. Representative entries include C, Go, Java, Python, Julia, Perl, Raku, Ruby, Nim, Wren, J, and Wolfram Language.

## Connections
- [[PrimalityTesting]] — each of the five expressions must be checked for primality
- [[NumberTheory]] — the task is a number-theoretic sequence-generation problem
- [[SieveOfEratosthenes]] — a common technique for generating the small primes used in trial-division tests
- [[PolynomialEvaluation]] — the five conditions are polynomials in n evaluated and tested

## Contradictions
- None — reference task page.
