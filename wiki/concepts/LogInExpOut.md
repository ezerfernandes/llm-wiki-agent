---
title: "Log In, Exp Out"
type: concept
tags: [feature-engineering, target-transform, regression]
sources: [mechanics-of-ml]
last_updated: 2026-06-04
---

# Log In, Exp Out

A target-transformation trick from [[mechanics-of-ml|*The Mechanics of Machine Learning*]] (Ch 5): when a regression target is **right-skewed** with a long tail (e.g. apartment prices), train on `np.log(y)` and exponentiate predictions with `np.exp` to recover the original units. The log compresses large values, turning a skewed distribution into an approximately normal one and making average-based predictors (like [[RandomForests|Random Forests]]) robust to outliers — *without* manual [[Denoising|denoising]].

In the book it reaches OOB R² **0.8767** on *unfiltered, noisy* data, matching hand-denoising's 0.8677. **Trade-off:** it matches on R² but its [[RMSLE|MAE]] is worse — "If we care more about MAE than R², then cleaning the data gets us a better model than simply taking the log of the prices." Training on log-target is also why [[RMSLE]] is the natural metric for skewed-price problems.

## Connections
- [[mechanics-of-ml]] — Ch 5 *Exploring and Denoising Your Data Set*.
- [[Denoising]] — the manual alternative this trick can stand in for.
- [[RMSLE]] — log-space error metric, the natural pairing.
- [[FeatureEngineering]] — target transformation is feature engineering on `y`.
