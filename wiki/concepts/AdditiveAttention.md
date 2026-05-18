---
title: "Additive Attention"
type: concept
tags: [attention, mechanism]
sources: [d2l-attention-and-transformers]
last_updated: 2026-05-16
---

# Additive Attention

An [[AttentionScoringFunctions|attention scoring function]] introduced by [[BahdanauAttention|Bahdanau, Cho & Bengio 2014]] for differentiable alignment in [[MachineTranslation|machine translation]]. Given query $\mathbf{q} \in \mathbb{R}^q$ and key $\mathbf{k} \in \mathbb{R}^k$ (possibly of different dimensions):

$$a(\mathbf{q}, \mathbf{k}) = \mathbf{w}_v^\top \tanh(\mathbf{W}_q\mathbf{q} + \mathbf{W}_k\mathbf{k}) \in \mathbb{R}$$

with learnable $\mathbf{W}_q \in \mathbb{R}^{h\times q}$, $\mathbf{W}_k \in \mathbb{R}^{h\times k}$, $\mathbf{w}_v \in \mathbb{R}^h$. Equivalent to concatenating the query and key and feeding them through a one-hidden-layer MLP with $\tanh$ activation and disabled bias.

## When to use it

- **Different query and key dimensions** — no projection matrix needed.
- **Compatibility is "hard"** — the MLP can express a richer function than a bare dot product (cited as a reason additive attention can outperform unscaled dot-product attention for large $d$).
- **Legacy / RNN-era seq2seq** — additive attention is what Bahdanau, Luong, etc. used in pre-Transformer NMT.

## Why dot-product won

Modern [[Transformer|Transformers]] use [[ScaledDotProductAttention|scaled dot-product attention]] instead because matrix multiplication is "much faster and more space-efficient in practice" on accelerators. The $1/\sqrt{d}$ scaling closes the quality gap with additive attention.

## See also

- [[Attention]] · [[AttentionScoringFunctions]] · [[BahdanauAttention]] · [[ScaledDotProductAttention]]
