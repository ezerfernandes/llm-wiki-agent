---
title: "Reentrant"
type: concept
tags: [parallel-programming, concurrency, library-design, signal-safety]
sources: [dis-14-6-thread-safety]
last_updated: 2026-05-18
---

# Reentrant

A **reentrant** function is one that can be safely **paused mid-execution** and **re-invoked** before the first invocation completes, without corrupting state. The classical hazard is a **signal handler** or **interrupt handler** that calls back into a function the interrupted thread was already executing — if the function relies on hidden static state, the second invocation will clobber it.

## Reentrancy vs Thread Safety

*"All thread safe code is re-entrant; however, not all re-entrant code is thread safe"* ([[dis-14-6-thread-safety|DIS Ch 14.6]]).

| Property | Hazard model | Sufficient condition |
|---|---|---|
| **Reentrant** | Same thread re-enters mid-call (signal handler, interrupt) | No shared mutable state across invocations within one thread |
| **[[ThreadSafety|Thread-safe]]** | Multiple threads call concurrently | Reentrant + safe under truly simultaneous execution |

Reentrancy is the **strictly weaker** property. A function can be reentrant but not thread-safe if it uses mechanisms that prevent re-entry within a single thread (e.g., a global counter) but cannot prevent two threads from racing on the same global from different cores.

## The `_r` Suffix Convention

[[POSIX]] established the **`_r` suffix** (for *reentrant*) as the naming convention for reentrant variants of historically non-reentrant libc functions:

- [[Strtok|`strtok`]] → [[StrtokR|`strtok_r`]] — explicit `saveptr` parameter replaces hidden static.
- `localtime` → `localtime_r` — caller-supplied `struct tm *` buffer replaces shared static.
- `rand` → `rand_r` — caller-supplied `unsigned int *seed` replaces hidden state.
- `gmtime` → `gmtime_r`, `asctime` → `asctime_r`, etc.

In practice these `_r` variants are also **thread-safe** because they remove the hidden shared state entirely — the distinction between reentrancy and thread safety collapses for the *no-shared-state* design.

## Signal-Handler Safety

POSIX defines a separate **async-signal-safe** category for functions safely callable from signal handlers (the minimal set includes `write`, `_exit`, `signal`, `kill` — but **not** `printf`, `malloc`, `free`, or most stdio). Async-signal-safety is even stricter than reentrancy: the function must work correctly even when interrupting `malloc` mid-allocation.

## Connections

- [[ThreadSafety]] — strictly stronger sibling property.
- [[Strtok]] / [[StrtokR]] — canonical reentrant-variant example.
- [[SignalHandler]] — the historical motivation for the reentrancy concept.
- [[Signal]] — the interrupt mechanism that drove reentrancy discipline.
- [[POSIX]] — defines the `_r` suffix convention.
- [[dis-14-6-thread-safety]] — DIS introduction.
- [[dis-13-4-1-signals]] — signals chapter (the parent context for reentrancy in the OS arc).
