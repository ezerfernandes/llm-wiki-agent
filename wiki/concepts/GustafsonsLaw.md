---
title: "Gustafson-Barsis Law"
type: concept
tags: [parallel-computing, performance, scaling, theory, multicore]
sources: [dis-14-4-2-performance-advanced]
last_updated: 2026-05-18
---

# Gustafson-Barsis Law

**Gustafson-Barsis Law** (John Gustafson and Edwin Barsis, 1988) is the **problem-scaling alternative** to [[AmdahlsLaw|Amdahl's Law]]. Where Amdahl assumes problem size is fixed and asks *"how fast can I run the same problem on more cores?"*, Gustafson assumes problem size scales with available cores and asks *"how much more work can I do in the same time?"*

[[DiveIntoSystems]] [[dis-14-4-2-performance-advanced|Ch 14.4.2]] introduces Gustafson-Barsis as the practical corrective to [[AmdahlsLaw|Amdahl]]'s pessimism.

## Core assertion

> "The amount of work that can be done in parallel varies linearly with the number of processors."
> — *Gustafson-Barsis*

In practice, **larger machines get used for larger problems**. The parallelizable fraction $P$ and the core count $c$ are *"virtually never"* independent.

## Statement

Let $S'$ be the **serial fraction of the scaled problem** (the version of the workload that fully utilizes $c$ cores). Then:

$$\text{Speedup}(c) = c - S' \cdot (c - 1)$$

equivalently $\text{Speedup}(c) = S' + c \cdot (1 - S')$ — linear in $c$ when the serial fraction is small.

## Why it differs from Amdahl

- **Amdahl** fixes the workload and asks *"what's the max speedup?"* — caps at $1/S$.
- **Gustafson** fixes the wall-clock budget and asks *"how much more work fits?"* — grows linearly in $c$.

Both are correct; they answer different questions. [[StrongScaling|Strong scaling]] (fixed problem) lives in Amdahl's frame; [[WeakScaling|weak scaling]] (scaled problem) lives in Gustafson's.

## Practical implications

- **Supercomputers / HPC** justify themselves under Gustafson's frame — bigger machines tackle bigger problems (higher-resolution simulations, larger datasets).
- **Mobile / embedded** workloads with fixed problem sizes live under Amdahl's ceiling.
- **Cloud autoscaling** workloads typically follow Gustafson (more cores → more concurrent users → more total work).

## Connections

- [[AmdahlsLaw]] — the fixed-problem-size law Gustafson critiques and complements.
- [[ParallelSpeedup]] — the metric both laws bound differently.
- [[ParallelEfficiency]] — under Gustafson, efficiency can stay near 1 as cores grow (the [[WeakScaling|weak-scaling]] regime).
- [[StrongScaling]] — the [[AmdahlsLaw|Amdahl]]-governed regime (fixed problem, grow cores).
- [[WeakScaling]] — the Gustafson-governed regime (problem and cores grow together).
- [[ParallelComputing]] / [[SharedMemoryParallelism]] — the paradigms.
- [[dis-14-4-2-performance-advanced]] — primary DIS source.
