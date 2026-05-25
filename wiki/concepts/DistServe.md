---
title: "DistServe"
type: concept
tags: [inference, serving, gpu, paper, llm-engineering]
sources: [ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

# DistServe

**Zhong et al. (2024) — the paper that establishes [[PrefillDecodeDisaggregation|prefill-decode disaggregation]] as a production serving optimization.** Cited in [[ai-engineering-ch09-inference-optimization|*AI Engineering* Ch 9]]:

> *"'DistServe' (Zhong et al., 2024) and 'Inference Without Interference' (Hu et al., 2024) show that for various popular LLMs and applications, assigning prefill and decode operations to different instances (e.g., different GPUs) can significantly improve the volume of processed requests while adhering to latency requirements."*

## Core claim

Colocated prefill+decode causes destructive resource contention on a single GPU:
- **Prefill** is [[ComputeBound|compute-bound]] — wants FLOPs.
- **[[Decode|Decode]]** is [[MemoryBandwidthBound|memory-bandwidth-bound]] — wants HBM bandwidth.

A new request's prefill can drain compute from in-flight decode jobs, hurting their TPOT. Routing prefill and decode to *separate* GPU pools eliminates this interference.

## Key empirical finding

Disaggregation **significantly improves the volume of processed requests adhering to latency requirements** (i.e. goodput) — and the inter-instance communication overhead is acceptable on modern fabrics with NVLink-class interconnects.

## Sibling work

**Inference Without Interference** (Hu et al. 2024) — reports the same conclusion from a different angle: that co-located prefill jobs introduce unpredictable latency spikes for decode-only queues.

## Connections

- [[PrefillDecodeDisaggregation]] — the technique DistServe established.
- [[Prefill]] / [[Decode]] — the two phases.
- [[ComputeBound]] / [[MemoryBandwidthBound]] — the regime asymmetry.
- [[NVLink]] — the interconnect that makes disaggregation practical.
- [[Goodput]] — the metric the paper improves.
- [[ContinuousBatching]] — complementary serving-side optimization.
- [[ai-engineering-ch09-inference-optimization]] — primary source.
