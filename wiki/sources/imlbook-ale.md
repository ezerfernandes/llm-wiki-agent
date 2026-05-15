---
title: "Accumulated Local Effects (ALE)"
type: source
tags: [book, interpretable-ml, ml]
date: 2026-05-10
source_file: raw/interpretable-ml-book/manuscript/ale.qmd
book: "Interpretable Machine Learning"
author: "Christoph Molnar"
---


## Summary
Accumulated local effects [@apley2020visualizingeffects] describe how features influence the prediction of a machine learning model on average. ALE plots are a faster and unbiased alternative to partial dependence plots (PDPs).

## Key Claims
- **Motivation and intuition** — If features of a machine learning model are correlated, the partial dependence plot cannot be trusted.
- **Theory** — How do PDP, M-plot, and ALE plot differ mathematically?
- **Estimation** — First I'll describe how ALE plots are estimated for a single numerical feature, later for two numerical features, and for a single categorical feature.
- **ALE versus PDP** — Let's see ALE plots in action.
- **Examples** — Turning to a real dataset, let's predict the [number of rented bikes](#bike-data) based on weather and day, and check if the ALE plots really work as well as promised.
- **Strengths** — **ALE plots are unbiased**, which means they still work when features are correlated.
- **Limitations** — An **interpretation of the effect across intervals is not permissible** if the features are strongly correlated.
- **Software and alternatives** — Did I mention that [partial dependence plots](#pdp) and [individual conditional expectation curves](#ice) are an alternative?

## Key Quotes
> See `source_file` for full text. Quotes omitted in bulk ingest; pull on demand.

## Connections
- [[imlbook-adversarial]] — referenced via @sec or [text](#adversarial).
- [[imlbook-decomposition]] — referenced via @sec or [text](#decomposition).
- [[imlbook-ice]] — referenced via @sec or [text](#ice).
- [[imlbook-pdp]] — referenced via @sec or [text](#pdp).
- **Cited works** (sample): `apley2020visualizingeffects`, `gkolemis2023rhale`, `gromping2020model`.

## Contradictions
None noted in this chapter.
