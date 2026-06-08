---
title: "CUDA MPS (Multi-Process Service)"
type: concept
tags: [serving, gpu, multi-model, cuda, nvidia, mlsysbook]
sources: [mlsysbook-ch13-model-serving]
last_updated: 2026-06-05
---

# CUDA MPS (Multi-Process Service)

A CUDA feature (since CUDA 5.0) that runs a **daemon mediating GPU access through a shared [[CUDA]] context**, enabling *true concurrent kernel execution* across processes rather than time-sliced scheduling between separate contexts ([[mlsysbook-ch13-model-serving|mlsysbook Ch 13]]).

For multi-model serving, MPS eliminates redundant per-process context initialization (the 0.3–0.5 s CUDA-context [[ColdStart|cold-start]] cost) and lets replicas share GPU streaming multiprocessors efficiently, reducing aggregate cold start and improving utilization. The trade-off is **fault isolation**: all clients share one context, so a segfault in one process can corrupt GPU state for all others — a risk that hardware-level [[MIG]] eliminates (at the cost of fixed partition granularity).

## Connections

- [[MIG]] — the hardware-isolation alternative (stronger isolation, fixed granularity).
- [[CUDA]] — the context MPS shares across processes.
- [[ColdStart]] — MPS amortizes the per-process context-creation cost.
- [[InferenceServer]] — multi-model serving on a single GPU.
- [[mlsysbook-ch13-model-serving]] — source.
