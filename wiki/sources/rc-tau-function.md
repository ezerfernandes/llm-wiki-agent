---
title: "Tau function (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Tau_function
---

## Summary
The task asks the programmer to implement the divisor-counting function τ(n) (tau), which returns the number of positive divisors of a positive integer n. The expected output is τ(n) for the first 100 positive integers. The key insight is that τ is a multiplicative function: for n = p1^a1 · p2^a2 · …, τ(n) = (a1+1)(a2+1)…, so it can be derived efficiently from prime factorization rather than trial-counting every divisor.

## Task Requirements
- Given a positive integer, count the number of its positive divisors.
- Show the result for the first 100 positive integers.

## Language Coverage
87 languages implement this task, spanning a very broad range from low-level assembly to high-level functional and array languages. Representative implementations include C, C++, Rust, Go, Python, Haskell, Julia, J, APL, and REXX.

## Connections
- [[DivisorFunction]] — τ(n) = σ0(n), the order-zero divisor function
- [[NumberTheory]] — the branch of mathematics this counting problem belongs to
- [[PrimeFactorization]] — the efficient route to computing τ via exponents
- [[MultiplicativeFunction]] — τ is multiplicative, enabling the product formula
- [[TauNumber]] — related Rosetta Code task on integers divisible by their own τ

## Contradictions
- None — reference task page.
