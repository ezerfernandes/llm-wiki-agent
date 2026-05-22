---
title: "Parallel Speedup"
type: concept
tags: [parallel-computing, performance, metrics, multicore]
sources: [dis-14-4-1-performance-basics, dis-14-4-performance]
last_updated: 2026-05-18
---

# Parallel Speedup

**Parallel speedup** is the formal performance metric for parallel programs: the ratio of single-threaded execution time $T_1$ to $c$-threaded execution time $T_c$.

$$\text{Speedup}(c) = \frac{T_1}{T_c}$$

[[DiveIntoSystems]] [[dis-14-4-1-performance-basics|Ch 14.4.1]] formalizes the metric that [[dis-14-1-multicore|Ch 14.1.2]] only introduced informally via the **1/c approximation rule** (see [[Speedup]] for the prior informal treatment).

## Interpretation

- **Speedup = 1** — parallel version is no faster than serial.
- **Speedup ∈ (1, c)** — partial benefit; the realistic regime.
- **Speedup = c** — **linear speedup**, the [[AmdahlsLaw|Amdahl]] ceiling assuming zero serial fraction and zero overhead.
- **Speedup > c** — **superlinear speedup**, rare but real, typically when the partitioned working set per thread fits in cache where the single-thread set did not.

## Relationship to efficiency

[[ParallelEfficiency|Efficiency]] = Speedup / c — the per-core normalization that makes speedup numbers comparable across machines with different core counts.

## What kills speedup

1. **Serial fractions** — code that *must* run sequentially caps speedup at $1/S$ where $S$ is the serial fraction ([[AmdahlsLaw|Amdahl's Law]]).
2. **[[Synchronization|Coordination overhead]]** — [[Mutex|mutex]] contention, [[Barrier|barrier]] waits, [[ConditionVariable|condition-variable]] blocking.
3. **Shared-resource contention** — [[CacheCoherency|cache-coherence]] traffic, memory-bandwidth saturation, false sharing.
4. **Load imbalance** — uneven partitioning forces fast threads to idle at join.

## Strong vs weak scaling

- **[[StrongScaling|Strong scaling]]** holds problem size fixed and grows core count — measures pure parallel speedup. Bounded by [[AmdahlsLaw|Amdahl]].
- **[[WeakScaling|Weak scaling]]** grows problem size and core count together — measures how throughput scales. The regime [[GustafsonsLaw|Gustafson]] highlights.

## Connections

- [[Speedup]] — prior wiki page on the informal 1/c rule from [[dis-14-1-multicore|Ch 14.1.2]]; this page is the formal sibling.
- [[ParallelEfficiency]] — speedup normalized by core count.
- [[AmdahlsLaw]] — the serial-fraction speedup ceiling.
- [[GustafsonsLaw]] — the problem-scaling alternative that softens Amdahl's pessimism.
- [[StrongScaling]] / [[WeakScaling]] — the two scaling regimes speedup is measured in.
- [[ParallelComputing]] / [[SharedMemoryParallelism]] — the paradigm being measured.
- [[Throughput]] — the related but distinct metric (jobs / time, not single-task wall-clock ratio).
- [[dis-14-4-1-performance-basics]] — primary DIS source.
