---
title: "Dive into Systems — 13.3 Virtual Memory"
type: source
tags: [textbook, operating-systems, virtual-memory, paging, page-table, tlb, demand-paging]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C13-OS/vm.html
---

## Summary

**Third leaf of Ch 13 *The Operating System*** of [[DiveIntoSystems]]. Section 13.3 codifies **[[VirtualMemory|virtual memory]]** as *"an abstraction that gives each process its own private, logical address space in which its instructions and data are stored"* — making the per-process [[AddressSpace|address space]] the prior leaves named ([[dis-13-1-booting-running|13.1]] / [[dis-13-2-processes|13.2]]) into a hardware-and-OS mechanism. Splits memory addresses into **[[VirtualAddress|virtual]]** (process view) vs **[[PhysicalAddress|physical]]** (RAM location); divides each address space into fixed-size **[[Page|pages]]** (virtual side) and **frames** (physical side). The **[[PageTable|page table]]** holds per-process virtual-to-physical mappings consulted on every memory access via the **MMU** + **PTBR** (page-table base register). When a [[PageTable|PTE]]'s valid bit is 0, the access traps as a **[[PageFault|page fault]]** — the OS fetches the missing page from disk into a free frame, updates the PTE, and restarts the instruction. **[[DemandPaging|Demand paging]]** lets processes run with only their working set in RAM and the rest in the **[[SwapFile|swap]] area** on disk, enabling RAM to serve as a cache for disk. The **[[TLB|Translation Lookaside Buffer]]** — promoted from the forward-reference [[TranslationLookasideBuffer|TLB]] page already in the wiki — caches recent translations so a typical access costs **one** RAM read instead of two. Closes with **LRU page replacement** + **dirty bit write-back** as the eviction discipline when RAM is full, and the [[ContextSwitch|context-switch]] protocol of repointing the **PTBR** as the hardware-enforced process-isolation mechanism.

## Key Claims

- **[[VirtualMemory|Virtual memory]]** is *"an abstraction that gives each process its own private, logical address space in which its instructions and data are stored"* — each [[Process|process]] sees a contiguous range from address 0 to a maximum (`2^32 − 1` on a 32-bit system) and has no visibility of any other process's space.
- **[[VirtualAddress|Virtual]] vs [[PhysicalAddress|physical]] addresses**: two processes running identical code share the *same* virtual addresses for their variables, but the OS maps those virtual addresses to *different* physical RAM locations — the **structural mechanism for process isolation**.
- **[[Paging|Paging]]** divides the [[AddressSpace|address space]] into fixed-size **[[Page|pages]]** (virtual side, commonly **4 KB**) and physical RAM into same-size **frames**. Any virtual page may load into any physical frame; pages need not occupy contiguous RAM; *"a process can execute with only a partial address space loaded into RAM"*.
- **Address split**: high-order bits encode the page number (virtual) or frame number (physical); low-order bits encode the byte **offset** within the page/frame. The offset is **identical** in virtual and physical addresses — only the page number is translated.
- The **[[PageTable|page table]]** is the per-[[Process|process]] OS data structure storing **page-table entries (PTEs)** — each PTE records the physical **frame number**, a **valid bit** (1 = in RAM, 0 = on disk), and a **dirty bit** (1 = in-RAM copy has been written and differs from disk).
- The **Page Table Base Register (PTBR)** is a hardware register pointing to the current process's page table. *"The OS maintains virtual memory mappings for each process to ensure that it can correctly translate virtual to physical addresses."*
- **Four-step translation** performed by the [[MMU|MMU]] on every memory access: (1) split [[VirtualAddress|VA]] into page-number + offset; (2) index the page table at `PTBR + page_number`; (3) check the valid bit — if 0, raise a [[PageFault|page fault]]; (4) concatenate the frame number from the PTE with the page offset to form the [[PhysicalAddress|physical address]].
- **[[PageFault|Page fault]]** is *"triggered when a process accesses a virtual address whose PTE has a valid bit of 0"* — the page is not in RAM. The OS handler: locate a free frame → read the missing page from disk → update the PTE (frame number + valid = 1) → restart the faulting instruction.
- **[[DemandPaging|Demand paging]]**: pages are loaded **only when accessed** — *"a process can execute with only a partial address space loaded into RAM while other pages reside on disk."* Enables more concurrent [[Process|processes]] than RAM could hold and uses RAM as a cache for the **[[SwapFile|swap]] area** on disk.
- **Page replacement** (when no free frames exist): the OS applies a **policy** to evict an existing page; **[[LeastRecentlyUsed|LRU]]** is the canonical choice (leverages [[TemporalLocality|temporal locality]]). If the evicted page's **dirty bit** is set, it must be **written back to disk** first to preserve modifications; clean pages can be dropped.
- **[[TLB|Translation Lookaside Buffer]]** (*"a hardware cache that stores (page number, frame number) mappings"*) eliminates the double-memory-access overhead of paging: **TLB hit** = one RAM access (data only); **TLB miss** = two RAM accesses (page-table walk, then data). High [[LocalityOfReference|memory locality]] keeps TLB hit rates high, making paged virtual memory practical.
- **[[ContextSwitch|Context switch]] protocol**: the OS updates the PTBR to point to the incoming process's page table — *"this hardware-enforced mechanism prevents one process from accessing another's virtual address space"* — the primary security feature protecting process isolation.

