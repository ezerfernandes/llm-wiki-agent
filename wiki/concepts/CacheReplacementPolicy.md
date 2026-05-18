---
title: "Cache Replacement Policy"
type: concept
tags: [cache, memory-hierarchy, systems, hardware]
sources: [dis-11-4-caching]
last_updated: 2026-05-17
---

# Cache Replacement Policy

A **cache replacement policy** is the rule that decides **which existing [[CacheLine|cache line]] to evict** when a [[CacheMiss|miss]] requires installing a new block into an already-full set. The policy is irrelevant for [[DirectMappedCache|direct-mapped]] caches (one line per index — no choice), but central to [[SetAssociativeCache|set-associative]] and [[FullyAssociativeCache|fully associative]] designs where multiple lines compete for the same incoming block.

## Goals

The policy targets **hit-rate maximization** by predicting which line is *least likely to be used again soon*. Three classical options:

- **[[LeastRecentlyUsed|LRU]]** — evict the line whose last access is furthest in the past. Leverages [[TemporalLocality|temporal locality]]: *"recently used data is likely to be used again"* ([[dis-11-4-caching|DIS Ch 11.4]]). **Standard choice for general-purpose CPU caches.**
- **FIFO** — evict the line that has been resident longest, regardless of recent access. Simpler bookkeeping; worse hit rate.
- **Random** — evict an arbitrary line. Cheapest hardware; surprisingly competitive at high associativity.

LRU's optimality follows from temporal locality being the dominant program-behavior pattern; programs that violate temporal locality (streaming through gigabytes once) defeat LRU regardless of cache size.

## Metadata cost

LRU requires per-set bookkeeping bits to track access recency: roughly `log2(N)` bits per line for an N-way set, doubled to track the ordering. For high-associativity caches, **pseudo-LRU** approximations (binary-tree LRU, NRU) reduce metadata cost at modest hit-rate loss.

## Connections

- [[LeastRecentlyUsed]] — the canonical policy; uses [[TemporalLocality|temporal-locality]] as its predictive prior.
- [[CacheLine]] — the unit being evicted; the dirty bit ([[WriteBackCache|write-back]] caches) determines whether eviction requires a writeback.
- [[CacheMiss]] — the event that triggers replacement; the policy converts incoming-miss into outgoing-eviction.
- [[SetAssociativeCache]] / [[FullyAssociativeCache]] — the architectures where the policy matters.
- [[DirectMappedCache]] — replacement is trivial (one choice).
- [[TemporalLocality]] — the program property that justifies recency-based prediction.
- [[PageReplacementAlgorithm]] — the [[OperatingSystem|OS]]-level analog at the [[VirtualMemory|virtual-memory]] tier; same LRU / FIFO / clock heuristics scaled up.
