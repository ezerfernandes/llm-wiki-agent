---
title: "Regression Tree"
type: concept
tags: [trees, regression]
sources: [islr-seventh-printing]
last_updated: 2026-05-16
---

# Regression Tree

[[DecisionTrees|Decision tree]] for continuous targets: each terminal region predicts the mean of the training $y_i$ falling inside it. Split criterion: residual sum of squares. Trees are pruned via cost-complexity ($\alpha$) chosen by [[CrossValidation]].

## Connections
- [[islr-seventh-printing]] — Ch.8.1.1.
- [[DecisionTrees]] — parent.
- [[ClassificationTree]] — categorical-response sibling.
