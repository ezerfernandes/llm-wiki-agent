---
title: "Shared-Memory Parallelism"
type: concept
tags: [parallel-computing, concurrency, multicore, threads, shared-memory]
sources: [dis-14-1-multicore]
last_updated: 2026-05-18
---

# Shared-Memory Parallelism

**Shared-memory parallelism** is the [[ParallelComputing|parallel-programming]] paradigm in which multiple flows of execution (typically [[Thread|threads]]) cooperate on a single computation by **reading and writing a common address space**, rather than communicating via [[MessagePassing|messages]] over private address spaces. It is the paradigm [[DiveIntoSystems]] Ch 14 (*Leveraging Shared Memory in the Multicore Era*) is built around — [[dis-14-1-multicore|§14.1]] supplies the motivation and the [[Thread|thread]] vocabulary; subsequent §14.x sections (deferred from this ingest) supply the [[Mutex|mutex]] / [[Semaphore|semaphore]] / [[Barrier|barrier]] coordination machinery.

## Why it's the natural fit for [[MulticoreProcessor|multicore]]

A [[MulticoreProcessor|multicore CPU]] is, by hardware construction, a [[SharedMemoryArchitecture|shared-memory architecture]] — all cores see the same physical RAM through a coherent [[CacheLevel|cache hierarchy]] (the [[CacheCoherency|coherence]] machinery [[dis-11-6-cache-coherency|Ch 11.6]] codified). The programmer pays no per-access syscall (unlike [[SharedMemoryIPC|cross-process shared memory]] which needs `shmget`-style aliasing setup) — [[Thread|threads]] inside one [[Process|process]] **share global variables, the heap, and code** by default, with only the per-thread [[CallStack|stack]] kept private (as [[dis-13-4-3-shared-memory|Ch 13.4.3]]'s thread sidebar already foreshadowed).

## Contrast with the other IPC families

[[DiveIntoSystems]] [[dis-13-4-ipc|Ch 13.4]] enumerates three [[InterprocessCommunication|IPC]] families across **private**-address-space processes:

- [[Signal|Signals]] — fixed namespace, event notification only.
- [[MessagePassing|Message passing]] (pipes, sockets) — OS-mediated copy per message.
- [[SharedMemoryIPC|Shared memory (cross-process)]] — `shmget` / `mmap` aliasing of [[VirtualAddress|VAs]] in two processes to the same [[PhysicalAddress|physical frame]].

**Shared-memory parallelism via threads** is the **in-process** analog of the third family — same mechanism (common physical memory) with the per-process address-space-aliasing setup *eliminated* because all threads in one process already share it by construction. This is why threads are *"lightweight"* (the [[dis-14-1-multicore|Ch 14.1]] adjective): no kernel-mediated aliasing, no per-access permission check.

## Coordination obligations

Shared writes that two threads can both perform require explicit coordination — the chapter forward-references but does not introduce:

- **[[CriticalSection|Critical sections]]** — code regions only one thread may execute at a time.
- **[[Mutex|Mutexes]]** — locks enforcing mutual exclusion around critical sections.
- **[[Semaphore|Semaphores]]** — counted resource-availability primitives.
- **[[Barrier|Barriers]]** — collective synchronization points all threads must reach before any continues.
- **[[ConditionVariable|Condition variables]]** — wait-for-predicate primitives.

Without these, races corrupt the shared state — the headline cost of the paradigm, paid in exchange for the *"no syscall per access"* speed advantage.

## Programmer-facing APIs

- [[Pthreads]] — POSIX threads, the C-language reference API (the one [[dis-3-6-gdb-pthreads|Ch 3.6]] introduces for debugging and [[dis-14-1-multicore|Ch 14.1]] forward-references for §14.x deepening).
- [[OpenMP]] — pragma-directive layer that hides explicit thread management; the [[parproc-ch04-openmp|parproc Ch 4]] subject.
- C++11 `std::thread` — language-standard equivalent.
- Java threads, Python `threading`, Go `go` statements — language-native sugar.

## The 1/c speedup ceiling

For an [[EmbarrassinglyParallel|embarrassingly parallel]] workload (no shared writes), the [[dis-14-1-multicore|Ch 14.1]] rule applies — *t* threads on *c* cores gives approximately **1/c** wall-clock time when `t = c` and the OS schedules them onto distinct cores. See [[Speedup]] for the formal metric. Shared-memory contention, coordination overhead, and false sharing pull the realized speedup below this ceiling — [[AmdahlsLaw|Amdahl's law]] (not covered by Ch 14.1, but covered by [[parproc-ch01-intro-parallel-processing|parproc Ch 1]]) formalizes the serial-fraction tax.

## Connections

- [[ParallelComputing]] — the umbrella paradigm; shared-memory parallelism is one of two top-level branches (the other being [[MessagePassing|message-passing parallelism]] of [[MPI]] / distributed-memory clusters).
- [[Thread]] — the canonical execution unit.
- [[SharedMemoryArchitecture]] — the hardware substrate.
- [[SharedMemoryIPC]] — the cross-process analog.
- [[CacheCoherency]] — the hardware property that makes shared-memory parallelism *correct* across cores.
- [[MulticoreProcessor]] — the modern target.
- [[OpenMP]] / [[Pthreads]] — the programming surfaces.
- [[ConcurrencyVsParallelism]] — the conceptual split shared-memory parallelism rests on.
- [[Speedup]] — the metric the 1/c rule predicts.
- [[dis-14-1-multicore]] — DIS source.
