---
title: "Parallel Efficiency"
type: concept
tags: [parallel-computing, performance, metrics, multicore]
sources: [dis-14-4-1-performance-basics]
last_updated: 2026-05-18
---

# Parallel Efficiency

**Parallel efficiency** normalizes [[ParallelSpeedup|speedup]] by core count, giving a **per-core utilization** measure:

$$\text{Efficiency}(c) = \frac{\text{Speedup}(c)}{c} = \frac{T_1}{c \cdot T_c}$$

[[DiveIntoSystems]] [[dis-14-4-1-performance-basics|Ch 14.4.1]] introduces efficiency as the companion metric to speedup — *"the ratio of speedup to the number of processors used."*

## Interpretation

- **Efficiency = 1.0** — every core contributes its full share; the **linear-speedup ideal**.
- **Efficiency ∈ (0, 1)** — partial utilization; the realistic regime.
- **Efficiency ≪ 1** at high core counts — diminishing returns from overhead, contention, [[AmdahlsLaw|Amdahl]] limits.
- **Efficiency > 1** — possible only when [[ParallelSpeedup|speedup]] exceeds *c* (superlinear case — cache effects).

## Why efficiency matters

Raw speedup hides cost. A program with **8× speedup on 16 cores** (efficiency 0.5) is wasting half the hardware — possibly fine, possibly the prompt to re-examine [[Synchronization|synchronization]] or partitioning. Efficiency makes the per-core cost visible.

## Degradation pattern

Real-world efficiency curves **decline as cores grow** because:
- Serial fractions (per [[AmdahlsLaw|Amdahl]]) cap absolute speedup → efficiency = $1/(Sc + P)$ approaches $0$.
- [[Synchronization|Coordination overhead]] grows with thread count (more lock acquisitions, more barrier participants).
- [[CacheCoherency|Coherence traffic]] and memory-bandwidth contention scale superlinearly with cores.

## Connections

- [[ParallelSpeedup]] — the metric efficiency normalizes.
- [[AmdahlsLaw]] — the serial-fraction ceiling that drives efficiency-degradation curves.
- [[GustafsonsLaw]] — the problem-scaling alternative that lets efficiency stay near 1 under [[WeakScaling|weak scaling]].
- [[StrongScaling]] — the regime efficiency typically falls in.
- [[WeakScaling]] — the regime efficiency can stay near 1.
- [[ParallelComputing]] / [[SharedMemoryParallelism]] — the paradigm being measured.
- [[dis-14-4-1-performance-basics]] — primary DIS source.
