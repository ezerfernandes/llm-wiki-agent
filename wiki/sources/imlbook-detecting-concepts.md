---
title: "Detecting Concepts"
type: source
tags: [book, interpretable-ml, ml]
date: 2026-05-10
source_file: raw/interpretable-ml-book/manuscript/detecting-concepts.qmd
book: "Interpretable Machine Learning"
author: "Christoph Molnar"
---


## Summary
*Author: Fangzhou Li @ University of California, Davis*

## Key Claims
- **TCAV: Testing with Concept Activation Vectors** — TCAV is proposed to generate global explanations for neural networks, but in theory, it should also work for any model where taking a directional derivative is possible.
- **Example** — Let's see an example available on the TCAV [GitHub](https://github.com/tensorflow/tcav/blob/master/Run_TCAV.ipynb).
- **Strengths** — Since users are only required to collect data for training the concepts that they are interested in, **TCAV does not require users to have machine learning expertise**.
- **Limitations** — TCAV might **perform badly on shallower neural networks**.
- **Other concept-based approaches** — The concept-based approach has attracted increasing popularity in recent times, and there are many new methods inspired by the utilization of concepts.
- **Software** — The official Python library of [TCAV](https://pypi.org/project/tcav/) requires TensorFlow, but there are other versions implemented online.

## Key Quotes
> See `source_file` for full text. Quotes omitted in bulk ingest; pull on demand.

## Connections
- **Cited works** (sample): `alain2018understanding`, `chen2020concept`, `ghorbani2019automatic`, `kim2018interpretability`, `koh2020concept`, `szegedy2016rethinking`.

## Contradictions
None noted in this chapter.
