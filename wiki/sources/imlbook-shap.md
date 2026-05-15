---
title: "SHAP"
type: source
tags: [book, interpretable-ml, ml]
date: 2026-05-10
source_file: raw/interpretable-ml-book/manuscript/shap.qmd
book: "Interpretable Machine Learning"
author: "Christoph Molnar"
---


## Summary
SHAP (SHapley Additive exPlanations) by @lundberg2017unified is a method to explain individual predictions. SHAP is based on the game-theoretically optimal Shapley values. I recommend reading the chapter on [Shapley values](#shapley) first.

## Key Claims
- **SHAP theory** — The goal of SHAP is to explain the prediction of an instance $\mathbf{x}$ by computing the contribution of each feature to the prediction.
- **SHAP estimation** — This section is about three ways to estimate Shapley values for explaining predictions: KernelSHAP, Permutation Method, and TreeSHAP.
- **Example** — I trained a random forest classifier with 100 trees to predict the [penguin sex](#penguins).
- **SHAP aggregation plots** — The section before showed explanations for individual predictions.
- **Strengths** — Since SHAP computes Shapley values, all the advantages of Shapley values apply: SHAP has a **solid theoretical foundation** in game theory.
- **Limitations** — **KernelSHAP is slow**.
- **Software** — Lundberg implemented SHAP in the [shap](https://github.com/slundberg/shap) Python package, which is now maintained by a much bigger team.

## Key Quotes
> See `source_file` for full text. Quotes omitted in bulk ingest; pull on demand.

## Connections
- [[imlbook-ale]] — referenced via @sec or [text](#ale).
- [[imlbook-feature-importance]] — referenced via @sec or [text](#feature-importance).
- [[imlbook-lime]] — referenced via @sec or [text](#lime).
- [[imlbook-pdp]] — referenced via @sec or [text](#pdp).
- [[imlbook-shapley]] — referenced via @sec or [text](#shapley).
- [[2605.03808-agentic-imodels]] — modern extension: SHAP is the Shapley-additive interpretability standard the AGENTIC-IMODELS simulatability metric ultimately competes against.
- **Cited works** (sample): `aas2021explaining`, `janzing2020feature`, `lundberg2017unified`, `lundberg2019consistent`, `mitchell2022sampling`, `muschalik2024shapiq`, `slack2020fooling`, `strumbelj2011general` (+2 more).

## Contradictions
None noted in this chapter.
