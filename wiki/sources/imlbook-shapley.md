---
title: "Shapley Values"
type: source
tags: [book, interpretable-ml, ml]
date: 2026-05-10
source_file: raw/interpretable-ml-book/manuscript/shapley.qmd
book: "Interpretable Machine Learning"
author: "Christoph Molnar"
---


## Summary
A prediction can be explained by assuming that each feature value of the instance is a "player" in a game where the prediction is the payout. Shapley values -- a method from coalitional game theory -- tell us how to fairly distribute the "payout" among the features.

## Key Claims
- **General idea** — Assume the following scenario: You've trained a machine learning model to predict apartment prices.
- **Examples and interpretation** — instance_indices = 7  x.interest = penguins_test[instance_indices,]
- **Shapley value theory** — This section goes deeper into the definition and computation of the Shapley value for the curious reader.
- **Estimating Shapley values** — All possible coalitions (sets) of feature values have to be evaluated with and without the $j$-th feature to calculate the exact Shapley value.
- **Strengths** — The difference between the prediction and the average prediction is **fairly distributed** among the feature values of the instance -- the Efficiency property of Shapley values.
- **Limitations** — The Shapley value requires **a lot of computing time**.
- **Software and alternatives** — Shapley values are implemented in both the `iml` and [fastshap](https://github.com/bgreenwell/fastshap) packages for R.

## Key Quotes
> See `source_file` for full text. Quotes omitted in bulk ingest; pull on demand.

## Connections
- [[imlbook-ceteris-paribus]] — referenced via @sec or [text](#ceteris-paribus).
- [[imlbook-ice]] — referenced via @sec or [text](#ice).
- [[imlbook-lime]] — referenced via @sec or [text](#lime).
- [[imlbook-shap]] — referenced via @sec or [text](#shap).
- **Cited works** (sample): `bilodeau2024impossibility`, `janzing2020feature`, `lundberg2017unified`, `shapley1953value`, `staniak2018explanationsa`, `strumbelj2014explaining`, `sundararajan2020many`.

## Contradictions
None noted in this chapter.
