---
title: "Translation Lookaside Buffer"
type: concept
tags: [hardware, operating-systems, performance, memory]
sources: [parproc-appA-systems-issues]
last_updated: 2026-05-17
---

# Translation Lookaside Buffer

The **Translation Lookaside Buffer (TLB)** is a small, fast hardware cache that stores recent virtual-to-physical page-number translations. It exists to eliminate the performance penalty of [[VirtualMemory|virtual memory]] address translation.

## The problem it solves

Without a TLB, every memory access in a VM system requires two memory accesses: one to look up the virtual page number in the page table (itself stored in RAM), and one to access the actual data. This would double the memory latency for every instruction — an unacceptable overhead.

## How it works

The TLB caches a small number of recently used page-table entries. On a memory access:

- **TLB hit**: the virtual page number is in the TLB; the physical address is computed immediately without accessing RAM for the page table.
- **TLB miss**: the entry is not in the TLB; the CPU (or OS, depending on architecture) walks the page table in RAM to find the entry, loads it into the TLB, and retries.

Because programs exhibit [[LocalityOfReference|spatial and temporal locality]], the same pages are accessed repeatedly, so TLB hit rates are high in practice.

## Cost of TLB flushes

A [[ContextSwitch]] typically requires flushing or tagging the TLB, because a new process has different virtual-to-physical mappings. This adds to the cost of context switching, particularly for processes with large working sets that take many accesses to warm the TLB again.

## Connections

- [[parproc-appA-systems-issues]] — §A.2.3; primary source.
- [[VirtualMemory]] — the mechanism the TLB accelerates.
- [[CacheMemory]] — the TLB is a specialized cache; both exploit locality; both have miss penalties.
- [[LocalityOfReference]] — the property that keeps TLB hit rates high.
- [[ContextSwitch]] — context switches flush or invalidate TLB entries, adding warm-up cost.
- [[MemoryHierarchy]] — the TLB is part of the hardware infrastructure supporting the memory hierarchy.
