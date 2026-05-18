---
title: "Page Fault"
type: concept
tags: [operating-systems, virtual-memory, memory, interrupt]
sources: [dis-13-3-virtual-memory]
last_updated: 2026-05-17
---

# Page Fault

A **page fault** is the hardware-raised interrupt the [[MMU]] generates *"when a process accesses a virtual address whose PTE has a valid bit of 0"* — i.e., the referenced [[Page|page]] is not currently in RAM. Per [[dis-13-3-virtual-memory|DIS Ch 13.3]], the page fault is the structural mechanism that makes [[DemandPaging|demand paging]] work: the process *believes* its entire [[AddressSpace|address space]] is in memory, while the OS quietly fetches pages from disk only as they are touched.

## Handling

When the [[MMU]] reads a [[PageTable|PTE]] with `valid == 0`, it transfers control to the OS's page-fault handler in [[KernelMode|kernel mode]]. The handler:

1. **Locate a free frame** in RAM (or evict one via [[LeastRecentlyUsed|LRU]] page replacement; if the victim's dirty bit is 1, write it back to disk first).
2. **Read the missing page from disk** ([[SwapFile|swap area]] or the backing file) into the chosen frame.
3. **Update the [[PageTable|PTE]]**: set `frame_number`, set `valid = 1`, clear `dirty = 0`.
4. **Restart the faulting instruction** — the access now finds a valid PTE and completes normally.

## Cost

A page fault is **catastrophically expensive** compared to a normal memory access — disk reads are mechanical (HDD ms-scale) or at best NAND-flash ([[SolidStateDrive|SSD]] sub-ms-scale), orders of magnitude slower than a [[CacheMiss|cache miss]]. Programs that fault frequently are said to **thrash**; the page-replacement [[LeastRecentlyUsed|LRU]] policy and the [[DemandPaging|demand-paging]] working-set discipline exist to keep fault rates low.

## Distinguishing legitimate faults from bugs

Not every page fault is recoverable. The OS distinguishes:

- **Resolvable fault** — the [[PageTable|PTE]] indicates the page exists but lives on disk → handle as above.
- **Access violation** — the virtual address is not allocated to the process at all (or violates a protection bit) → kill the process with [[SegmentationFault|`SIGSEGV`]] (segfault).

DIS Ch 13.3 covers the resolvable case; the segfault path is treated separately via the [[Signal|signal]] mechanism from [[dis-13-2-processes|Ch 13.2]].

## Connections

- [[dis-13-3-virtual-memory]] — primary source.
- [[VirtualMemory]] — the umbrella mechanism.
- [[PageTable]] — the data structure whose `valid == 0` bit triggers the fault.
- [[Page]] — the unit being faulted in.
- [[Paging]] — the mechanism page faults are part of.
- [[DemandPaging]] — the policy that uses page faults as its primary trigger.
- [[SwapFile]] — the source of the page being faulted in.
- [[LeastRecentlyUsed]] — the eviction policy used when no free frames are available.
- [[Interrupt]] — page faults are a hardware-raised interrupt class.
- [[KernelMode]] — handler runs here.
- [[SegmentationFault]] — the failure mode for non-resolvable address-space violations.
