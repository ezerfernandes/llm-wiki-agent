---
title: "LIME"
type: source
tags: [book, interpretable-ml, ml]
date: 2026-05-10
source_file: raw/interpretable-ml-book/manuscript/lime.qmd
book: "Interpretable Machine Learning"
author: "Christoph Molnar"
---


## Summary
get.ycomments.classifier = function(ycomments){   labeledTerms = prepare_data(ycomments$CONTENT)   labeledTerms$class = factor(ycomments$CLASS, levels = c(0,1), labels = c('no spam', 'spam'))   rp = rpart::rpart(class ~ ., data = labeledTerms)   get_predict_fun(rp, labeledTerms) }

## Key Claims
- **LIME for tabular data** — Tabular data is data that comes in tables, with each row representing an instance and each column a feature.
- **LIME for text data** — LIME for text differs from LIME for tabular data.
- **LIME for image data** — *This section was written by Verena Haunschmid.*
- **Strengths** — Even if you **replace the underlying machine learning model**, you can still use the same local, interpretable model for explanation.
- **Limitations** — The **choice of neighborhood is an unsolved problem** when using LIME with tabular data.
- **Software** — The original Python implementation is in the [lime package](https://github.com/marcotcr/lime).

## Key Quotes
> See `source_file` for full text. Quotes omitted in bulk ingest; pull on demand.

## Connections
- [[imlbook-tree]] — referenced via @sec or [text](#tree).
- **Cited works** (sample): `alberto2015tubespam`, `melis2018robustness`, `ribeiro2016why`, `slack2020fooling`.

## Contradictions
None noted in this chapter.
