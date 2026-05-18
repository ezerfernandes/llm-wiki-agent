---
title: "Temporal Locality"
type: concept
tags: [systems, cache, memory, locality]
sources: [dis-11-3-locality, parproc-appA-systems-issues]
last_updated: 2026-05-17
---

# Temporal Locality

**Temporal locality** is the empirical observation that programs tend to access the same data repeatedly over a short time window. Per [[dis-11-3-locality|DIS Ch 11.3]]: *"if a program has used a variable recently, it's likely to use that variable again soon."* One of the two axes of [[LocalityOfReference|locality of reference]] — the sibling axis is [[SpatialLocality|spatial locality]].

## Canonical example (DIS)

[[dis-11-3-locality|Ch 11.3]] uses the array-sum loop as the textbook temporal-locality demonstration:

```c
int sum_array(int *array, int len) {
    int sum = 0;
    for (int i = 0; i < len; i++) {
        sum += array[i];
    }
    return sum;
}
```

Variables `i`, `sum`, and `array` are accessed **every iteration** — on a system with a [[CacheMemory|cache]], the first iteration's miss installs them in a fast tier; every subsequent iteration is a hit. Loop induction variables, accumulators, and base pointers are the canonical temporal-locality consumers.

## Why it matters

Temporal locality is the property that justifies:

- **[[CacheMemory|Caches]] of any kind** — small fast storage is only useful if the same items are referenced more than once before eviction.
- **[[LeastRecentlyUsed|LRU]] (and approximations) as block-replacement policy** — *least recently used* is the best heuristic for *least likely to be reused soon* precisely because temporal locality says recent items are likely to recur.
- **[[CpuRegister|Register allocation]]** — compilers exploit temporal locality at the smallest tier of the [[MemoryHierarchy|hierarchy]] by keeping frequently-referenced variables in [[CpuRegister|registers]] across many instructions.

## The mechanism in the hierarchy

| Tier | How temporal locality is exploited |
|---|---|
| [[CpuRegister|Register]] | Compiler keeps the variable resident across many instructions |
| [[CacheMemory|Cache]] (L1/L2/L3) | Hardware keeps the [[CacheLine|cache line]] resident until evicted by LRU-approximation |
| [[RAM]] | OS page replacement keeps the page resident until evicted by working-set / LRU |
| Disk | Filesystem cache keeps file blocks in RAM until evicted |

Each tier is a smaller, faster slice of the one below — and temporal locality is *the* property that makes the layered design pay off.

## Connections

- [[LocalityOfReference]] — umbrella concept; temporal + [[SpatialLocality|spatial]] together.
- [[SpatialLocality]] — sibling axis: access *nearby* items vs (here) the *same* item.
- [[WorkingSet]] — the currently-active subset; small working sets benefit most from temporal locality.
- [[CacheMemory]] / [[CacheLine]] — temporal locality is what makes cache hits common.
- [[dis-11-3-locality]] — primary DIS source.
- [[parproc-appA-systems-issues]] — prior wiki treatment (parallel-programming perspective).
