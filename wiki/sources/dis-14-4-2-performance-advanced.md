---
title: "Dive into Systems — Ch 14.4.2 Advanced Performance Considerations"
type: source
tags: [parallel-computing, performance, scaling, amdahl, gustafson, benchmarking, multicore, dive-into-systems]
date: 2026-05-18
source_file: https://diveintosystems.org/book/C14-SharedMemory/performance_advanced.html
---

## Summary

**Second sub-leaf** of [[dis-14-4-performance|Ch 14.4]] *Measuring Parallel Performance* of *[[DiveIntoSystems]]* — extends [[dis-14-4-1-performance-basics|14.4.1]]'s [[AmdahlsLaw|Amdahl]] pessimism with the **[[GustafsonsLaw|Gustafson-Barsis Law]]** problem-scaling alternative, then codifies the two complementary scalability metrics — **[[StrongScaling|strong scaling]]** (fixed problem size, grow cores) and **[[WeakScaling|weak scaling]]** (grow problem and cores together) — and closes with a benchmarking-discipline checklist.

## Key Claims

- **Amdahl vs Gustafson framing**: [[AmdahlsLaw|Amdahl's Law]] **assumes fixed problem size** — under that assumption the serial fraction dominates as cores grow. [[GustafsonsLaw|Gustafson-Barsis]] inverts the assumption: in real workloads, **problem size grows with available cores**, so the parallelizable fraction also grows, breaking Amdahl's asymptotic ceiling.
- **Gustafson's empirical claim**: in practice the core count $c$ and the parallel fraction $P$ are *"virtually never"* independent — bigger machines get used for bigger problems.
- **[[StrongScaling|Strong scaling]]**: how speedup grows when **core count grows but problem size stays fixed**. *Linear strong scaling* means $\text{Speedup}(c) = c$ — the ideal Amdahl's Law caps.
- **[[WeakScaling|Weak scaling]]**: how performance behaves when **core count and problem size grow proportionally** (each core gets the same amount of work). *Linear weak scaling* means runtime stays constant as both grow — the regime Gustafson highlights.
- **Hyperthreaded cores** can produce **nonlinear speedup curves** due to shared-execution-resource contention — two HT siblings share a core's pipeline, so doubling threads on HT siblings does not double throughput.
- **Benchmarking discipline**: (1) run multiple trials and aggregate (mean / median / variance), (2) measure only the relevant code section (exclude I/O, setup), (3) account for hyperthreading effects in core-count claims, (4) monitor system resource contention (other processes, [[CacheMemory|cache]], memory bandwidth) during testing.

## Key Quotes

> "The amount of work that can be done in parallel varies linearly with the number of processors."
> ([[GustafsonsLaw|Gustafson-Barsis]] core assertion)

> Core count and the parallelizable fraction of work are "virtually never" independent in real scenarios.
> (Gustafson's critique of [[AmdahlsLaw|Amdahl]]'s fixed-problem assumption)

## Connections

- [[dis-14-4-performance]] — parent hub leaf.
- [[dis-14-4-1-performance-basics]] — sibling sub-leaf supplying [[ParallelSpeedup|speedup]] / [[ParallelEfficiency|efficiency]] / [[AmdahlsLaw|Amdahl]] foundations this section builds on.
- [[GustafsonsLaw]] — the problem-scaling alternative to [[AmdahlsLaw|Amdahl]], introduced here.
- [[StrongScaling]] / [[WeakScaling]] — the two scalability classes codified here.
- [[AmdahlsLaw]] — the fixed-problem-size ceiling Gustafson critiques.
- [[Hyperthreading]] / [[SimultaneousMultithreading]] — the hardware-resource-sharing phenomenon that produces nonlinear scaling curves.
- [[Benchmarking]] — the methodological discipline this section closes on.
- [[ParallelComputing]] / [[SharedMemoryParallelism]] — the paradigm being measured.

## Contradictions

- **None directly** — but the section structurally **softens** [[AmdahlsLaw|Amdahl]]'s pessimism (introduced in [[dis-14-4-1-performance-basics|14.4.1]]) by reframing its fixed-problem-size assumption as unrealistic in practice. The two laws are complementary lenses on the same underlying ratio, not contradictions.
