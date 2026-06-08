---
name: ShapleyValues
title: "Shapley Values"
type: concept
tags: [interpretability, explainability, game-theory, attribution]
sources: [mlsysbook-ch15-responsible-engineering]
last_updated: 2026-06-05
---

# Shapley Values

A feature-attribution method adapted from **cooperative game theory** that distributes a prediction's "payout" fairly among input features by averaging each feature's marginal contribution over all coalitions. Per [[mlsysbook-ch15-responsible-engineering|mlsysbook Vol 1 Ch 15]], [[SHAP]] (Lundberg & Lee 2017) applies Shapley values under a unified additive framework. Exact computation is exponential and expensive, so practical implementations use approximations or model-specific algorithms — explanation fidelity, latency, and complexity must be budgeted explicitly.

## Connections
- [[SHAP]] — the ML implementation.
- [[LIME]] — the alternative local-surrogate approach.
- [[Explainability]] — the capability Shapley values provide.
- [[Interpretability]] — the intrinsic counterpart.
- [[mlsysbook-ch15-responsible-engineering]] — source.
