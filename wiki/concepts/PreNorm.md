---
title: "Pre-Normalization"
type: concept
tags: [transformer, architecture, training]
sources: [d2l-attention-and-transformers, hands-on-llm-ch03-looking-inside-llms]
last_updated: 2026-05-23
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
- [[RMSNorm]] — the modern normalization typically combined with pre-norm.

## From [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]]

Ch 3 records pre-norm as one of the **modern Transformer block tweaks** vs. the 2017 original:

> "One of the differences we see in this version of the Transformer block is that normalization happens prior to attention and the feedforward layers. This has been reported to reduce the required training time." — Ch 3

The chapter cites *"On layer normalization in the Transformer architecture"* (Xiong et al. 2020) — the same paper the wiki's prior pre-norm coverage uses. In [[Phi3Mini|Phi-3-mini]]'s PyTorch print-out from Ch 3, pre-norm is visible as `input_layernorm` (before attention) and `post_attention_layernorm` (before MLP) — both [[RMSNorm|RMSNorm]] — applied **before** their respective sublayers inside the residual path.
