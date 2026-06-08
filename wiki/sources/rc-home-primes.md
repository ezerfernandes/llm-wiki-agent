---
title: "Home primes (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, prime-factorization]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Home_primes
---

## Summary
The home prime HP(n) of an integer n > 1 is found by repeatedly factoring n into its prime factors (with repetitions), concatenating those factors in increasing order to form a new integer, and iterating until the result is itself prime. The notation HP_k(n) records the number k of iterations needed; primes are their own home prime. The key insight is the deceptively explosive growth of the concatenation chains — some inputs (notably HP49) generate astronomically large composites that have never been fully resolved.

## Task Requirements
- Find and display the home prime iteration chains for each integer from 2 through 20 inclusive.
- Stretch goal: produce the iteration chain for 65.
- Impossible goal: show the home prime HP(49) — included to illustrate that the chain remains unresolved (it requires factoring numbers too large for current methods).

## Language Coverage
22 languages implement this task, giving moderate breadth and showing how each language handles big-integer factorization. Representative implementations include Python, Go, Rust, Java, JavaScript, Julia, Perl, Raku, Ruby, and Wren, with several relying on built-in or library factorization support (e.g. Factor, PARI/GP, Mathematica).

## Connections
- [[PrimeFactorization]] — each iteration step factors the current integer into primes
- [[NumberTheory]] — the home prime is a number-theoretic construct (OEIS A037274)
- [[BigIntegerArithmetic]] — concatenation chains quickly exceed native integer ranges
- [[PrimalityTesting]] — each iteration must check whether the concatenated value is prime
- [[IteratedFunctions]] — HP is defined as repeated application of a factor-and-concatenate map

## Contradictions
- None — reference task page.
