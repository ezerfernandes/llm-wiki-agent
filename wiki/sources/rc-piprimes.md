---
title: "Piprimes (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-numbers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Piprimes
---

## Summary
The task asks the programmer to compute pi(n), the prime-counting function, which returns the number of primes less than or equal to n. The specific scope is constrained to values of n where pi(n) is below 22, so only a small range near the start of the integers needs handling. The key insight is that pi(n) can be found simply by counting primes up to n (e.g. via a sieve or trial division) rather than needing the advanced analytic approximations used for large arguments.

## Task Requirements
- Implement pi(n), the count of primes <= n.
- Restrict consideration to the regime where pi(n) < 22 (small n).
- Reference material: the Wikipedia Prime-counting function article and OEIS sequence A000720.

## Language Coverage
44 languages implement this task, showing broad coverage across mainstream and niche languages. Representative implementations include Python, C, C++, Java, Go, Julia, Perl, Raku, Ruby, Lua, and J.

## Connections
- [[PrimeCountingFunction]] — pi(n) is exactly this function
- [[PrimeNumbers]] — the task counts members of this set
- [[SieveOfEratosthenes]] — common technique for enumerating primes up to n
- [[NumberTheory]] — the broader field this problem belongs to

## Contradictions
- None — reference task page.
