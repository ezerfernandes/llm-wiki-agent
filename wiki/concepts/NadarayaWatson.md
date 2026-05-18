---
title: "Nadaraya–Watson Kernel Regression"
type: concept
tags: [kernel-method, regression, attention, precursor]
sources: [d2l-attention-and-transformers]
last_updated: 2026-05-16
---

# Nadaraya–Watson Kernel Regression

A non-parametric regression / classification estimator independently proposed by Nadaraya (1964) and Watson (1964). For training pairs $\{(\mathbf{x}_i, y_i)\}_{i=1}^n$ and a query point $\mathbf{q}$:

$$f(\mathbf{q}) = \sum_i y_i \frac{\alpha(\mathbf{q}, \mathbf{x}_i)}{\sum_j \alpha(\mathbf{q}, \mathbf{x}_j)}$$

where $\alpha(\mathbf{q}, \mathbf{x})$ is a similarity kernel — Gaussian, Boxcar, Epanechikov, etc. Equivalent to [[AttentionPooling|attention pooling]] with each $(\mathbf{x}_i, y_i)$ playing the role of a [[QueryKeyValue|(key, value)]] pair.

## Why it lives on the wiki

[[d2l-attention-and-transformers|D2L]] uses Nadaraya–Watson as the half-century precursor of modern attention. Three pedagogical points:

1. **Visualization.** With scalar inputs and a Gaussian kernel, you can plot the attention weights directly — the "Reds" heatmaps in §attention-pooling show how kernel width controls locality.
2. **Limits of hand-crafted attention.** All four kernels are heuristics; tuning $\sigma$ globally is rigid (Silverman's heuristic helps); the natural next step is to *learn* the kernel — i.e. to learn query/key representations.
3. **Bridge to the Gaussian-kernel derivation of dot-product attention.** Expanding $-\tfrac{1}{2}\|\mathbf{q}-\mathbf{k}\|^2 = \mathbf{q}^\top\mathbf{k} - \tfrac{1}{2}\|\mathbf{k}\|^2 - \tfrac{1}{2}\|\mathbf{q}\|^2$ — with the last two terms either cancelling in softmax or bounded by LayerNorm — drops out as [[ScaledDotProductAttention|dot-product attention]] up to the $1/\sqrt{d}$ scaling.

Mack (1982) proved Nadaraya–Watson estimation is consistent under suitably shrinking kernel widths.

## See also

- [[Attention]] · [[AttentionPooling]] · [[ScaledDotProductAttention]] · [[KernelTrick]]