## Key Quotes

> "Virtual memory is an abstraction that gives each process its own private, logical address space in which its instructions and data are stored." — definition of virtual memory.

> "The MMU constructs the physical address using the frame number (f) bits from the PTE entry as the high-order bits, and the page offset (d) bits from the VA as the low-order bits." — the address-construction half of the four-step translation.

> "The OS needs to implement a good page replacement policy for selecting which frame in RAM will be written back to disk." — names the policy/mechanism split for eviction.

> "A translation look-aside buffer (TLB) is a hardware cache that stores (page number, frame number) mappings." — definition of the TLB.

## Connections

- [[DiveIntoSystems]] — third leaf of Ch 13 *The Operating System*; **120th ingested DIS chapter**.
- [[dis-13-2-processes]] — sibling second leaf. 13.2 named the per-process [[AddressSpace|address space]] inside the [[ProcessControlBlock|PCB]] but treated it as a token; 13.3 makes it the chapter's subject — mechanism (paging), data structure ([[PageTable|page table]]), and hardware ([[MMU]] + PTBR + [[TLB]]).
- [[dis-13-1-booting-running]] — opening Ch 13 leaf. Named [[KernelMode]] / [[UserMode]] / [[Interrupt]]; 13.3's [[PageFault|page fault]] is the canonical hardware-[[Interrupt|interrupt]] / [[KernelMode|kernel-mode]] handler example.
- [[AddressSpace]] — the per-process abstraction 13.3 operationalizes via paging.
- [[ProcessMemory]] — the four-region program-memory layout from [[dis-2-1-scope-memory|Ch 2.1]] now revealed as virtual; the physical backing is non-contiguous frames stitched by the [[PageTable|page table]].
- [[VirtualMemory]] — **substantially extended in place** from the [[parproc-appA-systems-issues|ParProc App A]] stub into the canonical OS-textbook treatment (pages/frames + PTE/PTBR + four-step translation + demand paging + LRU eviction + dirty bit + TLB integration).
- [[VirtualAddress]] — **new concept page**; the process-view address split into page number + offset.
- [[PhysicalAddress]] — **new concept page**; the RAM-location address split into frame number + offset.
- [[PageTable]] — **new concept page**; the per-process virtual-to-physical mapping table consulted on every memory access.
- [[Page]] — **new concept page**; the fixed-size unit of virtual address space (commonly 4 KB) — paired with the same-size physical *frame*.
- [[Paging]] — **new concept page**; the memory-management mechanism itself.
- [[PageFault]] — **new concept page**; the interrupt raised when a referenced page is not in RAM.
- [[TLB]] — **promoted from forward-reference**; the existing [[TranslationLookasideBuffer]] page is the canonical anchor — `TLB.md` becomes a short alias/redirect-style page pointing to it.
- [[DemandPaging]] — **new concept page**; the load-on-first-access strategy that makes the partial-resident execution model work.
- [[SwapFile]] — **new concept page**; the disk-resident backing store for evicted / unloaded pages.
- [[MMU]] — extended/named: the hardware unit that performs the four-step translation on every memory access.
- [[ContextSwitch]] — extended in place: 13.3 adds the **PTBR-update protocol** as the hardware-enforced isolation mechanism, complementing 13.1's kernel-stack-pointer + 13.2's register-snapshot framing.
- [[TranslationLookasideBuffer]] — pre-existing concept page; 13.3 makes the integration concrete (TLB caches PTEs to avoid double memory access).
- [[LeastRecentlyUsed]] — pre-existing concept page; 13.3 adds the **page-replacement** use case alongside the [[CacheReplacementPolicy|cache-replacement]] use case from [[dis-11-4-caching|Ch 11.4]].
- [[TemporalLocality]] — pre-existing concept page; the property LRU exploits.
- [[LocalityOfReference]] — pre-existing concept page; the property that keeps TLB hit rates high.
- [[CacheMemory]] — pre-existing concept page; RAM-as-cache-for-disk in 13.3 is the highest-level instance of the [[MemoryHierarchy|memory-hierarchy]] caching pattern from [[dis-11-1-memory-hierarchy|Ch 11.1]].
- [[parproc-appA-systems-issues]] — the wiki's prior canonical VM source; 13.3 supersedes the App-A treatment at the OS-textbook level of detail.

## Contradictions

- None with existing wiki content. 13.3's treatment is consistent with and extends [[parproc-appA-systems-issues]] §A.2.2 (the prior canonical source for [[VirtualMemory]]) and [[dis-11-1-memory-hierarchy|Ch 11.1]]'s memory-hierarchy framing.
