---
title: "SHAP"
type: concept
tags: [interpretability, explainability]
sources: [madewithml-evaluation, madewithml-monitoring, mlsysbook-ch14-ml-operations, mlsysbook-ch15-responsible-engineering]
last_updated: 2026-06-05
---

# SHAP

SHapley Additive exPlanations — a game-theoretic framework for attributing a prediction to input features. A pillar of [[interpretablemachinelearning]] alongside [[LIME]].

## Connections

- [[LIME]] — sibling post-hoc [[Explainability|explanation]] method (local surrogate).
- [[ShapleyValues]] — the cooperative-game-theory quantity SHAP computes.
- [[Interpretability]] — the broader property SHAP serves post-hoc.
- [[mlsysbook-ch15-responsible-engineering]] — mlsysbook Vol 1 Ch 15 places SHAP (Shapley values, exact computation expensive) opposite [[LIME]] on its post-hoc [[Explainability|explainability]] axis vs. intrinsically [[Interpretability|interpretable]] models, with explanation requirements varying by domain (credit, medical, fraud).
