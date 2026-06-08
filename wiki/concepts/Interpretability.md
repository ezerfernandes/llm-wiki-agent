---
title: "Interpretability"
type: concept
tags: [explainability, safety]
sources: [mlsysbook-ch15-responsible-engineering]
last_updated: 2026-06-05
---

# Interpretability

The degree to which a model's decisions can be understood by humans — via inherently transparent models (linear, trees) or post-hoc methods (SHAP, LIME, attention attribution, probing). Critical for high-stakes deployment, debugging, and the [[CapabilityVsAlignment]] research agenda.

## Connections

- [[Explainability]] — the post-hoc counterpart; Ch 15 distinguishes intrinsic *interpretability* from post-hoc *explainability*.
- [[SHAP]] / [[LIME]] — the post-hoc explanation tools used when a model is not intrinsically interpretable.
- [[mlsysbook-ch15-responsible-engineering]] — mlsysbook Vol 1 Ch 15 defines interpretability as *intrinsic* (linear regression yes, a 100-layer net no), contrasting it with post-hoc [[Explainability|explainability]] ([[SHAP]]/[[LIME]]); requirements vary by domain (credit, medical, content moderation, fraud).
