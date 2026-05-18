---
title: "Patsy"
type: concept
tags: [library, python, formula, design-matrix]
sources: [pydata-modeling]
last_updated: 2026-05-15
---

# Patsy

Python library for describing statistical models with R-style **formula strings** (`y ~ x0 + x1 + C(category)`). Translates a formula + data into NumPy / pandas-aware *design matrices* with column-name metadata. Installed automatically with [[statsmodels]] and is the formula backend for `statsmodels.formula.api`.

## Syntax
- `+` separates terms in the design (does NOT mean arithmetic addition).
- `:` interaction; `*` main effects + interactions.
- `I(x0 + x1)` — escape arithmetic into actual numeric computation.
- `np.log(x)`, `standardize(x)`, `center(x)` — function transforms.
- `C(category)` — treatment-code a categorical.

## Connections
- [[statsmodels]] — primary consumer.
- [[Rlanguage]] — formula syntax inspired by R / S.
- [[pandas]] — DataFrames as the typical input.
