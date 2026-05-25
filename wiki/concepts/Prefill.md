---
title: "Prefill"
type: concept
tags: [inference, transformer, kv-cache]
sources: [ai-engineering-ch02-foundation-models, ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

# Prefill

The **first phase of transformer-LM inference**: the model processes all input tokens in parallel, producing the intermediate state — including the key and value vectors for every input token — needed to generate the first output token. Per [[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]], prefill is *the parallelizable phase* of LLM inference, in contrast to [[Decode|decode]] which is sequential.

## Why it's parallel

Transformer self-attention computes K, V, Q for all input tokens at once, with no token-to-token sequential dependency. The model can saturate GPU compute during prefill because there's no waiting for earlier tokens to finish.

## What gets stored

The output of prefill includes:
- The **K and V vectors for every input token** (the basis of the [[KVCache|KV cache]]).
- The first output token's logits.

## Why context-length is expensive for transformers

Because each input token contributes a K-vector and a V-vector that must be retained for the rest of the generation, longer prompts use more memory. Per Ch 2:

> "Because each previous token has a corresponding key and value vector, the longer the sequence, the more key and value vectors need to be computed and stored. This is one reason why it's so hard to extend context length for transformer models."

## Inference cost asymmetry

Prefill is **compute-bound** (parallel matrix multiplications); [[Decode|decode]] is **memory-bound** (one token at a time, reading the entire KV cache per step). Inference-optimization techniques therefore target the two phases differently — discussed in Chapter 9 of the book.

## Connections
- [[Decode]] — the sequential second phase.
- [[KVCache]] — the artifact prefill produces.
- [[transformer|Transformer]] — the architecture this phase belongs to.
- [[Attention]] / [[multiheadattention]] — what's computed in parallel during prefill.
- [[InferenceOptimization]] — the engineering response.
- [[ai-engineering-ch02-foundation-models]] — primary source.
- [[TTFT]] — the latency metric prefill dominates (time-to-first-token).

## From [[ai-engineering-ch09-inference-optimization|AI Engineering Ch 9]]

Ch 9 confirms and operationalizes the asymmetry: **prefill is [[ComputeBound|compute-bound]]**, decode is [[MemoryBandwidthBound|memory-bandwidth-bound]]. This single fact justifies:

### Prefill-decode disaggregation

> *"One common optimization technique for inference servers is to disaggregate prefill and decode."* — Ch 9

[[DistServe]] (Zhong et al. 2024) shows assigning prefill and decode to **different GPUs** significantly improves goodput. See [[PrefillDecodeDisaggregation]] for the deep-dive.

**Prefill : decode instance ratio** depends on workload:
- Long inputs, TTFT priority → 2:1 to 4:1.
- Short inputs, TPOT priority → 1:2 to 1:1.

### Anyscale's 100:1 ratio

> *"An experiment by Anyscale shows that 100 input tokens have approximately the same impact on the overall latency as a single output token."* — Ch 9 footnote (Kadous et al. 2023)

This puts a number on the prefill/decode latency asymmetry: even though prefill is compute-bound (and thus parallelizable), 100 input tokens still cost roughly **one** decode-step's latency.

### Prefill MFU > Decode MFU

Because prefill is compute-bound, [[MFU]] during prefill is typically higher than MFU during decode. The same hardware utilization gap that makes decode bandwidth-limited makes prefill compute-limited — orthogonal regimes.

### Prompt caching skips prefill

[[PromptCaching|Prompt caching]] (Gim et al. 2023) — for cache-hit prompts, the entire prefill stage is replaced with a cache lookup. Anthropic numbers: 100K-token cached prompt → **TTFT drops 79% (11.5s → 2.4s)**.
