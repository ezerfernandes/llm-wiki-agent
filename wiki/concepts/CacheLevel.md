---
title: "Cache Level (L1 / L2 / L3)"
type: concept
tags: [hardware, systems, memory, cache, performance]
sources: [dis-11-1-memory-hierarchy, parproc-appA-systems-issues, d2l-computational-performance]
last_updated: 2026-05-17
---

# Cache Level (L1 / L2 / L3)

Modern processors do not contain *a* cache — they contain a **stack of caches** at different sizes and distances from the [[ALU]]. [[DiveIntoSystems|DIS]] Ch 11.1 names the three standard levels:

> *"L1 (very small and fast, near the [[ALU]]), L2 (larger and slower), and L3 (shared among multicore CPUs)."* — [[dis-11-1-memory-hierarchy]]

## The three levels

| Level | Position | Sharing | Size order | Speed order |
|---|---|---|---|---|
| **L1** | Closest to [[ALU]] | Per-core (often split inst / data) | Smallest | Fastest |
| **L2** | One step further from [[ALU]] | Per-core (typical) | Larger than L1 | Slower than L1 |
| **L3** | Last on-die cache | **Shared among multicore CPUs** | Largest | Slowest on-die tier |

Each level is **larger and slower** than the level above it — the [[MemoryHierarchy|memory hierarchy]] pattern repeated *inside* the cache tier. [[dis-11-1-memory-hierarchy|DIS Ch 11.1]] treats the three levels collectively as the single *Cache* tier for the pyramid overview, deferring the multi-level mechanics to later subsections.

## Why three levels (and not one)

The same performance/capacity trade-off that creates the outer [[MemoryHierarchy|memory hierarchy]] (registers → cache → RAM → disk) also operates *inside* the cache: making L1 large enough to hold a working set would push it physically further from the [[ALU]] and slow it down. The compromise is **stratification** — a tiny ultra-fast L1, a medium L2, and a large slow L3 that catches what spills out of L2.

## L3 as the cross-core shared tier

L1 and L2 are private to each core; **L3 is shared across all cores of a [[MulticoreProcessor|multicore CPU]]** ([[dis-11-1-memory-hierarchy]]). This makes L3 the natural place for **inter-core data exchange** in shared-memory parallel programs — a thread on core A can pre-warm L3 for a thread on core B without going to DRAM. It also makes L3 the **contention point** for [[FalseSharing|false sharing]] and [[CacheCoherency|cache-coherence]] traffic.

## Connections

- [[dis-11-1-memory-hierarchy]] — naming source.
- [[MemoryHierarchy]] — the broader six-tier pyramid; the three cache levels are the second tier collectively.
- [[CacheMemory]] — generic cache mechanics (block / hit / miss / eviction / write-back); applies at every level.
- [[ALU]] — the reference point for *"near the [[ALU]]"* describing L1.
- [[MulticoreProcessor]] — L3 is shared across all cores of a multicore CPU.
- [[CacheCoherency]] — the protocol that keeps per-core L1/L2 copies consistent.
- [[FalseSharing]] — multi-core pathology operating at the L1/L2 cache-line granularity, resolved by L3.
- [[LocalityOfReference]] — the access-pattern property that makes the multi-level structure pay off.
- [[d2l-computational-performance]] — provides the numeric latency picture (L1 ≈ 1.5 ns, L2 ≈ 5 ns, L3 local ≈ 16 ns, L3 remote-socket ≈ 40 ns).
- [[parproc-appA-systems-issues]] — parallel-programming view of the same structure.
