---
title: "Layer normalization"
type: concept
tags: [deep-learning, regularization, normalization]
sources: [d2l-convolutional-modern, hands-on-llm-ch03-looking-inside-llms, mlsysbook-ch06-network-architectures]
last_updated: 2026-06-05
---

# Layer normalization

A per-observation variant of [[BatchNormalization|batch normalization]] introduced by [[Ba|Ba]], [[JamieKiros|Kiros]] & [[GeoffreyHinton|Hinton]] (2016). Where BN normalizes each feature/channel using statistics from *across the minibatch*, LN normalizes each observation using statistics from *across its own features* — making it independent of batch size and identical at train and test time ([[d2l-convolutional-modern]] §batch-norm).

## Definition

For an $n$-dimensional vector $\mathbf{x}$:

$$\textrm{LN}(\mathbf{x}) = \frac{\mathbf{x} - \hat{\mu}}{\hat{\sigma}}$$

where

$$\hat{\mu} = \frac{1}{n}\sum_{i=1}^n x_i, \quad \hat{\sigma}^2 = \frac{1}{n}\sum_{i=1}^n (x_i-\hat{\mu})^2 + \epsilon$$

Both statistics are computed **within a single observation** (no batch dimension involved). Like BN, learnable scale $\boldsymbol{\gamma}$ and shift $\boldsymbol{\beta}$ typically follow.

## Properties

- **Batch-size independent.** Works for batch size 1.
- **Train/test identical.** No moving averages, no mode switch — purely deterministic.
- **Scale-invariant.** $\textrm{LN}(\mathbf{x}) \approx \textrm{LN}(\alpha\mathbf{x})$ for any $\alpha \neq 0$ (exact in the $|\alpha|\to\infty$ limit, ignoring $\epsilon$). Helps prevent divergence in optimization.

## LN vs. BN

| Property | [[BatchNormalization\|BN]] | LN |
|---|---|---|
| Statistics over | Minibatch, per-feature/channel | Single observation, per-features |
| Batch-size dependent? | **Yes** (best at 50–100) | No |
| Different at train vs. test? | **Yes** | No |
| Standard in CNNs? | **Yes** | Rarely |
| Standard in Transformers? | Rare | **Yes** (post-LN and pre-LN are both default) |
| Works for variable-length sequences? | Awkward | Natural |

## Where LN dominates

- **[[transformer|Transformers]]** (Vaswani et al. 2017 and successors) — every sub-layer is wrapped in LN. Two conventions: **post-LN** `LayerNorm(x + sublayer(x))` (original Transformer) and **pre-LN** `x + sublayer(LayerNorm(x))` (modern; more stable training).
- **RNNs / LSTMs** — batch-size dependence and variable sequence lengths make BN awkward; LN drops in cleanly.
- **Recommender systems / tabular** — where minibatch statistics are unstable.

## Where BN remains better

- **CNNs on fixed-resolution images** with large minibatches — BN's per-channel rescaling-over-spatial-locations matches translation invariance better than LN.

## Connections

- [[d2l-convolutional-modern]] — canonical reference.
- [[BatchNormalization]] — sibling normalization.
- [[GeoffreyHinton]] — co-author.
- [[transformer]] — heavy user.
- [[Attention]] — every attention block is wrapped in LN.
- [[CNN]] — context where LN is sometimes a BN alternative for small batches.
- [[RMSNorm]] — the simpler successor used by modern LLMs.
- [[PreNorm]] — the placement scheme modern LLMs favor over post-norm.
- [[mlsysbook-ch06-network-architectures]] — Ch 6 positions LayerNorm in the normalization-evolution chain ([[BatchNormalization|BatchNorm]] → LayerNorm → [[RMSNorm]]) as a *portable building block*: it removed BatchNorm's batch-size dependency and training-serving skew, behaving identically in train and inference (cost $\mathcal{O}(d_{\text{model}})$ per sample).

## From [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]]

Ch 3 records that modern 2024-era LLMs have moved off LayerNorm to **[[RMSNorm|RMSNorm]]**:

> "Another improvement in normalization here is using RMSNorm, which is simpler and more efficient than the LayerNorm used in the original Transformer (read: 'Root mean square layer normalization')." — Ch 3

Plus the **placement** change from post-norm to **[[PreNorm|pre-norm]]**:

> "One of the differences we see in this version of the Transformer block is that normalization happens prior to attention and the feedforward layers. This has been reported to reduce the required training time." — Ch 3

The chapter cites *"On layer normalization in the Transformer architecture"* for the pre-norm finding. Together, **RMSNorm + pre-norm** is the modern replacement for the original Transformer's **LayerNorm + post-norm** — see the [[transformer|Transformer page]]'s "2024-era block recipe" table for the full bundle.
