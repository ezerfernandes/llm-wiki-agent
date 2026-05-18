---
title: "Hard Disk Drive (HDD)"
type: concept
tags: [storage, secondary-storage, mechanical, nonvolatile, hdd, memory-hierarchy]
sources: [dis-11-2-storage-devices]
last_updated: 2026-05-17
---

# Hard Disk Drive (HDD)

**Hard Disk Drive** — the **mechanical, magnetic-platter-based** non-volatile secondary-storage device that anchors the bottom of the on-machine [[MemoryHierarchy|memory hierarchy]] (above only remote / network storage). Stores bits as magnetic polarity on **rotating platters**; accessed by a moving read/write head. Cheap-per-byte and high-capacity, but **mechanical motion gates latency** — ~5–10 ms per access, four to five orders of magnitude slower than [[DRAM]] ([[dis-11-2-storage-devices|DIS Ch 11.2]]).

## Anatomy (per [[dis-11-2-storage-devices|Ch 11.2]])

- **Platters** — circular magnetic disks stacked on a common spindle, rotating at **5,000–15,000 RPM**.
- **Tracks** — concentric circles on each platter surface.
- **Sectors** — angular slices of each track (the unit of read/write).
- **Disk head** — magnetic transducer on a mechanical arm; one head per platter surface.
- **Arm assembly** — moves all heads radially in unison.

## Access cost = seek + rotation + transfer

Latency for a single HDD access decomposes into three mechanical components:

1. **Seek time** — the mechanical arm extends/retracts to align the head with the target **track**. Several ms typical.
2. **Rotational latency** — wait for the target **sector** to rotate under the head. On average = half a revolution (~2 ms at 15k RPM, ~6 ms at 5k RPM).
3. **Transfer time** — once positioned, bits stream off the platter at the platter's linear velocity.

Total: **~5–10 ms** per random access ([[dis-11-2-storage-devices|Ch 11.2]] canonical figure). The mechanical-motion gate is why HDDs are ~10⁵× slower than [[DRAM]] despite being only one tier below it in the [[MemoryHierarchy|memory hierarchy]].

## Why it's at the bottom of the [[MemoryHierarchy|memory hierarchy]]

- **Capacity wins** — 0.5–10 TB per drive ([[dis-11-2-storage-devices|Ch 11.2]]); cheapest non-volatile per-byte tier.
- **Latency loses** — mechanical motion (seek + rotation) is fundamental to the technology; cannot be hidden by clock-rate improvements.
- **Sequential >> random** — once positioned, transfer is fast; the latency penalty is paid per *seek*, not per byte. This biases HDD-aware code toward sequential / block-oriented access patterns ([[LocalityOfReference|locality]] matters even at the disk tier).

## HDD vs [[SolidStateDrive|SSD]]

| | HDD | [[SolidStateDrive|SSD]] |
|---|---|---|
| Storage medium | Magnetic platters | [[FlashMemory|Flash memory]] |
| Moving parts | Yes (platter + head) | No |
| Latency | 5–10 ms | 0.1–1 ms |
| Capacity | 0.5–10 TB | 0.5–2 TB |
| Cost / byte | Lowest non-volatile | Moderate |
| Sequential vs random | Sequential ≫ random | Roughly equal |
| Failure mode | Mechanical (head crash, bearing) | Electrical wear (flash cell endurance) |

## Connections

- [[MemoryHierarchy]] — Bottom on-machine tier (above only remote / network storage).
- [[dis-11-2-storage-devices]] — Source — DIS Ch 11.2.
- [[SolidStateDrive]] — Flash-based sibling; same tier role, ~10–100× faster, no moving parts.
- [[NonVolatileMemory]] — Parent category.
- [[DRAM]] — Primary-storage tier directly above; ~10⁵× faster.
- [[LocalityOfReference]] — Why HDD-aware code prefers sequential / block access.
- [[DiveIntoSystems]] — Introducing textbook.
