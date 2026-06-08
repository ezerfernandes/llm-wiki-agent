---
title: "LIME"
type: concept
tags: [interpretability, explainability]
sources: [madewithml-evaluation, mlsysbook-ch15-responsible-engineering]
last_updated: 2026-06-05
---

# LIME

Local Interpretable Model-Agnostic Explanations — fits a simple surrogate model around individual predictions to explain them. Complements [[SHAP]] within [[interpretablemachinelearning]].

## Connections

- [[SHAP]] — sibling post-hoc [[Explainability|explanation]] method (Shapley attributions).
- [[Interpretability]] — the broader property LIME serves post-hoc.
- [[mlsysbook-ch15-responsible-engineering]] — mlsysbook Vol 1 Ch 15 cites LIME as the canonical *local surrogate* post-hoc [[Explainability|explainability]] method (vs. [[SHAP]] and vs. intrinsically [[Interpretability|interpretable]] models), with requirements set by regulatory context (e.g. credit adverse-action notices).
