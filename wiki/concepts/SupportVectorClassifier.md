---
title: "Support Vector Classifier"
type: concept
tags: [classification, classical-ml]
sources: [islr-seventh-printing]
last_updated: 2026-05-16
---

# Support Vector Classifier

Soft-margin generalization of the [[MaximalMarginClassifier]]: allow some training points to lie within or on the wrong side of the margin, paying a slack penalty controlled by a budget $C$. Tunable trade-off between margin width and training error.

## Connections
- [[islr-seventh-printing]] — Ch.9.2.
- [[MaximalMarginClassifier]] / [[HardMarginSVM]] — hard-margin special case.
- [[SoftMarginSVM]] — the [[mml-ch12-classification-svm|MML Ch 12]] name for this idea (slack $\xi_n$ + budget $C$).
- [[SupportVectorMachine]] — non-linear kernelized version.
