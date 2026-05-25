---
title: "Cross-Layer Attention"
type: concept
tags: [attention, architecture, inference-efficiency, kv-cache]
sources: [ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

# Cross-Layer Attention

An **attention-mechanism redesign that shares key and value vectors across adjacent transformer layers**, reducing the [[KVCache|KV cache]] memory footprint proportionally to the number of layers sharing K/V. Introduced by Brandon et al. (2024); covered in [[ai-engineering-ch09-inference-optimization|*AI Engineering* Ch 9]].

## How it works

> *"Cross-layer attention shares key and value vectors across adjacent layers. Having three layers sharing the same key-value vectors means reducing the KV cache three times."* — Ch 9

If `L` layers are grouped into `G` cross-layer-sharing groups of size `L/G`, the KV cache shrinks by a factor of `L/G`.

## Position in the attention-optimization family

Cross-layer attention is the **layer-side** analog of [[multiqueryattention|MQA]] / [[GroupedQueryAttention|GQA]], which are the **head-side** versions of the same idea:

| Optimization | Shares K/V across | KV-cache reduction |
|---|---|---|
| **[[multiqueryattention|MQA]]** | All query heads | ÷ number of heads |
| **[[GroupedQueryAttention|GQA]]** | Heads within a group | ÷ heads per group |
| **Cross-layer attention** | Adjacent layers | ÷ layers per group |

All three can be stacked.

## CharacterAI stack

[[CharacterAI]] reported (2024) combining:

1. **[[multiqueryattention|Multi-query attention]]**
2. **Interleaved local + global attention** ([[LocalAttention]])
3. **Cross-layer attention**

…to **reduce KV cache by > 20×**. With an average conversation of **180 messages**, this removed memory as a bottleneck for serving large batch sizes.

## Modification level

Cross-layer attention **changes the model architecture** and must therefore be applied during training or finetuning — not as a drop-in inference optimization on existing weights. Same caveat as MQA / GQA.

## Connections

- [[multiqueryattention]] / [[GroupedQueryAttention]] — head-side analogs.
- [[LocalAttention]] — orthogonal context-side optimization (cuts effective seq length).
- [[KVCache]] — the memory structure cross-layer attention shrinks.
- [[CharacterAI]] — the case study using cross-layer + MQA + local attention to cut KV cache > 20×.
- [[Attention]] — the mechanism being modified.
- [[PagedAttention]] / [[FlashAttention]] — orthogonal KV-side / kernel-side optimizations.
- [[InferenceOptimization]] — broader discipline.
- [[ai-engineering-ch09-inference-optimization]] — primary source.
