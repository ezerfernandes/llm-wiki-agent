---
title: "Benchmarking"
type: concept
tags: [systems, optimization, performance, measurement]
sources: [dis-12-1-first-steps, dis-12-2-compiler-optimizations, dis-12-3-memory-considerations]
last_updated: 2026-05-17
---

# Benchmarking

The **controlled empirical measurement** of a program's end-to-end performance — wall-clock runtime, throughput, latency — under representative workloads. Where [[Profiling|profiling]] *decomposes* execution to identify [[HotSpot|hot spots]], benchmarking *aggregates* it into a single performance number that can be compared across versions, compiler flags, or hardware.

[[DiveIntoSystems]] Ch 12 uses benchmarking throughout to **validate** every optimization claim:

| Benchmark | Result | Source |
|---|---|---|
| `isPrime`, 5,000,000 limit, before vs after loop-invariant motion | **47% runtime reduction** | [[dis-12-1-first-steps]] |
| `isPrime`, manual 2-factor [[LoopUnrolling|loop unroll]] vs `-funroll-loops` | comparable speedups | [[dis-12-2-compiler-optimizations]] |
| 10,000 × 10,000 matrix-vector multiply, column-stride vs row-stride loop order | **2.01 s → 0.27 s (~8×)** | [[dis-12-3-memory-considerations]] |

## Methodology

Sound benchmarks require: (1) **representative workload** (not toy data); (2) **warm-up runs** to fill the [[CacheMemory|cache]] / JIT state; (3) **multiple repetitions** for variance estimation; (4) **single variable change** between versions; (5) **noise control** (no concurrent processes, CPU governor pinned).

## Relation to profiling

Benchmarking answers *"is the program faster now?"* — a single end-to-end number. [[Profiling]] answers *"which part is slow?"* — a per-function decomposition. Ch 12 alternates between the two: profile to find the [[HotSpot|hot spot]], optimize, benchmark to verify.

## Connections

- [[Profiling]] — sibling discipline; decomposes what benchmarking aggregates.
- [[HotSpot]] — what profiling finds and benchmarking measures progress against.
- [[GccOptLevels]] — the choice of `-O0` / `-O1` / `-O2` / `-O3` must be benchmarked, not assumed.
- [[CompilerOptimization]] — the umbrella the benchmark validates.
- [[dis-12-1-first-steps]] / [[dis-12-2-compiler-optimizations]] / [[dis-12-3-memory-considerations]] — canonical [[DiveIntoSystems]] sources.
