---
title: "Spatial Locality"
type: concept
tags: [systems, cache, memory, locality]
sources: [dis-11-3-locality, parproc-appA-systems-issues]
last_updated: 2026-05-17
---

# Spatial Locality

**Spatial locality** is the empirical observation that programs tend to access data that is *nearby* other, previously accessed data — *"'nearby' here refers to the data's memory address"* ([[dis-11-3-locality|DIS Ch 11.3]]). One of the two axes of [[LocalityOfReference|locality of reference]] — the sibling axis is [[TemporalLocality|temporal locality]] (access the *same* item again, vs here a *nearby* item).

## The mechanism: cache-line / block fetch

Spatial locality is exploited because [[CacheMemory|caches]] operate at the granularity of a **block** (a [[CacheLine|cache line]] — typically 64 bytes on modern systems), not individual bytes. Fetching one element pulls its neighbors into the cache for free. Subsequent accesses to those neighbors are hits even though they were never explicitly demanded.

In [[dis-11-3-locality|DIS Ch 11.3]]'s `sum_array` example, spatial locality emerges because *"the system loads multiple consecutive integers into cache simultaneously via the block size mechanism"* — each cache miss on `array[i]` pre-loads `array[i+1]`, `array[i+2]`, ... up to the cache line boundary.

## Canonical demonstration: row-major vs column-major (DIS 11.3)

The headline programmer payoff from [[dis-11-3-locality|Ch 11.3]] — the same matrix-sum algorithm written two ways:

| Form | Inner access | Memory stride | Speed |
|---|---|---|---|
| Row-major | `mat[i][j]` | sequential ([[RowMajorOrder|row-major]] aligned) | baseline |
| Column-major | `mat[j][i]` | jumps `cols * sizeof(int)` bytes per step | ~**5× slower** |

The 5× gap comes entirely from spatial locality:

- **Row-major** access walks contiguous addresses → one cache miss per cache line → subsequent N elements are free hits.
- **Column-major** access jumps over a full row per step → each access is on a different cache line → near-100% miss rate.

The C compiler emits identical-shape loops. The speedup is purely a function of memory access pattern aligning (or not) with [[RowMajorOrder|C's row-major]] 2D-array layout.

## Why it matters

Spatial locality is the property that justifies:

- **[[CacheLine|Cache-line / block-size]] granularity** larger than one word — without spatial locality, fetching neighbors would be wasted bandwidth.
- **Hardware [[Prefetching|prefetchers]]** that detect sequential strides and pre-load further-ahead lines.
- **OS page-size granularity** (4 KiB or larger) — pages bundle spatially-close virtual addresses for the same reason.
- **[[RowMajorOrder|Row-major iteration discipline]]** in C/C++ — innermost loop walks the fastest-varying index so the inner loop sees sequential addresses.

## Connections

- [[LocalityOfReference]] — umbrella concept; [[TemporalLocality|temporal]] + spatial together.
- [[TemporalLocality]] — sibling axis: access the *same* item vs (here) a *nearby* item.
- [[CacheLine]] / [[CacheMemory]] — the cache-line / block is the granularity at which spatial locality pays off.
- [[RowMajorOrder]] — the C/C++ layout convention that aligns with spatial locality for the canonical inner loop.
- [[WorkingSet]] — programs with good spatial locality keep their working set small (many references hit few pages / lines).
- [[Prefetching]] — hardware extrapolation of spatial-locality patterns into pre-loaded blocks.
- [[dis-11-3-locality]] — primary DIS source; supplies the 5× row-vs-column speedup.
- [[parproc-appA-systems-issues]] — prior wiki treatment (parallel-programming perspective).
