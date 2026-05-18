---
title: "Feed-Forward Network (positionwise FFN)"
type: concept
tags: [transformer, architecture]
sources: [d2l-attention-and-transformers, 1706.03762-attention-is-all-you-need]
last_updated: 2026-05-16
---

# Feed-Forward Network (positionwise FFN)

The two-layer MLP applied to **every position independently** inside each [[Transformer]] encoder / decoder block, providing the non-attention nonlinearity that lets a Transformer block represent arbitrary functions of its self-attention output.

$$\textrm{FFN}(\mathbf{x}) = \max(0, \mathbf{x}\mathbf{W}_1 + \mathbf{b}_1)\,\mathbf{W}_2 + \mathbf{b}_2$$

— two linear layers with a [[ReLU]] (or [[GELU]] in [[VisionTransformer|ViT]] and modern LLMs) activation in between. The same parameters are applied **identically at each sequence position** — hence "positionwise."

## Why "positionwise"

Each token's representation passes through the same MLP independently — there is no mixing across positions inside the FFN. Cross-position mixing happens only in the [[SelfAttention|self-attention]] sublayer. Equivalent to two pointwise (kernel-size-1) convolutions over the sequence axis.

## Dimensions (vanilla Transformer)

- Input / output dimension: $d_{\textrm{model}} = 512$.
- Hidden dimension: $d_{\textrm{ff}} = 2048$ (4× expansion).
- Approximately two-thirds of the total parameter count of a Transformer block.

## In context

The FFN is the second sublayer of every encoder block (after self-attention) and the third sublayer of every decoder block (after self-attention + encoder–decoder attention). Each sublayer is wrapped in a [[ResidualConnection|residual connection]] and [[LayerNormalization|LayerNorm]].

## See also

- [[Transformer]] · [[MultiHeadAttention]] · [[ResidualConnection]] · [[LayerNormalization]] · [[ReLU]] · [[GELU]] · [[PreNorm]]
