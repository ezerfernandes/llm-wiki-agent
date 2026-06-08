---
title: "Queuing Theory (Serving)"
type: concept
tags: [serving, inference, latency, capacity-planning, mlsysbook]
sources: [mlsysbook-ch13-model-serving]
last_updated: 2026-06-05
---

# Queuing Theory (Serving)

The mathematics that predicts **how serving latency degrades as concurrent requests compete for finite resources** — the quantitative foundation for capacity planning that replaces intuition-based provisioning ([[mlsysbook-ch13-model-serving|mlsysbook Ch 13]]). Two results govern serving:

- **[[LittlesLaw|Little's Law]]** $N_{\text{req}} = \lambda \cdot T_{\text{lat}}$ — relates queue depth to throughput; holds for *any* stable system.
- **M/M/1 wait time** $T_{\text{lat}} = \text{service}/(1-\rho)$ — predicts the **nonlinear utilization-latency curve**.

The utilization (ρ) multiplier on service time: 50% ⇒ 2×, **70% ⇒ 3.3× (the "knee")**, 80% ⇒ 5×, 90% ⇒ 10×, 95% ⇒ 20×. This $(1-\rho)^{-1}$ divergence is a *mathematical inevitability*, not a heuristic — which is **why production systems must run at 40–70% utilization** to hold tail latency. p99 ≈ 4.6 × service/(1−ρ).

ML inference has near-constant (deterministic) service time, so **M/D/1** is more accurate, but the chapter uses M/M/1 deliberately: it over-predicts wait by ~2×, giving a built-in safety margin for capacity planning (Kendall notation A/S/c; "M" = Markovian/memoryless, "D" = deterministic; Erlang 1909). M/M/c shows c replicas drop p99 ~3× at c=4. The key insight: a system "achieving 10,000 QPS" while violating p99 on 5% of requests is really serving 9,500 valid QPS.

## Connections

- [[LittlesLaw]] — the concurrency/memory-floor result.
- [[TailLatency]] — the percentile divergence and tail-at-scale (Dean & Barroso).
- [[CapacityPlanning]] — the discipline that applies these equations (the 12-V100 worked example).
- [[LatencyBudget]] — queuing predicts the wait component; the "Black Friday" collapse.
- [[AdmissionControl]] / [[GracefulDegradation]] — the only levers once ρ→1.
- [[ServiceLevelObjective]] — the p99 target the math must satisfy.
- [[DynamicBatching]] — the batching tax adds formation delay to the queuing wait.
- [[mlsysbook-ch13-model-serving]] — source.
