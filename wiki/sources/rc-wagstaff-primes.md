---
title: "Wagstaff primes (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, primality-testing, big-integers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Wagstaff_primes
---

## Summary
A Wagstaff prime is a prime number of the form (2^p + 1)/3 where the exponent p is itself an odd prime. The task asks the programmer to find and display the first 10 Wagstaff primes alongside their corresponding exponents p. The key insight is that (2^p + 1)/3 is always an integer when p is odd, so no divisibility pre-check is needed before primality testing.

## Task Requirements
- Find and show the first 10 Wagstaff primes together with their corresponding exponents p.
- For each candidate, p must be an odd prime and (2^p + 1)/3 must also be prime.
- Stretch goal: find the exponents p for the next 14 Wagstaff primes (and more if feasible), which requires arbitrary-precision integers.
- A probabilistic primality test (probably-prime with reasonable certainty) is acceptable for large numbers.

## Language Coverage
40 languages implement this task. Coverage is broad, spanning systems and functional languages as well as math-oriented and BASIC dialects; representative examples include Ada, ALGOL 68, C, C++, Go, Java, Julia, Python, Perl, Raku, Mathematica/Wolfram Language, and PARI/GP.

## Connections
- [[PrimeNumbers]] — the task is fundamentally about generating and testing primes.
- [[PrimalityTesting]] — large candidates require deterministic or probabilistic prime tests.
- [[ArbitraryPrecisionArithmetic]] — the stretch goal needs big integers since (2^p + 1)/3 grows exponentially.
- [[ModularExponentiation]] — underlies efficient computation of 2^p and probabilistic tests like Miller-Rabin.
- [[NumberTheory]] — Wagstaff primes are a named family within number theory.

## Contradictions
- None — reference task page.
