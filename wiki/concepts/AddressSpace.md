---
title: "Address Space"
type: concept
tags: [c-language, memory, operating-systems]
sources: [dis-2-1-scope-memory]
last_updated: 2026-05-17
---

# Address Space

A program's **address space** is the range of [[CMemoryAddress|memory addresses]] it can access — *"storage locations for everything it needs in its execution, namely storage for its instructions and data,"* per [[dis-2-1-scope-memory|DIS Ch 2.1]].

For a [[CLanguage|C]] process running under a modern [[OperatingSystem|OS]], the address space is the byte-indexed range `0` through `2^N - 1` (where `N` is 32 or 64 depending on architecture). The OS partitions this range into the **four [[ProcessMemory|program-memory]] regions** Ch 2.1 names — [[CodeSection|code]], [[DataSection|data]], [[HeapSection|heap]], [[StackSection|stack]] — plus OS-reserved regions the program cannot touch.

## What it is — and isn't

- **It is a *virtual* range** — under modern OSes, each process gets its own virtual address space; the OS + MMU maps virtual addresses to physical RAM. Two processes can both store data at virtual address `0x7fff...` without colliding because their virtual spaces are separate.
- **It is not physical RAM** — the address space can be *larger* than installed RAM (pages spill to swap) and is *fragmented* across physical pages from the program's point of view.
- **It is not portable across runs** — [[AddressSpaceLayoutRandomization|ASLR]] randomizes layout each launch, so addresses observed in one run are not meaningful in another.

## Pedagogical placement

Ch 2.1 introduces the address space *operationally* — it's the container the four [[ProcessMemory|program-memory]] regions live in. The mechanism (virtual memory, page tables, MMU, the OS's role in setting it up) is **deferred** to later [[DiveIntoSystems]] OS chapters; here it's enough to know that *every variable has an address in this range* and *which region the address falls into determines the variable's lifetime / scope properties*.

## Connections

- [[dis-2-1-scope-memory]] — introducing source.
- [[ProcessMemory]] — the four-region partition of the address space.
- [[CMemoryAddress]] — pre-existing; the address space is the range these addresses index into.
- [[CodeSection]] / [[DataSection]] / [[HeapSection]] / [[StackSection]] — the four regions.
- [[OperatingSystem]] — sets up and maps the virtual address space (hosted world).
- [[CLanguage]] / [[DiveIntoSystems]].
