---
title: "Influential Instances"
type: source
tags: [book, interpretable-ml, ml]
date: 2026-05-10
source_file: raw/interpretable-ml-book/manuscript/influential.qmd
book: "Interpretable Machine Learning"
author: "Christoph Molnar"
---


## Summary
Machine learning models are ultimately a product of training data, and deleting one of the training instances can affect the resulting model. We call a training instance "influential" when its deletion from the training data considerably changes the parameters or predictions of the model. By identifying influential training instances, we can "debug" machine learning models and better explain their behaviors and predictions.

## Key Claims
- **Deletion Diagnostics** — Statisticians have already done a lot of research in the area of influential instances, especially for (generalized) linear regression models.
- **Influence Functions** — *You*: I want to know the influence a training instance has on a particular prediction.
- **Strengths** — The approaches of deletion diagnostics and influence functions are very different from feature-perturbation based approaches like SHAP.
- **Limitations** — Deletion diagnostics are very **expensive to calculate** because they require retraining.
- **Software and Alternatives** — Deletion diagnostics are very simple to implement.

## Key Quotes
> See `source_file` for full text. Quotes omitted in bulk ingest; pull on demand.

## Connections
- [[imlbook-adversarial]] — referenced via @sec or [text](#adversarial).
- [[imlbook-feature-importance]] — referenced via @sec or [text](#feature-importance).
- [[imlbook-pdp]] — referenced via @sec or [text](#pdp).
- [[imlbook-proto]] — referenced via @sec or [text](#proto).
- [[imlbook-tree]] — referenced via @sec or [text](#tree).
- **Cited works** (sample): `cook1977detection`, `koh2017understanding`, `koh2019accuracy`.
- [[imlbook-limo]] — linear regression, the canonical interpretable baseline.
- [[imlbook-shap]] — Shapley-additive explanations referenced for individual prediction attribution.

## Contradictions
None noted in this chapter.
