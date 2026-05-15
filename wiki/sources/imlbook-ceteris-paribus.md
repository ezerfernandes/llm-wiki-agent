---
title: "Ceteris Paribus Plots"
type: source
tags: [book, interpretable-ml, ml]
date: 2026-05-10
source_file: raw/interpretable-ml-book/manuscript/ceteris-paribus.qmd
book: "Interpretable Machine Learning"
author: "Christoph Molnar"
---


## Summary
Ceteris paribus (CP) plots [@kuzba2019pyceterisparibus] visualize how changes in a single feature change the prediction of a data point.

## Key Claims
- **Algorithm** — Let's get started with the ceteris paribus algorithm.
- **Examples** — For our first example, we look at the random forest predicting the probability of a penguin being female.
- **Minimal version with sparklines** — CP plots can be packaged into sparklines, a minimalistic line-plot popularized by @tufte1983visual.
- **Strengths** — **Ceteris paribus plots are super simple to implement and understand.** This makes them a great entry point for beginners, but also for communicating model-agnostic explainability to others, especially non-experts.
- **Limitations** — **Ceteris paribus plots only show us one feature change at a time.** This means we don't see how two features interact.
- **Software and alternatives** — I created all plots in this chapter with the [ceterisParibus R package](https://cran.r-project.org/web/packages/ceterisParibus/index.html).

## Key Quotes
> See `source_file` for full text. Quotes omitted in bulk ingest; pull on demand.

## Connections
- [[imlbook-ice]] — referenced via @sec or [text](#ice).
- [[imlbook-pdp]] — referenced via @sec or [text](#pdp).
- **Cited works** (sample): `kuzba2019pyceterisparibus`, `tufte1983visual`.

## Contradictions
None noted in this chapter.
