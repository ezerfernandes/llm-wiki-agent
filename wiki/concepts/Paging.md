---
title: "Paging"
type: concept
tags: [operating-systems, virtual-memory, memory, mechanism]
sources: [dis-13-3-virtual-memory]
last_updated: 2026-05-17
---

# Paging

**Paging** is the [[VirtualMemory|virtual-memory]] mechanism that divides each [[Process|process]]'s [[AddressSpace|address space]] into fixed-size [[Page|pages]] and physical [[RAM]] into same-size **frames**, then maps pages to frames via the per-process [[PageTable|page table]]. Per [[dis-13-3-virtual-memory|DIS Ch 13.3]], paging is what makes the virtual-memory abstraction *implementable*: pages are flexibly placed in any free frame, need not be contiguous, and need not all be resident in RAM at once.

## Properties

- **Any-page-to-any-frame**: a virtual page can occupy any physical frame; the [[PageTable|page table]] is the bookkeeping device that makes this work.
- **Non-contiguous physical layout**: a process's virtually contiguous [[AddressSpace|address space]] is stitched together from frames scattered across RAM.
- **Partial residency**: a process can execute with only some of its pages in RAM — the rest live in the [[SwapFile|swap area]] on disk. See [[DemandPaging]].
- **Uniform replacement granularity**: all transfers between RAM and disk happen at page size — no special-casing per allocation.

## Address translation

The [[MMU]] performs translation on every memory access (see [[VirtualAddress]] / [[PhysicalAddress]] / [[PageTable]]):

1. Split [[VirtualAddress|VA]] into page number (high bits) + offset (low bits).
2. Index the [[PageTable|page table]] via the PTBR to find the [[PageTable|PTE]].
3. If `valid == 0`, raise a [[PageFault|page fault]].
4. Else, concatenate `PTE.frame_number` with the offset to form the [[PhysicalAddress|PA]].

The [[TLB|Translation Lookaside Buffer]] caches recent PTEs, so most accesses skip steps 2 entirely.

## Trade-offs

- **Internal fragmentation** — the tail page of any allocation is rarely fully used (avg ½ page wasted per region).
- **Page-table memory overhead** — one PTE per virtual page per process (mitigated in production by multi-level page tables, not covered in Ch 13.3).
- **Translation overhead** — would double memory latency without the [[TLB]].

## Connections

- [[dis-13-3-virtual-memory]] — primary source.
- [[VirtualMemory]] — the umbrella abstraction paging implements.
- [[Page]] — the unit paging operates on.
- [[PageTable]] — the data structure paging consults.
- [[VirtualAddress]] / [[PhysicalAddress]] — the two sides paging translates between.
- [[PageFault]] — the interrupt paging raises on a non-resident page.
- [[DemandPaging]] — the load-on-first-reference policy paging enables.
- [[SwapFile]] — the disk-resident backing store paging swaps to / from.
- [[TLB]] — the cache that makes paging affordable on every memory access.
- [[MMU]] — the hardware that executes the translation.
