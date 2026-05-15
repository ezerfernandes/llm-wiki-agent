---
title: "Surrogate Models"
type: source
tags: [book, interpretable-ml, ml]
date: 2026-05-10
source_file: raw/interpretable-ml-book/manuscript/global.qmd
book: "Interpretable Machine Learning"
author: "Christoph Molnar"
---


## Summary
A global surrogate model is an interpretable model that is trained to approximate the predictions of a black box model. We can draw conclusions about the black box model by interpreting the surrogate model. Solving machine learning interpretability by using more machine learning!

## Key Claims
- **Theory** — Surrogate models are also used in engineering: If an outcome of interest is expensive, time-consuming, or otherwise difficult to measure (e.g., because it comes from a complex computer simulation), a cheap and fast surrogate model of the…
- **Example** — To demonstrate the surrogate models, we consider a regression and a classification example.
- **Strengths** — The surrogate model method is **flexible**: Any interpretable model can be used.
- **Limitations** — You have to be aware that you draw **conclusions about the model and not about the data**, since the surrogate model never sees the real outcome.
- **Software** — I used the `iml` R package for the examples.

## Key Quotes
> See `source_file` for full text. Quotes omitted in bulk ingest; pull on demand.

## Connections
- (No outbound chapter cross-references detected.)
- [[imlbook-interpretability]] — foundational definition of interpretability invoked in this chapter.

## Contradictions
None noted in this chapter.
