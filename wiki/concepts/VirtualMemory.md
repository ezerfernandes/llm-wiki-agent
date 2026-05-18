---
title: "Virtual Memory"
type: concept
tags: [operating-systems, systems, performance, memory]
sources: [parproc-appA-systems-issues, dis-13-3-virtual-memory]
last_updated: 2026-05-17
---

# Virtual Memory

**Virtual memory (VM)** is a hardware/OS mechanism that gives each program a private, contiguous address space that may be larger than physical RAM. The OS maps *virtual addresses* (what the program sees) to *physical addresses* (actual RAM locations) via a data structure called the **page table**.

## Goals

VM serves three goals (per [[parproc-appA-systems-issues]] §A.2.2.1):

1. **Overcome memory-size limits**: a program (or the collective set of programs on the machine) may have memory needs larger than available physical RAM.
2. **Relieve the compiler and linker of real-address management**: the compiler can generate code that assumes a program starts at a fixed virtual address (e.g., 0x20200) without worrying about conflicts with other programs, because the OS maps each program to different physical locations.
3. **Enable security**: one program cannot access another program's memory, its I/O streams, or the OS itself, because the page table is controlled by the OS and encodes per-process access permissions.

## How it works

A virtual address is split into a **page number** (high-order bits) and an **offset** within the page (low-order bits). The offset is the same in both the virtual and physical addresses; only the page number is translated.

The OS maintains a **page table** — an array mapping virtual page numbers to physical page numbers — set up when the program is loaded into memory. On every memory access, the CPU hardware looks up the virtual page number in the page table, obtains the physical page number, and combines it with the offset to form the physical address.

If the page table entry indicates the page is **not resident** in RAM (it may be on disk), a **page fault** occurs: the CPU generates an internal interrupt, the OS handles it by loading the page from disk into RAM and updating the page table, then restarts the faulting instruction.

## Performance issues

- **Page faults are catastrophically expensive.** Disk access is mechanical, not electronic. A page fault triggers OS intervention plus a disk read — orders of magnitude slower than a [[CacheMemory|cache miss]]. On Unix, the `time` command reports page fault counts. The *page replacement policy* (which page to evict when RAM is full) is critical.
- **Double memory access per VM lookup.** Without optimization, each memory access requires two RAM reads: one to read the page table entry, one to read the actual data word. This overhead is eliminated by the [[TranslationLookasideBuffer]] (TLB), a special hardware cache for page-table entries.

## DIS Ch 13.3 OS-textbook treatment

[[dis-13-3-virtual-memory|*Dive into Systems* Ch 13.3]] sharpens this concept with the OS-textbook definition — *"virtual memory is an abstraction that gives each process its own private, logical address space in which its instructions and data are stored"* — and operationalizes it through five additions to the ParProc-App-A coverage:

1. **Pages and frames.** Each [[AddressSpace|address space]] is divided into fixed-size **[[Page|pages]]** (commonly 4 KB); physical RAM into same-size **frames**. Any virtual page can occupy any physical frame; pages need not be contiguous. See [[Paging]].
2. **Address split.** A [[VirtualAddress|virtual address]] splits into a page number (high bits) + offset (low bits); the corresponding [[PhysicalAddress|physical address]] uses the same offset and a translated frame number. Only the page number is translated.
3. **Page-table entry (PTE) bits.** Each [[PageTable|PTE]] has a frame number, a **valid bit** (0 ⇒ page is not in RAM ⇒ [[PageFault|page fault]] on access), and a **dirty bit** (1 ⇒ in-RAM copy was written ⇒ must be written back on eviction). The **PTBR** (page-table base register) points the [[MMU]] at the running process's page table.
4. **Demand paging + LRU eviction.** [[DemandPaging|Pages are loaded only on first reference]]; when free frames run out, an [[LeastRecentlyUsed|LRU]] page is evicted (dirty pages written to the [[SwapFile|swap area]] first, clean pages dropped). Makes RAM a cache for the on-disk view of memory.
5. **Process isolation via PTBR swap.** A [[ContextSwitch|context switch]] updates the PTBR to the incoming process's page table — the hardware-enforced mechanism that prevents one process from reaching another's address space.

## Connections

- [[dis-13-3-virtual-memory]] — DIS Ch 13.3; primary OS-textbook source.
- [[parproc-appA-systems-issues]] — §A.2.2; original wiki source (parallel-processing systems framing).
- [[VirtualAddress]] / [[PhysicalAddress]] — the two address kinds VM translates between.
- [[Page]] — fixed-size unit of the virtual address space.
- [[PageTable]] — per-process virtual-to-physical mapping data structure.
- [[Paging]] — the mechanism that implements VM.
- [[PageFault]] — interrupt raised when a referenced page is not in RAM.
- [[DemandPaging]] — load-on-first-reference policy enabled by paging.
- [[SwapFile]] — disk-resident backing store for non-resident pages.
- [[MMU]] — hardware unit that performs translation on every access.
- [[TLB]] / [[TranslationLookasideBuffer]] — hardware cache for page-table entries, avoiding double memory access.
- [[AddressSpace]] / [[ProcessMemory]] — the per-process layouts VM gives each process privately.
- [[ContextSwitch]] — updates the PTBR; hardware-enforced process isolation.
- [[MemoryHierarchy]] — VM is the lowest, slowest tier of the memory hierarchy (disk).
- [[CacheMemory]] — RAM acts as a cache for disk-resident pages; page faults are analogous to but far more expensive than [[CacheMiss|cache misses]].
- [[LocalityOfReference]] — access patterns that minimize both cache misses and page faults.
- [[MemoryAllocation]] — dynamic allocation interacts with the VM system: first-touch of newly allocated pages triggers page-table updates and may cause faults.
