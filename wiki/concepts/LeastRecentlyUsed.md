---
title: "Least Recently Used (LRU)"
type: concept
tags: [cache, memory-hierarchy, systems, hardware, algorithm, replacement-policy]
sources: [dis-11-3-locality, dis-11-4-caching]
last_updated: 2026-05-17
---

# Least Recently Used (LRU)

**Least Recently Used** is the canonical [[CacheReplacementPolicy|cache replacement policy]]: when a [[CacheMiss|cache miss]] requires installing a new block into a full set, the line whose **last access** is furthest in the past is evicted. The justification is one of the most robust empirical regularities in computing: *"recently used data is likely to be used again"* ([[dis-11-4-caching|DIS Ch 11.4]]) — the [[TemporalLocality|temporal-locality]] axiom.

## Why LRU works

Real programs exhibit strong [[TemporalLocality|temporal locality]]: loop variables, stack-frame slots, hot data structures, and constant tables are re-accessed many times within short windows. The line *least* recently touched is the line most likely to be either (a) outside the current [[WorkingSet|working set]], or (b) accessed only sparsely going forward. Evicting it minimizes expected future miss probability.

## Implementation cost

True LRU requires tracking the full access-order ranking of every line in a set:

- For an N-way set, ~`N × log2(N)` bits of metadata.
- Every hit updates the ranking (an O(log N) hardware operation).
- Cost grows quickly with associativity → high-associativity caches use **pseudo-LRU** approximations:
  - **Binary-tree LRU** (BTL / tree-PLRU) — N−1 bits per set, log N depth.
  - **Not-Recently-Used (NRU)** — single recency bit per line, periodically cleared.

## Worked behavior ([[dis-11-4-caching|DIS Ch 11.4]])

In the chapter's two-way set-associative walkthrough, the same access trace that produces 2 conflict misses in a [[DirectMappedCache|direct-mapped]] cache produces **zero conflict misses** under LRU + 2-way associativity — every potential conflict pair survives because LRU keeps both contenders alive until natural recency-based eviction.

## Where LRU breaks

LRU is **defeated** by access patterns that have no temporal locality:

- **Streaming traversals** (sequential read once through a gigabyte) — every line touched once and never again; LRU pessimally retains useless lines.
- **Working sets just larger than cache** — LRU thrashes (the *Belady anomaly* with FIFO is the dual pathology).

Modern caches mitigate via **bypass / non-temporal hints** (`MOVNTQ`, `_mm_stream_*`) that tell the cache to skip insertion.

## Connections

- [[CacheReplacementPolicy]] — the policy family LRU heads.
- [[TemporalLocality]] — the property LRU exploits ([[dis-11-3-locality|Ch 11.3]]).
- [[CacheLine]] — the unit being evicted.
- [[SetAssociativeCache]] / [[FullyAssociativeCache]] — the architectures where LRU is meaningful.
- [[WorkingSet]] — when working set ≤ cache, LRU keeps it fully resident.
- [[PageReplacementAlgorithm]] — the [[OperatingSystem|OS]] / [[VirtualMemory|VM]] analog (clock, LRU-K, ARC).
- [[Cache]] — analog of the LRU eviction heuristic in [[LLM|LLM]] [[KVCache|KV-cache]] / [[PromptCache|prompt-cache]] systems.
