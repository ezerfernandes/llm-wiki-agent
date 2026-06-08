---
title: "Layer Fusion (Kernel Fusion)"
type: concept
tags: [serving, inference, optimization, gpu, compiler, mlsysbook]
sources: [mlsysbook-ch13-model-serving]
last_updated: 2026-06-05
---

# Layer Fusion (Kernel Fusion)

The serving-runtime application of [[OperatorFusion|operator fusion]]: **combining multiple sequential operations into a single GPU kernel** so intermediate data stays in registers/L1-L2 cache instead of round-tripping to global VRAM ([[mlsysbook-ch13-model-serving|mlsysbook Ch 13]]). The canonical pattern is `Conv2D → BatchNorm → ReLU`: unfused requires three kernel launches and three memory round-trips; fused reads inputs once, computes in registers, writes once.

This eliminates kernel-launch overhead (15–60 μs saved per fusion) and cuts memory traffic 2–3×, converting memory-bound chains into compute-bound fused kernels. [[TensorRT]] auto-detects and fuses common patterns — a typical ResNet-50 drops from ~50 kernels to ~15 (~35 fusible operation pairs). The serving graph's *static* nature is what lets compilers fuse aggressively (unsafe during mutable-graph training). One of the highest-leverage node-level optimizations (2–5× latency/throughput).

## Connections

- [[OperatorFusion]] — the general technique (loop fusion analogy in compilers).
- [[TensorRT]] / [[InferenceRuntime]] — the engines that perform fusion at build time.
- [[MemoryWall]] / [[RooflineModel]] — fusion targets the memory-bandwidth bottleneck.
- [[TensorCore]] — fused kernels feed the dense MAC arrays efficiently.
- [[mlsysbook-ch13-model-serving]] — source.
