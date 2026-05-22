---
title: "Weak Scaling"
type: concept
tags: [parallel-computing, performance, scaling, multicore]
sources: [dis-14-4-2-performance-advanced]
last_updated: 2026-05-18
---

# Weak Scaling

**Weak scaling** measures performance when **problem size and core count grow proportionally** — each core sees the same amount of work. It is the regime [[GustafsonsLaw|Gustafson-Barsis Law]] highlights.

[[DiveIntoSystems]] [[dis-14-4-2-performance-advanced|Ch 14.4.2]] codifies the term — the complement of [[StrongScaling|strong scaling]].

## Definition

For a workload that grows with core count — each core handles a fixed amount of work $W$:
- 1 core handles $W$ units → $T_1$
- $c$ cores handle $c \cdot W$ units → $T_c$
- **Linear weak scaling** means $T_c \approx T_1$ (runtime stays constant as both grow).

Equivalently, weak speedup is defined as $T_1 / T_c$ on the **scaled problem**, and is linear in $c$ under Gustafson.

## Why it matters

Weak scaling is the regime that **justifies high-core / HPC machines** — you don't buy a 1000-core cluster to solve a 1-core problem faster; you buy it to solve a 1000-core-sized problem at all.

- **Climate / weather simulation** at higher spatial resolution.
- **Molecular dynamics** with more atoms.
- **Search / ranking / recommendation** over larger corpora.
- **Cloud autoscaling** to handle more concurrent users.

## Typical curve shape

Ideal weak-scaling curves are **flat** — runtime stays constant as $c$ and problem size grow together. Real curves rise gently due to inter-core communication overhead, but never hit Amdahl's asymptote because the parallelizable work is also growing.

## Contrast with strong scaling

- **Weak** — grow problem and cores together. Governed by [[GustafsonsLaw|Gustafson-Barsis]].
- **[[StrongScaling|Strong]]** — fixed problem, grow cores. Governed by [[AmdahlsLaw|Amdahl]].

## Connections

- [[ParallelSpeedup]] — the metric weak scaling measures (on scaled problems).
- [[ParallelEfficiency]] — can stay near 1 under weak scaling.
- [[GustafsonsLaw]] — the law bounding weak scaling.
- [[StrongScaling]] — the complementary regime.
- [[AmdahlsLaw]] — the law for strong scaling.
- [[ParallelComputing]] / [[SharedMemoryParallelism]] — the paradigms.
- [[dis-14-4-2-performance-advanced]] — primary DIS source.
