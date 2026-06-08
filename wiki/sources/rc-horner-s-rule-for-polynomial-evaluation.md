---
title: "Horner's rule for polynomial evaluation (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, numerical-methods]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Horner's_rule_for_polynomial_evaluation
---

## Summary
The task asks the programmer to implement Horner's rule, a fast scheme for evaluating a polynomial at a given value of x. The key insight is to rewrite the polynomial as nested multiplications (e.g. ((((0)x + 6)x + (-4))x + 7)x + (-19)) so that evaluation requires only n multiplications and n additions, processing coefficients from highest power inward. An accumulator starts at 0 and is repeatedly updated as accumulator = accumulator * x + coefficient.

## Task Requirements
- Create a routine that takes a list of coefficients of a polynomial in order of increasing powers of x, plus a value of x.
- Return the value of the polynomial evaluated at that x using Horner's rule.
- Worked example: coefficients [-19, 7, -4, 6] evaluated at x = 3 (i.e. -19 + 7x - 4x^2 + 6x^3).

## Language Coverage
128 languages implement this task, showing very broad coverage spanning systems, scripting, functional, and assembly languages. Representative implementations include C, C++, Python, Java, Haskell, Rust, Go, Common Lisp, Fortran, and 360 Assembly.

## Connections
- [[HornersMethod]] — the named algorithm this task implements
- [[PolynomialEvaluation]] — the general problem being optimized
- [[NumericalMethods]] — family of techniques for efficient numeric computation
- [[FormalPowerSeries]] — related Rosetta Code topic cross-referenced on the page

## Contradictions
- None — reference task page.
