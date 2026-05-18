---
title: "Set Associative Cache"
type: concept
tags: [cache, memory-hierarchy, systems, hardware, architecture]
sources: [dis-11-4-caching]
last_updated: 2026-05-17
---

# Set Associative Cache

A **set associative cache** is the modern dominant [[CacheMemory|cache]] placement architecture. Each memory address maps to a **set** of **N [[CacheLine|cache lines]]** (typically **N = 2, 4, or 8** — called *"N-way set associative"*). Lookup checks all N tags **in parallel**; an incoming block can be placed in any of the N lines, and a [[CacheReplacementPolicy|replacement policy]] (usually [[LeastRecentlyUsed|LRU]]) selects the eviction victim when the set is full. *"Offers a good compromise between complexity and conflicts"* ([[dis-11-4-caching|DIS Ch 11.4]]).

## Lookup mechanism ([[dis-11-4-caching|DIS Ch 11.4]])

1. **Index** bits select a **set** (group of N lines).
2. **All N tag comparators run in parallel** against the high-order address bits.
3. **Valid bit + tag match** on any line → [[CacheHit|hit]]: offset bits extract bytes.
4. No match → [[CacheMiss|miss]]: fetch from [[RAM|main memory]], install into one of the N lines per the [[CacheReplacementPolicy|replacement policy]] (typically [[LeastRecentlyUsed|LRU]]).

The N parallel comparators are the hardware cost over [[DirectMappedCache|direct-mapped]]; associativity > 8 is rare because comparator-network depth begins to gate cycle time.

## Trade-offs

**Vs [[DirectMappedCache|direct-mapped]]**:
- Eliminates most **conflict misses** — N addresses sharing an index can coexist instead of evicting each other.
- Pays in extra parallel-tag-comparison hardware and a (small) increase in access latency.
- Requires per-set [[CacheReplacementPolicy|replacement metadata]] ([[LeastRecentlyUsed|LRU]] bits).

**Vs [[FullyAssociativeCache|fully associative]]**:
- Far cheaper lookup — only N comparators instead of *all-lines* comparators.
- Slightly higher conflict-miss rate, but in practice N = 8 captures nearly all the hit-rate gains of full associativity.

## Worked example

The chapter's two-way set-associative walkthrough on the same access trace that produced 2 conflict misses in a [[DirectMappedCache|direct-mapped]] cache produces **zero conflict misses** — the canonical pedagogical demonstration of the associativity-vs-conflict-miss trade.

## Real-world dominance

Modern CPU caches are universally set-associative:

- **L1 D-cache** — typically 8-way (Intel) or 4-way (some ARM).
- **L1 I-cache** — typically 4-way.
- **L2 cache** — typically 4–16 way.
- **L3 cache** — typically 12–24 way ([[CacheLevel|shared across cores]]).

[[CacheCoherency|Coherence protocols]] like [[MESI]] operate at cache-line granularity regardless of associativity.

## Connections

- [[CacheMemory]] — the parent storage tier.
- [[CacheLine]] — the unit each set holds N copies of.
- [[DirectMappedCache]] — the N=1 degenerate case; suffers more conflict misses.
- [[FullyAssociativeCache]] — the N=all-lines extreme; impractical at scale.
- [[CacheReplacementPolicy]] / [[LeastRecentlyUsed]] — selects eviction victim from the N candidates.
- [[CacheMiss]] — the conflict-miss class is the one associativity attacks.
- [[CacheLevel]] — L1 / L2 / L3 all use set-associative placement, with associativity typically increasing down the hierarchy.
- [[CacheCoherency]] — operates at line granularity regardless of set structure.
