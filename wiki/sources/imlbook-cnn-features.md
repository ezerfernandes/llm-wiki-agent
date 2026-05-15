---
title: "Learned Features"
type: source
tags: [book, interpretable-ml, ml]
date: 2026-05-10
source_file: raw/interpretable-ml-book/manuscript/cnn-features.qmd
book: "Interpretable Machine Learning"
author: "Christoph Molnar"
---


## Summary
Convolutional neural networks learn abstract features and concepts from raw image pixels. [Feature Visualization](#feature-visualization) visualizes the learned features by activation maximization. [Network Dissection](#network-dissection) labels neural network units (e.g., channels) with human concepts.

## Key Claims
- **Feature visualization** — The approach of making the learned features explicit is called **Feature Visualization**.
- **Network Dissection** — The Network Dissection approach by @bau2017network quantifies the interpretability of a unit of a convolutional neural network.
- **Strengths** — Feature visualizations give **unique insight into the working of neural networks**, especially for image recognition.
- **Limitations** — **Many feature visualization images are not interpretable** at all, but contain some abstract features for which we have no words or mental concept.
- **Software and further material** — There's an open-source implementation of feature visualization called [Lucid](https://github.com/tensorflow/lucid).

## Key Quotes
> See `source_file` for full text. Quotes omitted in bulk ingest; pull on demand.

## Connections
- [[imlbook-adversarial]] — referenced via @sec or [text](#adversarial).
- [[imlbook-pixel-attribution]] — referenced via @sec or [text](#pixel-attribution).
- **Cited works** (sample): `bau2017network`, `deng2009imagenet`, `karpathy2015visualizing`, `nguyen2016synthesizing`, `nguyen2017plug`, `olah2017feature`, `olah2018the`.
- [[imlbook-interpretability]] — foundational definition of interpretability invoked in this chapter.

## Contradictions
None noted in this chapter.
