---
title: "MLPerf Execution Scenarios"
type: concept
tags: [benchmarking, mlperf, inference, latency, throughput, mlsysbook, serving]
sources: [mlsysbook-ch12-benchmarking, mlsysbook-ch13-model-serving]
last_updated: 2026-06-05
---

# MLPerf Execution Scenarios

The four canonical traffic patterns [[MLPerf]] Inference defines so that a benchmark score can be interpreted against a deployment context — plus a newer **Interactive** case for LLMs. The key insight ([[mlsysbook-ch12-benchmarking|mlsysbook Ch 12]]): the *same hardware reports dramatically different numbers* depending on how requests arrive, which is why vendor claims often fail to predict production performance.

| Scenario | Context | Strategy | Focus |
|---|---|---|---|
| **SingleStream** | Mobile/embedded | No batching (batch=1) | Per-request latency, power |
| **MultiStream** | Autonomous driving, video | Synchronized sensor fusion | Jitter, hard deadlines (33 ms / 30 FPS) |
| **Server** | Cloud APIs | Dynamic batching w/ timeout | Throughput–latency (p99) trade-off |
| **Offline** | Batch pipelines | Max batch size | Pure throughput, hardware utilization |
| **Interactive** | Chat, agents, local genAI | Token streaming, KV-cache mgmt | TTFT, time-per-output-token |

An accelerator achieving **10,000 samples/s in Offline mode might sustain only 200 QPS in Server mode** under a p99 SLO, because Server includes queuing and cannot use maximum batch sizes. Matching the scenario to the deployment context is what makes a benchmark result predictive.

## Connections

- [[MLPerf]] — the benchmark family defining these scenarios.
- [[TailLatency]] — Server mode's binding constraint (p99).
- [[BatchInference]] / [[OnlineInference]] — Offline vs. SingleStream/Server map onto these modes; the batch-size throughput-latency trade-off.
- [[RooflineModel]] — batching shifts memory-bound (SingleStream) to compute-bound (Offline).
- [[DynamicBatching]] / [[ServiceLevelObjective]] / [[CapacityPlanning]] — how each scenario maps to a batching strategy and the SLO-constrained-throughput rule.
- [[mlsysbook-ch12-benchmarking]] — source.
- [[mlsysbook-ch13-model-serving]] — Ch 13 uses these scenarios as the **decision framework for batching strategy**: Server (cloud APIs) → dynamic batching w/ timeout; MultiStream (autonomous driving, 6-camera 33 ms deadline) → synchronized sensor fusion; SingleStream (mobile) → no batching (batch-1, energy/thermal focus); Offline (pipelines) → max batch. Each pattern is a consequence of the physical walls behind the [[DeploymentSpectrum|deployment paradigms]].
