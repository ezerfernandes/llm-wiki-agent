---
title: "Dive into Systems — 13.4.3 Shared Memory"
type: source
tags: [textbook, operating-systems, ipc, shared-memory, shmget, page-table, synchronization]
date: 2026-05-18
source_file: https://diveintosystems.org/book/C13-OS/ipc_shm.html
---

## Summary

**Third sub-leaf of [[dis-13-4-ipc|Ch 13.4]]** — formalizes the **[[SharedMemoryIPC|shared-memory]]** IPC family: processes communicate by **sharing portions of their [[VirtualMemory|virtual address spaces]]** so that one process writes values to shared memory while another reads them. The **structural mechanism** rests directly on [[dis-13-3-virtual-memory|Ch 13.3]]'s [[PageTable|page-table]] infrastructure: *"the OS can support sharing pages of virtual address space by setting entries in the page tables of sharing processes to the same physical frame number"* — that is, the kernel arranges that two distinct [[VirtualAddress|virtual addresses]] in two different processes' page tables resolve to the *same* [[PhysicalAddress|physical frame]]. Names `shmget` as the Unix [[SystemCall|system call]] for creating or attaching to shared memory segments, but provides no implementation details. **Synchronization, race conditions, semaphores/mutexes, POSIX `shm_open`/`mmap`, and System V `shmat`/`shmdt`/`shmctl` mechanics are deferred** — the chapter briefly notes threads as an alternative for sharing full address spaces and **forward references Ch 14** for detailed [[Thread|threading]] and synchronization. The pivot vs [[MessagePassing|message passing]]: shared memory is **faster** because once the page-table aliasing is established, no per-message OS-mediated copy is needed — both processes simply load/store to ordinary virtual addresses; the trade-off is that **synchronization becomes the application's responsibility**.

## Key Claims

- **[[SharedMemoryIPC|Shared memory]] definition**: processes communicate by **sharing portions of their virtual address spaces** — one writes, another reads, both via ordinary [[Load|load]] / [[Store|store]] instructions to the shared region.
- **Mechanism rests on the [[PageTable|page table]]** — *"the OS can support sharing pages of virtual address space by setting entries in the page tables of sharing processes to the same physical frame number"* — two processes' virtual-address-space slots resolve to one physical frame.
- **[[Shmget|`shmget`]] is the Unix shared-memory syscall** — *creates or attaches* to a shared memory segment. (Implementation details deferred.)
- **Performance advantage over [[MessagePassing|message passing]]**: once the page-table aliasing is in place, there is **no per-access OS mediation** — load/store is direct hardware traffic against the shared frames.
- **Synchronization burden falls on the application** — concurrent writes to overlapping shared regions create [[RaceCondition|race conditions]]; coordination primitives ([[Mutex|mutexes]], [[Semaphore|semaphores]]) are needed but **not covered in 13.4.3** — forward-referenced to Ch 14.
- **[[Thread|Threads]] are the alternative for sharing full address spaces** — briefly noted as the in-process analog of cross-process shared memory; full treatment deferred to Ch 14.

## Key Quotes

> "The OS can support sharing pages of virtual address space by setting entries in the page tables of sharing processes to the same physical frame number." — the page-table mechanism behind shared memory.

> "Processes with shared memory can read or write to addresses in shared space to communicate with one another." — definition of the shared-memory IPC mechanism (from the [[dis-13-4-ipc|parent hub]]).

## Connections

- [[DiveIntoSystems]] — third sub-leaf of Ch 13.4; **124th ingested DIS chapter** — closes the IPC sub-arc.
- [[dis-13-4-ipc]] — parent hub.
- [[dis-13-4-1-signals]] — first sibling. Signals + shared memory are often paired in practice (signal to notify "data ready", shared memory carries the data).
- [[dis-13-4-2-message-passing]] — prior sibling. Shared memory removes the per-message copy overhead of message passing.
- [[dis-13-3-virtual-memory]] — **structural prerequisite**. Shared memory works by aliasing entries in two different [[PageTable|page tables]] to the same physical [[Page|frame]] — direct reuse of 13.3's machinery.
- [[SharedMemoryIPC]] — **new concept page**; canonical anchor for the POSIX/System-V process-IPC shared-memory family. Disambiguated from the unrelated [[SharedMemory|CUDA on-chip shared memory]].
- [[InterprocessCommunication]] — parent umbrella concept.
- [[PageTable]] — pre-existing concept; the data structure 13.4.3 reuses for page aliasing.
- [[VirtualAddress]] / [[PhysicalAddress]] — pre-existing; the layers between which the page-table aliasing operates.
- [[SystemCall]] — `shmget` is the named syscall.
- [[Thread]] — forward-referenced as the in-process analog.

## Contradictions

- **Naming collision (not a contradiction)**: the wiki already has a [[SharedMemory|`SharedMemory.md`]] page anchored to the **[[CUDA|CUDA]] on-chip programmer-managed cache** ([[parproc-ch05-cuda-gpu-programming|ParProc Ch 5]]). The Ch 13.4.3 IPC mechanism is a **distinct concept** at a different abstraction layer — minted here as [[SharedMemoryIPC]] to avoid overloading the existing page.
