---
title: "Individual Conditional Expectation (ICE)"
type: source
tags: [book, interpretable-ml, ml]
date: 2026-05-10
source_file: raw/interpretable-ml-book/manuscript/ice.qmd
book: "Interpretable Machine Learning"
author: "Christoph Molnar"
---


## Summary
Individual Conditional Expectation (ICE) plots display one line per instance that shows how the instance's prediction changes when a feature changes. An ICE plot [@goldstein2015peeking] visualizes the dependence of the prediction on a feature for *each* instance separately, resulting in one line per instance of a dataset. The values for a line (and one instance) can be computed by keeping all other features the same, creating variants of this instance by replacing the feature's value with values from a grid, and making predictions with the black box model for these newly created instances.…

## Key Claims
- **Examples** — @fig-ice-bike shows ICE plots for the [bike rental prediction](#bike-data).
- **Centered ICE plot** — There's a problem with ICE plots: Sometimes it can be hard to tell whether the ICE curves differ between data points because they start at different predictions.
- **Derivative ICE plot** — Another way to make it visually easier to spot heterogeneity is to look at the individual derivatives of the prediction function with respect to a feature.
- **Strengths** — Individual conditional expectation curves are **intuitive to understand**.
- **Limitations** — ICE curves **can only display one feature** meaningfully, because two features would require the drawing of several overlaying surfaces, and you would not see anything in the plot.
- **Software and alternatives** — ICE plots are implemented in the R packages `iml` [@molnar2018iml] (used for these examples), `ICEbox`, and `pdp`.

## Key Quotes
> See `source_file` for full text. Quotes omitted in bulk ingest; pull on demand.

## Connections
- [[imlbook-ceteris-paribus]] — referenced via @sec or [text](#ceteris-paribus).
- [[imlbook-pdp]] — referenced via @sec or [text](#pdp).
- **Cited works** (sample): `goldstein2015peeking`, `molnar2018iml`, `sudjianto2023piml`.

## Contradictions
None noted in this chapter.
