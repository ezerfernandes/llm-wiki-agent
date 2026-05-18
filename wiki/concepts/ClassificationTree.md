---
title: "Classification Tree"
type: concept
tags: [trees, classification]
sources: [islr-seventh-printing]
last_updated: 2026-05-16
---

# Classification Tree

[[DecisionTrees|Decision tree]] for categorical targets: each terminal region predicts the majority class of training observations falling inside it. Splits chosen to minimize an impurity measure — typically the [[GiniIndex]] or cross-entropy (misclassification error is a less sensitive alternative).

## Connections
- [[islr-seventh-printing]] — Ch.8.1.2.
- [[DecisionTrees]] — parent.
- [[RegressionTree]] — continuous-response sibling.
- [[GiniIndex]] — common split criterion.
