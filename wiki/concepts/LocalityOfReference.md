---
title: "Locality of Reference"
type: concept
tags: [systems, performance, cache, memory]
sources: [parproc-appA-systems-issues, dis-11-3-locality, mlsysbook-ch03-ml-workflow]
last_updated: 2026-06-05
---

# Locality of Reference

**Locality of reference** is the empirical observation that most programs access memory in clustered patterns rather than uniformly at random. It is the property that makes [[CacheMemory|caches]] and [[VirtualMemory|virtual memory]] practical: despite caches being tiny relative to RAM, hit rates typically exceed 90%.

## Two kinds of locality

- **[[TemporalLocality|Temporal locality]]**: a program tends to access the same memory item repeatedly within a short time window. On first access the item is fetched into cache; subsequent accesses within the window hit the cache. [[dis-11-3-locality|DIS Ch 11.3]]: *"if a program has used a variable recently, it's likely to use that variable again soon."*
- **[[SpatialLocality|Spatial locality]]**: a program tends to access items that are near each other in memory within a short time window. Because cache operates at the granularity of a block ([[CacheLine|cache line]]), fetching one item pre-loads its neighbors, which are likely to be accessed soon. [[dis-11-3-locality|DIS Ch 11.3]]: *"'nearby' here refers to the data's memory address."*

## DIS row-major-vs-column-major payoff

[[dis-11-3-locality|DIS Ch 11.3]] supplies the canonical empirical demonstration: identical matrix-sum algorithms differing only in inner-loop access (`mat[i][j]` vs `mat[j][i]`) execute ~**5× apart in wall-clock time** — the row-major form aligns with C's [[RowMajorOrder|row-major]] memory layout and reaps spatial locality; the column-major form jumps cache lines and incurs near-100% miss rate. Programmer-side: access pattern dominates execution cost at zero algorithmic-complexity change.

## Practical consequences

- **Cache hit rates above 90%** for typical workloads, despite cache being much smaller than RAM (per [[parproc-appA-systems-issues]] §A.2.3).
- **Block replacement policies** such as LRU exploit temporal locality: the least recently used block is least likely to be needed again soon.
- **Page fault rates** are also governed by locality: programs with good spatial locality keep their working set small and resident in RAM.

## Implications for parallel programming

Parallel programs must be designed to preserve locality:

- **[[RowMajorOrder]]**: access C/C++ 2D arrays with the rightmost (fastest-varying) index in the innermost loop to traverse cache lines sequentially.
- **Data partitioning**: assign contiguous data chunks to each thread so that each thread's working set fits in cache and threads do not compete for cache lines (avoiding [[FalseSharing]]).
- **Tiling / blocking**: restructure loop nests so that each tile's data fits in cache before moving to the next tile (classical cache-oblivious technique used in matrix multiplication and stencil codes).

## Connections

- [[parproc-appA-systems-issues]] — §A.2.3; original wiki source (parallel-programming perspective).
- [[dis-11-3-locality]] — [[DiveIntoSystems]] Ch 11.3 — systems-textbook perspective with code examples and the 5× row-vs-column matrix benchmark.
- [[TemporalLocality]] — first axis (re-access the same item) as its own concept page.
- [[SpatialLocality]] — second axis (access nearby items) as its own concept page.
- [[WorkingSet]] — the *size* property locality controls; small working sets keep programs running at fast-tier speed.
- [[CacheMemory]] / [[CacheLine]] — locality is the reason caches are effective; cache-line granularity is where spatial locality cashes in.
- [[VirtualMemory]] — locality also limits page fault rates.
- [[MemoryHierarchy]] — locality is the key property that makes the full hierarchy workable.
- [[RowMajorOrder]] — the C/C++ array layout that aligns with spatial locality.
- [[gpumemoryhierarchy]] — GPU shared memory reuse requires similar locality reasoning within a thread block.
- [[mlsysbook-ch03-ml-workflow]] — argues ML training *violates* this 50-year OS assumption at scale: randomly shuffling a multi-TB dataset every epoch is the worst case for VM prefetchers (L1 ~1 ns vs. DRAM 50–100 ns vs. NVMe 10–100 µs), forcing ML data loaders to implement their own prefetching rather than trusting the OS page cache.
