---
title: "Arbitrary-precision integers (included) (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, arbitrary-precision, number-theory, exponentiation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Arbitrary-precision_integers_(included)
---

## Summary
This task asks the programmer to compute the exact integer value of 5^(4^(3^2)) using only the language's built-in or natively-endorsed big-integer capabilities, not a hand-rolled arbitrary-precision implementation. The exponent tower evaluates right-to-left to 5^262144, a number with hundreds of thousands of digits, so the key insight is that the language (or its standard library) must provide native bignum arithmetic. The result is verified by checking its leading and trailing twenty digits and counting its total decimal digits.

## Task Requirements
- Compute the integer value of 5^(4^(3^2)) (i.e. 5^262144) using built-in capabilities.
- Confirm the first twenty digits are 62060698786608744707 and the last twenty are 92256259918212890625.
- Find and display the total number of decimal digits in the answer.
- Do not submit a self-written arbitrary-precision arithmetic implementation; an overwhelming, home-site-endorsed library (e.g. CPAN, Boost) is acceptable. Fixed-precision libraries with manually-set precision are discouraged unless they are the only recourse.

## Language Coverage
117 languages implement this task, spanning systems, scripting, functional, and array languages — reflecting how broadly native bignum support exists. Representative implementations include Python, Haskell, Java, Go, Ruby, Common Lisp, REXX, Mathematica, dc, and Raku.

## Connections
- [[ArbitraryPrecisionArithmetic]] — the core capability the task probes
- [[Exponentiation]] — right-associative tower 5^(4^(3^2))
- [[BigInteger]] — native big-number types/libraries used to hold the result
- [[NumberTheory]] — exact integer computation and digit analysis

## Contradictions
- None — reference task page.
