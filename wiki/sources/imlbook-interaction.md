---
title: "Feature Interaction"
type: source
tags: [book, interpretable-ml, ml]
date: 2026-05-10
source_file: raw/interpretable-ml-book/manuscript/interaction.qmd
book: "Interpretable Machine Learning"
author: "Christoph Molnar"
---


## Summary
When features interact with each other in a prediction model, the prediction cannot be expressed as the sum of the feature effects because the effect of one feature depends on the value of the other feature. Aristotle's predicate "The whole is greater than the sum of its parts" applies in the presence of interactions.

## Key Claims
- **What are feature interactions?** — If a machine learning model makes a prediction based on two features, we can decompose the prediction into four terms: a constant term, a term for the first feature, a term for the second feature, and a term for the interaction between the…
- **Friedman's H-statistic** — We are going to deal with two cases: First, a two-way interaction measure that tells us whether and to what extent two features in the model interact with each other; second, a total interaction measure that tells us whether and to what…
- **Examples** — Let's see what feature interactions look like in practice!
- **Strengths** — The interaction H-statistic has an **underlying theory** through the partial dependence decomposition.
- **Limitations** — The first thing you will notice: The interaction H-statistic takes a long time to compute because it's **computationally expensive**.
- **Software and alternatives** — For the examples in this book, I used the R package `iml`, which is available on [CRAN](https://cran.r-project.org/web/packages/iml) and the development version on [GitHub](https://github.com/christophM/iml).

## Key Quotes
> See `source_file` for full text. Quotes omitted in bulk ingest; pull on demand.

## Connections
- [[imlbook-pdp]] — referenced via @sec or [text](#pdp).
- [[imlbook-rulefit]] — referenced via @sec or [text](#rulefit).
- **Cited works** (sample): `friedman2008predictive`, `greenwell2018simple`, `hooker2004discovering`, `inglis2022visualizing`.

## Contradictions
None noted in this chapter.
