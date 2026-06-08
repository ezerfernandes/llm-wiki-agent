---
title: "Pisano period (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Pisano_period
---

## Summary
The Fibonacci sequence taken modulo any integer n is periodic, and the length of that repeating cycle is called the Pisano period. The task asks the programmer to compute Pisano periods efficiently rather than by brute force: the key insight is that the period is multiplicative over coprime factors (the period of m×n equals the LCM of the individual periods when m and n are coprime), and the period of a prime power p^k equals p^(k-1) times the period of p (a conjectured but exception-free formula).

## Task Requirements
- Write `pisanoPrime(p, k)` returning the Pisano period of p^k, where p is prime and k is a positive integer.
- Write `pisano(m)` that uses `pisanoPrime` (via prime factorization plus LCM) to return the Pisano period of any positive integer m.
- Print `pisanoPrime(p, 2)` for every prime below 15.
- Print `pisanoPrime(p, 1)` for every prime below 180.
- Print `pisano(m)` for every integer from 1 to 180.

## Language Coverage
31 languages implement this task, spanning array/APL-style, functional, scripting, and systems languages. Representative entries include C++, Go, Haskell, Java, JavaScript, Julia, Python, Perl, Raku, Lua, and Wren.

## Connections
- [[FibonacciSequence]] — the period is the cycle length of Fibonacci numbers under a modulus
- [[PisanoPeriod]] — the named number-theoretic quantity this task computes
- [[PrimeFactorization]] — decomposing m into prime powers drives the efficient algorithm
- [[LeastCommonMultiple]] — combines per-factor periods for coprime components
- [[ModularArithmetic]] — the sequence is evaluated modulo n

## Contradictions
- None — reference task page.
