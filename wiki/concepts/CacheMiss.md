---
title: "Cache Miss"
type: concept
tags: [cache, memory-hierarchy, systems, hardware, performance]
sources: [dis-11-4-caching]
last_updated: 2026-05-17
---

# Cache Miss

A **cache miss** occurs when the [[CPU]] requests a memory address that is **not** currently held in the [[CacheMemory|cache]] — the [[CPU]] must wait for the slower [[RAM|main-memory]] access to complete. On completion, hardware loads the retrieved block into a [[CacheLine|cache line]] *"so that subsequent requests for the same address... can be serviced quickly"* ([[dis-11-4-caching|DIS Ch 11.4]]) — the mechanism that converts a one-time miss into a stream of future hits.

## The 3C miss taxonomy ([[dis-11-4-caching|DIS Ch 11.4]])

Every miss falls into one of three structural categories — the classic **3C model**:

- **Compulsory miss** (cold miss) — the first access to a block the cache has never seen. Unavoidable: even an infinite-capacity cache suffers compulsory misses on every distinct block touched.
- **Capacity miss** — the line was evicted because the program's [[WorkingSet|working set]] exceeds total cache capacity. Fix: increase cache size or shrink the working set.
- **Conflict miss** — the line was evicted because **placement restrictions** forced contention even though cache space was free elsewhere. The miss class [[SetAssociativeCache|set-associative]] caches are built to attack — increasing associativity converts conflict misses to hits at the cost of parallel tag comparison.

## Miss penalty dominates AMAT

The miss penalty (~100 ns to [[DRAM]], ~5–10 ms to [[HardDisk|HDD]]) is **orders of magnitude** larger than the hit time, so even a low miss rate dominates average memory-access time:

```
AMAT = hit_time + miss_rate × miss_penalty
```

This is why the 5× speedup of row-major vs column-major matrix traversal ([[dis-11-3-locality|Ch 11.3]]) is real: column-major produces a conflict-/capacity-miss avalanche.

## Connections

- [[CacheHit]] — complementary outcome.
- [[CacheLine]] — the unit fetched on a miss; sized 16–64 bytes typically.
- [[CacheReplacementPolicy]] — selects which existing line to evict to make room for the missing block; [[LeastRecentlyUsed|LRU]] is canonical.
- [[DirectMappedCache]] / [[SetAssociativeCache]] — placement design directly determines conflict-miss rate.
- [[WorkingSet]] — when working set exceeds cache size, capacity misses dominate.
- [[LocalityOfReference]] — programs with poor locality miss frequently; programs with good locality miss rarely.
- [[Cachegrind]] — Valgrind tool for measuring miss rates by miss-class (deferred to [[dis-11-5-cache-analysis-cachegrind|Ch 11.5]]).
