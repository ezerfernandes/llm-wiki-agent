---
title: "Physical Address"
type: concept
tags: [operating-systems, virtual-memory, memory, addressing, hardware]
sources: [dis-13-3-virtual-memory]
last_updated: 2026-05-17
---

# Physical Address

A **physical address (PA)** is an address that *"reference[s] actual locations in RAM"* — what the [[MemoryBus|memory bus]] uses to fetch or store bytes in physical [[RAM]]. Per [[dis-13-3-virtual-memory|DIS Ch 13.3]], physical addresses are the translation target of [[VirtualAddress|virtual addresses]] in a paged [[VirtualMemory|virtual-memory]] system.

## Structure

In a paged system, a physical address splits into two fields, parallel to the structure of a [[VirtualAddress|virtual address]]:

- **Frame number** (high-order bits) — selects a fixed-size frame in physical RAM (a frame is the physical-side counterpart of a [[Page|page]]).
- **Page offset** (low-order bits) — byte position within the frame, **identical** to the offset in the originating [[VirtualAddress|virtual address]].

## Construction

The [[MMU]] constructs the physical address by *"using the frame number (f) bits from the PTE entry as the high-order bits, and the page offset (d) bits from the VA as the low-order bits."* The frame number is read from the [[PageTable|page-table entry]] (PTE) selected by the [[VirtualAddress|virtual address]]'s page number.

## Why processes don't see physical addresses

User-mode code references virtual addresses only — physical addresses are an OS / hardware concern. This is the structural mechanism for **process isolation**: two processes' identical [[VirtualAddress|virtual addresses]] map to different physical addresses under the OS's control, so neither can reach the other's RAM bytes.

## Connections

- [[dis-13-3-virtual-memory]] — primary source.
- [[VirtualAddress]] — the translation source.
- [[VirtualMemory]] — the umbrella mechanism.
- [[PageTable]] — supplies the frame number used to build the PA.
- [[Page]] — page and frame are the same size; the offset is identical on both sides.
- [[Paging]] — the mechanism that motivates the frame-number/offset split.
- [[MMU]] — the hardware unit that constructs the PA.
- [[RAM]] — the storage device PAs index into.
