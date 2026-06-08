---
title: "Little's Law"
type: concept
tags: [serving, queuing-theory, capacity-planning, mlsysbook]
sources: [mlsysbook-ch13-model-serving]
last_updated: 2026-06-05
---

# Little's Law

$$N_{\text{req}} = \lambda \cdot T_{\text{lat}}$$

The most celebrated result in [[QueuingTheory|queuing theory]]: the average number of requests in a stable system equals the arrival rate (λ) times the average time each spends in the system ($T_{\text{lat}}$). John D. C. Little proved (1961) it holds for **any** stable system — regardless of arrival distribution, service-time distribution, or scheduling discipline — the only requirement being stability (λ < μ) ([[mlsysbook-ch13-model-serving|mlsysbook Ch 13]]).

For serving it sets a **hard memory floor**: 1,000 QPS at a 50 ms SLO ⇒ 50 concurrent request slots must fit in RAM for batch + queue activation state. If the GPU OOMs at batch 32, the system *physically cannot* hit 1,000 QPS at 50 ms — the only options are to reduce latency or add memory. Conversely, capping concurrency at 10 with 10 ms service time limits throughput to 1,000 req/s. When stability breaks (λ ≥ μ), no optimization prevents the queue diverging — latency $T_{\text{lat}}$ must grow with queue depth $N_{\text{req}}$ because service rate μ is maxed out.

## Connections

- [[QueuingTheory]] — the broader framework; M/M/1 adds the utilization-latency curve.
- [[CapacityPlanning]] — Little's Law is step one in sizing GPU fleets.
- [[LatencyBudget]] / [[DynamicBatching]] — explains why latency spikes under overload (queue growth, not slower inference).
- [[AdmissionControl]] — rejecting requests is the only way to hold $T_{\text{lat}}$ when λ exceeds μ.
- [[mlsysbook-ch13-model-serving]] — source.
