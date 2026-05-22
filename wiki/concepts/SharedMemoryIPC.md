---
title: "Shared Memory (IPC)"
type: concept
tags: [posix, unix, ipc, shared-memory, page-table, shmget, mmap, system-v]
sources: [dis-13-4-3-shared-memory, dis-13-4-ipc]
last_updated: 2026-05-18
---

# Shared Memory (IPC)

The third and **fastest** [[InterprocessCommunication|IPC]] family ([[dis-13-4-3-shared-memory|DIS Ch 13.4.3]]): *"a process to share all or part of its virtual address space with other processes. Processes with shared memory can read or write to addresses in shared space to communicate with one another."*

> **Naming note.** The wiki also has [[SharedMemory|`SharedMemory.md`]] documenting [[CUDA|CUDA]]'s on-chip programmer-managed cache — a **different concept at a different layer**. This page is the **POSIX/System-V process-IPC** family.

## Structural mechanism

Shared memory rides directly on [[dis-13-3-virtual-memory|Ch 13.3]]'s [[PageTable|page-table]] machinery:

> "The OS can support sharing pages of virtual address space by setting entries in the page tables of sharing processes to the same physical frame number."

That is: the [[Kernel|kernel]] arranges that **distinct [[VirtualAddress|virtual addresses]]** in **distinct [[PageTable|page tables]]** resolve to the **same [[PhysicalAddress|physical frame]]**. After this aliasing is established, both processes read and write the shared region with **ordinary [[Load|load]] / [[Store|store]] instructions** — **no syscall per access**.

```
Process A virtual page V_A  ─┐
                              ├──► physical frame F  (RAM)
Process B virtual page V_B  ─┘
```

## API surface (named only — full coverage deferred to Ch 14)

[[dis-13-4-3-shared-memory|13.4.3]] names `shmget` and stops. The real POSIX/System-V APIs are:

| API | Family | Role |
|---|---|---|
| `shmget(key, size, flags)` | System V | Create / attach segment by integer key. |
| `shmat` / `shmdt` / `shmctl` | System V | Attach into address space / detach / control. |
| `shm_open` + `mmap` | POSIX | Modern path — opens a named shm object then maps into address space. |

## Performance vs synchronization trade-off

| Dimension | [[MessagePassing\|Message passing]] | Shared memory |
|---|---|---|
| Per-operation cost | Syscall + kernel copy | Ordinary memory access |
| Bandwidth ceiling | OS / channel-buffer-bound | Memory-system-bound |
| Synchronization | OS-managed (channel semantics) | **Application-managed** ([[Mutex]] / [[Semaphore]]) |

**Synchronization burden falls on the application** — concurrent overlapping writes create [[RaceCondition|race conditions]]. [[dis-13-4-3-shared-memory|13.4.3]] forward-references **Ch 14** for the coordination primitive coverage ([[Thread|threads]], [[Mutex|mutexes]], [[Semaphore|semaphores]]).

## Threads — the in-process analog

13.4.3 briefly notes [[Thread|threads]] as the same-process analog of shared memory: threads inside one process **share the full [[AddressSpace|address space]] by default**, so cross-thread "shared memory" needs no special syscall — the synchronization story carries over directly.

## Related

- [[InterprocessCommunication]] — parent umbrella concept.
- [[Signal]] — adjacent IPC family; commonly paired (signal = "data ready" notification + shared memory carries payload).
- [[MessagePassing]] — adjacent IPC family; slower but OS-synchronized.
- [[PageTable]] — the data structure the kernel mutates to install the alias.
- [[VirtualAddress]] / [[PhysicalAddress]] — the two layers between which the alias operates.
- [[VirtualMemory]] — the broader abstraction.
- [[SharedMemory]] — distinct concept (CUDA on-chip cache); same short name, different layer.
- [[Mutex]] / [[Semaphore]] — coordination primitives needed but deferred to Ch 14.
- [[Thread]] — in-process analog.
- [[dis-13-4-3-shared-memory]] — primary source.
- [[dis-13-3-virtual-memory]] — structural prerequisite.
