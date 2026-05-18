---
title: "scikit-learn"
type: concept
tags: [library, python, machine-learning]
sources: [pydata-preliminaries, pydata-modeling]
last_updated: 2026-05-15
---

# scikit-learn

The dominant general-purpose Python machine-learning library. Started ~2007 (David Cournapeau) as a Google Summer of Code project; now a flagship project of the scientific Python ecosystem. Provides a *uniform estimator API* — every model has `.fit(X, y)`, `.predict(X)`, `.score(X, y)` and (where applicable) `.predict_proba`, `.transform`. Submodules cover classification, regression, clustering, dimensionality reduction, model selection, preprocessing.

## Pipeline primitives
- `Pipeline([("step", est), ...])` — chain transformers + a final estimator.
- `ColumnTransformer` — apply different preprocessors to different columns.
- `GridSearchCV` / `RandomizedSearchCV` — hyperparameter search with cross-validation.
- `cross_val_score(est, X, y, cv=)` — quick k-fold evaluation.

## Connections
- [[NumPy]] — ndarrays as the data substrate.
- [[SciPy]] — underlying numerical routines.
- [[pandas]] — typical upstream of `X` and `y`.
- [[statsmodels]] — overlapping classical-stats subset (e.g. linear regression); statsmodels emphasizes inference, sklearn emphasizes prediction.
- [[imlbook-data]] and the wider [[imlbook-future|IML book]] corpus — uses sklearn estimators throughout.
