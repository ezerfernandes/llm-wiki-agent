---
title: "Sieve of Eratosthenes (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-numbers, algorithms]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sieve_of_Eratosthenes
---

## Summary
The task asks the programmer to implement the classic Sieve of Eratosthenes, which finds all prime numbers up to a given integer limit by iteratively marking the multiples of each prime as composite. The key insight is that genuine sieving must be used (not trial division), and the only permitted optimizations are stopping the outer loop at the square root of the limit and starting the inner marking loop at the square of each prime just found.

## Task Requirements
- Implement the Sieve of Eratosthenes to find primes up to a given integer.
- Allowed optimizations: outer loop may stop at sqrt(limit); inner loop may start at the square of the prime.
- Do NOT use precomputed wheel optimizations (e.g. skipping even numbers, or numbers that are 1/5 mod 6) in the main version.
- If a wheel-based optimization is added, present it as a separate alternative version.
- The sieve itself must be the actual algorithm producing the primes (not trial division).

## Language Coverage
223 languages implement this task, making it one of the most widely covered Rosetta Code entries, spanning everything from low-level assembly to high-level functional languages. Representative implementations include C, C++, Python, Java, Haskell, Rust, Go, Lisp, Forth, and APL.

## Connections
- [[SieveOfEratosthenes]] — the named algorithm this task implements
- [[PrimeNumbers]] — the mathematical objects being computed
- [[NumberTheory]] — the branch of mathematics underlying the problem
- [[TrialDivision]] — the contrasting primality approach explicitly disallowed here
- [[WheelFactorization]] — the optimization permitted only as a separate alternative version

## Contradictions
- None — reference task page.
