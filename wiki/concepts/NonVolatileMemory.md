---
title: "Non-Volatile Memory"
type: concept
tags: [memory, storage, nonvolatile, persistence, secondary-storage]
sources: [dis-11-2-storage-devices]
last_updated: 2026-05-17
---

# Non-Volatile Memory

**Non-Volatile Memory** (NVM) — the category of storage technologies that **retain their contents when power is removed**. The opposite axis from *volatile* memory ([[CpuRegister|registers]], [[SRAM]], [[DRAM]]), which loses everything on power loss. In the [[MemoryHierarchy|memory hierarchy]], every tier *below* main memory is non-volatile: [[FlashMemory|Flash]] / [[SolidStateDrive|SSDs]], [[HardDisk|HDDs]], magnetic tape, optical media, and remote-network storage ([[dis-11-2-storage-devices|DIS Ch 11.2]]).

## The volatility split (per [[dis-11-2-storage-devices|Ch 11.2]])

| Tier | Volatility | Examples |
|---|---|---|
| **Primary storage** | Volatile | [[CpuRegister|Registers]], [[SRAM]] [[CacheMemory|cache]], [[DRAM]] main memory |
| **Secondary storage** | **Non-volatile** | [[SolidStateDrive|SSDs]], [[HardDisk|HDDs]], magnetic tape, optical, network-remote |

The split is **physics-driven**:

- **Volatile** technologies store state in **active electrical structures** (capacitor charge for [[DRAM]], cross-coupled transistor latches for [[SRAM]]) that require continuous power to maintain.
- **Non-volatile** technologies store state in **passive physical structures** — *magnetic polarity* (HDDs, tape), *trapped charge in floating-gate transistors* ([[FlashMemory|Flash]], SSDs), or *physical pits* (optical media) — that persist without external power.

## Members in the wiki

- [[FlashMemory]] — Floating-gate-transistor-based. Used in MCU firmware storage and [[SolidStateDrive|SSDs]].
- [[SolidStateDrive]] — Flash-based, no moving parts, 0.1–1 ms latency.
- [[HardDisk]] — Magnetic-platter, mechanical, 5–10 ms latency.
- **Magnetic tape / optical / network-remote** — Named in Ch 11.2 but not yet expanded into their own pages.

## Why the hierarchy ends in non-volatile tiers

A computer must survive power cycles. The **non-volatile floor** of the [[MemoryHierarchy|memory hierarchy]] is what holds the program binary, the [[OperatingSystem|OS]] kernel, the user's data — anything that must outlive a reboot. Primary-storage tiers exist only to *cache* the working set of this non-volatile floor closer to the [[CPU]].

## Persistence ≠ reliability

Non-volatile only means "doesn't lose state at power-off" — it does *not* mean "indefinitely reliable":

- **HDDs** wear via mechanical fatigue (bearing failure, head crash).
- **Flash / SSDs** wear via **finite write endurance** — each flash cell can only be erased a bounded number of times.
- **Tape / optical** degrade over decades via magnetic field decay or substrate breakdown.

Each non-volatile technology has a distinct **wear / failure model** layered on top of its persistence property.

## Connections

- [[MemoryHierarchy]] — Defines the volatile / non-volatile split at the primary / secondary boundary.
- [[dis-11-2-storage-devices]] — Source — DIS Ch 11.2.
- [[HardDisk]] / [[SolidStateDrive]] / [[FlashMemory]] — Concrete non-volatile members.
- [[DRAM]] / [[SRAM]] / [[CpuRegister]] — Volatile contrast on the primary-storage side.
- [[DiveIntoSystems]] — Introducing textbook.
