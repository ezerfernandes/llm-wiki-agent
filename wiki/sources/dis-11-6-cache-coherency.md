---
title: "Dive into Systems — Ch 11.6 Looking Ahead: Caching on Multicore Processors"
type: source
tags: [systems, memory-hierarchy, cache, multicore, coherency, parallel-computing]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C11-MemHierarchy/coherency.html
---

## Summary
Chapter 11.6 of *[[DiveIntoSystems]]* extends the [[dis-11-1-memory-hierarchy|Ch 11.1]]–[[dis-11-5-cachegrind|Ch 11.5]] uniprocessor [[CacheMemory|cache]] story to **[[Multicore|multicore]]** systems where each core owns a **private L1** but **shares L2/L3** with siblings. The chapter names the resulting **[[CacheCoherency|cache-coherence problem]]** — *"the value of a copy of a block of memory stored in one core's L1 cache is different than the value of a copy of the same block stored in another core's L1 cache"* — and introduces the **MSI** invalidate protocol (Modified / Shared / Invalid) as the simplest solution, along with **snooping** vs **directory-based** implementations. [[FalseSharing|False sharing]] is named as the multithreaded-program pathology that coherency creates, with full discussion deferred to Ch 14.5.

## Key Claims
- **Multicore [[CacheMemory|cache]] topology**: private L1 per core (separate I/D), shared L2/L3 — *"each core executes independent instruction streams"*, so per-core L1 hit-rates beat a single shared L1.
- **[[CacheCoherency|Cache-coherence problem]]** stated verbatim: *"the value of a copy of a block of memory stored in one core's L1 cache is different than the value of a copy of the same block stored in another core's L1 cache"* — occurs when one core writes a line cached elsewhere.
- **System requirement**: must *"maintain a coherent single value of the memory contents across all copies of the cached block"*.
- **MSI protocol** — three states per cache line:
  - **M (Modified)** — this cache wrote the line; sole valid copy.
  - **S (Shared)** — unmodified; safely cacheable at multiple cores.
  - **I (Invalid)** — line in cache is stale; must reload.
- **Read on I** — load from another core's L1 (if M elsewhere) or from a lower-level cache.
- **Write on I/S** — broadcast invalidation; remote copies → I; local → M.
- **Snooping** — every cache controller monitors the shared bus for read/write transactions to addresses it caches; supports **write-invalidate** protocols. Simple and broadcast-cheap on a bus but doesn't scale.
- **Directory-based** — a directory tracks which caches currently hold each block; coherence messages target only those caches. Scales better than snooping but adds metadata and latency.
- **[[FalseSharing|False sharing]]** — *"can occur in multithreaded programs when threads access nearby memory locations, causing unnecessary cache coherency traffic"*. Details deferred to Ch 14.5.
- **Justification**: the added complexity of coherency protocols is worth it because **per-core L1** beats a shared-L1 design.

## Key Quotes
> "The value of a copy of a block of memory stored in one core's L1 cache is different than the value of a copy of the same block stored in another core's L1 cache." — canonical definition of the cache-coherence problem.

> "Maintain a coherent single value of the memory contents across all copies of the cached block." — the system requirement coherence protocols deliver.

## Connections
- [[CacheCoherency]] — the **central concept**; this chapter is [[DiveIntoSystems|DIS]]'s introduction to the topic, complementing the deeper treatment in [[parproc-ch03-shared-memory-parallelism|ParProc Ch 3]] §3.5.1. **Extended in place** with DIS's MSI framing.
- [[MESI]] — DIS uses the **simpler MSI** (Modified/Shared/Invalid) form; the [[parproc-ch03-shared-memory-parallelism|ParProc]] / Pentium variant adds the **Exclusive** state. MSI is the pedagogical introduction; MESI the production protocol.
- [[FalseSharing]] — named but not developed in 11.6; the line-granularity pathology cache-coherency introduces. Full chapter-anchored treatment lives in [[parproc-ch03-shared-memory-parallelism|ParProc Ch 3]] §3.5.3 and Ch 14.5 of DIS (not yet ingested).
- [[CacheLevel]] — multicore topology: private **L1** (split I/D), shared **L2/L3**. Sharpens the [[dis-11-1-memory-hierarchy|Ch 11.1]] tier definition with the per-core/shared split.
- [[Multicore]] — the substrate that creates the problem; coherency is the price of independent instruction streams + shared memory.
- [[SharedMemoryArchitecture]] — the memory model coherency preserves.
- [[CacheMemory]] / [[CacheLine]] — the unit at which coherence is tracked.
- [[MemoryBus]] — the substrate snooping monitors.
- [[dis-11-5-cachegrind|Ch 11.5]] — *the uniprocessor measurement chapter Ch 11.6 generalizes*; [[dis-11-4-caching|Ch 11.4]] — *the mechanism*; [[dis-11-3-locality|Ch 11.3]] — *the theory*; [[dis-11-2-storage-devices|Ch 11.2]] — *the device taxonomy*; [[dis-11-1-memory-hierarchy|Ch 11.1]] — *the opening pyramid*.
- [[DiveIntoSystems]] — 111th ingested chapter; **sixth leaf of Ch 11 *The Memory Hierarchy***.
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — authors.

## Contradictions
- **MSI vs MESI**: DIS uses 3-state **MSI**; [[parproc-ch03-shared-memory-parallelism|ParProc Ch 3]] uses 4-state **MESI** (adds **Exclusive** to distinguish *only-copy-but-unmodified* from *shared*). Not a contradiction — MSI is the pedagogically simpler introduction; MESI is the production refinement. The Exclusive state optimizes the *first* write to a line by avoiding a broadcast when no other cache holds the block.
