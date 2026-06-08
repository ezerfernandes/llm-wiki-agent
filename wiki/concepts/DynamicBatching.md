---
title: "Dynamic Batching"
type: concept
tags: [inference, serving, batching, latency, mlsysbook]
sources: [ai-engineering-ch09-inference-optimization, mlsysbook-ch13-model-serving]
last_updated: 2026-06-05
---

# Dynamic Batching

**A [[Batching|batching]] strategy that processes a batch when *either* the configured size N is reached *or* a time-window T elapses — whichever happens first.** Per [[ai-engineering-ch09-inference-optimization|*AI Engineering* Ch 9]]:

> *"Dynamic batching, on the other hand, sets a maximum time window for each batch. If the batch size is four and the window is 100 ms, the server processes the batch either when it has four requests or when 100 ms has passed, whichever happens first. It's like a bus that leaves on a fixed schedule or when it's full. This approach keeps latency under control, so earlier requests aren't held up by later ones."*

## Trade-off vs [[StaticBatching|static batching]]

- **Wins:** bounded worst-case TTFT (≤ T even on empty queue) — no more "first request held hostage by the last."
- **Loses:** batches may be processed before they're full, wasting compute slots. "The downside is that batches may not always be full when processed, possibly leading to wasted compute."

## Trade-off vs [[ContinuousBatching|continuous batching]]

- **Wins:** simpler to implement; doesn't require sophisticated KV-cache management.
- **Loses:** still suffers from the **head-of-line-blocking** problem for LLM workloads — once a batch starts, short responses wait for the long one to finish before being returned.

## When dynamic batching is the right choice

- **Vision / classification / embedding APIs** where every request takes roughly the same time → head-of-line blocking is mild.
- **Workloads where implementation simplicity outweighs the head-of-line cost** → mature dynamic-batching libraries exist for almost every serving stack.

For LLM autoregressive workloads in 2024, [[ContinuousBatching|continuous batching]] is preferred.

## Connections

- [[Batching]] — umbrella concept.
- [[StaticBatching]] — the simpler precursor.
- [[ContinuousBatching]] — the LLM-grade successor.
- [[TTFT]] — the latency metric dynamic batching keeps bounded.
- [[Goodput]] — the optimization target.
- [[InferenceOptimization]] — broader discipline.
- [[ai-engineering-ch09-inference-optimization]] — primary source.

## From [[mlsysbook-ch13-model-serving|mlsysbook Ch 13]]

Ch 13 quantifies the **latency-throughput Pareto frontier** and the **"batching tax."** Total batched latency ≈ formation delay $(B-1)/(2\lambda)$ + inference $T_{\text{inf}}(B)$; average batching-window wait = window/2. ResNet-50/V100 sweep: batch-1 = 200 img/s @ 15% util; batch-32 = 1,280 img/s @ 95% util (**6.4× throughput**) but inference stretches 5 ms→25 ms — the "knee" past which throughput saturates while latency spikes. Batch sizes follow a Poisson distribution (mean λ·window), so p99 latency exceeds the mean. Counterintuitively, **as traffic rises the optimal window shrinks while batch size grows** (law of large numbers). Typical config: 5–50 ms windows, max batch 8–32; allocate ~30% of the SLO to batching wait. The scheduler is the [[InferenceServer|inference server]]'s "brain" tuning this. See also [[QueuingTheory]], [[LatencyBudget]], [[mlsysbook-ch13-model-serving]].
