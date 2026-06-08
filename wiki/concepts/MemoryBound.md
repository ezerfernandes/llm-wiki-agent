---
title: "Memory-Bound"
type: concept
tags: [hardware, ml-systems, performance, roofline]
sources: [mlsysbook-ch05-neural-computation]
last_updated: 2026-06-05
---

# Memory-Bound

A workload whose performance is limited by **memory bandwidth** (how fast data arrives) rather than raw arithmetic capacity — the counterpart to [[ComputeBound|compute-bound]]. An operation is memory-bound when its [[ArithmeticIntensity|arithmetic intensity]] (FLOP/byte loaded) falls *below* the hardware's [[RooflineModel|roofline]] crossover point: it finishes its arithmetic before the next tile of weights arrives from memory, so adding compute units yields little speedup until bandwidth or data reuse improves.

Per [[mlsysbook-ch05-neural-computation|mlsysbook Vol 1 Ch 5]]:

- **Element-wise ops** ([[ReLU]], activations) are memory-bound: ~1/(2s) FLOP/byte (0.125 for FP32), independent of size.
- **Small networks** like the MNIST MLP have arithmetic intensity <1 FLOP/byte — *far* below the A100/H100 dense-FP16 ridge points (hundreds of FLOP/byte), so they stay memory-bound even on a large GPU. A commodity CPU can match an expensive accelerator on such workloads; the accelerator only pays off for compute-bound GPT-scale models.

This is the practical face of the [[MemoryWall|memory wall]], and explains why teams report wildly varying GPU utilization depending on architecture, and why "more compute" does not automatically mean faster training.

## Connections

- [[ComputeBound]] — the opposite regime ([[GEMM]], dense matmul).
- [[ArithmeticIntensity]] / [[RooflineModel]] — the crossover that classifies workloads.
- [[MemoryWall]] / [[MemoryBandwidth]] / [[MemoryBandwidthBound]] — the underlying constraint.
- [[mlsysbook-ch05-neural-computation]] — source of the MNIST-vs-ridge-point example.
