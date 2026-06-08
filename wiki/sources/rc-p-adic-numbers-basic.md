---
title: "P-Adic numbers, basic (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, modular-arithmetic]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/P-Adic_numbers,_basic
---

## Summary
The task asks the programmer to convert two rational numbers into their p-adic representations, add them together, and then recover an exact rational result via rational reconstruction. P-adic expansions (introduced by Hensel around 1900) are sequences of digits 0 ≤ d < p weighted by powers of p that are finite-tailed and converge toward higher positive powers of p. The key insight is that p-adic long division proceeds from the right, using the modular inverse of the divisor's denominator (mod p) to zero out the partial remainder one digit at a time.

## Task Requirements
- Convert two rational numbers a/b to p-adic numbers via p-adic long division, removing the 'p-part' from the denominator first and using the inverse of b modulo p.
- At each step, zero the most significant digit of the partial remainder by subtracting a proper multiple d = partial_remainder * (1/b mod p) of the divisor, then shift out the zero digit and repeat until the remainder is zero or precision is exhausted.
- Add the two p-adic numbers, carrying from right to left (carry drops off the leftmost, least-significant term).
- Perform rational reconstruction on the sum: repeatedly add the p-adic to itself (counting iterations to get the denominator) until an integer is reached, giving the numerator as the weighted digit sum.
- Choose prime-exponent combinations with enough precision for valid reconstruction.

## Language Coverage
14 languages implement this task, a relatively small set reflecting the mathematical sophistication required. Representative implementations include C++, C#, Go, Haskell, Java, JavaScript, Julia, Rust, Nim, and Wren.

## Connections
- [[PAdicNumbers]] — the number system being implemented
- [[ModularArithmetic]] — the modular inverse drives each long-division step
- [[RationalReconstruction]] — recovers an exact fraction from the p-adic sum
- [[NumberTheory]] — the broader field underpinning p-adic valuations and norms
- [[ModularInverse]] — computing 1/b (mod p) is the core per-digit operation

## Contradictions
- None — reference task page.
