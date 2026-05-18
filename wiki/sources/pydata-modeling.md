---
title: "Python for Data Analysis 3E — Ch.12: Introduction to Modeling Libraries in Python"
type: source
tags: [book, modeling, statsmodels, scikit-learn, patsy, pydata]
date: 2026-05-15
source_file: raw/pydata-book-web/modeling.md
book: "Python for Data Analysis, 3rd Edition"
author: "Wes McKinney"
url: https://wesmckinney.com/book/modeling.html
chapter: 12
---

## Summary
Bridge between pandas data wrangling and the two dominant Python modeling toolkits — [[statsmodels]] (classical inferential statistics) and [[scikitlearn]] (machine learning). Covers passing data between pandas and modeling libraries via `to_numpy()`, dummy variables, [[Patsy]] formula strings (`y ~ x0 + x1`, transformations `+ I(x0*x1)`, treatment-coded categoricals), statsmodels linear / time series estimators (`sm.OLS`, `sm.AR`, ARIMA), and scikit-learn's `fit` / `predict` / `cross_val_score` pipeline.

## Key Claims
- **Interface convention** — pandas → modeling library typically passes through NumPy: `data.to_numpy()` (loses column names; heterogeneous data coerced to `object` dtype).
- **Dummy variables** — `pd.get_dummies(data["category"], prefix="cat")` one-hots; join back after dropping the categorical column.
- **Patsy formulas** — `y ~ x0 + x1` declares a design matrix; `patsy.dmatrices(formula, data)` returns `(y, X)` DesignMatrix objects (NumPy-like with column-name metadata). Supports R-style transforms: `I(x0+x1)` (raw arithmetic), `np.log(x)`, `standardize(x)`, `center(x)`; categoricals coerced with `C(x)` or treatment-coded by default.
- **statsmodels** — `sm.OLS(y, X).fit()` returns `RegressionResults` with `.params`, `.tvalues`, `.summary()`. Also `sm.GLM`, `sm.Logit`, `sm.add_constant` (intercept column). Time-series: `sm.tsa.AutoReg`, `sm.tsa.ARIMA`.
- **scikit-learn** — uniform estimator API: instantiate (`LogisticRegression(C=10)`), `.fit(X, y)`, `.predict(X_new)`, `.predict_proba`, `.score`. `cross_val_score(estimator, X, y, cv=4)` for cross-validation; `StratifiedKFold`, `GridSearchCV`, `Pipeline`, `ColumnTransformer` for end-to-end pipelines.
- **Where to go next** — Andreas Müller & Sarah Guido, *Introduction to Machine Learning with Python*; Hastie/Tibshirani/Friedman, *Elements of Statistical Learning*; Aurélien Géron, *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow*.

## Key Quotes
> See `source_file` for full text. Quotes omitted in bulk ingest; pull on demand.

## Connections
- [[statsmodels]] — classical statistics + inferential models.
- [[scikitlearn]] — ML toolkit; uniform fit/predict API.
- [[Patsy]] — R-style formula syntax for design matrices.
- [[pandas]] — upstream of all modeling.
- [[pydata-data-analysis-examples]] — chapter 13 closes the book with worked examples.
- [[imlbook-extend-lm]] / [[imlbook-limo]] — Molnar's textbook covers GLM / linear models in depth.

## Contradictions
- None.
