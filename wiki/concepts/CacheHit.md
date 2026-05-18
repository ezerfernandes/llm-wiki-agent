---
title: "Cache Hit"
type: concept
tags: [cache, memory-hierarchy, systems, hardware]
sources: [dis-11-4-caching]
last_updated: 2026-05-17
---

# Cache Hit

A **cache hit** occurs when the [[CPU]] requests data at a memory address and finds that data already present in the [[CacheMemory|cache]] — the request is satisfied from fast on-chip storage **without** stalling for [[RAM|main memory]]. The hit/miss outcome is the central performance lever of the [[MemoryHierarchy|memory hierarchy]]: a single L1 hit takes ~1 ns; a miss to DRAM takes ~100 ns — a **~100× gap**.

## Mechanism ([[dis-11-4-caching|DIS Ch 11.4]])

Hardware sends each memory address simultaneously to the [[CacheMemory|cache]] and to [[RAM|main memory]]. The cache responds faster:

1. The **index** bits select a [[CacheLine|cache line]] (or set).
2. The **valid bit** is checked — must be `1`.
3. The **tag** field is compared against the high-order address bits — must match.
4. If both conditions hold → **cache hit**: the **offset** bits extract the desired bytes from the data block.
5. The CPU cancels the pending [[RAM|main-memory]] request (which would have completed later).

## Hit-rate as the performance metric

The fraction of accesses that hit — the **hit rate** — captures cache effectiveness. Hit rates of **>90 %** are routine on programs with good [[LocalityOfReference|locality]] (see [[parproc-appA-systems-issues|ParProc App A]]). Because the miss penalty is ~100× the hit cost, even small hit-rate drops dominate average memory-access time:

```
AMAT = hit_time + miss_rate × miss_penalty
```

A 95 % → 90 % hit-rate degradation roughly **doubles** AMAT.

## Connections

- [[CacheMemory]] — the storage tier where hits land.
- [[CacheMiss]] — the complementary outcome; together they partition every memory access.
- [[CacheLine]] — the unit the tag/valid check identifies.
- [[LocalityOfReference]] — the empirical property that makes hits the common case.
- [[TemporalLocality]] — re-accessing the same line → hit on the second access.
- [[SpatialLocality]] — accessing a neighbor within the same line → hit on first access.
- [[CacheLevel]] — multi-level caches give multiple chances to hit before falling through to [[RAM]].
