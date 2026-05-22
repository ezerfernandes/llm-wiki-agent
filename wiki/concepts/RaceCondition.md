---
title: "Race Condition"
type: concept
tags: [concurrency, synchronization, failure-mode]
sources: [dis-14-3-synchronization]
last_updated: 2026-05-18
---

# Race Condition

**Any situation where simultaneous execution of operations yields incorrect outcomes** ([[dis-14-3-synchronization|DIS Ch 14.3]]). The broader sibling of [[DataRace|data race]] — every data race is a race condition, but race conditions also include ordering bugs that don't involve concurrent writes (e.g., check-then-act sequences on shared state, time-of-check-to-time-of-use, signal-ordering bugs).

## Race condition vs data race

[[dis-14-3-synchronization|DIS Ch 14.3]] distinguishes:

| Term | Definition |
|---|---|
| **[[DataRace|Data race]]** | Two or more threads simultaneously write to the same memory location, producing incorrect results. |
| **Race condition** | Any situation where simultaneous execution of operations yields incorrect outcomes. |

Data races are the most common race-condition class but not the only one. A check-then-act pattern (`if (!exists(file)) create(file)`) can produce wrong results even with each access individually serialized — the *interleaving between* atomic accesses is the race.

## Why race conditions are hard

[[dis-14-3-synchronization|DIS Ch 14.3]]'s headline observation: *"Not all concurrent execution sequences cause errors — races occur only under specific timing conditions, making them difficult to detect and reproduce."* The Heisenbug property — adding `printf` or running under a debugger can change scheduling enough to hide the bug.

## The default-unsafe principle

*"All operations should be assumed to be nonatomic unless mutual exclusion is explicitly enforced"* ([[dis-14-3-synchronization|DIS Ch 14.3]]). The inversion of trust the entire [[Synchronization|synchronization]] arc rests on: do not assume any machine instruction sequence is uninterruptible; reach for the appropriate primitive ([[Mutex|mutex]], [[Semaphore|semaphore]], [[Atomic|atomic]], [[CriticalSection|critical section]]) explicitly.

## The canonical example — `COUNTER += 1`

The [[ReadModifyWrite|read-modify-write]] pattern is three machine instructions (load → add → store). Two threads interleaving load/load/add/add/store/store on the same counter produce `+1` instead of `+2`. The same example appears across [[dis-14-3-synchronization|DIS]] / [[parproc-ch01-intro-parallel-processing|Pacheco]] / [[rust-embedded-book-concurrency-index|Embedded Rust]] as the textbook race.

## Connections

- [[dis-14-3-synchronization]] — DIS Ch 14.3 source.
- [[DataRace]] — strict sub-case; the concurrent-write specialization.
- [[Synchronization]] — the family of primitives that prevents race conditions.
- [[CriticalSection]] — the atomicity unit.
- [[AtomicOperation]] — the indivisibility property race conditions exploit the absence of.
- [[ReadModifyWrite]] — the canonical danger pattern.
- [[Mutex]] / [[Semaphore]] / [[Atomic]] — the fixes.
- [[Heisenbug]] — the observation that races are timing-dependent and hard to reproduce.
- [[parproc-ch01-intro-parallel-processing]] — Pacheco's prime-sieve race.
- [[rust-embedded-book-concurrency-index]] — `main`-vs-interrupt race; Rust's type system criminalizes data races at compile time, but not all race conditions.
