---
title: "Dive into Systems — Ch 11.2 Storage Devices"
type: source
tags: [systems, memory-hierarchy, storage, hdd, ssd, dram, sram, registers, latency]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C11-MemHierarchy/devices.html
---

## Summary

**Ch 11.2 *Storage Devices*** is the **second leaf** of [[DiveIntoSystems|DIS]] Ch 11 *[[MemoryHierarchy|The Memory Hierarchy]]*. It populates the six-tier pyramid named in [[dis-11-1-memory-hierarchy|Ch 11.1]] with concrete device technologies and their **latency / capacity / cost / volatility** profiles. Splits storage into **primary** (volatile — registers, [[CacheMemory|cache]], [[RAM|main memory]]) and **secondary** ([[NonVolatileMemory|non-volatile]] — [[HardDisk|HDD]], [[SolidStateDrive|SSD]], magnetic tape, optical, network-remote). Introduces the **[[SRAM]] vs [[DRAM]]** split for RAM technology and motivates why the memory hierarchy exists physically — *distance + mechanical motion + manufacturing cost = irreducible latency gradient*.

## Key Claims

- **Primary vs secondary storage axis.** Primary = directly addressable by the [[CPU]] ([[CpuRegister|registers]], [[CacheMemory|L1/L2/L3 cache]], [[RAM|main memory]]) — all **volatile**. Secondary = persistent / [[NonVolatileMemory|non-volatile]] ([[HardDisk|HDDs]], [[SolidStateDrive|SSDs]], magnetic tape, floppy, optical, remote network servers). The CPU never directly addresses secondary storage — it goes through I/O controllers.
- **Latency / capacity / cost table** (canonical DIS numbers for Ch 11.2):

| Device | Volatility | Latency | Capacity | Cost |
|---|---|---|---|---|
| [[CpuRegister|Registers]] | Volatile | <1 ns | 4–8 bytes (each) | Very high |
| [[SRAM]] cache | Volatile | ~5 ns | 1–32 MB | High |
| [[DRAM]] main memory | Volatile | ~100 ns | 4–64 GB | Moderate |
| [[SolidStateDrive|SSD]] | [[NonVolatileMemory|Non-volatile]] | 0.1–1 ms | 0.5–2 TB | Moderate |
| [[HardDisk|HDD]] | [[NonVolatileMemory|Non-volatile]] | 5–10 ms | 0.5–10 TB | Low |

- **SRAM vs DRAM technology choice.** [[SRAM]] uses **circuit-based latches** (six-transistor cross-coupled cell) — fastest, but power-hungry and area-expensive, so capacity is capped. Sits on-chip for [[CpuRegister|registers]] and [[CacheMemory|cache]]. [[DRAM]] uses **capacitor-based 1T1C cells** — denser and cheaper, but capacitors leak charge and require periodic **refresh**. Lives on DIMMs across the [[MemoryBus|memory bus]] for main memory.
- **HDD mechanical anatomy.** Rotating magnetic platters at **5,000–15,000 RPM**, concentric **tracks** divided into **sectors**. Access cost = **seek time** (mechanical arm extends/retracts to align disk head with target track) + **rotational latency** (waiting for the desired sector to rotate under the head). The mechanical steps total *several milliseconds* — the ~10⁵× latency gap vs DRAM.
- **SSD = flash memory, no moving parts.** Flash-based [[SolidStateDrive|SSDs]] "allow for reading, writing, and erasing data at speeds faster than traditional hard disks" with "no moving parts (and thus lower latency)." Ch 11.2 explicitly under-specifies — no pages, blocks, or wear-leveling discussion (deferred / out of scope).
- **Physics-level explanation for hierarchy.** Distance matters — *electrical signals propagate through circuits in measurable time*. **Grace Hopper's "nanoseconds"** were 11.8-inch wire strands representing the maximum distance light/electrical signal travels in one nanosecond — physical justification for why compactness ⇒ speed.
- **Von Neumann bottleneck named.** The [[MemoryBus|memory bus]] between [[CPU]] and main memory remains a performance constraint even when the two are physically close — the *bandwidth-and-latency wall* that the [[CacheMemory|cache]] hierarchy is designed to hide.

## Key Quotes

> "Static RAM (SRAM) uses small electrical circuits to store values; it is faster and more expensive than DRAM." — Ch 11.2

> "Dynamic RAM (DRAM) uses capacitors that require periodic refreshing; it is denser and cheaper than SRAM." — Ch 11.2

> "Before accessing data, the disk's mechanical arm must seek to the correct track, and the system must then wait for the platter to rotate the desired location under the disk head." — Ch 11.2 (paraphrased — HDD seek + rotational latency)

> "Solid-state drives have no moving parts (and thus lower latency)." — Ch 11.2

> The Grace Hopper *nanosecond* — *"a piece of wire roughly 11.8 inches long, representing the maximum distance an electrical signal travels in one nanosecond"* — Ch 11.2 (pedagogical motif for why distance ⇒ latency).

## Connections

- [[DiveIntoSystems]] — **107th** ingested chapter; **second leaf of Ch 11 *Memory Hierarchy*** (follows [[dis-11-1-memory-hierarchy|Ch 11.1]]; precedes Ch 11.3 *Locality*).
- [[dis-11-1-memory-hierarchy]] — Direct parent — 11.1 names the six-tier pyramid; 11.2 fills it with device technologies and latency numbers.
- [[MemoryHierarchy]] — Concept tier-list that this chapter operationalizes with concrete devices + latency table.
- [[CacheLevel]] — L1 / L2 / L3 — the [[SRAM]] tier sitting between [[CpuRegister|registers]] and [[DRAM]] main memory.
- [[SRAM]] — Re-anchored to Ch 11.2's circuit-based / cache-tier framing (not just MCU on-chip memory).
- [[DRAM]] — Re-anchored to Ch 11.2's main-memory framing with explicit latency (~100 ns).
- [[HardDisk]] — **New page** — mechanical platter-based secondary storage; seek + rotational latency.
- [[SolidStateDrive]] — **New page** — flash-memory secondary storage; no moving parts.
- [[NonVolatileMemory]] — **New page** — abstract category that contains [[HardDisk]] / [[SolidStateDrive]] / [[FlashMemory]] / magnetic tape.
- [[CpuRegister]] — Topmost tier; <1 ns; SRAM-cell-based.
- [[CacheMemory]] — SRAM-based on-chip caches.
- [[RAM]] — DRAM-based main memory tier.
- [[FlashMemory]] — Storage technology underlying [[SolidStateDrive|SSDs]].
- [[MemoryBus]] — Von-Neumann bottleneck named in this chapter.
- [[CPU]] — Addresses primary storage directly; reaches secondary storage via I/O controllers.

## Contradictions

- None. Ch 11.2 is consistent with [[dis-11-1-memory-hierarchy|Ch 11.1]]'s pyramid and with existing [[d2l-computational-performance|D2L]] latency framing in [[MemoryHierarchy]]. Adds device-level granularity rather than overturning prior claims.
