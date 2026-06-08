---
title: "Cold Start (Serving)"
type: concept
tags: [serving, inference, autoscaling, latency, mlsysbook]
sources: [mlsysbook-ch13-model-serving]
last_updated: 2026-06-05
---

# Cold Start (Serving)

The **initialization latency incurred when instantiating a new model replica** — a *per-replica* cost (unlike per-request inference latency) that occurs at every deployment, scaling event, and failure recovery ([[mlsysbook-ch13-model-serving|mlsysbook Ch 13]]). The misconception that it is "just loading weights" misses graph compilation and memory allocation, which often dominate the bandwidth-limited data transfer.

ResNet-50 cold-start timeline: weight load 0.5 s (SSD) / 3–5 s (S3), **CUDA context 0.3–0.5 s**, **TensorRT compilation 15–30 s**, warmup 0.2 s, runtime overhead 0.4 s → ~1.5 s (optimized local) vs **~35 s (first cloud deploy)**. Precompiling and storing the optimized engine eliminates the 30 s compilation. Without **warmup** (synthetic inferences that trigger CUDA kernel compilation, cuDNN autotune, memory-pool allocation), the first live request runs >100× slower.

It is *not* an edge case: cold starts compound during the events that matter most (traffic spikes, deployments, recovery), violating SLOs precisely when reliability matters. Mitigations: loading strategies (full / memory-mapped / lazy + warmup), infrastructure model caching (container embedding, shared filesystem, node-local NVMe SSD), [[Safetensors]] zero-copy loading, and pinned memory.

## Connections

- [[Safetensors]] — zero-copy format that cuts weight-load time 30–100× vs pickle.
- [[CUDA]] / [[CUDAMPS]] — context creation cost; MPS shares one context across replicas.
- [[InferenceServer]] — performs loading + warmup before exposing the model.
- [[Autoscaling]] / [[CapacityPlanning]] — GPU startup (2–5 min) >> CPU (30–60 s) shapes scaling strategy.
- [[TensorRT]] — the engine whose compilation dominates first-deploy cold start.
- [[PinnedMemory]] — page-locked host memory for 2–3× faster DMA transfers.
- [[mlsysbook-ch13-model-serving]] — source.
