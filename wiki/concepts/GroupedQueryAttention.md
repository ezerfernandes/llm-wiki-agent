---
title: "Grouped-Query Attention (GQA)"
type: concept
tags: [attention, architecture, inference-efficiency, kv-cache]
sources: [hands-on-llm-ch03-looking-inside-llms, ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

# Grouped-Query Attention (GQA)

An attention variant that **interpolates between full [[multiheadattention|multi-head attention]] and [[multiqueryattention|multi-query attention (MQA)]]** by sharing key and value matrices **within groups of attention heads** instead of across all heads. Introduced by Ainslie et al. in *"GQA: Training generalized multi-query transformer models from multi-head checkpoints"*. Used by [[Llama|Llama 2]] and [[Llama|Llama 3]].

## Mechanism

In standard multi-head attention each head has its own Q, K, and V projection matrices. MQA cuts this to one K and one V matrix shared across all heads (only Q stays per-head). **GQA partitions the heads into groups**, and within each group all heads share a single K and V matrix while keeping per-head Q.

Conceptually:
- **Multi-head**: `g = h` groups (each head is its own group).
- **MQA**: `g = 1` group (all heads share K/V).
- **GQA**: `1 < g < h` (the intermediate regime).

## Why it exists

> "As model sizes grow ... [MQA] can be too punishing and we can afford to use a little more memory to improve the quality of the models. This is where grouped-query attention comes in. Instead of cutting the number of keys and values matrices to one of each, it allows us to use more (but less than the number of heads)." — [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]]

The motivation: MQA's quality regression is acceptable for moderate-size models but compounds as model size grows. GQA recovers most of the quality at a modest memory cost vs MQA.

## Where it appears in the wiki

- **[[Llama|Llama 2]]** and **[[Llama|Llama 3]]** — primary deployment context per *Hands-On LLMs* Ch 3.
- [[multiqueryattention|Multi-query attention]] — the MQA endpoint GQA generalizes from.
- [[multiheadattention|Multi-head attention]] — the original endpoint GQA generalizes from.

## See also

- [[multiqueryattention]] — the `g = 1` limit.
- [[multiheadattention]] — the `g = h` limit.
- [[KVCache]] — the inference-time concern GQA optimizes.
- [[FlashAttention]] — the orthogonal IO-side optimization.
- [[transformer]] — the architecture.
- [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]] — primary source.

## From [[ai-engineering-ch09-inference-optimization|AI Engineering Ch 9]]

Ch 9 frames GQA explicitly as a **generalization of [[multiqueryattention|multi-query attention]]**:

> *"Grouped-query attention (Ainslie et al., 2023) is a generalization of multi-query attention. Instead of using only one set of key-value pairs for all query heads, its grouped-query attention puts query heads into smaller groups and shares key-value pairs only among query heads in the same group. This allows for a more flexible balance between the number of query heads and the number of key-value pairs."*

GQA is one of four **attention-mechanism redesigns** Ch 9 names (alongside [[LocalAttention|local windowed attention]], [[CrossLayerAttention|cross-layer attention]], and MQA) — all of which reduce [[KVCache|KV-cache]] memory by sharing K/V across some axis (heads, groups of heads, layers, or sequence positions). All require **architectural change**, applied during training or finetuning, not as a drop-in inference modification.
