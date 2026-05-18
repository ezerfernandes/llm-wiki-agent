---
title: "Demand Paging"
type: concept
tags: [operating-systems, virtual-memory, memory, policy]
sources: [dis-13-3-virtual-memory]
last_updated: 2026-05-17
---

# Demand Paging

**Demand paging** is the [[VirtualMemory|virtual-memory]] policy of loading a [[Page|page]] into [[RAM]] **only when it is first accessed** — never proactively. Per [[dis-13-3-virtual-memory|DIS Ch 13.3]], demand paging is what enables *"a process [to] execute with only a partial address space loaded into RAM while other pages reside on disk"*, making it possible to run more (and larger) processes than RAM could hold all at once.

## Mechanism

- A process starts with most (or even all) of its pages **not resident** — their [[PageTable|PTEs]] have `valid = 0`.
- First reference to such a page raises a [[PageFault|page fault]]; the OS reads the page from the [[SwapFile|swap area]] (or the backing executable / file), installs it in a free frame, and updates the PTE.
- Subsequent accesses to the now-resident page are fast (TLB-hit or PTE-walk only).

## Why it works

Programs exhibit [[LocalityOfReference|locality]]: only a small **working set** of pages is actively used at any moment. Demand paging matches that distribution by paying the load cost only for pages the program actually touches, and lets the [[LeastRecentlyUsed|LRU]] eviction policy keep the hot working set resident.

## Consequences

- **Throughput** — more concurrent [[Process|processes]] can share limited RAM, increasing CPU utilization (one process can run while another's pages are being fetched from disk).
- **Startup latency** — large programs start *faster* because not all pages need to be loaded before execution begins; the cost is paid lazily.
- **Thrashing risk** — if the **collective** working set exceeds RAM capacity, the system spends most of its time servicing page faults instead of executing instructions — the failure mode demand paging makes possible.

## Connections

- [[dis-13-3-virtual-memory]] — primary source.
- [[VirtualMemory]] — the umbrella mechanism.
- [[Paging]] — the mechanism demand paging is a policy for.
- [[PageFault]] — the trigger demand paging relies on.
- [[Page]] — the unit demand paging loads.
- [[SwapFile]] — the disk-resident source pages are demand-loaded from.
- [[PageTable]] — the data structure whose `valid` bit demand paging flips on first access.
- [[LeastRecentlyUsed]] — the standard companion eviction policy when free frames run out.
- [[LocalityOfReference]] — the property that makes demand paging efficient.
- [[WorkingSet]] — the set of pages actively in use; demand paging targets keeping this resident.
