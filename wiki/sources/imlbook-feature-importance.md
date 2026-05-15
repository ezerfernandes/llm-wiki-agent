---
title: "Permutation Feature Importance"
type: source
tags: [book, interpretable-ml, ml]
date: 2026-05-10
source_file: raw/interpretable-ml-book/manuscript/feature-importance.qmd
book: "Interpretable Machine Learning"
author: "Christoph Molnar"
---


## Summary
Permutation feature importance (PFI) measures the increase in the prediction error of the model after we permute the values of the feature, which breaks the relationship between the feature and the true outcome.

## Key Claims
- **Theory** — The permutation feature importance measurement was introduced by @breiman2001random for random forests.
- **Use unseen data for PFI** — Estimate PFI on data not used for model training to avoid overly optimistic results, especially with overfitting models.
- **Example and interpretation** — For the first example, we explain the support vector machine model trained to predict [the number of rented bikes](#bike-data), given weather conditions and calendar information.
- **Conditional feature importance** — Like all the model-agnostic methods, permutation feature importance has a problem when features are dependent.
- **Group-wise PFI example** — Let's go back to the penguins.
- **Strengths** — **Nice interpretation**: Feature importance is the increase in model error when the feature's information is destroyed.
- **Limitations** — Permutation feature importance is **linked to the error of the model**.
- **Software and alternatives** — The `iml` R package was used for the examples.

## Key Quotes
> See `source_file` for full text. Quotes omitted in bulk ingest; pull on demand.

## Connections
- [[imlbook-decomposition]] — referenced via @sec or [text](#decomposition).
- [[imlbook-lofo]] — referenced via @sec or [text](#lofo).
- [[imlbook-pdp]] — referenced via @sec or [text](#pdp).
- [[imlbook-shap]] — referenced via @sec or [text](#shap).
- **Cited works** (sample): `breiman2001random`, `debeer2020conditional`, `fisher2019all`, `molnar2023modelagnostic`, `strobl2008conditional`, `watson2021testing`, `wei2015variable`.

## Contradictions
None noted in this chapter.
