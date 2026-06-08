---
title: "Jacobi symbol (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, modular-arithmetic]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Jacobi_symbol
---

## Summary
The task asks the programmer to compute the Jacobi symbol (a | n), a multiplicative function that generalizes the Legendre symbol to composite odd moduli. It equals the product of Legendre symbols over the prime factorization of n, where each Legendre symbol (a | p) is a^((p-1)/2) mod p, taking the value 1, -1, or 0. The key insight is that the symbol can be evaluated efficiently without factoring n by repeatedly applying quadratic reciprocity and reduction rules, yielding an O(log n) algorithm.

## Task Requirements
- Calculate the Jacobi symbol (a | n) for a given integer a and odd positive integer n.
- Return one of the values 1, -1, or 0 according to the symbol's definition.
- (Implicitly) demonstrate the implementation on sample inputs.

## Language Coverage
49 languages implement this task, spanning systems languages, functional languages, scripting languages, and math-oriented tools. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, F#, Julia, Perl, and Mathematica / Wolfram Language.

## Connections
- [[NumberTheory]] — the symbol is a core construct in elementary number theory
- [[ModularArithmetic]] — computation relies on exponentiation and reduction modulo n
- [[LegendreSymbol]] — the Jacobi symbol generalizes this for prime moduli
- [[QuadraticReciprocity]] — enables the efficient factoring-free evaluation algorithm
- [[PrimalityTesting]] — Jacobi symbols underpin the Solovay-Strassen primality test

## Contradictions
- None — reference task page.
