---
title: "TLB (Translation Lookaside Buffer)"
type: concept
tags: [hardware, operating-systems, virtual-memory, cache, performance]
sources: [dis-13-3-virtual-memory, parproc-appA-systems-issues]
last_updated: 2026-05-17
---

# TLB — Translation Lookaside Buffer

The **TLB (Translation Lookaside Buffer)** is *"a hardware cache that stores (page number, frame number) mappings"* ([[dis-13-3-virtual-memory|DIS Ch 13.3]]). It eliminates the otherwise crippling overhead of [[VirtualMemory|virtual-memory]] translation — without a TLB, every memory access would require **two** RAM reads (one for the [[PageTable|PTE]], one for the data).

> This page is the **promoted canonical anchor** for the TLB concept. The wiki's prior page [[TranslationLookasideBuffer]] (filed under the spelled-out name from [[parproc-appA-systems-issues|ParProc App A]]) remains the long-form treatment; this short-name alias exists so `[[TLB]]` resolves directly.

## How it accelerates paging

On every memory access (after the [[MMU]] splits the [[VirtualAddress|VA]] into page number + offset):

- **TLB hit** — `(page_number → frame_number)` is in the TLB. The [[MMU]] constructs the [[PhysicalAddress|PA]] immediately. Total RAM accesses for the operation: **1** (the data itself).
- **TLB miss** — the [[MMU]] walks the [[PageTable|page table]] in RAM, reads the [[PageTable|PTE]], and inserts the mapping into the TLB. Total RAM accesses: **2** (PTE + data).

Because programs exhibit [[LocalityOfReference|spatial and temporal locality]], the same pages are accessed repeatedly, keeping TLB hit rates high.

## TLB and context switches

A [[ContextSwitch|context switch]] typically **flushes** or **tags** the TLB, because the incoming process has different virtual-to-physical mappings. The cold-cache TLB warm-up adds to the cost of context switching, especially for processes with large working sets.

## Cross-references

- The longer-form treatment lives at [[TranslationLookasideBuffer]] — both names refer to the same hardware component. Future ingests may consolidate.

## Connections

- [[dis-13-3-virtual-memory]] — promotes this concept from forward-reference to a first-class short-name page.
- [[parproc-appA-systems-issues]] — prior canonical source (under the [[TranslationLookasideBuffer]] long-name page).
- [[TranslationLookasideBuffer]] — sibling long-form page.
- [[VirtualMemory]] — the mechanism the TLB accelerates.
- [[PageTable]] — what the TLB caches entries from.
- [[VirtualAddress]] / [[PhysicalAddress]] — what the TLB translates between.
- [[Paging]] — the mechanism the TLB is a performance optimization for.
- [[MMU]] — the hardware unit that consults the TLB on every access.
- [[ContextSwitch]] — flushes / invalidates the TLB.
- [[LocalityOfReference]] — the property that keeps TLB hit rates high.
- [[CacheMemory]] — the TLB is a specialized cache; the general cache hierarchy operates on cache lines, the TLB on PTEs.
