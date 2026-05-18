---
title: "Write-Back Cache"
type: concept
tags: [cache, memory-hierarchy, systems, hardware, write-policy]
sources: [dis-11-4-caching]
last_updated: 2026-05-17
---

# Write-Back Cache

A **write-back cache** is the modern dominant cache **write policy**: when the CPU writes to a memory address, the [[CacheMemory|cache]] is updated immediately, but [[RAM|main memory]] is **not** — the [[CacheLine|cache line]] is marked **dirty** (via the **dirty bit** metadata) and the dirty data is propagated to [[RAM]] **only on eviction**. *"Amortizing the cost of a memory access across many writes significantly improves performance"* ([[dis-11-4-caching|DIS Ch 11.4]]) — the policy's defining property.

## Mechanism ([[dis-11-4-caching|DIS Ch 11.4]])

On a **write hit**:
1. Update the data block in the [[CacheLine|cache line]].
2. Set the line's **dirty bit** to `1`.
3. **Do nothing to [[RAM|main memory]]** — the cache and RAM now disagree, but the cache is authoritative.

On **eviction** of a dirty line (because the set is full and a new block must be installed):
1. **Write the dirty block back to [[RAM|main memory]]** — restores cache/RAM coherence.
2. Clear the dirty bit.
3. Install the incoming block.

## Why write-back wins

Programs **repeatedly write to the same locations** (loop counters, accumulator variables, hot data-structure fields). A counter incremented a million times in a tight loop hits the cache a million times but reaches [[RAM|main memory]] **once** at eviction — a million-fold write traffic reduction. *"Amortizing the cost of a memory access across many writes significantly improves performance, making write-back the dominant approach in modern caches."*

## Trade-offs

**Vs [[WriteThroughCache|write-through]]**:
- **Vastly less memory bandwidth** consumed by writes — the dominant performance win.
- **Cache and RAM diverge** — special handling required on eviction, on DMA, and on coherence-protocol invalidations.
- Requires the **dirty bit** in every line's metadata.
- Worst-case eviction is more expensive: a write miss that evicts a dirty line costs two memory accesses (writeback + fill).

**Vs [[WriteThroughCache|write-through]] for [[CacheCoherency|coherence]]**:
- Write-back caches make multi-core coherence harder — a write that didn't propagate to memory is invisible to other cores until eviction.
- Modern coherence protocols ([[MESI]], MOESI) explicitly track dirty-shared and dirty-exclusive states to handle this.

## Connections

- [[WriteThroughCache]] — the simpler dual policy that updates [[RAM]] on every write.
- [[CacheLine]] — uses the dirty bit metadata field.
- [[CacheMemory]] — the parent storage tier.
- [[CacheCoherency]] — write-back complicates coherence; protocols like [[MESI]] track dirty states explicitly.
- [[CacheReplacementPolicy]] — eviction of a dirty line triggers writeback as a side effect.
- [[CacheMiss]] — a write miss that evicts a dirty line costs writeback + fill.
- [[FalseSharing]] — multi-core ping-pong of dirty lines is the pathological case.
