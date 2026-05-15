---
title: "Functional Decomposition"
type: source
tags: [book, interpretable-ml, ml]
date: 2026-05-10
source_file: raw/interpretable-ml-book/manuscript/decomposition.qmd
book: "Interpretable Machine Learning"
author: "Christoph Molnar"
---


## Summary
A supervised machine learning model can be viewed as a function that takes a high-dimensional feature vector as input and produces a prediction or classification score as output. Functional decomposition is an interpretation technique that deconstructs the high-dimensional function and expresses it as a sum of individual feature effects and interaction effects that can be visualized. In addition, functional decomposition is a fundamental principle underlying many interpretation techniques -- it helps you better understand other interpretation methods.

## Key Claims
- **Decomposing a function** — A prediction function takes $p$ features as input, $\hat{f}: \mathbb{R}^p \mapsto \mathbb{R}$, and produces an output.
- **Functional ANOVA** — Functional ANOVA was proposed by @hooker2004discovering.
- **Generalized Functional ANOVA for dependent features** — Similar to most interpretation techniques based on sampling data (such as the PDP), the functional ANOVA can produce misleading results when features are correlated.
- **Accumulated Local Effects** — ALE plots [@apley2020visualizingeffects] also provide a functional decomposition, meaning that adding all ALE plots from intercept, 1D ALE plots, 2D ALE plots, and so on yields the prediction function.
- **Decomposing tree ensembles** — @yang2024inherently proposed a functional decomposition of tree ensembles, for example, trained with XGBoost.
- **Statistical regression models** — This approach ties in with interpretable models, in particular [generalized additive models](#extend-lm).
- **Strengths** — I consider functional decomposition to be a **key concept of machine learning interpretability** that helps to better understand many other methods.
- **Limitations** — The concept of functional decomposition quickly reaches its **limits for high-dimensional components** beyond interactions between two features.

## Key Quotes
> See `source_file` for full text. Quotes omitted in bulk ingest; pull on demand.

## Connections
- [[imlbook-ale]] — referenced via @sec or [text](#ale).
- [[imlbook-extend-lm]] — referenced via @sec or [text](#extend-lm).
- [[imlbook-feature-importance]] — referenced via @sec or [text](#feature-importance).
- [[imlbook-pdp]] — referenced via @sec or [text](#pdp).
- [[imlbook-shapley]] — referenced via @sec or [text](#shapley).
- **Cited works** (sample): `apley2020visualizingeffects`, `caruana2015intelligible`, `hooker2004discovering`, `hooker2007generalized`, `yang2024inherently`.
- [[imlbook-interpretability]] — foundational definition of interpretability invoked in this chapter.

## Contradictions
None noted in this chapter.
