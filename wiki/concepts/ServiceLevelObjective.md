---
title: "Service Level Objective (SLO)"
type: concept
tags: [serving, slo, latency, reliability, mlsysbook]
sources: [mlsysbook-ch13-model-serving, mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# Service Level Objective (SLO)

An **internal target** that shapes every architectural decision in the serving stack — e.g., "p99 latency under 50 ms" ([[mlsysbook-ch13-model-serving|mlsysbook Ch 13]]). Distinct from an **SLA (Service Level Agreement)**, which is an *external contractual commitment* with financial penalties for violation. SLOs are deliberately set *tighter* than SLAs to provide a safety margin.

For ML serving the SLO is **multi-dimensional**: both model accuracy and inference latency contribute, so improving one (deploying a larger model for accuracy) can violate the other (latency). Production SLOs specify **percentile targets (p95, p99), not averages**, because [[TailLatency|tail latency]] determines user experience and revenue (~100 ms of added latency ≈ 1% sales loss in the Google/Amazon studies). A throughput number is only "real" if requests still meet the percentile SLO under load (the MLPerf Server rule).

## Connections

- [[LatencyBudget]] — the SLO is the hard bound the budget must respect.
- [[TailLatency]] — why SLOs target percentiles, not means.
- [[QueuingTheory]] / [[CapacityPlanning]] — sizing infrastructure to meet the SLO with headroom.
- [[AdmissionControl]] / [[GracefulDegradation]] — protect the SLO for admitted requests under overload.
- [[MLPerfScenarios]] — the Server scenario enforces a p99 SLO.
- [[mlsysbook-ch13-model-serving]] — source.
- [[mlsysbook-ch14-ml-operations]] — mlsysbook Vol 1 Ch 14 uses SLOs as the latency-budget target (e.g., 100 ms P99) and ties rollback thresholds to SLO violations (P99 > 2× baseline for 5 min).

