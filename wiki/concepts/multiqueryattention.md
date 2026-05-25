---
title: "Multi-Query Attention"
type: concept
tags: [attention, architecture, inference-efficiency]
sources: [2312.11805-gemini, hands-on-llm-ch03-looking-inside-llms, ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
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

## From [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]]

Ch 3 frames MQA against multi-head as a head-side efficiency tweak:

> "The way that multi-query attention optimizes [multi-head attention] is to share the keys and values matrices between all the heads. So the only unique matrices for each head would be the queries matrices." — Ch 3

And contextualizes the trade-off vs. GQA:

> "As model sizes grow, however, this optimization can be too punishing and we can afford to use a little more memory to improve the quality of the models. This is where grouped-query attention comes in. Instead of cutting the number of keys and values matrices to one of each, it allows us to use more (but less than the number of heads)." — Ch 3

Original-paper citation: [[NoamShazeer|Shazeer]] (2019) *"Fast transformer decoding: One write-head is all you need."*

## See also
- [[GroupedQueryAttention]] — the modern interpolation between MQA and multi-head, used by [[Llama|Llama 2]] / [[Llama|Llama 3]].
- [[NoamShazeer]] — the MQA paper author.
- [[multiheadattention]] — the original-Transformer attention MQA optimizes.
- [[KVCache]] — the inference-time memory consumer MQA shrinks.
- [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]] — secondary source.

## From [[ai-engineering-ch09-inference-optimization|AI Engineering Ch 9]]

Ch 9 places MQA in its **"redesign the attention mechanism"** bucket alongside [[LocalAttention|local windowed attention]] (Longformer, Beltagy et al. 2020), [[CrossLayerAttention|cross-layer attention]] (Brandon et al. 2024), and [[GroupedQueryAttention|grouped-query attention]] (Ainslie et al. 2023). These techniques **change the model architecture** and must be applied during training or finetuning.

### CharacterAI's > 20× KV-cache reduction stack

[[CharacterAI]] (2024) — average conversation has **180 messages**. Their stack:

1. **Multi-query attention** (head-side K/V sharing).
2. **Interleaved local + global attention** (context-side reduction).
3. **[[CrossLayerAttention|Cross-layer attention]]** (layer-side K/V sharing).

**Combined effect: > 20× KV-cache reduction**, removing memory as a bottleneck for serving large batches.

This combination is a useful template for any team facing KV-cache memory pressure at long context lengths.
