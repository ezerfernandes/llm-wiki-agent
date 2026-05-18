---
title: "Max-Over-Time Pooling"
type: concept
tags: [cnn, nlp, pooling]
sources: [d2l-nlp-applications]
last_updated: 2026-05-16
---

# Max-Over-Time Pooling

The 1-D analogue of global max-pooling, used in [[TextCNN|textCNN]] (Collobert, Weston, Bottou et al. 2011; popularized by [[YoonKim|Kim]] 2014) to extract the **single most-salient activation per channel across all time steps** of a variable-length sequence.

## Definition

For a multi-channel input where each channel stores values at different time steps, the output at each channel is the *maximum* value for that channel. The variable-length input collapses to a fixed-length vector (one scalar per channel), enabling a fully-connected classifier head regardless of input length.

## Why "over time"

The temporal (sequence) axis is the one being pooled — different from spatial max-pooling in 2-D CNNs. Per [[d2l-nlp-applications]] §`sentiment-analysis-cnn`: "the max-over-time pooling allows different numbers of time steps at different channels."

## Connections

- [[TextCNN]] / [[CNN]] / [[MaxPooling]] / [[GlobalAveragePooling]].
- [[d2l-nlp-applications]] §`sentiment-analysis-cnn`.
