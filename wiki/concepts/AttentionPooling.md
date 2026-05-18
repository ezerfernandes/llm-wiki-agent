---
title: "Attention Pooling"
type: concept
tags: [attention, mechanism]
sources: [d2l-attention-and-transformers]
last_updated: 2026-05-16
---

# Attention Pooling

The aggregation step of any [[Attention|attention mechanism]]: a *normalized weighted sum* of values $\mathbf{v}_i$ where the weights $\alpha(\mathbf{q}, \mathbf{k}_i)$ are computed from a query–key [[AttentionScoringFunctions|scoring function]] (typically passed through softmax):

$$\textrm{Attention}(\mathbf{q}, \mathcal{D}) = \sum_{i=1}^m \alpha(\mathbf{q}, \mathbf{k}_i)\,\mathbf{v}_i,\qquad \alpha(\mathbf{q}, \mathbf{k}_i) = \frac{\exp(a(\mathbf{q}, \mathbf{k}_i))}{\sum_j \exp(a(\mathbf{q}, \mathbf{k}_j))}.$$

[[d2l-attention-and-transformers|D2L]] motivates it as the differentiable generalization of a database lookup over [[QueryKeyValue|(key, value) pairs]], where ordinary [[AveragePooling|average pooling]] is the uniform-weights case and an exact key lookup is the one-hot case.

## Why softmax

Softmax over exponentiated scores gives all four desirable properties at once:
- **Nonnegativity** — $\alpha_i \ge 0$.
- **Convex combination** — $\sum_i \alpha_i = 1$.
- **Differentiability** — for end-to-end training.
- **Never-vanishing gradient** — unlike argmax / top-$k$.

A non-differentiable attention model trainable via RL ([[mnih2014recurrent|Mnih, Heess, Graves 2014]]) is possible but harder to train; modern attention essentially uses softmax universally.

## In practice

The earliest example is the [[NadarayaWatson|Nadaraya–Watson]] kernel regression estimator from 1964 — a hand-crafted, non-learned form of attention pooling. Modern attention adds learned linear projections producing [[QueryKeyValue|Q, K, V]] and uses [[ScaledDotProductAttention|scaled dot-product]] as the score.

## See also

- [[Attention]] · [[QueryKeyValue]] · [[AttentionScoringFunctions]] · [[ScaledDotProductAttention]] · [[NadarayaWatson]] · [[MaskedSoftmax]] · [[Softmax]]
