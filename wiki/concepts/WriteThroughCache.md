---
title: "Write-Through Cache"
type: concept
tags: [cache, memory-hierarchy, systems, hardware, write-policy]
sources: [dis-11-4-caching]
last_updated: 2026-05-17
---

# Write-Through Cache

A **write-through cache** is the simpler cache **write policy**: when the CPU writes to a memory address, **both** the [[CacheMemory|cache]] and [[RAM|main memory]] are updated **simultaneously**. The cache and main memory are *always in sync* — no **dirty bit** is needed. The cost: every write pays the [[RAM|main-memory]] latency, even when the same location is written repeatedly.

## Mechanism ([[dis-11-4-caching|DIS Ch 11.4]])

On a **write hit**:
1. Update the data block in the [[CacheLine|cache line]].
2. **Simultaneously** write the same data to [[RAM|main memory]].
3. No dirty-bit bookkeeping required.

On eviction:
- **No writeback needed** — every line in the cache is already coherent with [[RAM]].
- Simply install the incoming block.

## Trade-offs

**Vs [[WriteBackCache|write-back]]**:
- **Simpler hardware** — no dirty bit, no writeback path on eviction, no special handling of dirty-shared states in [[CacheCoherency|coherence]].
- **Bandwidth-hungry** — every store hits the [[MemoryBus|memory bus]]; loop-counter-style repeated writes pay the cost every iteration instead of once at eviction.
- Often paired with a **write buffer** that batches writes to amortize the latency penalty.

**[[CacheCoherency|Coherence]] advantage**:
- Multi-core write-through caches see a single coherent view of memory — every write is immediately visible system-wide. Modern multi-core CPUs nonetheless adopt [[WriteBackCache|write-back]] (with explicit coherence protocols like [[MESI]]) because the bandwidth penalty of write-through is unacceptable at memory speeds.

## Where write-through persists

Despite being dominated by [[WriteBackCache|write-back]] for general-purpose CPU caches, write-through survives in:

- **Some L1 caches** that pair with a write-buffer / store-queue (older designs, some embedded).
- **GPU caches** — many GPU memory hierarchies use write-through at the L1 level for simplicity.
- **Embedded / microcontroller caches** — gate-count savings outweigh bandwidth costs.
- **Safety-critical contexts** — guaranteeing RAM-cache equality simplifies failure recovery.

## Connections

- [[WriteBackCache]] — the modern dominant alternative; trades bandwidth savings for coherence complexity.
- [[CacheMemory]] — the parent storage tier.
- [[CacheLine]] — does **not** need the dirty bit.
- [[CacheCoherency]] — write-through gives natural coherence; write-back requires explicit protocols.
- [[MemoryBus]] — bandwidth on this bus is what write-through consumes.
- [[CacheMiss]] — write misses still occur; policy applies only to write hits.
