---
title: "Value Projection Matrix"
type: concept
tags: [attention, transformer]
sources: [hands-on-llm-ch03-looking-inside-llms]
last_updated: 2026-05-23
---

# Value Projection Matrix

One of the three learned projection matrices that produce the components of [[selfattention|self-attention]]. The value projection $W^V$ multiplies each input token's vector to produce its **value vector** — used in the second step of attention, where value vectors are combined according to relevance scores.

## Role in attention

> "Now that we have the relevance scores, we multiply the value vector associated with each token by that token's score. Summing up those resulting vectors produces the output of this attention step." — [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]]

The value vectors carry the **content** to be passed forward, while [[QueryProjection|queries]] and [[KeyProjection|keys]] determine the **routing weights**.

## Sharing across heads

In [[multiqueryattention|multi-query attention]] the value projection is **shared across all heads**. In [[GroupedQueryAttention|grouped-query attention]] it is **shared within groups**. Together with key sharing, this is what gives MQA/GQA their inference-time savings.

## In code

Visible in [[Phi3Mini|Phi-3-mini]]'s PyTorch module print-out (Ch 3) as part of the fused `qkv_proj: Linear(3072 → 9216)`.

## See also

- [[QueryProjection]] / [[KeyProjection]] — the other two projection matrices.
- [[selfattention]] / [[multiheadattention]] / [[scaleddotproductattention]] — the operations.
- [[multiqueryattention]] / [[GroupedQueryAttention]] — variants that share values.
- [[KVCache]] — the caching mechanism that stores per-position values for reuse during decoding.
- [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]] — primary source.
