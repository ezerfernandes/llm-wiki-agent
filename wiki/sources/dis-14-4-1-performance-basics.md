---
title: "Dive into Systems — Ch 14.4.1 Parallel Performance Basics"
type: source
tags: [parallel-computing, performance, speedup, efficiency, amdahl, multicore, dive-into-systems]
date: 2026-05-18
source_file: https://diveintosystems.org/book/C14-SharedMemory/performance_basics.html
---

## Summary

**First sub-leaf** of [[dis-14-4-performance|Ch 14.4]] *Measuring Parallel Performance* of *[[DiveIntoSystems]]* — formalizes the two foundational metrics ([[ParallelSpeedup|speedup]] and [[ParallelEfficiency|efficiency]]) and the **theoretical ceiling** on them ([[AmdahlsLaw|Amdahl's Law]]). Promotes the informal **1/c rule** from [[dis-14-1-multicore|Ch 14.1.2]]'s [[Speedup]] discussion into the precise ratio $\text{Speedup} = T_1 / T_c$, normalizes it by core count to define efficiency, and frames the universal counting-sort example as the empirical demonstration that real-world efficiency degrades sharply as cores grow.

## Key Claims

- **Speedup formal definition**: $\text{Speedup} = T_1 / T_c$, where $T_1$ is single-threaded execution time and $T_c$ is *c*-thread execution time. Values > 1 mean improvement; values > *c* are **superlinear speedup** (possible but rare).
- **Efficiency formal definition**: $\text{Efficiency} = \text{Speedup} / c$. Range typically $[0, 1]$; measures **per-core utilization** — how effectively each additional core is exploited.
- **[[AmdahlsLaw|Amdahl's Law]]**: $\text{Speedup}(c) = \frac{1}{S + P/c}$ where $S$ = serial fraction, $P = 1 - S$ = parallelizable fraction. As $c \to \infty$, $\text{Speedup} \to 1/S$ — the **asymptotic ceiling** imposed by the inherently serial portion.
- **Worked Amdahl example**: 90% parallelizable code ($S = 0.10$) caps at **10× speedup** regardless of core count.
- **Not all programs parallelize well**: serial-dependency chains (e.g., generating Fibonacci numbers where $F_n$ requires $F_{n-1}$ and $F_{n-2}$) have no parallelizable fraction to exploit.
- **Critical path** — the longest chain of sequential dependencies — fundamentally bounds achievable parallelism, independent of core count.
- **Real-world efficiency degrades** with more cores due to [[Synchronization|synchronization]] overhead, [[Mutex|lock]] contention, [[CacheCoherency|coherence]] traffic, and load imbalance.

## Key Quotes

> "The ratio of the execution time of the sequential program to the execution time of the parallel version using $c$ cores."
> (definition of speedup)

> "If $S$ is the fraction of operations in a computation that must be performed sequentially, then the maximum speedup that can be achieved by a parallel computer with $c$ processors is $\text{Speedup}(c) = \frac{1}{S + (1-S)/c}$."
> ([[AmdahlsLaw|Amdahl's Law]] verbatim)

## Connections

- [[dis-14-4-performance]] — parent hub leaf.
- [[ParallelSpeedup]] — the metric this section formalizes.
- [[ParallelEfficiency]] — the per-core-utilization companion metric.
- [[AmdahlsLaw]] — the serial-fraction ceiling on speedup; **promoted from forward-reference** ([[Speedup]] had named it but deferred coverage).
- [[Speedup]] — prior wiki page on the informal 1/c rule from [[dis-14-1-multicore|Ch 14.1.2]]; this section formalizes what that page deferred.
- [[dis-14-1-multicore]] — supplied the informal 1/c rule that 14.4.1 now bounds via Amdahl.
- [[CountingSort]] / [[Fibonacci]] — worked examples (counting sort is partly parallelizable; Fibonacci is the serial-only foil).
- [[CriticalPath]] — the dependency-chain concept Amdahl's serial fraction captures structurally.

## Contradictions

- None. Strictly extends [[Speedup]] — promotes the informal 1/c rule into the formal ratio and supplies the [[AmdahlsLaw|Amdahl]] formalism the prior page deferred.
