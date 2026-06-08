---
title: "Numerical integration/Tanh-Sinh Quadrature (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, numerical-integration, numerical-analysis]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Numerical_integration/Tanh-Sinh_Quadrature
---

## Summary
The task asks the programmer to implement tanh-sinh quadrature (also called double-exponential integration), a numerical method for computing a definite integral. The key idea is a change of variables built from hyperbolic functions that maps the integration interval onto the real line so the transformed integrand decays double-exponentially toward the endpoints, which makes a simple trapezoidal sum converge extremely fast. The routine starts with 3 intervals and repeatedly doubles the count (step k uses 2^k - 1 points) until either a step limit or a target accuracy is reached.

## Task Requirements
- Write a routine that computes the definite integral of f(x) over [lower, upper] using tanh-sinh quadrature.
- Use the fixed step size h = 0.1 (the integrand-dependent optimal h is not required).
- Accept the function, bounds, number of steps, and required accuracy, doubling the interval count each step until the limit or accuracy is hit.
- Test by computing the integral of exp(x) from -3 to 3 with 5 steps, expecting approximately 20.0357499.

## Language Coverage
20 languages implement this task, spanning systems and numeric languages alongside scripting and BASIC dialects. Representative examples include C, C++, Rust, Fortran, Java, Python, Julia, R, JavaScript, and Raku.

## Connections
- [[NumericalIntegration]] — the broader problem class this task belongs to
- [[Quadrature]] — the family of weighted-sum integration rules
- [[DoubleExponentialIntegration]] — the variable substitution that drives convergence
- [[HyperbolicFunctions]] — sinh, cosh, and tanh underpin the change of variables
- [[TrapezoidalRule]] — the underlying equal-spacing sum applied after the transform

## Contradictions
- None — reference task page.
