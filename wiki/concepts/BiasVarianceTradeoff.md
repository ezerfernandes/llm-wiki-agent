---
title: "Bias-Variance Trade-Off"
type: concept
tags: [theory, statistical-learning, model-selection]
sources: [islr-seventh-printing]
last_updated: 2026-05-16
---

# Bias-Variance Trade-Off

Decomposition of expected test error: $\mathbb{E}[(y_0-\hat f(x_0))^2] = \mathrm{Var}(\hat f(x_0)) + [\mathrm{Bias}(\hat f(x_0))]^2 + \mathrm{Var}(\epsilon)$. More flexible models *reduce bias* but *raise variance*; the optimum is data-dependent and chosen empirically via [[CrossValidation]]. The unifying lens of [[islr-seventh-printing|ISLR]] Chapter 2 — applied in every later chapter.

## Connections
- [[islr-seventh-printing]] — Ch.2.2.2 derivation.
- [[CrossValidation]] — empirical procedure for picking flexibility.
- [[StatisticalLearning]] — central trade-off of the field.
