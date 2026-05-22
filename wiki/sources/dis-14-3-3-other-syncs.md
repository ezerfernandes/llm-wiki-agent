---
title: "Dive into Systems — Ch 14.3.3 Other Synchronization Constructs"
type: source
tags: [book, textbook, dive-into-systems, pthreads, barrier, condition-variable, readers-writer-lock, synchronization, concurrency]
date: 2026-05-18
source_file: https://diveintosystems.org/book/C14-SharedMemory/other_syncs.html
---

## Summary

Chapter 14.3.3 of *[[DiveIntoSystems]]* — **third and final sub-leaf** of [[dis-14-3-synchronization|Ch 14.3 *Synchronizing Threads*]]. Surveys the synchronization primitives that the [[Mutex|mutex]] ([[dis-14-3-1-mutex|14.3.1]]) and [[Semaphore|semaphore]] ([[dis-14-3-2-semaphores|14.3.2]]) sub-leaves leave on the table: **[[Barrier|barriers]]**, **[[ConditionVariable|condition variables]]**, and (by reference) [[ReadersWriterLock|readers-writer locks]]. **Barriers** — *"forces all threads to reach a common execution point before proceeding concurrently"* — three-function [[Pthreads]] API: [[PthreadBarrierInit|`pthread_barrier_init(&barr, NULL, N)`]] (where `N` is the thread count required to release the barrier), [[PthreadBarrierWait|`pthread_barrier_wait(&barr)`]] (the rendezvous primitive — first `N-1` callers block, the `N`-th releases all), [[PthreadBarrierDestroy|`pthread_barrier_destroy(&barr)`]]. Worked example: a barrier prevents array processing until every thread prints its startup message — the canonical *phase-separator* use case. **Condition variables** — *"blocks threads until specific conditions are satisfied, eliminating wasteful CPU polling"* — the **blocking-wait + signaling** primitive that pairs with a mutex to implement event-driven coordination. Five-function API: [[PthreadCondInit|`pthread_cond_init`]] / [[PthreadCondWait|`pthread_cond_wait(&cond, &mutex)`]] (*"causes the calling thread to block on the condition variable `cond` until another thread signals it"* — atomically releases the mutex while blocking, re-acquires before returning) / [[PthreadCondSignal|`pthread_cond_signal`]] (wake one waiter) / [[PthreadCondBroadcast|`pthread_cond_broadcast`]] (wake all waiters) / [[PthreadCondDestroy|`pthread_cond_destroy`]]. **Egg-laying worked example**: farmers (consumers) wait for chickens (producers) to lay eggs — farmers block on the condition variable until signaled, then atomically collect eggs. **Critical pattern — spurious-wakeup defense**: *"the content emphasizes using a predicate loop (while, not if) around `pthread_cond_wait()` to handle spurious wakeups and condition changes"* — the canonical `while (!predicate) pthread_cond_wait(&cond, &mutex);` idiom that defends against (a) spurious wakeups (the OS may wake the waiter without a corresponding signal), and (b) condition changes between signal and waiter resumption (another consumer racing in). **132nd ingested DIS chapter — closes the Ch 14.3 *Synchronizing Threads* arc.** Mints **9 new concept pages** ([[ConditionVariable]], [[PthreadBarrierInit]], [[PthreadBarrierWait]], [[PthreadBarrierDestroy]], [[PthreadCondInit]], [[PthreadCondWait]], [[PthreadCondSignal]], [[PthreadCondBroadcast]], [[PthreadCondDestroy]]) and **extends [[Barrier]] in place** with DIS's Pthreads barrier API.

## Key Claims

- **[[Barrier|Barrier]] = rendezvous primitive.** *"Forces all threads to reach a common execution point before proceeding concurrently."* The phase-separator: useful when phase *k+1* requires phase *k*'s outputs from every thread.
- **Pthreads barrier API (3 functions)**:
  - [[PthreadBarrierInit|`pthread_barrier_init(&barr, attr, count)`]]: `count` = number of threads required to trip the barrier.
  - [[PthreadBarrierWait|`pthread_barrier_wait(&barr)`]]: rendezvous point; first `count - 1` callers block, last caller releases all.
  - [[PthreadBarrierDestroy|`pthread_barrier_destroy(&barr)`]]: teardown.
