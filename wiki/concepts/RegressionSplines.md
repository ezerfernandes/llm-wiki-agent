---
title: "Regression Splines"
type: concept
tags: [nonlinear, regression, basis-functions]
sources: [islr-seventh-printing]
last_updated: 2026-05-16
---

# Regression Splines

Piecewise polynomials of degree $d$ joined at knots, constrained for continuity of the function and its first $d-1$ derivatives. Implemented as a [[BasisFunctions|basis expansion]] (truncated power or B-spline basis) and fit by ordinary least squares. Flexibility controlled by the number/placement of knots.

## Connections
- [[islr-seventh-printing]] — Ch.7.4.
- [[BasisFunctions]], [[PolynomialRegression]], [[StepFunctions]] — basis variants.
- [[SmoothingSplines]] — penalty-based alternative.
- [[GeneralizedAdditiveModels]] — combines splines additively in $p$ predictors.
