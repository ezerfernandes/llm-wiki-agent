---
title: "PagedAttention"
type: concept
tags: [llm-engineering, inference, attention, kv-cache]
sources: [leh-ch08-inference-optimization, ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

## Definition
OS-paging-inspired block KV cache (Kwon et al. 2023, vLLM).

## In LLM Engineer's Handbook
PagedAttention (Kwon et al. 2023) partitions the [[KVCache]] into fixed-size pages, each holding K/V of a constant number of tokens. A custom kernel fetches pages regardless of physical location. Per [[leh-ch08-inference-optimization]] this eliminates internal fragmentation, enables memory sharing across sequences from the same prompt, and yields ~55% memory savings and ~2.2x throughput. First implemented in [[vLLM]]; adopted by [[TGI]] and [[TensorRTLLM]].

## From [[ai-engineering-ch09-inference-optimization|AI Engineering Ch 9]]

> *"One of the fastest growing inference frameworks, vLLM, gained popularity for introducing PagedAttention, which optimizes memory management by dividing the KV cache into non-contiguous blocks, reducing fragmentation, and enabling flexible memory sharing to improve LLM serving efficiency (Kwon et al., 2023)."*

Ch 9 places PagedAttention in its **"optimize the KV cache"** bucket — one of three attention-mechanism-optimization buckets, alongside *redesign the attention mechanism* (MQA/GQA/cross-layer attention) and *write kernels for attention computation* ([[FlashAttention]]).

### Sibling KV-cache techniques mentioned in Ch 9

- **KV-cache quantization** (Hooper et al. 2024; Kang et al. 2024) — reduce precision of cache contents.
- **Adaptive KV-cache compression** (Ge et al. 2023).
- **Selective KV cache** (Liu et al. 2024) — store only the most relevant K/V pairs.

PagedAttention is the most mainstream of these as of late 2024 — it's what powers vLLM's leading inference throughput numbers.
