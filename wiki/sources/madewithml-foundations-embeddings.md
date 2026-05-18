---
title: "Made With ML — Embeddings"
type: source
tags: [foundations, made-with-ml, deep-learning, embeddings, nlp]
date: 2026-05-15
source_file: raw/madewithml/foundations-embeddings.md
---

## Summary
Foundations lesson motivating dense embeddings as the successor to one-hot encoding. Explains [[Word2Vec]] (CBOW and skip-gram), [[FastText]] (sub-word n-gram extensions for OOV robustness), and [[GloVe]] (pretrained co-occurrence-based vectors). Builds a CNN text classifier three ways — with randomly initialized embeddings learned from scratch, with frozen pretrained GloVe vectors, and with fine-tuned GloVe — to empirically compare the three regimes. Closes with interpretability via filter activations and an inference example.

## Key Claims
- One-hot encoding has two fatal flaws for large vocabularies: dimensionality scales linearly with vocab size, and identical Euclidean distance between every pair of tokens destroys all semantic structure.
- Embeddings learn a fixed-length dense vector per token (`embed_dim` typically much smaller than `vocab_size`), preserving similarity relationships geometrically.
- [[Word2Vec]] trains embeddings via a self-supervised objective: CBOW predicts a target word from its context; skip-gram predicts the context from a target word.
- [[FastText]] extends Word2Vec to operate on sub-word character n-grams, producing robust embeddings even for out-of-vocabulary or rare tokens.
- [[GloVe]] is trained on a global word–word co-occurrence matrix, producing pretrained embeddings that can be downloaded and reused.
- Three usage patterns: train embeddings from scratch (slow, needs lots of data), use pretrained embeddings frozen (fast, leverages large external corpus), or use pretrained embeddings fine-tuned (often best — domain-adapted).
- A PyTorch `nn.Embedding` layer is just a learnable lookup table; setting `padding_idx` ensures padding tokens don't contribute gradients.
- Empirically in the lesson, fine-tuned pretrained embeddings outperform both random init and frozen pretrained on the text classification task.

## Key Quotes
> "The main idea of embeddings is to have fixed length representations for the tokens in a text regardless of the number of tokens in the vocabulary." — Overview

> "With one-hot encoding, each token is represented by an array of size vocab_size, but with embeddings, each token now has the shape embed_dim. The values in the representation … are not fixed binary values but rather, changing floating points allowing for fine-grained learned representations." — Overview

## Connections
- [[MadeWithML]] — course this lesson belongs to
- [[GokuMohandas]] — author
- [[PyTorch]] — framework
- [[Embedding]] — central concept
- [[Word2Vec]] — CBOW + skip-gram
- [[FastText]] — sub-word extension
- [[GloVe]] — pretrained co-occurrence embeddings
- [[OneHotEncoding]] — predecessor critiqued
- [[CNN]] — classifier architecture used for the comparison
- [[Tokenizer]] — preprocessing
- [[Padding]] — sequence-length normalization
- [[FineTuning]] — adapting pretrained embeddings to a downstream task
- [[TransferLearning]] — pretrained → downstream paradigm
- [[Interpretability]] — filter-activation analysis

## Contradictions
- None identified.
