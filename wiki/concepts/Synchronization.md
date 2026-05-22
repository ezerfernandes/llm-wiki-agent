---
title: "Synchronization (threads)"
type: concept
tags: [concurrency, parallel-computing, synchronization, threads]
sources: [dis-14-3-synchronization]
last_updated: 2026-05-18
---

# Synchronization

**Enforcing a particular execution order among threads to ensure program correctness, even though it may increase runtime** ([[dis-14-3-synchronization|DIS Ch 14.3]]). The umbrella term for the family of primitives — [[Mutex|mutexes]], [[Semaphore|semaphores]], [[Barrier|barriers]], [[ConditionVariable|condition variables]], [[ReadersWriterLock|readers-writer locks]] — that coordinate access to shared mutable state on a [[SharedMemoryParallelism|shared-memory]] [[Thread|multi-threaded]] system.

## Why synchronization

[[dis-14-2-posix|DIS Ch 14.2]] ends with the warning *"You should never make any assumptions about the order in which threads will execute"*: without coordination, threads scheduled across [[MulticoreProcessor|multicore]] CPUs interleave their instructions arbitrarily, exposing **non-atomic** machine-instruction sequences (especially [[ReadModifyWrite|read-modify-write]] like `COUNTER += 1`) to interruption mid-stream. The default-unsafe principle: *"all operations should be assumed to be nonatomic unless mutual exclusion is explicitly enforced"*.

## The synchronization-primitive catalogue

| Primitive | API surface | When to reach for it |
|---|---|---|
| [[Mutex]] | `pthread_mutex_lock` / `unlock` | Single-resource mutual exclusion; thread that locks must unlock |
| [[Semaphore]] | `sem_wait` / `sem_post` | Resource-pool counting; any thread can post |
| [[Barrier]] | `pthread_barrier_wait` | Phase rendezvous — all threads reach point before any proceeds |
| [[ConditionVariable]] | `pthread_cond_wait` / `signal` / `broadcast` | Blocking-wait-until-predicate; eliminates polling |
| [[ReadersWriterLock]] | `pthread_rwlock_rdlock` / `wrlock` | Read-heavy shared state — many readers OR one writer |
| [[CriticalSection]] (Cortex-M) | `cortex_m::interrupt::free` | Embedded single-core; disable interrupts |
| [[Atomic|Atomic operations]] | hardware CAS / fetch-add | Multi-core lock-free single-word updates |

## The two failure modes synchronization addresses

- **[[DataRace|Data race]]**: two threads concurrently write the same location, one ordering produces wrong results. Synchronization serializes accesses.
- **[[RaceCondition|Race condition]]** (broader): any ordering-dependent incorrect outcome — includes check-then-act bugs that don't involve concurrent writes.

## The failure mode synchronization can *introduce*

- **[[Deadlock]]**: interdependent locks held in conflicting orders → all threads blocked forever.
- **Contention**: too-coarse synchronization serializes execution and erases the parallelism benefit; too-fine synchronization buries CPU in lock overhead. [[dis-14-3-1-mutex|DIS Ch 14.3.1]]'s lock-placement lesson — *thread-local accumulator + single final lock* — is the canonical lesson.

## Connections

- [[dis-14-3-synchronization]] — DIS Ch 14.3 hub; defines the term.
- [[CriticalSection]] / [[DataRace]] / [[RaceCondition]] / [[AtomicOperation]] — the vocabulary.
- [[Mutex]] / [[Semaphore]] / [[Barrier]] / [[ConditionVariable]] / [[ReadersWriterLock]] — the primitives.
- [[Pthreads]] — the canonical CPU-side API.
- [[Deadlock]] — synchronization's principal new failure mode.
- [[SharedMemoryParallelism]] — the substrate.
- [[Thread]] — the entity being synchronized.
- [[ReadModifyWrite]] — the danger pattern.
- [[parproc-ch01-intro-parallel-processing]] — Pacheco's introduction; first wiki source on synchronization vocabulary.
- [[rust-embedded-book-concurrency-index]] — the Rust-embedded specialization (single-core, interrupt-based, type-system-enforced).
