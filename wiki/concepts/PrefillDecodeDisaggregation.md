---
title: "Prefill-Decode Disaggregation"
type: concept
tags: [inference, serving, optimization, gpu, llm-engineering]
sources: [ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

# Prefill-Decode Disaggregation

**Assigning the [[Prefill|prefill]] and [[Decode|decode]] phases of LLM inference to *different GPU instances*** — because they have opposite computational profiles ([[ComputeBound|compute-bound]] vs [[MemoryBandwidthBound|memory-bandwidth-bound]]) and compete destructively when colocated. Per [[ai-engineering-ch09-inference-optimization|*AI Engineering* Ch 9]]:

> *"Because prefill is compute-bound and decode is memory bandwidth-bound, using the same machine to perform both can cause them to inefficiently compete for resources and significantly slow down both TTFT and TPOT."*

## The interference problem

> *"Imagine a GPU that is already handling prefilling and decoding near its peak computational capacity. It might be able to handle another low computational job like decoding. However, adding a new query to this GPU means introducing a prefilling job along with a decoding job. This one prefilling job can drain computational resources from existing decoding jobs, slowing down TPOT for these requests."* — Ch 9

In other words: a single new request's prefill can degrade the TPOT of *all* in-flight decode requests sharing that GPU.

## Primary references

- **DistServe** (Zhong et al. 2024) — the primary citation; shows disaggregation significantly improves request volume under latency SLOs.
- **Inference Without Interference** (Hu et al. 2024) — corroborating result.

Both papers note that the intermediate-state communication (transferring prefill output to decode instances) is **not substantial on modern GPU clusters with high-bandwidth connections such as [[NVLink]]**.

## Prefill : decode ratio

The right ratio depends on workload and SLO:

| Workload / priority | Recommended ratio |
|---|---|
| Long input sequences, prioritize TTFT | **2:1 to 4:1** (more prefill instances) |
| Short input sequences, prioritize TPOT | **1:2 to 1:1** (more decode instances) |

Cited as discussed in *"Llama Inference at Meta"* (Meta 2024).

## Pairs naturally with

- **[[ContinuousBatching|Continuous batching]]** — decode-side admission/eviction is cleaner without prefill contention.
- **[[PromptCaching|Prompt caching]]** — prompt-cache hits skip prefill entirely; the prefill cluster handles cache misses; decode cluster runs the actual generation.
- **[[TensorParallelism|Tensor parallelism]]** — applied independently within each cluster.

## Cost vs benefit trade-off

Disaggregation adds **machine count** (separate prefill + decode pools instead of one shared pool) and **inter-instance communication overhead**. The papers argue the latency / goodput gains exceed both costs on modern fabrics.

## Connections

- [[Prefill]] / [[Decode]] — the two phases being separated.
- [[ComputeBound]] / [[MemoryBandwidthBound]] — the asymmetric profiles driving the separation.
- [[DistServe]] — the primary citation paper.
- [[TTFT]] / [[TPOT]] — the latency metrics that improve when phases are separated.
- [[Goodput]] — the joint optimization target.
- [[NVLink]] — the high-bandwidth interconnect that makes intermediate-state transfer cheap.
- [[ContinuousBatching]] — pairs naturally on the decode side.
- [[PromptCaching]] — pairs naturally on the prefill side.
- [[InferenceOptimization]] — broader discipline.
- [[ai-engineering-ch09-inference-optimization]] — primary source.
