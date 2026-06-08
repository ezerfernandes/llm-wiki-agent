---
title: "Capacity Planning (Serving)"
type: concept
tags: [serving, queuing-theory, economics, infrastructure, mlsysbook]
sources: [mlsysbook-ch13-model-serving]
last_updated: 2026-06-05
---

# Capacity Planning (Serving)

Translating three inputs — **traffic patterns** (peak rate, cycles, growth), **latency SLOs** (p50/p95/p99), and **model characteristics** (inference time by batch size) — into an infrastructure specification ([[mlsysbook-ch13-model-serving|mlsysbook Ch 13]]). It combines the cost analysis of [[CostPerInference|GPU-vs-CPU economics]] with the [[QueuingTheory|queuing theory]] foundations.

The worked ResNet-50 example (5,000 QPS @ 50 ms p99): from the M/M/1 p99 bound, safe utilization ρ ≤ 1 − (4.6 × 5 ms)/50 ms = **0.54**; required service rate μ = 5,000/0.54 ≈ 9,259 req/s; ÷ 1,143 img/s (V100 batch-16) = 8.1 → 9 GPUs; × **1.3 headroom** → 12; losing one leaves 11 at ~40% util (N+1 satisfied). The key insight: **a throughput number is only real if requests still meet the percentile SLO** — 10,000 QPS violating p99 on 5% of requests is really 9,500 valid QPS. GPU startup latency (2–5 min) >> CPU (30–60 s) shapes scaling strategy (predictive for GPU, reactive for CPU, hybrid for bursty loads).

## Connections

- [[QueuingTheory]] / [[LittlesLaw]] — the equations that size the fleet and set the memory floor.
- [[CostPerInference]] — the per-inference economics capacity planning aggregates.
- [[ServiceLevelObjective]] / [[TailLatency]] — the p99 target driving safe utilization.
- [[Autoscaling]] / [[ColdStart]] — headroom + startup latency for traffic spikes.
- [[MLPerfScenarios]] — the SLO-constrained-throughput rule (MLPerf Server).
- [[mlsysbook-ch13-model-serving]] — source.
