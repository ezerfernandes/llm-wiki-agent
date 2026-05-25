---
title: "Memory Bandwidth-Bound"
type: concept
tags: [inference, performance, hardware, roofline]
sources: [ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

# Memory Bandwidth-Bound

A **workload whose time-to-complete is determined by the rate at which data can be moved between memory and compute units**, not by arithmetic. Per [[ai-engineering-ch09-inference-optimization|*AI Engineering* Ch 9]], this is one of two basic bottleneck regimes (the other being [[ComputeBound|compute-bound]]). Memory bandwidth-bound is the **dominant regime for autoregressive LLM [[Decode|decode]]** and is what makes most of Ch 9's optimization machinery necessary.

## Terminology ambiguity (Huyen flags it)

> *"Memory-bound is also used by some people to refer to tasks whose time-to-complete is constrained by memory capacity instead of memory bandwidth."* — Ch 9

Huyen's anecdotal split: **systems/optimization engineers** use *memory-bound* → bandwidth; **AI/ML engineers** use *memory-bound* → capacity (OOM errors). The original Roofline paper (Williams et al. 2009) means bandwidth. Ch 9 sometimes shortens to "bandwidth-bound" to disambiguate.

## Why LLM decode is memory bandwidth-bound

Each decode step **loads the entire model weights from HBM** to compute one token. Compute per step is minimal; memory traffic per step is enormous. From Ch 9 footnote 19:

> *"Each token generation step necessitates the transfer of the entire model's parameters from the accelerator's high-bandwidth memory to its compute units. This makes this operation bandwidth-heavy. Because the model can produce only one token at a time, the process consumes only a small number of FLOP/s, resulting in computational inefficiency."*

This single fact is why so many of Ch 9's techniques target the KV cache, the decoding loop, or quantization (which reduces bytes moved per parameter).

## How to speed up memory-bandwidth-bound workloads

> *"A memory bandwidth-bound workload might be sped up by leveraging chips with higher bandwidth."* — Ch 9

Other levers from Ch 9:
- **[[Quantization]]** — fewer bytes per parameter → less bandwidth per step (the page literally says: *"Fewer bytes per parameter mean your model consumes less valuable bandwidth"*).
- **[[KVCache]] optimizations** — shrink the cache so each step touches less memory ([[multiqueryattention|MQA]], [[GroupedQueryAttention|GQA]], [[CrossLayerAttention]], [[PagedAttention]]).
- **[[SpeculativeDecoding|Speculative decoding]]** — convert sequential decode into prefill-shaped batches that *use* the otherwise-idle FLOPs.
- **[[FlashAttention]]** — restructure attention to minimize HBM ↔ SRAM traffic.

## The MBU diagnostic

A memory-bandwidth-bound workload typically achieves **high [[MBU]]** (Model Bandwidth Utilization) and **low [[MFU]]**. If your MFU is low and MBU is high, your inference is bandwidth-bound — adding more FLOPs won't help; you need higher-bandwidth memory or less bandwidth pressure per op.

## Connections

- [[ComputeBound]] — opposite regime.
- [[ArithmeticIntensity]] — the classifier.
- [[RooflineModel]] — Williams et al. 2009.
- [[Decode]] — the memory-bandwidth-bound phase of LLM inference.
- [[KVCache]] — the structure whose growth drives the bandwidth pressure.
- [[MFU]] / [[MBU]] — diagnostic metrics.
- [[Quantization]] / [[FlashAttention]] / [[SpeculativeDecoding]] — techniques for relieving the bottleneck.
- [[HBM]] / [[SRAM]] — the memory hierarchy whose bandwidth limits matter.
- [[InferenceOptimization]] — broader discipline.
- [[ai-engineering-ch09-inference-optimization]] — primary source.
