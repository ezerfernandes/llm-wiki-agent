---
title: "Scaling Efficiency"
type: concept
tags: [benchmarking, distributed-training, parallelism, metrics, mlsysbook]
sources: [mlsysbook-ch12-benchmarking]
last_updated: 2026-06-05
---

# Scaling Efficiency

The fraction of added computational capacity that translates into actual speedup. For **strong scaling** (fixed problem size, more processors), with single-GPU time $T(1)$ and $N$-GPU time $T(N)$:

$$\text{Eff}_{\text{scaling}}(N) = \frac{T(1)}{N \times T(N)} \times 100\%$$

Per [[mlsysbook-ch12-benchmarking|mlsysbook Ch 12]], scaling is reliably **sub-linear**: 24 h on one GPU → 4 h on 8 GPUs = **75% efficiency** (vs. the ideal 3 h). The missing 25% decomposes into measurable overheads: **gradient synchronization (10–15%)**, memory copy CPU↔GPU (3–5%), load imbalance (2–5%), and batch-size effects (2–5%). Efficiency falls further with scale — ≈50–60% at 64 GPUs, ≈30–40% at 1000+ GPUs even with sophisticated optimization (Google's 4,096-node TPU v4 pods, where gradient sync dominates). A $10M cluster expected to be 5× a $2M one delivered only 2.8×.

The systems lesson: MLPerf reports raw performance *and* scaling efficiency, because 2× throughput at 50% efficiency can be worse than 1.5× at 90% depending on cost. Extrapolating single-node results to clusters is a recurring pitfall.

## Connections

- [[DataParallelism]] — the dominant strategy whose gradient-sync overhead caps efficiency.
- [[AmdahlsLaw]] — the serial-fraction (gradient-sync) ceiling on multi-chip scaling.
- [[TimeToAccuracy]] — the metric scaling is meaningful relative to.
- [[MLPerf]] — reports both raw and scaling-efficiency numbers.
- [[mlsysbook-ch12-benchmarking]] — source.
