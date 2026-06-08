---
title: "Numerical integration/Gauss-Legendre Quadrature (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, numerical-analysis, numerical-integration, root-finding]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Numerical_integration/Gauss-Legendre_Quadrature
---

## Summary
The task asks the programmer to implement an n-point Gauss-Legendre quadrature rule that approximates a definite integral as a weighted sum of function values at specially chosen sample points (nodes). The key insight is that the nodes are the roots of the n-th order Legendre polynomial and the weights derive from the polynomial's derivative at those roots; once computed, the same nodes and weights can be reused for many integrals, making it far faster than naive numerical integration. Because Legendre roots are not analytically solvable, they must be found numerically (e.g. Newton-Raphson with a cosine-based initial guess).

## Task Requirements
- Implement a routine that takes a function f, integration bounds a and b, and a node count n.
- Compute the nodes as roots of the n-th order Legendre polynomial P_n(x), generated via the recurrence n·P_n = (2n−1)·x·P_{n−1} − (n−1)·P_{n−2}.
- Find each root numerically via Newton-Raphson, using the initial guess x0 = cos(π·(i − 1/4)/(n + 1/2)).
- Compute the corresponding weights w_i = 2 / ((1 − x_i²)·[P′_n(x_i)]²).
- Rescale the standard [−1, 1] rule to an arbitrary interval [a, b] via the linear change of variable.
- Demonstrate with a 5-point rule computing ∫ from −3 to 3 of exp(x) dx ≈ 20.036.

## Language Coverage
43 languages implement this task, spanning systems languages, functional languages, computer-algebra systems, and BASIC dialects. Representative examples include C, C++, Fortran, Go, Haskell, Python, Common Lisp (the reference), Julia, MATLAB, and Mathematica/Wolfram Language.

## Connections
- [[GaussianQuadrature]] — the general numerical-integration family this task specializes
- [[LegendrePolynomials]] — their roots define the quadrature nodes
- [[NewtonRaphsonMethod]] — used to find the polynomial roots numerically
- [[NumericalIntegration]] — the broader problem this rule solves more efficiently
- [[RecurrenceRelation]] — generates the Legendre polynomials and their derivatives

## Contradictions
- None — reference task page.
