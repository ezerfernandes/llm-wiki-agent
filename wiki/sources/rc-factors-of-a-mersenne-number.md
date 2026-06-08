---
title: "Factors of a Mersenne number (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, modular-arithmetic, primality]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Factors_of_a_Mersenne_number
---

## Summary
A Mersenne number has the form 2^P − 1. This task asks the programmer to find a small factor of such a number efficiently, so that candidate exponents can be eliminated before running the expensive Lucas-Lehmer test. The key insight is that testing whether a number q divides 2^P − 1 reduces to checking whether 2^P mod q = 1, computed quickly with binary modular exponentiation (modPow). Number-theoretic constraints sharply narrow the search space for candidate factors.

## Task Requirements
- Implement (or use a built-in) modular exponentiation that computes 2^P mod q via repeated squaring over the binary digits of the exponent.
- Use the fact that q divides 2^P − 1 exactly when 2^P mod q = 1.
- Restrict candidate factors q to the form q = 2kP + 1 (k a non-negative integer), with q congruent to 1 or 7 mod 8, and q itself prime.
- Stop trial division once the candidate exceeds sqrt(N).
- Concretely: find a factor of 2^929 − 1 (M929).

## Language Coverage
75 languages implement this task, spanning systems languages, scripting languages, functional languages, and assembly. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Common Lisp, Perl, Raku, Julia, REXX, and 360 Assembly.

## Connections
- [[ModularExponentiation]] — the modPow routine (repeated squaring) is the computational core.
- [[MersennePrime]] — the task's motivation: pruning exponents before the [[LucasLehmerTest]].
- [[TrialDivision]] — candidate factors are tested by constrained trial division up to sqrt(N).
- [[NumberTheory]] — factor constraints (q = 2kP+1, q ≡ 1 or 7 mod 8) derive from properties of Mersenne numbers.

## Contradictions
- None — reference task page.
