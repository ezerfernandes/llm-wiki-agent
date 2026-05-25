---
title: "Key Projection Matrix"
type: concept
tags: [attention, transformer]
sources: [hands-on-llm-ch03-looking-inside-llms]
last_updated: 2026-05-23
---

# Key Projection Matrix

One of the three learned projection matrices that produce the components of [[selfattention|self-attention]]. The key projection $W^K$ multiplies each input token's vector to produce its **key vector** — used in the relevance-scoring step of attention, where every previous token's key is matched against the current position's [[QueryProjection|query]].

## Role in attention

> "The relevance scoring step of attention is conducted by multiplying the query vector of the current position with the keys matrix. This produces a score stating how relevant each previous token is. Passing that by a softmax operation normalizes these scores so they sum up to 1." — [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]]

## Sharing across heads

In [[multiqueryattention|multi-query attention]] the key projection is **shared across all heads** (one $W^K$ per layer rather than one per head). In [[GroupedQueryAttention|grouped-query attention]] it is **shared within groups of heads**. This sharing is what shrinks the [[KVCache|KV cache]] and the attention compute for large models.

## In code

Visible in [[Phi3Mini|Phi-3-mini]]'s PyTorch module print-out (Ch 3) as part of the fused `qkv_proj: Linear(3072 → 9216)`.

## See also

- [[QueryProjection]] / [[ValueProjection]] — the other two projection matrices.
- [[selfattention]] / [[multiheadattention]] / [[scaleddotproductattention]] — the operations.
- [[multiqueryattention]] / [[GroupedQueryAttention]] — variants that share keys.
- [[KVCache]] — the caching mechanism that stores per-position keys for reuse during decoding.
- [[RoPE]] — the positional embedding scheme injected into keys before relevance scoring.
- [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]] — primary source.
