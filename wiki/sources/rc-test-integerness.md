---
title: "Test integerness (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, floating-point]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Test_integerness
---

## Summary
This task asks the programmer to determine whether a given number — rational, real, or complex — is mathematically an integer, meaning it could be represented as an integer with no loss of precision given an infinitely wide integer type. A rational is integral if its reduced denominator is 1, a real if it has no nonzero fractional part, and a complex if its real part is integral and its imaginary part is zero. The key subtlety is that very large floats like -2.1e120 are still integers mathematically even though they exceed native integer ranges.

## Task Requirements
- Test integerness across all numeric data types the language commonly uses (rational, real/fixed-point/floating-point, complex).
- Treat a value as an integer per the set-specific rules above; handle the tricky large-magnitude float case as integral.
- Return false for non-integral reals, NaN (and optionally Inf), and complex numbers with nonzero imaginary parts.
- Extra credit: accept an optional `tolerance` parameter for fuzzy testing, so values like 0.9999999998 round to the nearest integer.
- Discuss the limitations of the implementation.

## Language Coverage
49 languages implement this task, spanning systems and scripting languages, functional and math-oriented tools. Representative implementations include C, C++, C#, Java, Python, Haskell, Julia, Go, Perl, Raku, and Mathematica / Wolfram Language.

## Connections
- [[NumberTheory]] — the notion of integerness across number sets
- [[FloatingPoint]] — handling mantissa/exponent and precision concerns
- [[ComplexNumbers]] — testing real and imaginary parts
- [[RationalNumbers]] — reduced-fraction denominator check
- [[RoundOffError]] — motivates the tolerance-based fuzzy test

## Contradictions
- None — reference task page.
