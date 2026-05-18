---
title: "Virtual Address"
type: concept
tags: [operating-systems, virtual-memory, memory, addressing]
sources: [dis-13-3-virtual-memory]
last_updated: 2026-05-17
---

# Virtual Address

A **virtual address (VA)** is an address in a [[Process|process]]'s private, logical [[AddressSpace|address space]] — the form of addresses that **every** instruction the process executes uses to read or write memory. Per [[dis-13-3-virtual-memory|DIS Ch 13.3]], virtual addresses *"refer to storage locations within a process's view of memory"* — distinct from [[PhysicalAddress|physical addresses]] which reference actual RAM locations.

## Structure

In a paged [[VirtualMemory|virtual-memory]] system, a virtual address splits into two fields:

- **Page number** (high-order bits) — selects an entry in the [[PageTable|page table]].
- **Page offset** (low-order bits) — the byte position within the [[Page|page]].

For example, with **8-byte pages**, the low **3 bits** address bytes within a page (`2^3 = 8`), and the remaining bits index the page table. The offset is **identical** in the virtual and the corresponding [[PhysicalAddress|physical address]] — only the page number is translated.

## Translation

On every memory access the [[MMU]] reads the virtual address from the CPU, uses the page number to index the running process's [[PageTable|page table]] (located via the **PTBR** — page-table base register), reads the [[PageTable|PTE]]'s frame number, and concatenates it with the offset to produce the [[PhysicalAddress|physical address]]. If the PTE's valid bit is 0, the translation raises a [[PageFault|page fault]] instead.

## Why virtual addresses exist

- **Process isolation**: two processes can hold the *same* virtual address (e.g., the start of `main`) yet read or write *different* physical RAM bytes — the OS controls the mapping, so one process cannot reach another's data.
- **Compiler simplicity**: the [[CCompiler|compiler]] can emit a binary that assumes it owns memory from 0 upward, without knowing where the program will actually run in RAM.
- **Demand paging**: a virtual address may refer to a page that is currently on disk; the hardware/OS load it on first reference (see [[DemandPaging]]).

## Connections

- [[dis-13-3-virtual-memory]] — primary source.
- [[VirtualMemory]] — the umbrella mechanism virtual addresses live inside.
- [[PhysicalAddress]] — the translation target.
- [[PageTable]] — the data structure consulted to translate a VA.
- [[Page]] — the unit a VA's page number selects.
- [[Paging]] — the mechanism that justifies the page-number/offset split.
- [[AddressSpace]] — the set of VAs each process owns.
- [[MMU]] — the hardware unit that performs the translation.
- [[TLB]] — caches recent VA → frame-number translations to avoid page-table walks.
