---
title: "The sieve of Sundaram (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-numbers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/The_sieve_of_Sundaram
---

## Summary
This task asks the programmer to implement the Sieve of Sundaram, an algorithm that generates the odd prime numbers. Starting from the positive integers, it marks numbers of the form i + j + 2ij; every unmarked value n then yields the prime 2n+1. The key insight is that the Sundaram sieve is essentially equivalent to an odds-only Sieve of Eratosthenes, but because it culls using all odd "base" numbers rather than only the discovered primes, its time complexity is O(n log n) versus the SoE's O(n log log n) — making it noticeably slower at large ranges.

## Task Requirements
- Implement the Sieve of Sundaram: mark every kth element starting at the appropriate offset for successive odd strides (every 3rd from 4, every 5th from 12, every 7th from 17, etc.).
- For each unmarked value n, output 2*n+1, producing the ordered set of odd primes.
- Find and output the first 100 Sundaram primes and the millionth Sundaram prime.
- Optionally compare the results against those produced by the Sieve of Eratosthenes.

## Language Coverage
32 languages implement this task, spanning systems languages, functional languages, scripting, and array/math-oriented tools. Representative entries include C, C++, C#, Java, Go, Nim, Python, Haskell, F#, Julia, Raku, and J.

## Connections
- [[SieveOfSundaram]] — the named algorithm this task implements
- [[SieveOfEratosthenes]] — the closely related, asymptotically faster prime sieve
- [[PrimeNumbers]] — the output set (odd primes) the task generates
- [[NumberTheory]] — the mathematical domain underlying the technique
- [[TimeComplexity]] — O(n log n) vs O(n log log n) tradeoff highlighted in the task

## Contradictions
- None — reference task page.
