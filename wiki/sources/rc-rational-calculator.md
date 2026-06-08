---
title: "Rational calculator (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, parsing, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Rational_calculator
---

## Summary
The task asks the programmer to build a calculator that performs exact arithmetic on rational numbers, supporting the four binary operations (+, -, *, /), unary plus/minus, absolute value, and parenthesized expressions such as `1 + (2 - 7) / 5`. A special symbol `@` references the previous result. The key insight is that representing values as exact fractions (numerator/denominator pairs) avoids the rounding errors of floating point, so an expression parser must be combined with rational-number arithmetic.

## Task Requirements
- Support binary operators `+`, `-`, `*`, `/` on rational numbers with exact results.
- Support unary `+`, `-`, and `abs` (absolute value).
- Respect operator precedence and parentheses for ordering subexpressions.
- Use `@` to denote the previous computed result.
- Bonus: emit recurring-decimal notation, e.g. `1/3 = 0.(3)`, handling edge cases like `0.(9) = 1` and denominators that are not co-prime with 10.

## Language Coverage
14 languages implement this task, a modest spread covering systems, scripting, and BASIC-family tongues. Representative implementations include Ada, C, Crystal, Julia, Nim, Perl, Python, Raku, Phix, and Wren.

## Connections
- [[RationalNumbers]] — values are stored as exact numerator/denominator fractions
- [[ExpressionParsing]] — the calculator must tokenize and parse infix arithmetic
- [[OperatorPrecedence]] — parentheses and precedence determine evaluation order
- [[GreatestCommonDivisor]] — fractions are reduced to lowest terms via GCD
- [[RepeatingDecimals]] — the bonus task renders recurring decimal expansions

## Contradictions
- None — reference task page.
