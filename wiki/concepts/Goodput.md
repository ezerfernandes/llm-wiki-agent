---
title: "Goodput"
type: concept
tags: [inference, performance, metrics, slo]
sources: [ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

# Goodput

**Requests per second that satisfy the service-level objective (SLO)** — a metric borrowed from networking to capture *useful* throughput rather than raw throughput. Per [[ai-engineering-ch09-inference-optimization|*AI Engineering* Ch 9]]:

> *"Goodput measures the number of requests per second that satisfies the SLO, software-level objective."*

## Why goodput, not just throughput

Throughput alone is misleading because **batching** (and other throughput-multipliers) can dramatically inflate it while violating per-request latency targets. LinkedIn's AI team reported it's "not uncommon to double or triple throughput if you're willing to sacrifice TTFT and TPOT." A service that doubles throughput but blows past its TTFT SLO has *worse* goodput.

## Worked example (Ch 9)

Setup: SLO of **TTFT ≤ 200 ms ∧ TPOT ≤ 100 ms**. Service completes 100 requests/min, but **only 30 satisfy the SLO**.

→ Throughput = 100 req/min. **Goodput = 30 req/min.**

Figure 9-4 in the book visualizes this as a service completing 10 RPS but with only 3 satisfying the SLO → 3 RPS goodput.

## Choosing goodput as the optimization target

Optimizing throughput-alone leads to bad UX. Optimizing latency-alone leaves throughput on the table. **Goodput is the joint optimum**: maximize throughput *subject to* per-request latency SLOs.

This makes goodput especially relevant for decisions like:
- **Batch size selection** — larger batches raise throughput but worsen per-request latency; goodput peaks somewhere in between.
- **[[PrefillDecodeDisaggregation|Prefill-decode disaggregation]] ratios** — the right ratio is the one that maximizes goodput, not raw RPS.
- **[[ContinuousBatching|Continuous batching]] tuning** — admit-eviction policy should be tuned for goodput.

## Connections

- [[TTFT]] / [[TPOT]] — the latency components that goodput-bounding SLOs are usually expressed in.
- [[InferencePerformanceMetrics]] — broader metrics framework.
- [[ContinuousBatching]] — primary batching technique whose tuning targets goodput.
- [[PrefillDecodeDisaggregation]] — the parameter that affects goodput.
- [[InferenceOptimization]] — broader discipline.
- [[LinkedIn]] — the source of the throughput-vs-latency trade-off claim Ch 9 cites.
- [[ai-engineering-ch09-inference-optimization]] — primary source.
