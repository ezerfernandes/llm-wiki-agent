---
title: "Cache Line"
type: concept
tags: [cache, memory-hierarchy, systems, hardware]
sources: [dis-11-3-locality, dis-11-4-caching]
last_updated: 2026-05-17
---

# Cache Line

The **cache line** (also called a **cache block**) is the unit of storage inside a [[CacheMemory|CPU cache]]: a fixed-size chunk of consecutive bytes copied between [[RAM|main memory]] and cache as one atomic transfer. Each line bundles a **data block** (the program data) together with **metadata** that lets the hardware identify and validate the contents.

## Anatomy ([[dis-11-4-caching|DIS Ch 11.4]])

A cache line holds:

- **Cache data block** — typically **16–64 bytes** of consecutive program data. The block size is the granularity at which the hardware exploits [[SpatialLocality|spatial locality]] — fetching `array[i]` brings `array[i+1]` ... `array[i+block/4]` along for free.
- **Valid bit** — `1` if the line currently holds meaningful data, `0` if uninitialized or invalidated. Cleared at boot and on coherence-protocol invalidations.
- **Tag** — the high-order address bits identifying *which* region of [[RAM|main memory]] this line currently mirrors. The hardware compares the tag against the requested address on every access to decide hit vs miss.
- **Dirty bit** — present only in [[WriteBackCache|write-back]] caches; set when the CPU writes to this line, indicating the cached copy diverges from [[RAM|main memory]] and must be written back on eviction.

## Block-size trade-off

*"Cache designers balance a trade-off in choosing a cache's block size"* ([[dis-11-4-caching]]):

- **Larger blocks** → more [[SpatialLocality|spatial locality]] exploited per miss (one miss brings many useful bytes); fewer cold misses on sequential traversals.
- **Smaller blocks** → more distinct memory regions cacheable simultaneously (cache holds more diverse subsets of memory); less wasted space when program accesses are scattered.

Typical modern L1 lines are **64 bytes** — the de-facto industry consensus.

## Address decomposition

Every memory address splits into three fields used to locate the line:

| Field | Bits | Purpose |
|---|---|---|
| **Offset** | low | Selects a byte within the block (`log2(block_size)` bits) |
| **Index** | middle | Selects the cache line or set (`log2(num_lines)` bits) |
| **Tag** | high | Identifies which memory region the line currently holds |

The middle-bit choice for the index is deliberate: *"caches spread data more evenly among the available cache lines"* — using high bits would cluster nearby variables into the same line.

## Connections

- [[CacheMemory]] — the storage tier built out of cache lines.
- [[CacheHit]] / [[CacheMiss]] — the line's valid bit + tag comparison determines which outcome occurs.
- [[SpatialLocality]] — the program property the cache-line / block mechanism is designed to exploit ([[dis-11-3-locality|Ch 11.3]]).
- [[DirectMappedCache]] / [[SetAssociativeCache]] / [[FullyAssociativeCache]] — three placement policies for how addresses map to lines.
- [[WriteBackCache]] — uses the dirty bit metadata; [[WriteThroughCache]] does not.
- [[CacheReplacementPolicy]] — selects which line to evict when a set is full.
- [[FalseSharing]] — pathology where two cores ping-pong a single line because their independent variables share it.