- **[[ConditionVariable|Condition variable]] = blocking-wait-until-signaled primitive.** *"Blocks threads until specific conditions are satisfied, eliminating wasteful CPU polling."* Pairs with a mutex — the condition variable holds the wait queue; the mutex protects the predicate state.
- **Pthreads condition variable API (5 functions)**:
  - [[PthreadCondInit|`pthread_cond_init(&cond, attr)`]] / [[PthreadCondDestroy|`pthread_cond_destroy(&cond)`]]: lifecycle.
  - [[PthreadCondWait|`pthread_cond_wait(&cond, &mutex)`]]: atomically (a) release `mutex`, (b) block on `cond`. On wake: re-acquire `mutex` before returning. The mutex must be held on entry.
  - [[PthreadCondSignal|`pthread_cond_signal(&cond)`]]: wake one waiter (chosen by scheduler).
  - [[PthreadCondBroadcast|`pthread_cond_broadcast(&cond)`]]: wake all waiters.
- **Predicate-loop discipline**: *"use a predicate loop (while, not if) around `pthread_cond_wait()` to handle spurious wakeups and condition changes."* The textbook idiom:
  ```c
  pthread_mutex_lock(&mutex);
  while (!predicate) {
      pthread_cond_wait(&cond, &mutex);
  }
  /* use shared state */
  pthread_mutex_unlock(&mutex);
  ```
  Defends against (a) spurious wakeups, (b) condition-change races.
- **Producer/consumer**: condition variables are the textbook implementation of producer/consumer patterns — chickens (producers) call `pthread_cond_signal` after laying; farmers (consumers) call `pthread_cond_wait` while no eggs.
- **[[ReadersWriterLock|Readers-writer locks]]** (named in the parent chapter's catalogue but not detailed in 14.3.3 itself): allow many concurrent readers OR one exclusive writer — the asymmetric specialization of [[Mutex|mutex]] for read-heavy workloads. [[Pthreads]] surface: `pthread_rwlock_init` / `pthread_rwlock_rdlock` / `pthread_rwlock_wrlock` / `pthread_rwlock_unlock` / `pthread_rwlock_destroy`.

## Key Quotes

> *"Barriers force all threads to reach a common execution point before proceeding concurrently."*

> *"`pthread_cond_wait` causes the calling thread to block on the condition variable `cond` until another thread signals it."*

> *"The content emphasizes using a predicate loop (while, not if) around `pthread_cond_wait()` to handle spurious wakeups and condition changes."*

## Connections

- [[DiveIntoSystems]] — Ch 14.3.3.
- [[dis-14-3-synchronization]] — parent hub.
- [[dis-14-3-1-mutex]] / [[dis-14-3-2-semaphores]] — sibling sub-leaves; condition variables explicitly pair with a [[Mutex]].
- [[Barrier]] — extended in place with the Pthreads three-function barrier API; prior wiki coverage came from [[parproc-ch01-intro-parallel-processing]] + Ch 3.
- [[ConditionVariable]] — new concept; canonical anchor.
- [[ReadersWriterLock]] — new concept; surveyed at chapter level.
- [[PthreadBarrierInit]] / [[PthreadBarrierWait]] / [[PthreadBarrierDestroy]] — new concept pages.
- [[PthreadCondInit]] / [[PthreadCondWait]] / [[PthreadCondSignal]] / [[PthreadCondBroadcast]] / [[PthreadCondDestroy]] — new concept pages.
- [[Mutex]] — the mandatory partner for condition variables.
- [[Pthreads]] — the API surface.
- [[Synchronization]] — umbrella.
- [[ProducerConsumer]] — the dominant condition-variable pattern.
- [[parproc-ch01-intro-parallel-processing]] — Pacheco's parallel barrier coverage; condition variables surface there too.
- [[TreeBarrier]] / [[ButterflyBarrier]] — parallelized barrier implementations covered by Pacheco Ch 3 — DIS stops at the API, defers the implementation.

## Contradictions

None. Ch 14.3.3 strictly extends prior [[Barrier]] coverage with the Pthreads three-function API, and introduces [[ConditionVariable]] / [[ReadersWriterLock]] as first-class wiki concepts.
