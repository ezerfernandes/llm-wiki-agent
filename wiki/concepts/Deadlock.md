---
title: "Deadlock"
type: concept
tags: [concurrency, embedded, failure-mode]
sources: [rust-embedded-book-concurrency-index]
last_updated: 2026-05-16
---

# Deadlock

Failure mode in which two or more execution threads are each waiting on a resource the other holds, and **no thread can make progress**. In single-threaded preemptive contexts (e.g. an interrupt handler blocking on a lock held by `main`), it manifests as the system **hanging permanently**.

## Why it matters in embedded

[[rust-embedded-book-concurrency-index]] flags deadlock as the **specific reason classical blocking [[Mutex|mutexes]] (`std::sync::Mutex`-style) are inappropriate for interrupt handlers**:

> *"Using a mutex with interrupt handlers can be tricky: it is not normally acceptable for the interrupt handler to block, and it would be especially disastrous for it to block waiting for the main thread to release a lock, since we would then **deadlock** (the main thread will never release the lock because execution stays in the interrupt handler)."*

The mechanism: `main` holds a lock, an [[Interrupt|interrupt]] fires, the interrupt handler tries to take the same lock, **blocks waiting**, but `main` can never resume (CPU is stuck inside the interrupt handler) — so the lock is never released.

## "Deadlock is safe (in the Rust sense)"

*"Deadlocking is not considered unsafe: it is possible even in safe Rust."* ([[rust-embedded-book-concurrency-index]]). I.e. the Rust language's `unsafe` boundary catches [[DataRace|data races]] (UB) but does **not** catch deadlocks (well-defined liveness failures).

## The embedded escape: critical-section-gated mutexes

The chapter's `cortex_m::interrupt::Mutex` sidesteps deadlock by design — the "lock" is a [[CriticalSection|critical section]] (interrupts disabled). The interrupt handler **cannot fire while `main` holds the lock**, so the deadlock scenario is impossible. *"So long as the critical section must last as long as the lock, we can be sure we have exclusive access to the wrapped variable without even needing to track the lock/unlock state of the mutex."*

## Higher-level alternatives that *prove no deadlock*

[[RTIC]] is named in the chapter as a deadlock-free framework: *"this has a number of advantages such as **guaranteeing no deadlocks** and giving extremely low time and memory overhead."* Achieved via compile-time static-priority + resource-tracking.

## Connections

- [[Mutex]] — the primitive whose blocking variant produces deadlocks; the critical-section-gated variant avoids them.
- [[CriticalSection]] — the mechanism that makes the embedded `Mutex` deadlock-free.
- [[Interrupt]] — the typical second "thread" in the deadlock pair.
- [[DataRace]] — sibling failure mode; UB rather than liveness failure.
- [[RTIC]] — named as deadlock-free by construction.
- [[RustLanguage]] — `unsafe` catches data races, not deadlocks.
