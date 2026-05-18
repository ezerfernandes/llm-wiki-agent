---
title: "Fetch-and-Add (F&A)"
type: concept
tags: [parallel-computing, synchronization, hardware, shared-memory]
sources: [parproc-ch03-shared-memory-parallelism]
last_updated: 2026-05-17
---

# Fetch-and-Add (F&A)

Atomic read-modify-write primitive that adds a value to a memory location and returns the *pre*-increment value, in a single round trip. *"There would be hardware adders placed at each memory module. That means that the whole operation could be done in one round trip to memory."* ([[parproc-ch03-shared-memory-parallelism|ParProcBook Ch3]] §3.4.3).

C-level call:

```c
FETCH_AND_ADD(X, 1);
```

compiles to:

```
F&A X, R, 1
```

R receives the old value of X, X is incremented by 1, all atomically at the memory module. *"this is all done in an atomic manner."*

## Why it matters

Without F&A, the naïve

```
LOCK(K);
Y = ++X;
UNLOCK(K);
```

requires **two** round-trips for the `X++` (load X into a CPU register, increment, write back) **plus** round-trips for the LOCK and UNLOCK. F&A collapses all of this into one. *"This could be a huge time savings, especially for long-latency interconnects."*

## Packet combining in multistage networks (§3.7)

Generalizes nicely in [[OmegaNetwork|omega]]-style multistage interconnects. F&A is encoded as a packet type (e.g. a 2-bit transaction field). When two F&A packets to the same address `X` meet at the same network switch at the same time, the switch can **coalesce them into a single F&A with summed delta**: two `F&A(X, 1)` packets become one `F&A(X, 2)`. *"this is a delicate operation, and we must make sure that different CPUs get different return values, etc."*

## Connections
- [[parproc-ch03-shared-memory-parallelism]] — §3.4.3 + §3.7 packet combining.
- [[TestAndSet]] — sibling synchronization primitive, oriented around lock variables rather than counters.
- [[OmegaNetwork]] — where packet combining lives.
- [[SharedMemoryArchitecture]] — substrate.
- [[Latency]] — what F&A optimizes (one round-trip vs many).
