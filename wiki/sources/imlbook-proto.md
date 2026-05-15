---
title: "Prototypes and Criticisms"
type: source
tags: [book, interpretable-ml, ml]
date: 2026-05-10
source_file: raw/interpretable-ml-book/manuscript/proto.qmd
book: "Interpretable Machine Learning"
author: "Christoph Molnar"
---


## Summary
A **prototype** is a data instance that is representative of all the data. A **criticism** is a data instance that is not well represented by the set of prototypes. The purpose of criticisms is to provide insights together with prototypes, especially for data points which the prototypes do not represent well. Prototypes and criticisms can be used independently from a machine learning model to describe the data, but they can also be used to create an interpretable model or to make a black box model interpretable.

## Key Claims
- **Theory** — The MMD-critic procedure on a high level can be summarized briefly:
- **Examples** — The following example of MMD-critic uses a handwritten digit dataset.
- **Strengths** — In a user study, the authors of MMD-critic gave images to the participants, which they had to visually match to one of two sets of images, each representing one of two classes (e.g., two dog breeds).
- **Limitations** — While mathematically, prototypes and criticisms are defined differently, their **distinction is based on a cut-off value** (the number of prototypes).
- **Software and alternatives** — An implementation of MMD-critic can be found in [the authors' GitHub repository](https://github.com/BeenKim/MMD-critic).

## Key Quotes
> See `source_file` for full text. Quotes omitted in bulk ingest; pull on demand.

## Connections
- **Cited works** (sample): `kim2016examples`, `rdusseeun1987clustering`.

## Contradictions
None noted in this chapter.
