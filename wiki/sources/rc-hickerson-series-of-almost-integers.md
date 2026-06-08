---
title: "Hickerson series of almost integers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, arbitrary-precision]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Hickerson_series_of_almost_integers
---

## Summary
The task asks the programmer to evaluate D. Hickerson's function h(n) = n! / (2·(ln 2)^(n+1)) and verify the claim that it produces "almost integers" for n from 1 to 17. The key insight is that the fractional part of h(n) stays very close to 0 or 1 over this range — values qualify as almost integers if the first digit after the decimal point is a 9 or a 0. Adequate precision matters: by h(18) the result is already around 3,385,534,663,256,845,326.39, so arbitrary-precision arithmetic is recommended.

## Task Requirements
- Compute h(n) = n! / (2·(ln 2)^(n+1)) for each n.
- For n in 1..17, check whether each value is an "almost integer" — defined here as having either a 9 or a 0 as the first digit after the decimal point.
- Report each value along with whether it qualifies.
- Use extended/arbitrary precision if needed to keep enough significant digits.

## Language Coverage
51 languages implement this task, spanning systems languages, functional languages, and math/CAS environments. Representative implementations include C, C++, Rust, Go, Java, Haskell, Python, Julia, Raku, REXX, and Mathematica / Wolfram Language.

## Connections
- [[FactorialFunction]] — the numerator n! drives the rapid growth of the series
- [[ArbitraryPrecisionArithmetic]] — needed to retain enough digits for the almost-integer test
- [[NaturalLogarithm]] — ln 2 raised to the (n+1) power forms the denominator
- [[AlmostInteger]] — the central concept the task tests for

## Contradictions
- None — reference task page.
