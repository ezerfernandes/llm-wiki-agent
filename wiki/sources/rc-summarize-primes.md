---
title: "Summarize primes (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-numbers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Summarize_primes
---

## Summary
The task asks the programmer to consider running sums of consecutive primes starting from 2 (with each prime less than 1000), and to identify which of those partial sums are themselves prime. The key insight is to accumulate primes in sequence order, test each cumulative sum for primality, and report the qualifying sequences. For each prime cumulative sum it displays the sequence length, the last prime included, and the sum itself.

## Task Requirements
- Generate consecutive primes p from 2 onward where p < 1000.
- For each sequence length n > 0, compute the sum of the first n consecutive primes.
- Select only those sequences whose cumulative sum is itself prime.
- For each selected sequence, display the length n, the last prime in the sequence, and the prime sum.

## Language Coverage
43 languages implement this task, giving broad coverage across functional, imperative, array, and scripting paradigms. Representative implementations include Python, C, C++, Go, Rust, Haskell, Julia, Raku, J, and Wren.

## Connections
- [[PrimeNumber]] — the task is built entirely on generating and testing primes.
- [[SieveOfEratosthenes]] — a common technique for producing the consecutive primes below 1000.
- [[PrimalityTest]] — each cumulative sum must be checked for primality.
- [[PrefixSum]] — the running sums of consecutive primes are prefix (cumulative) sums.

## Contradictions
- None — reference task page.
