---
title: "Dive into Systems — 13.4 Interprocess Communication"
type: source
tags: [textbook, operating-systems, ipc, interprocess-communication, signals, message-passing, shared-memory]
date: 2026-05-18
source_file: https://diveintosystems.org/book/C13-OS/ipc.html
---

## Summary

**Fourth leaf of Ch 13 *The Operating System*** of [[DiveIntoSystems]] — opening **hub page** for the three-leaf IPC sub-arc (13.4.1 Signals + 13.4.2 Message Passing + 13.4.3 Shared Memory). Pivots from [[dis-13-3-virtual-memory|Ch 13.3]]'s **per-process isolation via paging** into the **inverse problem**: when applications *want* to coordinate, the [[VirtualMemory|virtual-memory]] wall prevents them. Codifies [[InterprocessCommunication|interprocess communication]] (**IPC**) as *"mechanisms by which operating systems enable processes to exchange information or coordinate their execution"*. Introduces the **three canonical IPC mechanism families**: (1) **[[Signal|signals]]** — *"a very restricted form of interprocess communication by which one process can send a signal to another process to notify it of some event"*; (2) **[[MessagePassing|message passing]]** — *"the OS implements an abstraction of a message communication channel that is used by a process to exchange messages with another process"*; (3) **[[SharedMemoryIPC|shared memory]]** — *"a process to share all or part of its virtual address space with other processes. Processes with shared memory can read or write to addresses in shared space to communicate with one another"*. Each leaf chapter (13.4.1 / 13.4.2 / 13.4.3) drills one family.

## Key Claims

- **[[InterprocessCommunication|IPC]] solves the inverse of the isolation problem** — [[dis-13-3-virtual-memory|Ch 13.3]]'s paging design prevents [[Process|processes]] from interfering by giving each a private [[AddressSpace|virtual address space]]; IPC adds back the **controlled** coordination channels applications need.
- **Three IPC mechanism families**: [[Signal|signals]] (event notification, restricted, no payload), [[MessagePassing|message passing]] (OS-mediated channel abstraction), [[SharedMemoryIPC|shared memory]] (overlap virtual address spaces directly).
- **Trade-off axis**: signals are simplest but least expressive (fixed signal set, no payload); message passing carries arbitrary data through an OS-managed channel; shared memory is fastest (no OS-mediated copy per message) but requires explicit synchronization.

## Key Quotes

> "Sometimes a user or programmer may want their application processes to communicate with one another (or to share some of their execution state) as they run." — motivating sentence for the chapter.

> "Signals are a very restricted form of interprocess communication by which one process can send a signal to another process to notify it of some event." — definition of the [[Signal|signal]] IPC family.

> "Processes with shared memory can read or write to addresses in shared space to communicate with one another." — defines the [[SharedMemoryIPC|shared-memory]] mechanism.

## Connections

- [[DiveIntoSystems]] — fourth leaf of Ch 13 *The Operating System*; **121st ingested DIS chapter** — opens the IPC sub-arc.
- [[dis-13-3-virtual-memory]] — sibling third leaf. 13.3's [[VirtualMemory|virtual-memory]] isolation is the precise property 13.4 needs to *work around* for inter-process coordination.
- [[dis-13-2-processes]] — second leaf. Names the [[Process|process]] abstraction whose [[AddressSpace|address-space]] privacy makes IPC necessary.
- [[dis-13-1-booting-running]] — opening leaf. The [[Kernel|kernel]] / [[SystemCall|system-call]] machinery is what implements every IPC channel.
- [[dis-13-4-1-signals]] — **next sibling**; drills the signal family.
- [[dis-13-4-2-message-passing]] — **second sibling**; drills [[Pipe|pipes]] / [[Socket|sockets]].
- [[dis-13-4-3-shared-memory]] — **third sibling**; drills the [[SharedMemoryIPC|shared-memory]] family.
- [[InterprocessCommunication]] — **new concept page**; canonical anchor for the IPC umbrella concept.
- [[Signal]] — pre-existing concept page (from [[dis-3-4-gdb-advanced|Ch 3.4]]); 13.4 promotes it from the GDB-debugger context into the IPC context.
- [[MessagePassing]] — **new concept page**; the OS-mediated channel abstraction.
- [[SharedMemoryIPC]] — **new concept page**; *not* the [[SharedMemory|CUDA on-chip cache]] of the same short name — disambiguated as the POSIX/System-V process-IPC family.

## Contradictions

- None — 13.4 extends the [[Process|process]] / [[VirtualMemory|virtual-memory]] arc; the [[Signal|signal]] treatment is consistent with and extends [[dis-3-4-gdb-advanced|Ch 3.4]]'s GDB-side coverage.
