---
title: "Lucas-Lehmer test (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, primality-testing, arbitrary-precision]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Lucas-Lehmer_test
---

## Summary
This task asks the programmer to implement the Lucas-Lehmer primality test, a deterministic test for Mersenne numbers. For an odd prime p, the Mersenne number 2^p − 1 is prime if and only if it divides S(p−1), where the recurrence is S(1) = 4 and S(n+1) = S(n)² − 2. The key practical insight is that the rapidly growing S values must be reduced modulo 2^p − 1 at each step, which requires arbitrary-precision arithmetic to find large Mersenne primes.

## Task Requirements
- Implement the Lucas-Lehmer test for Mersenne numbers 2^p − 1 with p an odd prime.
- Use the iteration S(1) = 4, S(n+1) = S(n)² − 2 carried out p − 1 times.
- Report 2^p − 1 as prime exactly when 2^p − 1 divides S(p − 1).
- Calculate all Mersenne primes up to the implementation's maximum precision, or up to the 47th Mersenne prime, whichever comes first.

## Language Coverage
90 languages implement this task, giving very broad coverage across assembly, functional, scripting, and big-integer-capable languages. Representative implementations include C, C++, Java, Python, Haskell, Rust, Go, Common Lisp, REXX, Raku, J, and Mathematica.

## Connections
- [[MersennePrimes]] — the numbers this test identifies
- [[PrimalityTest]] — the broader class of algorithms this belongs to
- [[NumberTheory]] — the mathematical domain of the problem
- [[ArbitraryPrecisionArithmetic]] — required to handle the very large intermediate S values
- [[ModularArithmetic]] — the modulo reduction at each iteration step

## Contradictions
- None — reference task page.
