---
title: "Multi-Query Attention"
type: concept
tags: [attention, architecture, inference-efficiency]
sources: [2312.11805-gemini]
last_updated: 2026-05-10
---

# Multi-Query Attention (MQA)

A variant of [[MultiHeadAttention]] (Shazeer, 2019) in which **all attention heads share a single Key and Value projection** while keeping per-head Query projections. The KV cache shrinks by a factor of `h` (the number of heads), dramatically reducing memory bandwidth at decode time. With long-context decoding (e.g. Gemini's 32K window in [[2312.11805-gemini]]) the KV cache dominates inference cost, so MQA is the standard choice for production-deployed [[Transformer]] decoders.

## Where it appears in the wiki

- [[2312.11805-gemini]] — Gemini 1.0 uses MQA for "efficient attention mechanisms" at 32K context.
- Implicitly assumed by every 2026 paper that depends on a Gemini-class or Llama-class base model. Modern models also use **Grouped-Query Attention (GQA)** — an interpolation between full multi-head and MQA, sharing K/V across groups of heads.

## Trade-off

- **Saves:** ~h× KV cache memory; commensurate decode-time bandwidth.
- **Costs:** small quality regression vs. full multi-head; partly recovered by GQA.

The Gemini paper does not quantify the quality cost; it only reports MQA as one of several inference-time optimizations stacked on the Transformer decoder backbone.
