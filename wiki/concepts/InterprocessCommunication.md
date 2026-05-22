---
title: "Interprocess Communication (IPC)"
type: concept
tags: [operating-system, ipc, posix, unix, process, kernel]
sources: [dis-13-4-ipc, dis-13-4-1-signals, dis-13-4-2-message-passing, dis-13-4-3-shared-memory]
last_updated: 2026-05-18
---

# Interprocess Communication (IPC)

[[OperatingSystem|OS]]-mediated mechanisms by which [[Process|processes]] *"exchange information or coordinate their execution"* ([[dis-13-4-ipc|DIS Ch 13.4]]). The structural **inverse** of [[VirtualMemory|virtual-memory]] isolation: [[dis-13-3-virtual-memory|Ch 13.3]]'s [[PageTable|page-table]] machinery deliberately walls each process into a private [[AddressSpace|address space]] so processes cannot interfere — IPC re-opens **controlled** coordination channels through the [[Kernel|kernel]].

## The three IPC families

| Family | Mechanism | Payload | Speed | Synchronization |
|---|---|---|---|---|
| [[Signal\|Signals]] | Kernel-delivered software interrupt | None (identity only) | Fast | OS-managed |
| [[MessagePassing\|Message passing]] | OS-managed channel ([[Pipe]] / [[Socket]]) | Arbitrary byte stream | Medium (per-message OS copy) | OS-managed (channel semantics) |
| [[SharedMemoryIPC\|Shared memory]] | Aliased [[PageTable\|page-table]] entries to same physical frame | Arbitrary in-memory data | Fastest (direct load/store) | **Application responsibility** |

## Trade-off axis

- **Expressiveness**: signals carry no payload — only "event X occurred"; messaging and shared memory carry arbitrary bytes.
- **Performance**: shared memory is fastest (no per-access syscall), then message passing (syscall per send/receive), then signals (syscall to send, async delivery to receive).
- **Synchronization burden**: signals and message passing are OS-coordinated; shared memory pushes coordination to the application — [[Mutex|mutexes]] / [[Semaphore|semaphores]] / [[Atomic|atomics]] are required.

## Why three families exist

Each family hits a different point on the **fixed-namespace ↔ arbitrary-data** and **OS-mediated ↔ direct-memory** axes. Signals are sufficient when *"event happened"* is the whole message. Pipes/sockets dominate when a structured byte stream suffices (shell pipelines, network protocols). Shared memory is the high-bandwidth choice for tight-coupling co-resident processes — but pays in synchronization complexity.

## Related

- [[Signal]] — first family; software interrupts. See also [[SignalHandler]], [[Kill]].
- [[MessagePassing]] — second family; OS channel abstraction.
  - [[Pipe]] — same-machine one-way channel.
  - [[NamedPipe]] — filesystem-named pipe (FIFO).
  - [[Socket]] — two-way channel, spans network.
- [[SharedMemoryIPC]] — third family; page-table aliasing. (*Not* the [[SharedMemory|CUDA on-chip cache]] of the same short name.)
- [[Process]] — what communicates.
- [[VirtualMemory]] / [[PageTable]] — the isolation IPC works around.
- [[Kernel]] / [[SystemCall]] — IPC is implemented as kernel-mediated syscalls.
- [[dis-13-4-ipc]] — opening hub of the Ch 13.4 IPC sub-arc.
