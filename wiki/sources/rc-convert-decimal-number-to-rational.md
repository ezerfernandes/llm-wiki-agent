---
title: "Convert decimal number to rational (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, rational-numbers]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Convert_decimal_number_to_rational
---

## Summary
The task is to transform a decimal number into a fraction expressed in lowest terms. The key insight is that a terminating decimal with n digits after the point equals (digits without the point) over 10^n, which is then reduced by dividing both numerator and denominator by their greatest common divisor. Exact conversion is not always possible: repeating decimals such as 1/3 = 0.333... cannot be reliably recovered from a finite decimal representation unless the language supports repeating-decimal notation.

## Task Requirements
- Convert a given decimal number into a fraction reduced to lowest terms.
- Handle finite (terminating) decimals exactly, e.g. 0.75 → 3 / 4.
- Accept approximate results for truncated repeating decimals, e.g. 0.9054054 → 4527027 / 5000000 and 0.518518 → 259259 / 500000.
- Reduce the resulting fraction using the greatest common divisor.

## Language Coverage
67 languages implement this task, spanning systems and scripting languages as well as math-oriented and Lisp dialects. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Perl, Raku, Julia, Mathematica, and REXX.

## Connections
- [[GreatestCommonDivisor]] — used to reduce the fraction to lowest terms
- [[RationalNumbers]] — the target representation of the conversion
- [[RepeatingDecimals]] — the case that cannot be recovered exactly from finite input
- [[NumberTheory]] — the mathematical domain of the task

## Contradictions
- None — reference task page.
