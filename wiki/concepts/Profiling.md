---
title: "Profiling"
type: concept
tags: [systems, optimization, performance, valgrind, tooling]
sources: [dis-12-1-first-steps, dis-12-3-memory-considerations, dis-12-4-summary]
last_updated: 2026-05-17
---

# Profiling

The **empirical measurement** of a program's runtime behavior — which functions execute most often, how long they take, how much memory they allocate, how often the [[CacheMemory|cache]] misses — to identify the [[HotSpot|hot spots]] worth optimizing. [[DiveIntoSystems]] Ch 12 elevates profiling from a tool category to a **methodology**: *"Optimization should never be based on gut feelings"* ([[dis-12-4-summary]]).

## Why it precedes optimization

Without profiling, optimization effort is misallocated — programmers consistently mis-guess which code is slow. Ch 12.1 introduces the **profile-then-optimize loop**:

1. Run the program under a profiler.
2. Identify the function or loop consuming a disproportionate share of execution time / instructions / cache misses / memory.
3. Apply a targeted transformation.
4. Re-profile to verify improvement.
5. Stop when the [[HotSpot|hot spot]] is no longer dominant.

## Tooling: the Valgrind triad

[[DiveIntoSystems]] introduces three [[Valgrind]] sub-tools, each profiling a different dimension:

| Tool | Dimension | Source |
|---|---|---|
| [[Callgrind]] | Instructions per function | [[dis-12-1-first-steps]] |
| [[Cachegrind]] | [[CacheHit|Cache hits]] / [[CacheMiss|misses]] per source line | [[dis-11-5-cachegrind]] |
| [[Massif]] | Heap allocation over time | [[dis-12-3-memory-considerations]] |

> *"Tools like Valgrind enable data-driven decisions rather than assumptions about performance bottlenecks."* — [[dis-12-4-summary]]

## Worked example

Ch 12.1's `isPrime` profiling showed `sqrt` executing **2.7 million times** (20.5% of total instructions). [[Callgrind]] made the hot spot visible; loop-invariant code motion reduced `sqrt` to **100,001 calls** (96% reduction) and runtime by **47%**.

## Related disciplines

- **[[Benchmarking]]** — controlled performance measurement of full program runs (wall-clock, throughput); narrower than profiling, which decomposes time/resources per function or line.
- **Tracing** — chronological event recording (e.g., DTrace, eBPF); orthogonal to profiling, which aggregates.

## Connections

- [[Valgrind]] — the dynamic-analysis suite hosting [[Callgrind]] / [[Cachegrind]] / [[Massif]].
- [[Callgrind]] / [[Cachegrind]] / [[Massif]] — the three [[DiveIntoSystems]]-introduced profilers.
- [[HotSpot]] — the diagnostic target.
- [[Benchmarking]] — sibling discipline.
- [[CompilerOptimization]] — what profiling justifies.
- [[dis-12-1-first-steps]] / [[dis-12-3-memory-considerations]] / [[dis-12-4-summary]] — canonical sources.
