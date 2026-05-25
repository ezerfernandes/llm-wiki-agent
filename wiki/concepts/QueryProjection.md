---
title: "Query Projection Matrix"
type: concept
tags: [attention, transformer]
sources: [hands-on-llm-ch03-looking-inside-llms]
last_updated: 2026-05-23
---

# Query Projection Matrix

One of the three learned projection matrices that produce the components of [[selfattention|self-attention]]. The query projection $W^Q$ multiplies an input token's vector to produce its **query vector** — used in the relevance-scoring step of attention.

## Role in attention

> "Attention starts by multiplying the inputs by the projection matrices to create three new matrices. These are called the queries, keys, and values matrices. These matrices contain the information of the input tokens projected to three different spaces." — [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]]

The current position's query vector is multiplied against the keys matrix (containing every previous token's [[KeyProjection|key vector]]) to score how relevant each previous token is to the current position. The scores are softmax-normalized and used to combine [[ValueProjection|value vectors]] into the final attention output.

## In multi-head attention

In multi-head attention, **every head has its own query projection matrix**. In [[multiqueryattention|multi-query attention (MQA)]] and [[GroupedQueryAttention|grouped-query attention (GQA)]], queries remain per-head while keys and values are shared (across all heads in MQA, within groups in GQA).

## In code

Visible in [[Phi3Mini|Phi-3-mini]]'s PyTorch module print-out (Ch 3) as `qkv_proj: Linear(3072 → 9216)` — a fused projection producing the Q, K, V concatenation in one matmul (3072 × 3 = 9216).

## See also

- [[KeyProjection]] / [[ValueProjection]] — the other two projection matrices.
- [[selfattention]] / [[multiheadattention]] / [[scaleddotproductattention]] — the operations these projections serve.
- [[multiqueryattention]] / [[GroupedQueryAttention]] — variants that share K/V but keep per-head queries.
- [[RoPE]] — the positional embedding scheme injected into queries (and keys) before relevance scoring.
- [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]] — primary source.
