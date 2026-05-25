---
title: "Shared-State Concurrency"
type: concept
tags: [programming-languages, concurrency, shared-memory, mutex]
sources: [vanroy-programming-paradigms-for-dummies]
last_updated: 2026-05-22
---

# Shared-State Concurrency

The concurrency paradigm of mainstream languages: **threads access shared data items using special control structures (e.g., monitors) to manage concurrent access**. *"This paradigm is by far the most popular. It used by almost all mainstream languages, such as Java and C#."* — [[vanroy-programming-paradigms-for-dummies|Van Roy 2009]].

## Mechanism

- **Threads** share a common address space (same heap, same global variables, same mutable structures).
- **Synchronization primitives** ([[Mutex|mutexes]], [[Semaphore|semaphores]], monitors, [[ConditionVariable|condition variables]], [[Barrier|barriers]], [[Atomic|atomic]] operations) coordinate access to shared mutable state.
- **Transactions** ([[SoftwareTransactionalMemory|software transactional memory]] — STM) are an alternative coordination model: threads atomically update shared data items.

## Van Roy's critique

> *"Despite their popularity, monitors are the most difficult concurrency primitive to program with [29]. Transactions and message passing are easier, but still difficult. All three approaches suffer from their expressiveness: they can express nondeterministic programs (whose execution is not completely determined by their specifications), which is why it is hard to reason about their correctness."*

Van Roy cites Doug Lea's *Concurrent Programming in Java: Design Principles and Patterns* (1999) as the canonical reference for the difficulty of shared-state-monitor programming.

## Why it dominates mainstream languages anyway

- **Hardware model** — shared-memory multi-core processors are the dominant architecture; mapping threads to cores via shared memory is hardware-direct.
- **Path dependence** — Java / C# / C++ shaped the curriculum; most programmers learn concurrency through threads + locks.
- **Library support** — every mainstream language ships a synchronization-primitives library; alternative paradigms ([[DeclarativeConcurrency|declarative concurrency]], [[MessagePassingConcurrency|message passing]], [[FunctionalReactiveProgramming|FRP]], [[DiscreteSynchronousProgramming|synchronous]]) require either non-mainstream languages or limited library substitutes.

## Position in Van Roy's taxonomy

| Property | Value |
|---|---|
| [[ObservableNondeterminism|Observable nondeterminism]] | Yes |
| [[NamedState|Named state]] | Yes (named + nondeterministic + concurrent — most expressive corner) |
| [[RaceCondition|Race conditions possible]] | Yes |
| Default recommended for concurrent programming? | **No** ([[MessagePassingConcurrency|message passing]] preferred) |

## In this wiki

The wiki's anchor for the **mainstream-language concurrency tradition** the wiki's existing [[DiveIntoSystems]] Ch 14 ([[Pthreads]] / [[Mutex]] / [[Semaphore]] / [[ConditionVariable]] / [[Barrier]]) and [[TheEmbeddedRustBook]] Concurrency chapter ([[Send]] / [[Sync]] / [[CriticalSection]] / [[Atomic]] / [[Mutex]] / [[CellRust]] / [[RefCell]]) corpora target. Van Roy's chapter is the paradigm-level critique those corpora do not engage with: shared-state concurrency is the **default**, not the **best** — for many programs [[DeclarativeConcurrency]] or [[MessagePassingConcurrency]] would be more correct and equally fast.
