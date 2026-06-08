---
title: "Tail Latency"
type: concept
tags: [benchmarking, inference, latency, serving, slo, mlsysbook]
sources: [mlsysbook-ch12-benchmarking, mlsysbook-ch13-model-serving]
last_updated: 2026-06-05
---

# Tail Latency

The high-percentile response time (p95, p99, p99.9) that determines production reliability — **not the mean**. The chapter's slogan ([[mlsysbook-ch12-benchmarking|mlsysbook Ch 12]]): *"Average latency is a vanity metric; tail latency is the user experience."*

A system with 10 ms mean but **500 ms p99 violates SLOs for 1% of requests** — at 10,000 QPS that is 100 users/second experiencing unacceptable delays. MLPerf reports p99 alongside the mean for exactly this reason, and the Server scenario enforces a p99 SLO. The tail also exposes the **SLO-constrained-vs-unconstrained throughput gap**: peak QPS with no latency constraint (Offline) can be 2–3× the sustainable rate under a p99 target (Server), because queuing delays push the tail above target at high load.

The tail has structural floors no tuning can lower: managed-runtime **garbage-collection pauses** (the Discord lesson) and queue-wait time, which can dominate the end-to-end latency breakdown. Poisson-arrival benchmark harnesses *underestimate* the tail because real traffic is bursty.

## Connections

- [[MLPerfScenarios]] — Server mode's binding metric; Offline-vs-Server gap.
- [[InferencePerformanceMetrics]] — the broader latency/throughput/energy metric set.
- [[Benchmarking]] / [[BenchmarkComponents]] — why percentiles belong in the metric set.
- [[AmdahlsLaw]] — the end-to-end latency breakdown where queue wait and preprocessing dominate.
- [[QueuingTheory]] / [[LittlesLaw]] — the M/M/1 mathematics behind the tail explosion (p99 ≈ 4.6× mean).
- [[GracefulDegradation]] / [[AdmissionControl]] / [[HedgedRequests]] — tail-tolerant techniques ([[mlsysbook-ch13-model-serving|Ch 13]]).
- [[ServiceLevelObjective]] / [[CapacityPlanning]] — why SLOs target p95/p99 and how headroom enforces them.
- [[mlsysbook-ch12-benchmarking]] — source.
- [[mlsysbook-ch13-model-serving]] — Ch 13 makes p99 the binding serving constraint: the tail explodes nonlinearly past the ~70% utilization knee (Dean & Barroso tail-at-scale; fan-out amplification), driving the 40–60% headroom rule.
