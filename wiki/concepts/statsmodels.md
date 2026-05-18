---
title: "statsmodels"
type: concept
tags: [library, python, statistics, regression, time-series]
sources: [pydata-preliminaries, pydata-modeling]
last_updated: 2026-05-15
---

# statsmodels

Python library for classical statistical modeling — regression (OLS, GLS, WLS, GLM, Logit/Probit), time series (AR/ARIMA/SARIMAX, VAR, state-space), survival analysis, nonparametric methods, and statistical tests. Where [[scikitlearn]] emphasizes *prediction* (point estimates, cross-validated accuracy), statsmodels emphasizes *inference* (coefficient standard errors, p-values, confidence intervals, hypothesis tests, residual diagnostics).

## Common API
```python
import statsmodels.api as sm
X = sm.add_constant(X)
res = sm.OLS(y, X).fit()
print(res.summary())          # rich table with t-stats, R², F, diagnostics
```
- Time series: `sm.tsa.AutoReg`, `sm.tsa.ARIMA`, `sm.tsa.statespace.SARIMAX`.
- Patsy formula API: `smf.ols("y ~ x0 + x1 + C(category)", data=df).fit()`.

## Connections
- [[Patsy]] — R-style formula language used by `statsmodels.formula.api`.
- [[scikitlearn]] — complementary; sklearn for prediction, statsmodels for inference.
- [[pandas]] — typical input; results integrate with DataFrames.
