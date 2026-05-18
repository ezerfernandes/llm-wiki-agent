---
title: "Direct-Mapped Cache"
type: concept
tags: [cache, memory-hierarchy, systems, hardware, architecture]
sources: [dis-11-4-caching]
last_updated: 2026-05-17
---

# Direct-Mapped Cache

A **direct-mapped cache** is the simplest [[CacheMemory|cache]] placement architecture: each memory address maps to **exactly one** [[CacheLine|cache line]]. Determined by the **index** bits of the address — `line_id = index_bits(address)` — with no flexibility and no choice. The simplest design, but suffers the highest **conflict-miss rate** of the three placement families.

## Lookup mechanism ([[dis-11-4-caching|DIS Ch 11.4]])

A direct-mapped lookup is four deterministic steps:

1. **Index** bits select the unique candidate line.
2. The line's **valid bit** is checked — must be `1`.
3. The line's **tag** field is compared against the high-order address bits — must match.
4. If both hold → [[CacheHit|hit]]: offset bits extract the desired bytes from the block. Otherwise → [[CacheMiss|miss]]: fetch from [[RAM|main memory]], install in this line (evicting whatever was there).

No replacement policy required — eviction target is always *the* line at this index.

## Trade-offs

**Advantages**:
- Cheapest lookup hardware — single tag comparator, single line check, no parallel-comparator network.
- Lowest access latency at fixed transistor budget — minimal critical-path delay.
- No replacement-policy metadata bits.

**Weakness — conflict misses dominate**:
- Two hot addresses mapping to the same index ping-pong each other out indefinitely, even when the rest of the cache sits idle. *"Direct-mapped designs suffer most from conflict misses"* ([[dis-11-4-caching]]).
- Pathological example: looping over two arrays whose elements share index bits — every access misses despite vast empty cache space.

## Worked example

The chapter's worked walkthrough runs the **same access trace** through a direct-mapped cache and a two-way [[SetAssociativeCache|set-associative]] cache of equal total size. The direct-mapped design suffers **2 conflict misses** where the set-associative design suffers **0** — the canonical demonstration that associativity attacks conflict misses.

## Where direct-mapped survives

Modern L1 / L2 / L3 caches are universally [[SetAssociativeCache|set-associative]] for hit-rate reasons, but direct-mapped persists in:

- **Embedded / microcontroller** caches — gate-count budget rules out associativity.
- **Branch-prediction structures** (some BTB designs) — speed > accuracy.
- **L3 victim caches** in some older AMD designs.

## Connections

- [[CacheMemory]] — the parent storage tier.
- [[CacheLine]] — what an index selects.
- [[SetAssociativeCache]] — the middle-ground successor that mitigates conflict misses.
- [[FullyAssociativeCache]] — the maximum-flexibility extreme.
- [[CacheMiss]] — conflict-miss is the failure mode direct-mapped is most prone to.
- [[CacheReplacementPolicy]] — trivial here (no choice); meaningful only in higher-associativity designs.
- [[LocalityOfReference]] — direct-mapped exploits [[TemporalLocality|temporal]] and [[SpatialLocality|spatial]] locality but can be defeated by index-aliased access patterns.
