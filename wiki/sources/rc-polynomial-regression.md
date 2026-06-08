---
title: "Polynomial regression (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, numerical-methods, linear-algebra, curve-fitting]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Polynomial_regression
---

## Summary
The task asks the programmer to find an approximating polynomial of a known degree that best fits a given set of (x, y) data points. The canonical example fits the points to a degree-2 polynomial and recovers the coefficients (3, 2, 1) for 3x² + 2x + 1. The core insight is that fitting a polynomial of fixed degree reduces to a linear least-squares problem solvable via the normal equations or a Vandermonde-matrix system.

## Task Requirements
- Given arrays of data points x and y and a target polynomial degree, compute the best-fit polynomial's coefficients.
- For the supplied example (x = 0..10, y = 1, 6, 17, ... 321), the degree-2 fit should yield coefficients (3, 2, 1).
- This task is intended as a subtask for measuring relative performance of sorting-algorithm implementations.

## Language Coverage
62 languages implement this task, spanning general-purpose languages, numerical/statistical environments, and calculator dialects. Representative implementations include C, C++, Python, Java, Go, Rust, Haskell, Julia, R, Octave, MATLAB, Fortran, and Mathematica.

## Connections
- [[LeastSquares]] — polynomial fitting is a linear least-squares minimization
- [[LinearAlgebra]] — solved via matrix operations on the design matrix
- [[VandermondeMatrix]] — the design matrix of powers of x
- [[CurveFitting]] — the broader problem class this task belongs to
- [[NormalEquations]] — closed-form route to the coefficient vector

## Contradictions
- None — reference task page.
