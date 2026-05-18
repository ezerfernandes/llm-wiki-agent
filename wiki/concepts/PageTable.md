---
title: "Page Table"
type: concept
tags: [operating-systems, virtual-memory, memory, data-structure]
sources: [dis-13-3-virtual-memory]
last_updated: 2026-05-17
---

# Page Table

A **page table** is the per-[[Process|process]] data structure (stored in [[RAM]]) that holds the virtual-to-physical mappings the [[MMU]] consults on every memory access. Per [[dis-13-3-virtual-memory|DIS Ch 13.3]], *"the OS maintains virtual memory mappings for each process to ensure that it can correctly translate virtual to physical addresses."*

## Page Table Entry (PTE)

Each entry records, at minimum:

- **Frame number** — the physical [[Page|frame]] this virtual page currently occupies (valid only when the **valid bit** is 1).
- **Valid bit** — `1` = page is resident in RAM; `0` = page is **not** resident (on disk in the [[SwapFile|swap]] area, or never allocated) — accessing it raises a [[PageFault|page fault]].
- **Dirty bit** — `1` = the in-RAM copy has been written and *differs from* the disk copy, so eviction must write it back; `0` = clean, can be dropped without write-back.

Real systems add protection bits (read / write / execute / user-vs-kernel), accessed bits, and so on, but DIS Ch 13.3 covers only the three above.

## Lookup

The hardware **Page Table Base Register (PTBR)** stores the physical address of the current process's page table. On every memory access, the [[MMU]]:

1. Splits the [[VirtualAddress|virtual address]] into page-number + offset.
2. Reads `PTE = PageTable[page_number]` at `PTBR + page_number * sizeof(PTE)`.
3. If `PTE.valid == 0` → raise [[PageFault|page fault]].
4. Else construct the [[PhysicalAddress|physical address]] = `PTE.frame_number || offset`.

The [[TLB|Translation Lookaside Buffer]] caches recent PTEs so that this lookup is one RAM access (TLB hit) instead of two (TLB miss + data fetch).

## Per-process protection

A [[ContextSwitch|context switch]] updates the PTBR to point at the incoming process's page table — *"this hardware-enforced mechanism prevents one process from accessing another's virtual address space"* — the primary mechanism for process isolation.

## Connections

- [[dis-13-3-virtual-memory]] — primary source.
- [[VirtualMemory]] — the umbrella mechanism.
- [[VirtualAddress]] / [[PhysicalAddress]] — the two address spaces the page table maps between.
- [[Page]] — the fixed-size unit each PTE describes one mapping for.
- [[Paging]] — the mechanism that uses the page table.
- [[PageFault]] — what happens on `PTE.valid == 0`.
- [[TLB]] — hardware cache of recent PTEs.
- [[MMU]] — performs the lookup on every memory access.
- [[ContextSwitch]] — updates the PTBR on every process swap.
- [[ProcessControlBlock]] — the OS data structure containing the page-table pointer (among other per-process state).
