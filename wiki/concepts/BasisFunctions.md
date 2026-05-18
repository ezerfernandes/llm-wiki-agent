---
title: "Basis Functions"
type: concept
tags: [nonlinear, regression, theory]
sources: [islr-seventh-printing]
last_updated: 2026-05-16
---

# Basis Functions

Replace $x$ in a linear model with a fixed family of transforms $\{b_1(x), \dots, b_K(x)\}$ and fit $y = \beta_0 + \sum_k \beta_k b_k(x) + \epsilon$ by ordinary least squares. Choices: polynomial powers ([[PolynomialRegression]]), indicator functions ([[StepFunctions]]), truncated power or B-spline bases ([[RegressionSplines]]).

## Connections
- [[islr-seventh-printing]] — Ch.7.3.
- [[PolynomialRegression]], [[StepFunctions]], [[RegressionSplines]] — concrete bases.
