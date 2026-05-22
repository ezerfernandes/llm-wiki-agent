---
title: "Dive into Systems — Ch 14.6 Thread Safety"
type: source
tags: [dive-into-systems, textbook, parallel-programming, thread-safety, reentrancy, pthreads]
date: 2026-05-18
source_file: https://diveintosystems.org/book/C14-SharedMemory/thread_safety.html
---

## Summary

**Sixth leaf** of Ch 14 *Leveraging Shared Memory in the Multicore Era* of *[[DiveIntoSystems]]* — turns the *library function* dimension that prior Ch 14 sections sidestepped into a first-class hazard. Codifies **[[ThreadSafety|thread safety]]** as a per-function property: a function is thread-safe iff multiple threads can call it concurrently without producing incorrect results or unintended side effects. **Not all C library functions are thread-safe** — the Open Group maintains an explicit catalog of unsafe ones, and the programmer's burden is to consult it. The chapter draws the **[[ThreadSafety|thread-safe]] vs [[Reentrant|reentrant]] distinction** — *"all thread safe code is re-entrant; however, not all re-entrant code is thread safe"* — and uses **[[Strtok|`strtok()`]]** vs **[[StrtokR|`strtok_r()`]]** as the canonical worked example: `strtok` keeps **hidden internal state** between calls, so concurrent callers stomp on each other and produce nondeterministic tokenization; `strtok_r` makes the state an **explicit `char **saveptr` parameter** the caller owns per thread, restoring safety.

## Key Claims

- **[[ThreadSafety|Thread safety]] is a per-function property**: *"a thread-safe function guarantees that it can be executed by multiple threads simultaneously without producing unintended side effects or incorrect results."* The C standard library is **not uniformly thread-safe**.
- **The Open Group maintains the unsafe list**: programmers must consult the official thread-unsafety catalog before using a libc function in parallel code. The chapter explicitly directs readers to it.
- **[[Reentrant|Re-entrancy]] and thread safety are distinct**: *"all thread safe code is re-entrant; however, not all re-entrant code is thread safe."* A reentrant function can be safely paused mid-execution and re-invoked (typical example: interrupt-handler-callable); thread safety additionally requires correct concurrent execution from independent threads. Reentrancy is necessary but not sufficient.
- **[[Strtok|`strtok()`]] is the canonical thread-unsafe example**: maintains hidden static state pointing into the previous call's string. The worked `countElemsStr` example demonstrates that multiple threads parsing different strings concurrently produce inconsistent results — one thread's `strtok` advance corrupts another's parsing position.
- **[[StrtokR|`strtok_r()`]] is the thread-safe replacement**: the `_r` suffix (POSIX convention for **reentrant**) signals an explicit `char **saveptr` parameter the caller threads through subsequent calls. Each thread owns its own `saveptr` on its private stack, so the hidden-state hazard disappears.
- **Synchronization is one cure; redesigning to remove shared state is the other**: a thread-unsafe function can be made safe externally by wrapping calls in a [[Mutex|mutex]] (correctness at the cost of serialization), or internally by re-architecting to take all state as parameters (the `_r` pattern). The `_r` pattern is strictly better when available — no contention.

## Key Quotes

> "all thread safe code is re-entrant; however, not all re-entrant code is thread safe"

> "verify that the C library functions used are indeed thread safe"

## Connections

- [[DiveIntoSystems]] — parent textbook; **sixth leaf** of Ch 14.
- [[dis-14-5-cache-coherence]] — immediate predecessor; both 14.5 and 14.6 are *hardware-and-library hazards* sections that complement Ch 14.3's synchronization correctness.
- [[ThreadSafety]] — central concept this section introduces.
- [[Reentrant]] — sibling concept; the chapter's most subtle definitional distinction.
- [[Strtok]] / [[StrtokR]] — the canonical worked example pair.
- [[Pthreads]] — the threading library whose users must care.
- [[Mutex]] / [[Synchronization]] — one cure for thread-unsafe library functions.
- [[CriticalSection]] / [[DataRace]] — what hidden-state libc functions create when called concurrently.
- [[Errno]] — the canonical *per-thread* libc variable (the chapter notes glibc makes `errno` thread-local via TLS to preserve safety).
- [[dis-14-3-synchronization]] — provides the synchronization-based cure (wrap unsafe calls in a mutex).
- [[POSIX]] — defines the `_r`-suffix reentrant-variant convention.

## Contradictions

- None. Net-new content — introduces [[ThreadSafety]] / [[Reentrant]] / [[Strtok]] / [[StrtokR]] as wiki pages for the first time.

## Notes

- **137th ingested DIS chapter.** Mints **4 new concept pages**: [[ThreadSafety]], [[Reentrant]], [[Strtok]], [[StrtokR]].
