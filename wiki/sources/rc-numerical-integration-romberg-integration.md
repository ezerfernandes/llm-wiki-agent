---
title: "Numerical integration/Romberg integration (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, numerical-methods, numerical-integration]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Numerical_integration/Romberg_integration
---

## Summary
This task asks the programmer to implement Romberg integration, a method for computing a definite integral that builds on the trapezium (or midpoint) rule and accelerates convergence using Richardson extrapolation. The algorithm proceeds in steps, each step doubling the number of intervals (step i uses 2**i intervals), and combines successive trapezoidal estimates in a triangular table to cancel error terms, reaching the requested precision faster than Simpson's or Boole's rule.

## Task Requirements
- Write a routine/function/method that computes the definite integral of a function f(x) using Romberg integration.
- Inputs are the function, lower and upper bounds, a maximum number of steps, and a required accuracy.
- Build the Romberg table: row i starts from the trapezoidal estimate over 2**i intervals, then refine each column via the extrapolation rule rr = (f*r1 - r2)/(f-1) with f multiplied by 4 each column.
- Stop when the requested accuracy is met or the step limit is reached.
- Test by computing the integral of exp(x) from -3 to 3 (approximately 20.0357499) using 5 steps.

## Language Coverage
17 languages implement this task, a moderate spread spanning systems, scientific, and scripting languages. Representative entries include C++, Fortran, Rust, Zig, Java, Julia, Python, R, Raku, REXX, Phix, and Wren.

## Connections
- [[NumericalIntegration]] — Romberg is a numerical quadrature method
- [[TrapezoidalRule]] — the base estimate each row refines
- [[RichardsonExtrapolation]] — the error-cancellation technique driving the refinement
- [[SimpsonsRule]] — a related quadrature rule the task contrasts against for speed
- [[DefiniteIntegral]] — the mathematical object being approximated

## Contradictions
- None — reference task page.
