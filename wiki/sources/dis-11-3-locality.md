---
title: "Dive into Systems — Ch 11.3 Locality"
type: source
tags: [textbook, systems, locality, cache, memory-hierarchy, dis]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C11-MemHierarchy/locality.html
---

## Summary

**Third leaf of Ch 11 *The Memory Hierarchy*** of *[[DiveIntoSystems]]* — pivots from [[dis-11-2-storage-devices|Ch 11.2]]'s storage-device taxonomy into the **empirical program-behavior property** that makes the entire [[MemoryHierarchy|memory hierarchy]] workable: **locality**. The section codifies the **two-axis locality taxonomy** — *"the two basic forms of locality are temporal locality and spatial locality"* — frames locality as the system-designer's exploit (move frequently-accessed data to fast storage, leave the rest in slow storage), and shows the **programmer-side payoff** via a worked **5× speedup on row-major vs column-major matrix traversal**. **108th ingested DIS chapter — third leaf of Ch 11.**

## Key Claims

- **Two forms of locality.** *"Programs tend to access the same data repeatedly over time"* ([[TemporalLocality|temporal]]) and *"programs tend to access data that is nearby other, previously accessed data. 'Nearby' here refers to the data's memory address"* ([[SpatialLocality|spatial]]) — the two empirical regularities that justify caching.
- **Locality is what makes the [[MemoryHierarchy|hierarchy]] workable.** System designers exploit locality to provide *"the illusion of having massive fast memory"* — frequently-accessed data lives in [[CpuRegister|registers]] / [[CacheMemory|cache]], infrequently-used data lives in [[RAM|main memory]] / disk; the hierarchy works because real programs concentrate accesses, not because hardware is fast.
- **Loop-variable access is the canonical temporal-locality example.** In `sum_array`'s `for (i = 0; i < len; i++) sum += array[i];`, the variables `i`, `sum`, and `array` are *"repeatedly accessed each iteration"* — temporal locality on the control variables of the loop.
- **[[CacheLine|Block-granularity]] cache fetching is the spatial-locality mechanism.** Systems load multiple consecutive integers into [[CacheMemory|cache]] simultaneously via the block / [[CacheLine|cache-line]] mechanism — so `array[i+1]`'s first access is a hit if `array[i]` was just touched.
- **Access-order can produce 5× speedup at no algorithmic cost** (headline programmer takeaway). The two-loop matrix sum — **row-major** `mat[i][j]` (sequential addresses, sequential cache lines) vs **column-major** `mat[j][i]` (jumping rows, repeated cache misses) — produces *"approximately five times faster"* execution for the row-major form. The C compiler emits identical-shape loops; the speedup comes entirely from access pattern alignment with [[RowMajorOrder|row-major]] memory layout.
- **Locality unlocks programmer agency.** *"Programmers can significantly influence execution costs through intentional memory access patterns"* — the systems-level analog of the [[dis-11-1-memory-hierarchy|Ch 11.1]] *"performance-critical code sections may justify such optimization"* commitment.

## Key Quotes

> "The two basic forms of locality are temporal locality and spatial locality." — defining quote of section 11.3.

> "Programs tend to access the same data repeatedly over time. That is, if a program has used a variable recently, it's likely to use that variable again soon." — temporal locality.

> "Programs tend to access data that is nearby other, previously accessed data. 'Nearby' here refers to the data's memory address." — spatial locality.

> "[Row-major access] executes approximately five times faster than [column-major access]." — the headline programmer payoff.

## Connections

- [[DiveIntoSystems]] — Ch 11.3 is the **third leaf of Ch 11 *The Memory Hierarchy*** — **108th ingested DIS chapter**, following [[dis-11-2-storage-devices|Ch 11.2 *Storage Devices*]] (107th) and [[dis-11-1-memory-hierarchy|Ch 11.1 *The Memory Hierarchy*]] (106th).
- [[dis-11-2-storage-devices]] — prior leaf; supplied the device technologies and latency numbers; 11.3 supplies the program-behavior property that makes hierarchy across those devices *work*.
- [[dis-11-1-memory-hierarchy]] — opening leaf of Ch 11; explicitly deferred the *locality* discussion to 11.3, now delivered.
- [[LocalityOfReference]] — the canonical umbrella concept page, previously sourced from [[parproc-appA-systems-issues|ParProc App A]]; **expanded in place** by this ingest with [[DiveIntoSystems|DIS]]'s explicit code examples (`sum_array` for temporal-and-spatial, row-major vs column-major matrix for spatial 5× speedup) and the *system-designer-illusion* framing.
- [[TemporalLocality]] — **new concept page** minted by this ingest; codifies the *re-access the same item* axis with the `sum_array` loop-variable example.
- [[SpatialLocality]] — **new concept page** minted by this ingest; codifies the *access nearby items* axis with the [[CacheLine|block-granularity]] mechanism and the row-major matrix example.
- [[WorkingSet]] — **new concept page** minted by this ingest; the *currently-active subset of memory* that locality keeps small and resident — the underlying property that makes caches effective.
- [[CacheMemory]] / [[CacheLine]] — the fast-storage tier whose existence is *justified* by locality; the [[CacheLine|cache line / block]] is the granularity at which spatial locality is exploited.
- [[RowMajorOrder]] — the [[CLanguage|C]] 2D-array memory layout convention that makes `mat[i][j]` traversal cache-friendly and `mat[j][i]` traversal cache-hostile; the 5× speedup is the empirical signature of [[RowMajorOrder|row-major]] aligning with spatial locality.
- [[MemoryHierarchy]] — the structural backdrop; locality is *why* the hierarchy works.
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — co-authors.

## Contradictions

None. Ch 11.3's two-axis ([[TemporalLocality|temporal]] / [[SpatialLocality|spatial]]) taxonomy matches the prior [[LocalityOfReference]] treatment from [[parproc-appA-systems-issues|ParProc App A]]; [[DiveIntoSystems|DIS]] adds the explicit code examples and the 5× speedup measurement not previously surfaced.
