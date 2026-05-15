---
title: "Leave One Feature Out (LOFO) Importance"
type: source
tags: [book, interpretable-ml, ml]
date: 2026-05-10
source_file: raw/interpretable-ml-book/manuscript/lofo.qmd
book: "Interpretable Machine Learning"
author: "Christoph Molnar"
---


## Summary
Leave One Feature Out (LOFO) Importance measures a feature's importance by retraining the model without the feature and comparing the predictive performances.[^loco]

## Key Claims
- **Examples** — We predict bike rentals based on weather and calendar information using a random forest trained on 2/3 of the data.
- **LOFO versus PFI** — LOFO differs from the other methods presented in this book, since most of the other methods don't require retraining the model.
- **Strengths** — **Implementing LOFO is simple**.
- **Limitations** — **LOFO is costly:** If you compute LOFO importance for all features, you have to retrain the model $p$ times.
- **Software and alternatives** — LOFO has a [Python implementation](https://github.com/aerdem4/lofo-importance).

## Key Quotes
> See `source_file` for full text. Quotes omitted in bulk ingest; pull on demand.

## Connections
- [[imlbook-feature-importance]] — referenced via @sec or [text](#feature-importance).
- **Cited works** (sample): `lei2018distributionfree`.

## Contradictions
None noted in this chapter.
