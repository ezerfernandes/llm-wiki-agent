---
title: "Numerical integration (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, numerical-methods, calculus]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Numerical_integration
---

## Summary
The task asks the programmer to write functions that approximate the definite integral of a function ƒ(x) using five classic quadrature methods. Each function takes the lower and upper bounds (a and b) and the number n of subintervals, then sums contributions from sample points within [a, b]. The key insight is that all of these methods estimate the area under a curve by partitioning the interval and approximating each slice with a simple shape (rectangle, trapezoid, or parabola), trading accuracy for computational simplicity.

## Task Requirements
- Implement rectangular rule in three variants: left endpoint, right endpoint, and midpoint sampling.
- Implement the trapezium (trapezoidal) rule.
- Implement Simpson's rule in its composite form, following the given pseudocode (h = (b-a)/n; answer = (h/6)·(f(a) + f(b) + 4·sum1 + 2·sum2)).
- Each function accepts bounds a, b and approximation count n, assuming ƒ(x) is already available.
- Demonstrate on four cases: x³ over [0,1] with n=100 (exact 0.25); 1/x over [1,100] with n=1000 (exact ln 100 ≈ 4.6052); x over [0,5000] with n=5,000,000 (exact 12,500,000); and x over [0,6000] with n=6,000,000 (exact 18,000,000).

## Language Coverage
79 languages implement this task, showing very broad coverage across functional, imperative, and scientific-computing ecosystems. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Common Lisp, Fortran, Julia, MATLAB / Octave, and Scheme.

## Connections
- [[NumericalIntegration]] — the overarching family of quadrature techniques this task surveys.
- [[SimpsonsRule]] — parabolic approximation, the most accurate of the required methods.
- [[TrapezoidalRule]] — linear-segment approximation of the integral.
- [[Calculus]] — definite integration is the underlying mathematical concept being approximated.
- [[RiemannSum]] — the rectangular variants are direct Riemann-sum estimates.

## Contradictions
- None — reference task page.
