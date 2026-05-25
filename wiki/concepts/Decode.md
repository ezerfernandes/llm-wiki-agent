---
title: "Decode"
type: concept
tags: [inference, transformer, autoregressive]
sources: [ai-engineering-ch02-foundation-models, ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

# Decode

The **second phase of transformer-LM inference**: the model generates one output token at a time, with each token conditioned on all previous tokens (both the input and previously generated tokens). Per [[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]], decode is *the sequential phase* of LLM inference — even though transformers eliminated the input-side sequential bottleneck via attention, **transformer-based autoregressive language models still have the sequential output bottleneck**.

## Why it's sequential

To generate token N, the model needs token N-1 — which is itself a sample from the previous step's softmax. No amount of compute parallelism can collapse this dependency chain.

## Memory-bound nature

Each decode step reads the entire [[KVCache|KV cache]] (one K, V vector per token so far), runs a relatively small amount of compute, then writes one new K, V pair. On modern GPUs the bottleneck is memory bandwidth, not compute — opposite of [[Prefill|prefill]].

## Inference latency implication

[[Decode]] is what makes generation latency scale with output length. From [[ai-engineering-ch01-intro|Ch 1]]: 10ms/token × 100 tokens = 1 second — far above the 100ms latency users expect of typical web apps. The latency metric specifically tied to decode is [[TPOT]] (time-per-output-token).

## Why this motivates inference optimization

Per Ch 2:

> "The parallelizable nature of prefilling and the sequential aspect of decoding both motivate many optimization techniques to make language model inference cheaper and faster."

Examples (covered in Ch 9 of the book): paged attention, continuous batching, speculative decoding, MQA / GQA ([[multiqueryattention]]), quantization for memory bandwidth, etc.

## Connections
- [[Prefill]] — the parallel first phase.
- [[KVCache]] — what gets read on every decode step.
- [[AutoregressiveLanguageModel]] — the model class whose sampling drives this phase.
- [[transformer|Transformer]] — the architecture.
- [[InferenceOptimization]] — the engineering response.
- [[TPOT]] — the latency metric decode dominates.
- [[ai-engineering-ch02-foundation-models]] — primary source.

## From [[ai-engineering-ch09-inference-optimization|AI Engineering Ch 9]]

Ch 9 makes the **[[MemoryBandwidthBound|memory-bandwidth-bound]]** framing the centerpiece of the chapter:

### Why decode is bandwidth-bound

> *"Each token generation step necessitates the transfer of the entire model's parameters from the accelerator's high-bandwidth memory to its compute units. This makes this operation bandwidth-heavy. Because the model can produce only one token at a time, the process consumes only a small number of FLOP/s, resulting in computational inefficiency."* — Ch 9 footnote

**One decode step = the entire model loaded from HBM, used to produce one token.** Arithmetic intensity is low; bandwidth saturates first.

### Output-token cost asymmetry

> *"Across model API providers, an output token costs approximately two to four times an input token."* — Ch 9

This is the cost shadow of prefill (parallel, compute-bound) vs decode (sequential, bandwidth-bound).

### Anyscale's 100:1 number

> *"In an experiment, Anyscale found that a single output token can have the same impact on latency as 100 input tokens (Kadous et al., 2023)."*

Improving the autoregressive decoding process by **a small percentage** can therefore yield outsized user-experience gains — which is why so much of Ch 9 attacks decoding.

### Attacks on the decoding bottleneck

Ch 9 names three families:
1. **[[SpeculativeDecoding]]** — draft model proposes K tokens; target verifies in parallel. Chinchilla-70B: > 50% latency cut.
2. **[[InferenceWithReference]]** — draft tokens come from input context. 2× speedup on RAG/code/multi-turn.
3. **[[ParallelDecoding]]** — break sequential dependency; [[LookaheadDecoding]] (Jacobi) and [[MedusaDecoding|Medusa]] (multi-head + tree attention).

Plus orthogonal levers: [[Quantization]] (fewer bytes per step), [[KVCache]] optimization ([[multiqueryattention|MQA]] / [[GroupedQueryAttention|GQA]] / [[PagedAttention]]), [[FlashAttention]] (fused kernel).

### Decode MFU < Prefill MFU

> *"For inference, since prefill is compute-bound and decode is memory bandwidth-bound, MFU during prefilling is typically higher than MFU during decoding."* — Ch 9
