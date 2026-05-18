---
title: "Solid-State Drive (SSD)"
type: concept
tags: [storage, secondary-storage, flash, nonvolatile, ssd, memory-hierarchy]
sources: [dis-11-2-storage-devices]
last_updated: 2026-05-17
---

# Solid-State Drive (SSD)

**Solid-State Drive** — non-volatile secondary-storage device built on **[[FlashMemory|flash memory]]** with **no moving parts**. Occupies the same [[MemoryHierarchy|memory-hierarchy]] tier as [[HardDisk|HDDs]] (secondary, non-volatile, persistent across power loss), but **10×–100× lower latency** because access is purely electrical rather than mechanical. Per [[dis-11-2-storage-devices|DIS Ch 11.2]]: *"Solid-state drives have no moving parts (and thus lower latency)."*

> **Naming note**: the wiki also has [[SSD|SSD (Single-Shot MultiBox Detector)]] — an *object-detection model*. This page (`SolidStateDrive.md`) covers the **storage device** sense of "SSD"; that page (`SSD.md`) covers the computer-vision sense. Use the full term **Solid-State Drive** to disambiguate when linking from systems / hardware pages.

## Headline properties (per [[dis-11-2-storage-devices|Ch 11.2]])

- **Latency**: 0.1–1 ms — between [[DRAM]] (~100 ns) and [[HardDisk|HDD]] (5–10 ms).
- **Capacity**: 0.5–2 TB typical (vs HDD's 0.5–10 TB).
- **Cost**: Moderate per-byte — more expensive than [[HardDisk|HDDs]], cheaper than [[DRAM]].
- **Volatility**: [[NonVolatileMemory|Non-volatile]] — flash cells retain charge across power loss.
- **Moving parts**: None. All access is electrical → no seek time, no rotational latency.

## Why it's faster than [[HardDisk|HDDs]]

HDD access cost = mechanical seek + rotational latency + transfer (~5–10 ms). SSD access cost = purely electrical addressing of flash pages (~0.1–1 ms). Eliminating mechanical motion removes the latency gate that physically limits HDDs.

## Why it's slower than [[DRAM]]

Flash cells require **higher voltages** for programming/erasing, and erase happens at **block granularity** (not byte granularity). These electrical asymmetries plus controller-level [[FlashTranslationLayer|FTL]] / wear-leveling overhead keep SSDs ~10³–10⁴× slower than DRAM despite both being all-electrical.

## SSD vs [[HardDisk|HDD]]

| | [[HardDisk|HDD]] | SSD |
|---|---|---|
| Storage medium | Magnetic platters | [[FlashMemory|Flash memory]] |
| Moving parts | Yes | No |
| Latency | 5–10 ms | 0.1–1 ms |
| Capacity | 0.5–10 TB | 0.5–2 TB |
| Cost / byte | Lower | Higher |
| Sequential vs random | Sequential ≫ random | Roughly equal |
| Failure mode | Mechanical wear | Flash cell endurance |

## Scope note

Ch 11.2 introduces SSDs by their headline property only ("flash memory, no moving parts, lower latency"). It does **not** cover internal SSD anatomy (pages, blocks, planes, dies), wear leveling, the flash translation layer, TRIM, or write amplification. Those mechanisms can be expanded when a later source covers them.

## Connections

- [[MemoryHierarchy]] — Secondary-storage tier (alongside [[HardDisk]]).
- [[dis-11-2-storage-devices]] — Source — DIS Ch 11.2.
- [[HardDisk]] — Mechanical-platter sibling at the same tier; slower, cheaper, higher-capacity.
- [[FlashMemory]] — Underlying storage technology.
- [[NonVolatileMemory]] — Parent category.
- [[DRAM]] — Primary-storage tier directly above; ~10³–10⁴× faster.
- [[DiveIntoSystems]] — Introducing textbook.
- [[SSD]] — **Disambiguation** — the *Single-Shot MultiBox Detector* object-detection model (not this page).
