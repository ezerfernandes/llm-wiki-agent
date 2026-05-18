---
title: "Dive into Systems — Ch 11.1 The Memory Hierarchy"
type: source
tags: [textbook, systems, memory-hierarchy, cache, dis]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C11-MemHierarchy/mem_hierarchy.html
---

## Summary

**First leaf of Ch 11 *The Memory Hierarchy*** of *[[DiveIntoSystems]]* — opens the wiki's coverage of Part IV's memory-hierarchy chapter. The single short section names the **fundamental performance/capacity trade-off** every storage system embodies: *"devices with higher capacities offer lower performance... no single device does both. This trade-off between performance and capacity is known as the memory hierarchy."* Enumerates the six-tier pyramid from highest-performance / lowest-capacity to lowest-performance / highest-capacity — **[[CpuRegister|Registers]] → [[CacheMemory|Cache]] ([[CacheLevel|L1 / L2 / L3]]) → [[RAM|Main Memory]] → [[FlashMemory|Flash Disk]] → Traditional Disk → Remote Secondary Storage** — and codifies why practical systems must combine multiple device types rather than choose a single one. No latency numbers, no [[LocalityOfReference|locality]] discussion, no *memory wall* terminology — those are deferred to later subsections (11.2 *Storage Devices* / 11.3 *Locality* / 11.4 *Caching* / 11.5 *Cache Analysis and Cachegrind* / 11.6 *Caching on Multicore Processors* / 11.7 *Summary* / 11.8 *Exercises*).

## Key Claims

- **The hierarchy is forced by a hardware trade-off, not a design choice.** *"devices with higher capacities offer lower performance... no single device does both"* — the source of the [[MemoryHierarchy|memory hierarchy]]'s existence is a physics-level fact about storage media, not an architectural decision.
- **Performance correlates inversely with cost per byte.** *"faster devices are more expensive, both in terms of bytes per dollar and operational costs (e.g., energy usage)"* — the same fact that prevents single-device solutions also makes the pyramid's narrow top expensive and its wide base cheap.
- **The hierarchy has six named tiers.** From top (fastest, smallest) to bottom (slowest, largest): [[CpuRegister|Registers]] → [[CacheMemory|Cache]] ([[CacheLevel|L1 / L2 / L3]]) → [[RAM|Main Memory]] → [[FlashMemory|Flash Disk]] → Traditional Disk → Remote Secondary Storage.
- **Cache itself is multi-level.** Modern systems contain *"multiple cache levels — L1 (very small and fast, near the [[ALU]]), L2 (larger and slower), and L3 (shared among multicore CPUs)"* — but 11.1 treats them collectively as the single *Cache* tier for simplicity, deferring detail to later subsections.
- **Practical systems combine device types.** *"Practical systems must utilize a combination of devices to meet the performance and capacity requirements of programs"* — the hierarchy is not an artifact of legacy decisions, it is the only way to satisfy both performance and capacity constraints simultaneously.
- **Ideal-world contrafactual.** *"Ideally, programmers wouldn't need to worry about data location, though performance-critical code sections may justify such optimization"* — locality-aware coding is opt-in, motivated by performance-critical code.

## Key Quotes

> "devices with higher capacities offer lower performance... no single device does both. This trade-off between performance and capacity is known as the memory hierarchy" — defining quote of section 11.1.

> "faster devices are more expensive, both in terms of bytes per dollar and operational costs (e.g., energy usage)" — the cost dimension of the same trade-off.

> "Practical systems must utilize a combination of devices to meet the performance and capacity requirements of programs" — the engineering corollary.

## Connections

- [[DiveIntoSystems]] — Ch 11.1 is the **opening leaf of Ch 11 *The Memory Hierarchy*** — the wiki's first Ch 11 ingest and the **106th ingested DIS chapter**, opening Part IV after the three-ISA assembly arc (Ch 7 / 8 / 9) and the cross-ISA closer (Ch 10) completed in prior ingests.
- [[MemoryHierarchy]] — the canonical concept page; this ingest **expands** the page from a [[d2l-computational-performance|D2L-perspective]] / [[parproc-appA-systems-issues|parallel-programming-perspective]] stub into full [[DiveIntoSystems|DIS]] coverage: explicit six-tier pyramid, performance/capacity-trade-off framing, multi-level cache structure, ideal-vs-practical-programmer commitment.
- [[CacheLevel]] — **new concept page** minted by this ingest; codifies the L1 / L2 / L3 multi-level cache distinction (L1 small/fast/near-ALU, L2 larger/slower, L3 shared across multicore).
- [[CacheMemory]] — already exists; now linked from [[MemoryHierarchy]] as the second tier; [[CacheLevel]] elaborates its internal L1/L2/L3 structure.
- [[CpuRegister]] — top tier (highest-performance, lowest-capacity).
- [[RAM]] / [[DRAM]] — middle tier (DIS's *Main Memory* label).
- [[FlashMemory]] — already exists; named as the *Flash Disk* tier.
- *Traditional Disk* tier (rotational HDD) — page not yet minted; deferred to a later 11.x ingest.
- *Remote Secondary Storage* tier (network-attached / cloud / datacenter-scale) — page not yet minted; deferred to a later 11.x ingest.
- [[ALU]] — the L1 cache's reference point per 11.1's *"near the ALU"* qualifier.
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — co-authors.
- [[UnitedStatesMilitaryAcademy]] / [[SwarthmoreCollege]] — author affiliations.

## Contradictions

None. 11.1's pyramid is consistent with the existing [[MemoryHierarchy]] page (which had the same six-tier shape from [[d2l-computational-performance|D2L]] / [[parproc-appA-systems-issues|ParProc App A]]). [[DiveIntoSystems|DIS]] adds an explicit named-tier ordering and the *Flash Disk* / *Remote Secondary Storage* labels not previously emphasized; the prior numeric latency tables (from D2L) remain valid and unchallenged.
