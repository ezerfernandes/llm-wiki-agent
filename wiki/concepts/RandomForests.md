---
title: "Random Forests"
type: concept
tags: [ensemble, trees]
sources: [islr-seventh-printing]
last_updated: 2026-05-16
---

# Random Forests

[[Bagging]] + a per-split twist: at each split consider only a random subset of $m \approx \sqrt{p}$ predictors. This *decorrelates* the trees so averaging reduces variance further than bagging alone. Introduced by Breiman (2001); a strong tabular-data baseline.

## Connections
- [[islr-seventh-printing]] — Ch.8.2.2.
- [[Bagging]] — the parent procedure.
- [[DecisionTrees]] — base learner.
- [[Boosting]] — sequential ensemble alternative.
