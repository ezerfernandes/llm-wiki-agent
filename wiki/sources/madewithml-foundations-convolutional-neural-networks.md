---
title: "Made With ML — Convolutional Neural Networks (CNN)"
type: source
tags: [foundations, made-with-ml, deep-learning, cnn, nlp]
date: 2026-05-15
source_file: raw/madewithml/foundations-convolutional-neural-networks.md
---

## Summary
Foundations lesson introducing convolutional neural networks, applied to text classification rather than images, to motivate CNNs as general-purpose feature extractors. Walks through tokenization, one-hot encoding, padding to a fixed length, and building a PyTorch CNN with multiple filter widths, ReLU activation, max-over-time pooling, and batch normalization. Closes with an interpretability section that visualizes which n-grams each filter responds to most strongly.

## Key Claims
- A convolution is a learned filter (kernel) slid across the input that extracts a local feature; weights are shared across positions, which dramatically reduces parameter count vs. fully-connected layers.
- CNNs are not image-specific: applied to text, a 1-D convolution with kernel size `k` acts as a learned n-gram detector over the token sequence.
- Filters are initialized randomly and learn to act as feature extractors via end-to-end gradient descent — no hand-engineered features needed.
- Pooling (typically max-pool) downsamples the per-position activations into a fixed-size summary, providing translation invariance and reducing dimensionality.
- [[BatchNormalization]] stabilizes training by normalizing activations within each mini-batch, often allowing higher learning rates.
- Inputs are first tokenized, padded to a max length, and one-hot encoded over the vocabulary; later lessons replace one-hot with learned [[Embedding]]s.
- CNNs are parallelizable (unlike RNNs) because all filter applications across positions are independent given the input.
- Interpretability: the input n-grams that maximally activate each filter can be extracted post-training, giving a human-readable view of what the model learned.
- Many hyperparameters require tuning: filter widths, number of filters per width, pooling, strides, padding.

## Key Quotes
> "At the core of CNNs are filters (aka weights, kernels, etc.) which convolve (slide) across our input to extract relevant features. The filters are initialized randomly but learn to act as feature extractors via parameter sharing." — Overview

> "Lot's of deep CNN architectures constantly updated for SOTA performance. Very popular feature extractor that acts as a foundation for many architectures." — Miscellaneous

## Connections
- [[MadeWithML]] — course this lesson belongs to
- [[GokuMohandas]] — author
- [[PyTorch]] — framework
- [[CNN]] — main concept
- [[Convolution]] — the underlying operation
- [[Filter]] — learned kernel
- [[Pooling]] — max-pool downsampling
- [[BatchNormalization]] — stabilization technique
- [[Tokenizer]] — preprocessing step
- [[OneHotEncoding]] — initial input representation
- [[Padding]] — fixing variable sequence lengths
- [[ReLU]] — activation
- [[NeuralNetwork]] — broader family
- [[Interpretability]] — n-gram filter visualization
- [[Embedding]] — replacement for one-hot in next lesson

## Contradictions
- None identified.
