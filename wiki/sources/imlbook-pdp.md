---
title: "Partial Dependence Plot (PDP)"
type: source
tags: [book, interpretable-ml, ml]
date: 2026-05-10
source_file: raw/interpretable-ml-book/manuscript/pdp.qmd
book: "Interpretable Machine Learning"
author: "Christoph Molnar"
---


## Summary
The partial dependence plot (short PDP or PD plot) shows the marginal effect one or two features have on the predicted outcome of a machine learning model [@friedman2001greedy]. A partial dependence plot can show whether the relationship between the target and a feature is linear, monotonic, or more complex. For example, when applied to a linear regression model, partial dependence plots always show a linear relationship.

## Key Claims
- **Definition and estimation** — The partial dependence function for regression is defined as:
- **Examples** — In practice, the set of features $S$ usually only contains one feature or a maximum of two, because one feature produces 2D plots, and two features produce 3D plots.
- **PDP-based feature importance** — @greenwell2018simple proposed a simple partial dependence-based feature importance measure.
- **Strengths** — The computation of partial dependence plots is **intuitive**: The partial dependence function at a particular feature value represents the average prediction if we force all data points to assume that feature value.
- **Limitations** — The realistic **maximum number of features** in a partial dependence function that can be meaningfully visualized is two.
- **Software and alternatives** — There are a number of R packages that implement PDPs.

## Key Quotes
> See `source_file` for full text. Quotes omitted in bulk ingest; pull on demand.

## Connections
- [[imlbook-ale]] — referenced via @sec or [text](#ale).
- [[imlbook-feature-importance]] — referenced via @sec or [text](#feature-importance).
- [[imlbook-ice]] — referenced via @sec or [text](#ice).
- **Cited works** (sample): `britton2019vine`, `friedman2001greedy`, `gkolemis2024fast`, `greenwell2018simple`, `herbinger2022repid`, `herbinger2024decomposing`, `molnar2020quantifying`, `zhao2019causal`.
- [[imlbook-limo]] — linear regression, the canonical interpretable baseline.

## Contradictions
None noted in this chapter.
