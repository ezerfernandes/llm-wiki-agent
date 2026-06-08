---
title: "Multiple regression (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, linear-algebra, statistics, numerical-methods]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Multiple_regression
---

## Summary
The task asks the programmer to fit a multiple linear regression model: given a response vector y and a design matrix X of predictor variables, compute the coefficient vector beta via ordinary least squares (OLS). The key insight is that beta is the solution to the normal equations, reducing the statistical problem to standard matrix operations (transpose, multiply, invert/solve).

## Task Requirements
- Accept y as a one-dimensional vector and X as a two-dimensional matrix (array of predictor vectors).
- Compute beta = {beta_1, ..., beta_k} so that each y_j is approximated by the sum over i of beta_i * x_ij.
- Use ordinary least squares regression to determine the coefficients.

## Language Coverage
47 languages implement this task, spanning general-purpose languages, statistics-focused environments, and computer-algebra systems. Representative implementations include C, C++, Go, Rust, Java, Python, Haskell, J, Fortran, R, MATLAB, Mathematica, and Stata.

## Connections
- [[OrdinaryLeastSquares]] — the estimation method the task specifies.
- [[LinearRegression]] — the statistical model being generalized to multiple predictors.
- [[NormalEquations]] — the matrix equation solved to obtain beta.
- [[MatrixInversion]] — a common numerical step in solving the least-squares system.
- [[QRDecomposition]] — an alternative, numerically stable way to solve the system.

## Contradictions
- None — reference task page.
