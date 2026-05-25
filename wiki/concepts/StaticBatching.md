---
title: "Static Batching"
type: concept
tags: [inference, serving, batching, latency]
sources: [ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

# Static Batching

**The simplest [[Batching|batching]] strategy: wait until exactly N requests have arrived, then process the batch.** Per [[ai-engineering-ch09-inference-optimization|*AI Engineering* Ch 9]]:

> *"The simplest batching technique is static batching. The service groups a fixed number of inputs together in a batch. It's like a bus that waits until every seat is filled before departing."*

## The fatal flaw

> *"The drawback of static batching is that all requests have to wait until the batch is full to be executed. Thus the first request in a batch is delayed until the batch's last request arrives, no matter how late the last request is."* — Ch 9

For workloads with bursty or low-volume traffic, **the first request's TTFT can be unboundedly bad** — it waits for N-1 more requests to arrive.

## When it might still make sense

- **Offline batch APIs** — where latency is irrelevant; cost matters; e.g. nightly summarization, document reprocessing. These match Ch 9's discussion of [[BatchInference|batch APIs]] (Google/OpenAI offer batch APIs at ~50% discount with hours-to-days turnaround).
- **Highly homogeneous workloads** — when request arrival is so dense that the batch fills almost immediately anyway.

## Why [[DynamicBatching|dynamic batching]] is the upgrade

Dynamic batching keeps the same batching benefit but caps the worst-case wait with a time-window. Continuous batching goes further, eliminating batch-formation waits entirely.

## Connections

- [[Batching]] — the umbrella concept.
- [[DynamicBatching]] — the upgrade.
- [[ContinuousBatching]] — the gold standard.
- [[BatchInference]] — offline-mode API where static batching could conceivably apply.
- [[Goodput]] — what static batching's first-request latency destroys.
- [[InferenceOptimization]] — broader discipline.
- [[ai-engineering-ch09-inference-optimization]] — primary source.
