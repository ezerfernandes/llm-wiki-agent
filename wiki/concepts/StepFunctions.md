---
title: "Step Functions"
type: concept
tags: [nonlinear, regression, basis-functions]
sources: [islr-seventh-printing]
last_updated: 2026-05-16
---

# Step Functions

Discretize a continuous predictor by binning into $K$ intervals (knots) and using bin-indicator [[BasisFunctions]]. Result: a piecewise-constant fit. Crude but easy to interpret; building block for [[RegressionSplines]].

## Connections
- [[islr-seventh-printing]] — Ch.7.2.
- [[BasisFunctions]] — general frame.
- [[RegressionSplines]] — refinement allowing continuity at knots.
