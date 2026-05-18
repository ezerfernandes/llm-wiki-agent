---
title: "Pre-Normalization"
type: concept
tags: [transformer, architecture, training]
sources: [d2l-attention-and-transformers]
last_updated: 2026-05-16
---

# Pre-Normalization

A variant of the [[Transformer]] block where [[LayerNormalization|LayerNorm]] is applied **before** each sublayer (multi-head attention or FFN), instead of after the residual addition:

$$\textrm{block}(\mathbf{x}) = \mathbf{x} + \textrm{sublayer}(\textrm{LayerNorm}(\mathbf{x}))$$

versus the [[1706.03762-attention-is-all-you-need|original]] **post-norm** form:

$$\textrm{block}_{\textrm{post}}(\mathbf{x}) = \textrm{LayerNorm}(\mathbf{x} + \textrm{sublayer}(\mathbf{x})).$$

## Why pre-norm

Pre-norm is "more effective or efficient" for training deep Transformers ([[baevski2018adaptive|Baevski & Auli 2018]]; [[xiong2020layer|Xiong et al. 2020]]; [[wang2019learning|Wang et al. 2019]]):

- **Stable gradients without warmup.** Post-norm Transformers require a learning-rate warmup schedule to avoid divergence early in training; pre-norm trains stably without it.
- **Easier scaling to depth.** Pre-norm Transformers scale to many more layers without optimization collapse.

The [[VisionTransformer|Vision Transformer]] adopts pre-norm, as do modern decoder-only LLMs (GPT-2 and later, LLaMA, etc.).

## Trade-off

Post-norm sometimes yields slightly better final performance at moderate depth; the consensus by 2026 is that pre-norm's training stability and depth-scaling advantages dominate.

## See also

- [[Transformer]] · [[VisionTransformer]] · [[LayerNormalization]] · [[ResidualConnection]]
