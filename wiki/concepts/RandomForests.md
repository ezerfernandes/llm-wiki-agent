---
title: "Random Forests"
type: concept
tags: [ensemble, trees]
sources: [islr-seventh-printing, mechanics-of-ml]
last_updated: 2026-06-04
---

# Random Forests

[[Bagging]] + a per-split twist: at each split consider only a random subset of $m \approx \sqrt{p}$ predictors. This *decorrelates* the trees so averaging reduces variance further than bagging alone. Introduced by Breiman (2001); a strong tabular-data baseline.

## As the default model — *The Mechanics of Machine Learning*

[[mechanics-of-ml|Parr & Howard]] elevate the RF from "strong baseline" to **default model** — "the Swiss Army Knife™ of the machine learning world," recommended for almost every tabular problem over surveying many algorithms. Their intuition for why averaging works: an RF "behaves very much like a group of real estate agents looking for comparable apartments and cooperating to estimate an apartment's price ('crowdsourcing')." The same machinery serves regression (leaf = mean target, `RandomForestRegressor`) and classification (leaf = majority vote → forest "meta-voting scheme," `RandomForestClassifier`). The book also leans on the [[OutOfBagScore|OOB score]] as a free validation estimate (with a time-series caveat) and tunes sequentially — `n_estimators` → `max_features` → `min_samples_leaf` (see [[Hyperparameter]]). Applied numbers: apartment OOB R² up to 0.8767; MNIST 94.45% vs LogisticRegression 90.20%; breast cancer 91.86%.

## Connections
- [[islr-seventh-printing]] — Ch.8.2.2 (the theory: $m\approx\sqrt p$ decorrelation, Breiman 2001).
- [[mechanics-of-ml]] — the applied scikit-learn recipe and "default model" thesis.
- [[Bagging]] — the parent procedure.
- [[Bootstrap]] — the resampling each tree trains on.
- [[OutOfBagScore]] — RF's built-in held-out estimate.
- [[DecisionTrees]] — base learner.
- [[Boosting]] — sequential ensemble alternative.
