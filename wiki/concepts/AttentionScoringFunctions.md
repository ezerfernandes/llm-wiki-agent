---
title: "Attention Scoring Functions"
type: concept
tags: [attention, mechanism]
sources: [d2l-attention-and-transformers, 1706.03762-attention-is-all-you-need]
last_updated: 2026-05-16
---

# Attention Scoring Functions

The function $a(\mathbf{q}, \mathbf{k})$ producing the *pre-softmax* compatibility score between a query and a key inside [[AttentionPooling|attention pooling]]. Modern deep learning has two dominant choices:

## Scaled dot-product (Vaswani et al. 2017)

$$a(\mathbf{q}, \mathbf{k}) = \frac{\mathbf{q}^\top\mathbf{k}}{\sqrt{d}}$$

— see [[ScaledDotProductAttention]]. Requires $\mathbf{q}$ and $\mathbf{k}$ to have the same dimension $d$; the $1/\sqrt{d}$ scaling keeps the variance of the dot product at 1 (for iid unit-variance inputs the unscaled dot product has variance $d$), preventing softmax saturation. **The mainstay of modern [[Transformer|Transformers]].**

## Additive (Bahdanau / MLP attention)

$$a(\mathbf{q}, \mathbf{k}) = \mathbf{w}_v^\top \tanh(\mathbf{W}_q\mathbf{q} + \mathbf{W}_k\mathbf{k})$$

— see [[AdditiveAttention]]. Equivalent to feeding $[\mathbf{q};\mathbf{k}]$ through a one-hidden-layer MLP with $\tanh$ activation. Used when query and key have *different* dimensions and as the original [[BahdanauAttention|Bahdanau attention]] scoring function for seq2seq translation.

## Comparison

- **Compute.** Dot-product is "much faster and more space-efficient in practice, since it can be implemented using highly optimized matrix multiplication code" — the practical reason it dominates.
- **Without scaling.** Additive outperforms unscaled dot-product for large $d$; the $1/\sqrt{d}$ scaling closes the gap.
- **All modern attention uses softmax** on top of these — see [[Softmax]] / [[MaskedSoftmax]].

## See also

- [[Attention]] · [[AttentionPooling]] · [[QueryKeyValue]] · [[ScaledDotProductAttention]] · [[AdditiveAttention]] · [[MaskedSoftmax]]
