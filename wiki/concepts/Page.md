---
title: "Page (memory)"
type: concept
tags: [operating-systems, virtual-memory, memory]
sources: [dis-13-3-virtual-memory]
last_updated: 2026-05-17
---

# Page

A **page** is the fixed-size unit a [[Process|process]]'s virtual [[AddressSpace|address space]] is divided into in a paged [[VirtualMemory|virtual-memory]] system — commonly **4 KB** on modern systems. Per [[dis-13-3-virtual-memory|DIS Ch 13.3]], a page is paired with a same-size **frame** in physical [[RAM]]: the page lives at a [[VirtualAddress|virtual address]], the frame lives at a [[PhysicalAddress|physical address]], and the [[PageTable|page table]] records which frame currently backs each page.

## Pages and frames

- **Page** — virtual-side unit; appears in a [[VirtualAddress|virtual address]] as the page number (high-order bits) + offset (low-order bits).
- **Frame** — physical-side unit, same size as a page; appears in a [[PhysicalAddress|physical address]] as the frame number (high-order bits) + offset (low-order bits, identical to the virtual offset).

Because pages and frames are the same size, *"any virtual page can load into any physical frame"* — the mapping is flexible and *"pages need not occupy contiguous RAM locations."*

## Why fixed-size

Fixed-size pages make the [[PageTable|page-table]] index a simple division of the [[VirtualAddress|VA]] into two bit-fields — no bounds metadata per mapping. The trade-off vs variable-size segmentation is internal fragmentation (the last page of a memory region is rarely fully used) in exchange for simpler bookkeeping and uniform replacement policy.

## Lifecycle

A page can be in one of three states tracked by its [[PageTable|PTE]]:

1. **Resident in RAM** — `valid = 1`, frame number points to its current frame.
2. **On disk in the swap area** — `valid = 0`; access raises a [[PageFault|page fault]] that triggers a load from the [[SwapFile]].
3. **Not allocated** — `valid = 0` and no backing on disk; access is a true bug ([[SegmentationFault|segfault]]).

## Connections

- [[dis-13-3-virtual-memory]] — primary source.
- [[VirtualMemory]] — the umbrella mechanism.
- [[Paging]] — the operation of moving pages between RAM and disk.
- [[PageTable]] — records the page-to-frame mapping.
- [[VirtualAddress]] / [[PhysicalAddress]] — addresses that name pages / frames + offsets.
- [[PageFault]] — interrupt raised when a non-resident page is referenced.
- [[DemandPaging]] — strategy of loading a page only on first reference.
- [[SwapFile]] — disk-resident backing store for non-resident pages.
- [[CacheLine]] — the analogous fixed-size unit in the [[CacheMemory|cache]] tier of the [[MemoryHierarchy|memory hierarchy]] (pages are far larger — typically 4 KB vs ~64 B for a cache line).
