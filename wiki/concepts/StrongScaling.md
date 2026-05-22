---
title: "Strong Scaling"
type: concept
tags: [parallel-computing, performance, scaling, multicore]
sources: [dis-14-4-2-performance-advanced]
last_updated: 2026-05-18
---

# Strong Scaling

**Strong scaling** measures how [[ParallelSpeedup|speedup]] grows when the **core count increases but problem size stays fixed**. It is the regime [[AmdahlsLaw|Amdahl's Law]] directly bounds.

[[DiveIntoSystems]] [[dis-14-4-2-performance-advanced|Ch 14.4.2]] codifies the term — one of two complementary scalability classes (the other is [[WeakScaling|weak scaling]]).

## Definition

For a fixed workload of size $N$:
- Run on 1 core → $T_1$
- Run on $c$ cores → $T_c$
- Strong speedup = $T_1 / T_c$

**Linear strong scaling** means $\text{Speedup}(c) = c$ — every doubling of cores halves the runtime. This is the ideal that [[AmdahlsLaw|Amdahl]] caps at $1/S$.

## Typical curve shape

Strong-scaling curves **flatten** as core counts grow — the serial fraction dominates, the [[ParallelEfficiency|efficiency]] declines, and adding more cores produces diminishing returns. The shape directly visualizes Amdahl's asymptote.

## When strong scaling is the right metric

- **Fixed problem sizes** — given workload must complete faster.
- **Latency-critical applications** — finish one big job sooner (e.g., a single rendering frame, a single MRI reconstruction).
- **Hardware-evaluation benchmarks** — same problem on more cores reveals the parallel-overhead floor.

## Contrast with weak scaling

- **Strong** — fixed problem, grow cores. Governed by [[AmdahlsLaw|Amdahl]].
- **[[WeakScaling|Weak]]** — grow problem and cores together (each core does the same work). Governed by [[GustafsonsLaw|Gustafson-Barsis]].

A program may scale well in one regime and poorly in the other. Real systems are typically reported on both.

## Connections

- [[ParallelSpeedup]] — the metric strong scaling measures.
- [[ParallelEfficiency]] — typically falls under strong scaling as cores grow.
- [[AmdahlsLaw]] — the law bounding strong scaling.
- [[WeakScaling]] — the complementary regime.
- [[GustafsonsLaw]] — the law for weak scaling.
- [[ParallelComputing]] / [[SharedMemoryParallelism]] — the paradigms.
- [[dis-14-4-2-performance-advanced]] — primary DIS source.
