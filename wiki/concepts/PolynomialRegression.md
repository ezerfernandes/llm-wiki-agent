---
title: "Polynomial Regression"
type: concept
tags: [nonlinear, regression]
sources: [islr-seventh-printing, d2l-linear-regression]
last_updated: 2026-05-16
---

# Polynomial Regression

[[LinearRegression]] with [[BasisFunctions|basis]] $\{x, x^2, \dots, x^d\}$. Captures global curvature with a single $d$; behaves badly at boundary regions for large $d$ — [[RegressionSplines]] and local methods are usually preferable.

## Connections
- [[islr-seventh-printing]] — Ch.7.1.
- [[BasisFunctions]] — frame.
- [[RegressionSplines]] — local, well-behaved alternative.
