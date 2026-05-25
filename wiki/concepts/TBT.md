---
title: "TBT (Time Between Tokens) / ITL (Inter-Token Latency)"
type: concept
tags: [latency, metrics, inference, streaming]
sources: [ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

# TBT — Time Between Tokens

**The time between two successive output tokens during streaming generation.** A variant of [[TPOT|TPOT]] focused on *user-visible cadence* during streaming. Per [[ai-engineering-ch09-inference-optimization|*AI Engineering* Ch 9]]:

> *"Variations of this metric include time between tokens (TBT) and inter-token latency (ITL). Both measure the time between output tokens."*

## TBT vs ITL

The book notes that the two names refer to essentially the same quantity:

- **TBT** — used by [[LinkedIn]].
- **ITL** — used by [[NVIDIA]].

The metric matters because streaming UIs (chat apps, code completion) show tokens as they arrive — and **uneven token arrival is more visible to users than a slightly higher average TPOT**. A bursty 50ms/200ms/50ms/200ms cadence feels worse than a steady 100ms cadence even though the *average* is the same.

## Reading speed reference

> *"A very fast reader can read 120 ms/token, so a TPOT of around 120 ms, or 6–8 tokens/second, is sufficient for most use cases."* — Ch 9

In streaming UIs, dropping below this threshold gives diminishing user-experience returns. Above it, you're letting the user wait.

## When TBT differs from TPOT

TBT is essentially TPOT *measured as user-visible cadence during streaming*. They're conceptually similar but TBT emphasizes the **distributional / jitter** view; TPOT emphasizes the **average / steady-state** view. Best practice: report both percentiles (p50, p90, p95, p99) of TBT, since outliers — a single 3-second stall during streaming — destroy UX more than a slightly worse average.

## Connections

- [[TPOT]] — closely related; TBT is the streaming-cadence sibling.
- [[TTFT]] — the startup-cost cousin.
- [[InferencePerformanceMetrics]] — broader metrics framework.
- [[Goodput]] — TBT/ITL is often part of the SLO that goodput is measured against.
- [[ContinuousBatching]] — affects TBT distribution (eviction/admission timing).
- [[LinkedIn]] / [[NVIDIA]] — sources of the two names.
- [[InferenceOptimization]] — broader discipline.
- [[ai-engineering-ch09-inference-optimization]] — primary source.
