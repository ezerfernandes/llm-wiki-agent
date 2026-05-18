---
title: "Dive into Systems — Ch 12.3 Memory Considerations"
type: source
tags: [systems, optimization, memory, cache, locality, valgrind]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C12-CodeOpt/memory_considerations.html
---

## Summary
Chapter 12.3 of *[[DiveIntoSystems]]* is the **third leaf** of Ch 12 *Code Optimization* — the **memory-locality lens** the [[CCompiler|compiler]] usually **cannot** optimize for programmers. Three transformations dominate: **loop interchange** (reorder nested loops so the innermost stride matches [[CacheLine|cache-line]] layout), **loop fission** (split a loop body into multiple loops for locality / multicore distribution), and **loop fusion** (the inverse — combine loops over the same range). Headline empirical result: reordering nested loops in a 10,000 × 10,000 matrix-vector multiply collapses **2.01 s → 0.27 s** — a **~8× speedup** at **zero algorithmic-complexity change**. The chapter introduces **[[Massif]]** — [[Valgrind]]'s heap-profiling tool — alongside [[Callgrind]] from [[dis-12-1-first-steps|Ch 12.1]], completing the [[Valgrind]] optimization-tools triad with [[Cachegrind]] from [[dis-11-5-cachegrind|Ch 11.5]].

## Key Claims
- **Loop interchange**: reordering nested loops to traverse [[RowMajorOrder|row-major]] aligned strides converts massive [[CacheMiss|cache miss]] storms into [[CacheHit|cache hits]] — *"data is loaded into cache in blocks not elements"*.
- **Empirical headline**: matrixVector multiply, 10,000 × 10,000 — original column-stride version **2.01 s**; row-stride reorder **0.27 s** = **~8× speedup**, zero algorithm change.
- **Loop fission**: splits one loop into two over the same range — can improve locality (smaller per-loop working set) and enables multicore work distribution.
- **Loop fusion**: combines loops over the same range — inverse of fission; reduces loop overhead and may improve [[TemporalLocality|temporal locality]] when the two bodies touch the same data.
- **Compiler limitation**: *"compilers cannot always optimize memory use automatically"* — manual transformations needed for cache-sensitive workloads.
- **[[Massif]] memory profiler**: [[Valgrind]] tool that profiles **heap allocation over time** — identifies memory leaks (unmatched `malloc`/`free`), peak heap usage, per-function allocation breakdown.
- **Massif empirical example**: the matrixVector program — 800 MB total allocation, **99.96% in the allocation function alone**.
- **Memory > instructions for cache-bound work**: *"Memory access patterns and cache locality often impact performance more significantly than instruction count"*.

## Key Quotes
> "Data is loaded into cache in blocks not elements." — the [[CacheLine|cache-line]] axiom that makes loop interchange profitable.

> "Compilers cannot always optimize memory use automatically." — the warrant for manual memory-pattern restructuring.

## Connections
- [[DiveIntoSystems]] — **116th ingested chapter — third leaf of Ch 12**.
- [[dis-12-2-compiler-optimizations|Ch 12.2]] — preceding leaf on compiler-side optimizations; this chapter pivots to the **programmer-side** memory dimension.
- [[dis-11-3-locality|Ch 11.3]] / [[dis-11-4-caching|Ch 11.4]] / [[dis-11-5-cachegrind|Ch 11.5]] — the [[LocalityOfReference|locality]] / [[CacheMemory|cache]] / [[Cachegrind]] foundations this chapter applies.
- [[LocalityOfReference]] / [[SpatialLocality]] / [[TemporalLocality]] — the principles loop interchange exploits.
- [[CacheLine]] / [[CacheMiss]] / [[CacheHit]] — the cache mechanics that explain the 8× speedup.
- [[RowMajorOrder]] — the [[CLanguage|C]] matrix layout that aligns with the interchange direction.
- [[Massif]] — new concept page; [[Valgrind]] heap profiler.
- [[Valgrind]] / [[Cachegrind]] / [[Callgrind]] — sibling tools.
- [[CompilerOptimization]] — umbrella.
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — authors.

## Contradictions
None.
