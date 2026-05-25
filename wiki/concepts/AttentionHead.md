---
title: "Attention Head"
type: concept
tags: [attention, transformer]
sources: [hands-on-llm-ch03-looking-inside-llms]
last_updated: 2026-05-23
---

# Attention Head

One parallel attention computation within a [[multiheadattention|multi-head attention]] layer. Each head has its own [[QueryProjection|Q]], [[KeyProjection|K]], and [[ValueProjection|V]] projection matrices and performs the full two-step attention computation (relevance scoring + combining information) over the input independently. The outputs of all heads in a layer are combined to produce the layer's output.

## Why multiple heads

> "To give the Transformer more extensive attention capability, the attention mechanism is duplicated and executed multiple times in parallel. Each of these parallel applications of attention is conducted into an attention head. This increases the model's capacity to model complex patterns in the input sequence that require paying attention to different patterns at once." — [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]]

Different heads specialize: some track long-range dependencies, some perform anaphora resolution, some align with syntactic structure (see [[multiheadattention|MultiHeadAttention page]] for the original Vaswani et al. ablations).

## Q/K/V sharing variants

- **[[multiheadattention|Multi-head attention]]**: each head has its own Q, K, V projections.
- **[[multiqueryattention|Multi-query attention]]**: each head has its own Q, but K and V are shared across all heads.
- **[[GroupedQueryAttention|Grouped-query attention]]**: heads are partitioned into groups; within each group all heads share K and V.

## See also

- [[multiheadattention]] — the layer composed of many attention heads.
- [[multiqueryattention]] / [[GroupedQueryAttention]] — head-side sharing variants.
- [[selfattention]] / [[scaleddotproductattention]] — what each head computes.
- [[QueryProjection]] / [[KeyProjection]] / [[ValueProjection]] — the per-head learned matrices.
- [[hands-on-llm-ch03-looking-inside-llms|*Hands-On LLMs* Ch 3]] — primary source.
