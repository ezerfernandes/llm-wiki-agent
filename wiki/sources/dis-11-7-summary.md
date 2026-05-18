---
title: "Dive into Systems — Ch 11.7 Summary"
type: source
tags: [systems, memory-hierarchy, cache, summary]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C11-MemHierarchy/summary.html
---

## Summary
Chapter 11.7 of *[[DiveIntoSystems]]* is the **single-page summary** of Ch 11 *The Memory Hierarchy*. It recapitulates the chapter's seven structural commitments: the storage-device **performance/capacity/cost/volatility trade-off** ([[dis-11-2-storage-devices|Ch 11.2]]), the **hierarchical organization** ([[dis-11-1-memory-hierarchy|Ch 11.1]]), the **data-management strategy** of keeping hot data in fast storage, the **two-axis [[LocalityOfReference|locality]] taxonomy** ([[dis-11-3-locality|Ch 11.3]]), the **[[CacheMemory|CPU cache]] mechanism** as locality's hardware exploit ([[dis-11-4-caching|Ch 11.4]]), the **tag/index/offset address-decoding** decomposition (also Ch 11.4), and **[[Cachegrind]] empirical performance profiling** ([[dis-11-5-cachegrind|Ch 11.5]]). Closes with a Further Reading pointer.

## Key Claims
- **Storage-device trade-off**: devices *"balance competing priorities like access latency, storage capacity, transfer latency, and cost"* — no single device optimizes all four.
- **Hierarchical organization**: fast/small primary ([[CpuRegister|registers]], [[CacheMemory|caches]], [[RAM|main memory]]) at the top; slow/dense secondary ([[SolidStateDrive|SSDs]], [[HardDisk|HDDs]]) below.
- **Data-management strategy**: *"data that's being actively used"* lives in faster storage; rarely-used data sinks to slower tiers.
- **Two locality axes**: [[TemporalLocality|temporal]] (repeated access to the same data) and [[SpatialLocality|spatial]] (access near previously accessed locations) — both empirical program-behavior properties.
- **Cache mechanism**: CPU caches hold *"a small subset of main memory in fast storage directly on the CPU chip"*, checking there before [[RAM|main memory]].
- **Address decoding**: three bit-field slices per address — **index** (which cache set), **tag** (which memory block), **offset** (which byte in the line) — same decomposition Ch 11.4 introduces.
- **Performance profiling**: *"Cachegrind enables analysis of cache interactions, measuring statistics including hit and miss rates"* — the [[Valgrind]] sibling tool from [[dis-11-5-cachegrind|Ch 11.5]].
- **Licensing**: CC BY-NC-ND 4.0.

## Key Quotes
> "Data that's being actively used in faster storage devices." — the universal data-placement heuristic that the entire hierarchy optimizes for.

## Connections
- [[dis-11-1-memory-hierarchy|Ch 11.1]] / [[dis-11-2-storage-devices|Ch 11.2]] / [[dis-11-3-locality|Ch 11.3]] / [[dis-11-4-caching|Ch 11.4]] / [[dis-11-5-cachegrind|Ch 11.5]] / [[dis-11-6-cache-coherency|Ch 11.6]] — the six leaf chapters this summary distills.
- [[MemoryHierarchy]] — the umbrella concept the chapter chartered.
- [[LocalityOfReference]] / [[TemporalLocality]] / [[SpatialLocality]] — the two-axis theory.
- [[CacheMemory]] / [[CacheHit]] / [[CacheMiss]] / [[CacheLine]] / [[CacheLevel]] — the mechanism vocabulary.
- [[Cachegrind]] — the measurement tool.
- [[DiveIntoSystems]] — 112th ingested chapter; **seventh leaf of Ch 11**.
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — authors.

## Contradictions
None. Pure recap.
