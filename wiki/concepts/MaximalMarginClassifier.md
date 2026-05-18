---
title: "Maximal Margin Classifier"
type: concept
tags: [classification, geometry]
sources: [islr-seventh-printing]
last_updated: 2026-05-16
---

# Maximal Margin Classifier

When the training data are linearly separable, the unique hyperplane that maximizes the *margin* — the minimum signed distance to any training point. Points achieving the margin are *support vectors*. The classical ancestor of the [[SupportVectorClassifier]] and [[SupportVectorMachine]].

## Connections
- [[islr-seventh-printing]] — Ch.9.1.
- [[SupportVectorClassifier]] — relaxed (soft-margin) extension.
- [[SupportVectorMachine]] — non-linear kernelized extension.
