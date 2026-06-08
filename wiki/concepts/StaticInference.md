---
title: "Static Inference"
type: concept
tags: [serving, inference, batch, mlsysbook]
sources: [mlsysbook-ch13-model-serving]
last_updated: 2026-06-05
---

# Static Inference

Also called **offline or batch inference**: predictions are **precomputed for anticipated inputs and stored for retrieval** ([[mlsysbook-ch13-model-serving|mlsysbook Ch 13]]). Example: a recommender that scores all user-item pairs nightly, then serves recommendations from a lookup table rather than running inference at request time.

This moves compute out of the request path, enables offline quality checks, and can reduce serving cost for *predictable* inputs — but needs a fallback online path (or a refreshed batch run) when requests include unanticipated inputs or a model update. Most production systems are **hybrid**: cache popular precomputed results (static), dynamic-serve the novel tail. Static inference optimizes for throughput during the batch run and storage efficiency for serving. This is the same axis [[BatchInference]] frames in earlier wiki sources, reframed by the serving-vs-precompute decision.

## Connections

- [[DynamicInference]] — the on-demand counterpart; the first architectural choice in any serving system.
- [[BatchInference]] / [[OnlineInference]] — the prior-source framing of the same axis.
- [[CostPerInference]] — static precompute can cut serving cost for predictable inputs.
- [[ModelServing]] — the practice.
- [[mlsysbook-ch13-model-serving]] — source.
