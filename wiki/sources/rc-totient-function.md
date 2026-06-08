---
title: "Totient function (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Totient_function
---

## Summary
The task asks the programmer to implement Euler's totient function φ(n), which counts the integers k in the range 1 ≤ k ≤ n that are coprime to n (i.e. gcd(n, k) = 1). The key insight exploited here is that n is prime exactly when φ(n) = n − 1, since a prime is coprime to every smaller positive integer. This lets the same totient routine double as a primality test and a prime counter.

## Task Requirements
- Create a `totient` function returning φ(n).
- For the first 25 integers, display one per line: the integer, its totient value, and whether the integer is prime.
- Count and display the number of primes up to 100, 1,000, and 10,000.
- Optionally count and display the number of primes up to 100,000.
- Show all output.

## Language Coverage
73 languages implement this task, giving broad coverage across functional, imperative, assembly, and array-oriented paradigms. Representative implementations include Python, C, C++, Rust, Go, Haskell, Java, APL, J, and REXX.

## Connections
- [[EulerTotientFunction]] — the arithmetic function being implemented.
- [[GreatestCommonDivisor]] — the coprimality test (gcd = 1) underpinning the count.
- [[PrimalityTest]] — φ(n) = n − 1 characterizes primes.
- [[NumberTheory]] — the mathematical domain of the task.
- [[Coprime]] — the relation φ counts.

## Contradictions
- None — reference task page.
