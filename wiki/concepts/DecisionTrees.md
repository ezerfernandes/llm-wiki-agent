---
title: "Decision Trees"
type: concept
tags: [classical-ml, trees, regression, classification]
sources: [islr-seventh-printing]
last_updated: 2026-05-16
---

# Decision Trees

Recursive binary splits of the feature space into rectangles, predicting a constant in each region (mean for [[RegressionTree|regression]], majority class for [[ClassificationTree|classification]]). Introduced as [[ClassificationAndRegressionTrees|CART]] by Breiman, Friedman, Olshen & Stone (1984). Single trees are *interpretable but high-variance* — hence the ensembles [[Bagging]], [[RandomForests]], [[Boosting]].

## Connections
- [[islr-seventh-printing]] — Ch.8.1.
- [[ClassificationAndRegressionTrees]] — original CART.
- [[Bagging]], [[RandomForests]], [[Boosting]] — variance-reducing ensembles.
- [[GiniIndex]] — common split criterion for classification trees.
