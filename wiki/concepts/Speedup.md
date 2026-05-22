---
title: "Speedup"
type: concept
tags: [parallel-computing, performance, multicore, metrics]
sources: [dis-14-1-multicore]
last_updated: 2026-05-18
---

# Speedup

**Speedup** is the standard performance metric in [[ParallelComputing|parallel computing]] — the ratio of single-threaded execution time to multi-threaded execution time for the same workload. [[DiveIntoSystems]] [[dis-14-1-multicore|Ch 14.1.2]] introduces speedup informally via the **1/c approximation rule** for [[Thread|thread]]-on-[[MulticoreProcessor|multicore]] workloads, but defers the formal serial-fraction analysis (i.e. [[AmdahlsLaw|Amdahl's Law]]) — Ch 14.1 itself does **not** name or formalize Amdahl.

## The DIS 14.1.2 rule

> "In general, if the number of threads matches the number of cores (c) and the operating system schedules each thread to run on a separate core in parallel, then the multithreaded process should run in approximately **1/c of the time**."

This is the **ideal-case linear speedup** approximation. It assumes:

1. **Thread count matches core count** — `t = c`. Fewer threads underuses cores; more threads forces time-sharing and adds context-switch overhead.
2. **OS schedules each thread to a distinct core** — not all to one core, not bouncing across cores destroying cache locality.
3. **The workload is partitionable with no shared writes** — i.e. close to [[EmbarrassinglyParallel|embarrassingly parallel]]. The chapter's *Scalar Multiplication* example is the canonical fit (each element is independent of every other).
4. **Negligible coordination overhead** — no [[Mutex|mutex]] contention, no [[Barrier|barrier]] waits, no [[CacheCoherency|coherence]] traffic dominating.

When these hold, *t* threads on *t* cores complete in **1/c** of the wall-clock time of the single-threaded baseline — a **speedup of c**. This is the ceiling. In practice, *"resource contention prevents ideal speedup in practice"* (Ch 14.1.2).

## Formal definition

Standard definition (not stated explicitly in 14.1 but consistent with its rule):

$$\text{Speedup}(c) = \frac{T_1}{T_c}$$

where $T_1$ is the single-threaded execution time and $T_c$ is the *c*-threaded execution time on *c* cores. **Linear speedup** is $\text{Speedup}(c) = c$ — the ceiling 14.1.2's 1/c rule approaches.

## Why ideal speedup is rare

Four standard speedup-killers (Ch 14.1.2 mentions the first three implicitly via *"resource contention prevents ideal speedup"*):

1. **Serial fractions** — any code section that *must* run sequentially (initialization, result aggregation, I/O) caps the speedup regardless of `c`. Formalized by [[AmdahlsLaw|Amdahl's Law]] (covered by [[parproc-ch01-intro-parallel-processing|parproc Ch 1]], not by DIS 14.1).
2. **Coordination overhead** — [[Mutex|mutex]] acquisition, [[Barrier|barriers]], and [[ConditionVariable|condition-variable]] waits all serialize threads at synchronization points.
3. **Shared-resource contention** — [[CacheLevel|cache]] thrashing, [[Bus|bus]] / memory-channel bandwidth saturation, false sharing across [[CacheLine|cache lines]].
4. **Load imbalance** — uneven partitioning forces fast threads to wait for slow threads at the join point.

## Superlinear speedup (rare, real)

Occasionally $\text{Speedup}(c) > c$ — typically because the partitioned working set per thread fits in cache where the single-thread working set did not. DIS 14.1 does not discuss this case.

## Connections

- [[ParallelComputing]] — the broader paradigm speedup measures performance in.
- [[Thread]] / [[MulticoreProcessor]] — the moving parts.
- [[ConcurrencyVsParallelism]] — concurrency without parallelism produces no speedup.
- [[SharedMemoryParallelism]] — the paradigm DIS Ch 14 uses; speedup is its target metric.
- [[Throughput]] — the related but distinct metric (process-count / time vs single-task wall-clock-time ratio).
- [[AmdahlsLaw]] — the formal serial-fraction ceiling on speedup; **not** covered in DIS 14.1 but covered elsewhere in the corpus.
- [[EmbarrassinglyParallel]] — the workload class that approaches the 1/c ideal.
- [[dis-14-1-multicore]] — DIS source for the 1/c approximation rule.
- [[parproc-ch01-intro-parallel-processing]] — supplies the Amdahl formalism DIS 14.1 defers.
