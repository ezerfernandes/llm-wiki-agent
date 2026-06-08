---
title: "Modular exponentiation (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, cryptography]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Modular_exponentiation
---

## Summary
The task asks the programmer to compute a^b mod m efficiently, demonstrated by finding the last 40 decimal digits of a^b for two enormous (~70-digit) values of a and b. Computing the full a^b is infeasible because the result has astronomically many digits, so the key insight is to reduce intermediate values modulo m at each step rather than materializing the full power.

## Task Requirements
- Compute a^b mod m for the given large a and b, with m = 10^40, to extract the last 40 decimal digits.
- The algorithm must work for any integers a, b, m where b >= 0 and m > 0.
- A naive full expansion of a^b is too slow; a fast modular-exponentiation method is required.

## Language Coverage
82 languages implement this task, spanning mainstream, functional, and arbitrary-precision-oriented ecosystems. Representative implementations include C, C++, Java, Python, Go, Rust, Haskell, Common Lisp, Ruby, and Raku — many leaning on built-in bignum support or library primitives (e.g. Python's three-argument pow).

## Connections
- [[ModularArithmetic]] — the operation is defined entirely within a residue system mod m
- [[ExponentiationBySquaring]] — the standard fast algorithm (square-and-multiply) used here
- [[NumberTheory]] — modular powers are a foundational tool in this field
- [[ArbitraryPrecisionArithmetic]] — large operands require bignum support to hold intermediate values
- [[PublicKeyCryptography]] — modular exponentiation underpins RSA and Diffie-Hellman

## Contradictions
- None — reference task page.
