---
title: "One-Hot Encoding"
type: concept
tags: [preprocessing, features, classification]
sources: [madewithml-preprocessing, d2l-linear-classification]
last_updated: 2026-05-16
---

# One-Hot Encoding

A representation that maps each value of [[CategoricalData]] to a binary indicator vector — a vector with as many components as categories, where the position of the active category is set to 1 and all others to 0. Simple and lossless but expands dimensionality; alternatives include embeddings and [[Tokenization]] for text.

## Why classification uses it

Per [[d2l-linear-classification]]: categories rarely have a natural ordering (cat / chicken / dog has no "ordering"), so an integer encoding $y \in \{1, 2, 3\}$ would impose a spurious metric structure. One-hot $y \in \{(1,0,0), (0,1,0), (0,0,1)\}$ removes this and is the natural label representation for [[CrossEntropyLoss|categorical cross-entropy]] training — the sum $\sum_j y_j \log\hat y_j$ collapses to a single $\log\hat y_{\text{true}}$ term, exactly the negative log-likelihood of the correct class. (For *ordinal* classification, where the categories *do* have a natural order — `baby < toddler < adolescent < adult`, ratings 1–5 — ordinal regression or rank-aware losses are preferable.)

## Connections

- [[Classification]] — the task this encoding is the canonical label format for.
- [[CrossEntropyLoss]] / [[Softmax]] — what one-hot labels are paired with in training.
- [[CategoricalData]] — the data type being encoded.
- [[d2l-linear-classification]] — corpus anchor for the classification rationale.
