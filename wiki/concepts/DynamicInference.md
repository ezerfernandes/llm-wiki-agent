---
title: "Dynamic Inference"
type: concept
tags: [serving, inference, real-time, mlsysbook]
sources: [mlsysbook-ch13-model-serving]
last_updated: 2026-06-05
---

# Dynamic Inference

Also called **online or real-time inference**: predictions are **computed on demand when requests arrive** ([[mlsysbook-ch13-model-serving|mlsysbook Ch 13]]). This handles any input — rare edge cases, novel combinations — and immediately reflects model updates, at the cost of strict latency requirements that constrain model complexity and demand robust monitoring.

Dynamic inference optimizes for *per-request latency under concurrent load*, which requires understanding where time goes within each request (the [[LatencyBudget|latency budget]]) and how requests queue ([[QueuingTheory|queuing theory]]). Stricter latency directly raises infrastructure cost: the chapter's worked example shows halving latency (batch-8→batch-1) can ~4× the cost per query. The static-vs-dynamic choice is the first architectural decision in any serving system; most production systems combine both.

## Connections

- [[StaticInference]] — the precompute counterpart.
- [[BatchInference]] / [[OnlineInference]] — the prior-source framing of the same axis.
- [[LatencyBudget]] / [[QueuingTheory]] — the analyses dynamic inference requires.
- [[DynamicBatching]] — the throughput lever applied to dynamic request streams.
- [[ModelServing]] — the practice.
- [[mlsysbook-ch13-model-serving]] — source.
