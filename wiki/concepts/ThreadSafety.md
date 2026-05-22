---
title: "Thread Safety"
type: concept
tags: [parallel-programming, concurrency, library-design]
sources: [dis-14-6-thread-safety]
last_updated: 2026-05-18
---

# Thread Safety

A **thread-safe** function is one that *"can be executed by multiple threads simultaneously without producing unintended side effects or incorrect results"* ([[dis-14-6-thread-safety|DIS Ch 14.6]]). It is a **per-function property**, not a per-program property — a thread-safe program is one that uses only thread-safe functions or wraps unsafe calls in explicit [[Synchronization|synchronization]].

## The Core Hazard

The C standard library is **not uniformly thread-safe**. Many libc functions maintain **hidden internal state** between calls (e.g., [[Strtok|`strtok()`]]'s saved-position pointer, `gmtime()`'s static buffer). When multiple threads call such a function concurrently, the hidden state is corrupted — each thread's call clobbers the others' bookkeeping, producing nondeterministic and wrong results. The bug is invisible at the call site: the function signature looks pure but the behavior is not.

## The Catalog

The Open Group maintains an explicit list of thread-unsafe POSIX functions. *"Verify that the C library functions used are indeed thread safe"* ([[dis-14-6-thread-safety|DIS Ch 14.6]]) is the chapter's programmer-discipline directive: consult the catalog *before* using a libc function in parallel code, not after debugging mysterious failures.

## Relationship to Reentrancy

*"All thread safe code is re-entrant; however, not all re-entrant code is thread safe"* ([[dis-14-6-thread-safety|DIS Ch 14.6]]). [[Reentrant|Re-entrancy]] is **necessary but not sufficient**: a reentrant function can be safely paused mid-execution and re-invoked (the typical hazard is signal handlers / interrupt handlers calling back into the same function), but multi-threaded concurrent execution adds the additional requirement that **no shared mutable state may be corrupted** by simultaneous calls. See [[Reentrant]] for the full distinction.

## Two Cures

1. **External cure — wrap in a [[Mutex|mutex]]**: serialize calls to the unsafe function with `pthread_mutex_lock` / `pthread_mutex_unlock`. Correctness restored at the cost of throughput.
2. **Internal cure — eliminate hidden state**: redesign the function to take all state as explicit parameters (the **`_r` suffix** [[POSIX]] convention — *reentrant* variant). [[StrtokR|`strtok_r()`]] is the canonical example: the previously-hidden saved-position pointer is now a `char **saveptr` parameter the caller owns per thread. No contention, no mutex needed.

## Canonical Example

[[Strtok|`strtok()`]] (unsafe) vs [[StrtokR|`strtok_r()`]] (safe) — see [[dis-14-6-thread-safety|DIS Ch 14.6]]'s `countElemsStr` worked example: concurrent `strtok` calls produce inconsistent tokenization counts; concurrent `strtok_r` calls each thread its own `saveptr` and produce correct independent results.

## Special-Case Thread-Local State

`errno` is the canonical case where **shared-looking** state is implemented thread-locally: glibc places `errno` in [[ThreadLocalStorage|thread-local storage (TLS)]] so each thread has its own copy. Code that reads `errno` after a libc call is implicitly thread-safe because no thread can clobber another's `errno`.

## Connections

- [[Reentrant]] — the strictly weaker sibling property.
- [[Strtok]] / [[StrtokR]] — the canonical pre/post pair.
- [[Mutex]] / [[Synchronization]] / [[CriticalSection]] — the external cure.
- [[DataRace]] / [[RaceCondition]] — what concurrent unsafe calls produce.
- [[Pthreads]] / [[POSIX]] — the threading API and the `_r` suffix convention.
- [[dis-14-6-thread-safety]] — DIS introduction.
- [[ThreadLocalStorage]] — the TLS mechanism `errno` uses to fake safety.
