---
title: "Swap File"
type: concept
tags: [operating-systems, virtual-memory, storage, memory]
sources: [dis-13-3-virtual-memory]
last_updated: 2026-05-17
---

# Swap File

A **swap file** (or swap area / swap partition) is the disk-resident backing store the OS uses to hold pages that are part of some [[Process|process]]'s [[AddressSpace|address space]] but are **not currently resident in [[RAM]]**. Per [[dis-13-3-virtual-memory|DIS Ch 13.3]], swap is what makes the **partial-residency** property of [[Paging|paging]] possible — *"a process can execute with only a partial address space loaded into RAM while other pages reside on disk."*

## Role in the page lifecycle

- **Page-out** — when the OS needs to evict an in-RAM [[Page|page]] (no free frames, victim chosen by a [[LeastRecentlyUsed|page-replacement policy]] such as LRU): if the victim's [[PageTable|dirty bit]] is set, write it to swap; if clean, drop it.
- **Page-in** — on a [[PageFault|page fault]] for a non-resident page, the OS reads it from swap into a free frame and updates the [[PageTable|PTE]].

## RAM-as-cache-for-disk

Together with paging, the swap file makes physical [[RAM]] act as a **cache for the swap area on disk** — the highest level of the [[MemoryHierarchy|memory hierarchy]] caching pattern from [[dis-11-1-memory-hierarchy|Ch 11.1]]. The cache analogy holds with the usual caveats: the *miss cost* (page fault → disk read) is many orders of magnitude greater than even an LL-cache miss, which is why the [[LeastRecentlyUsed|LRU]] eviction policy and [[LocalityOfReference|locality]] of access matter so much in practice.

## Why a file (or partition)?

Swap can be a dedicated partition (lower per-block overhead, fixed size) or a regular file in the filesystem (resizable on the fly). DIS Ch 13.3 treats the two interchangeably as the **swap area** — the OS sees only a block-addressable backing store.

## Connections

- [[dis-13-3-virtual-memory]] — primary source.
- [[VirtualMemory]] — the umbrella mechanism.
- [[Paging]] — the mechanism that moves pages between RAM and swap.
- [[Page]] — the unit that lives in swap.
- [[PageFault]] — the interrupt that triggers a page-in from swap.
- [[DemandPaging]] — the policy that decides *when* to pull pages back from swap.
- [[PageTable]] — its `valid` bit indicates whether a page is currently in RAM or on swap.
- [[LeastRecentlyUsed]] — the eviction policy choosing which pages get written out to swap.
- [[MemoryHierarchy]] — swap sits at the bottom (slowest, largest) tier.
- [[CacheMemory]] — paging makes RAM a cache for the swap-resident view of memory.
