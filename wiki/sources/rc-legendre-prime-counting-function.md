---
title: "Legendre prime counting function (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, primes, recursion]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Legendre_prime_counting_function
---

## Summary
This task asks the programmer to implement Legendre's prime-counting function π(n), which counts primes not greater than n using the inclusion/exclusion principle rather than a full sieve. The core is a recursive helper φ(x, a) that counts integers up to x with all multiples of the first a primes removed, from which π(n) = φ(n, a) + a − 1 where a = π(√n). The key insight is that only primes up to √n need to be enumerated, and a small terminating optimization (stop recursing when x is 0 or x ≤ pₐ) avoids exponential blow-up without needing a memoization cache.

## Task Requirements
- Implement φ(x, a) recursively: φ(x, 0) = x, and φ(x, a) = φ(x, a−1) − φ(⌊x/pₐ⌋, a−1).
- Implement π(n): 0 when n < 2, otherwise φ(n, a) + a − 1 with a = π(√n).
- Sieve only up to √n to obtain the required primes (an external sieve library is allowed).
- Compute and display π(n) for n = 1, 10, 100, ... up to 10⁹ (1 billion).
- Memoize φ(x, a) — or apply the obvious tree-pruning optimization — so performance is not exponential.

## Language Coverage
42 languages implement this task, giving broad coverage across functional, imperative, and scripting paradigms. Representative implementations include C, C++, Go, Rust-adjacent systems languages, Java, Python, Haskell, F#, Julia, Raku, Ruby, Nim, and Wren.

## Connections
- [[PrimeCountingFunction]] — π(n) is the quantity this task computes.
- [[InclusionExclusionPrinciple]] — the combinatorial basis of the φ recurrence.
- [[SieveOfEratosthenes]] — used to enumerate the primes up to √n.
- [[Memoization]] — caching φ(x, a) to tame the recurrence (or pruning instead).
- [[NumberTheory]] — the broader mathematical domain of the task.

## Contradictions
- None — reference task page.
