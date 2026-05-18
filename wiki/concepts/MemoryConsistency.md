---
title: "Memory Consistency Model"
type: concept
tags: [parallel-computing, hardware, memory, shared-memory, consistency]
sources: [parproc-ch03-shared-memory-parallelism]
last_updated: 2026-05-17
---

# Memory Consistency

The **timing contract** of a shared-memory system: *after one processor changes the value of a shared variable, when will that value become visible to the other processors?* ([[parproc-ch03-shared-memory-parallelism|ParProcBook Ch3]] §3.6).

Consistency is **not** the same as [[CacheCoherency|coherency]]:
- *Coherency* = many caches see one value of one address consistently with each other.
- *Consistency* = a write made now becomes visible at other processors *when?*

The two can co-exist with the coherency operations *postponed* until the consistency model says they fire.

## Why there's a question at all

Two sources of delay between "the CPU executes the store" and "the value reaches memory":

1. **Write buffers**: most multiprocessor CPUs queue writes and ship them in batches to amortize bus-acquisition cost. *"Reads following a write may proceed, without waiting for the write to get to memory, except for reads to the same address."*
2. **Register caching**: a compiler may keep a variable `x` in a register and only flush to memory eventually. Without a flush, other processors never see the update.

## Consistency models (weakest → strongest)

- **Sequential Consistency** (the strongest, slowest): memory operations executed in some order by one processor are observed in that same order by all other processors. *"Enforcement of this requirement makes a system slow, and it has been replaced on most systems by weaker models."*
- **Release Consistency**: processors' instruction sets include **ACQUIRE** and **RELEASE** instructions. RELEASE = "I'm done writing, flush my buffers." ACQUIRE = "tell me what they've written; wait for all pending RELEASEs."
- **Scope Consistency**: a relaxed release variant tied to *specific* lock variables — writes within a critical section guarded by lock L become visible to the *next* CPU that acquires L. This is the model [[JIAJIA]] uses. Barriers also force pending writes to complete.

Trade-off: *"weaker consistency models make for faster machines but require the programmer to do more work."*

## Hardware instructions

- SPARC's **`MEMBAR`** — pending writes flush to memory (with STORE operand); incoming writes are made visible to this processor (with LOAD operand).
- x86's **`MFENCE` / `LFENCE` / `SFENCE`** family.
- Programmer-induced consistency events (`MEMBAR`-style intrinsics) trigger the postponed [[MESI]] / [[CacheCoherency|cache-coherency]] operations.

## Pentium aside (with a caveat)

The chapter writes *"The recent Pentium models use Sequential Consistency, with any write done by a processor being immediately sent to its cache as well."* The modern documented model for x86 is **x86-TSO**, a relaxation that permits store-buffer reordering of younger loads past older stores to different addresses — strictly weaker than sequential consistency. Not a wiki-internal contradiction (no current page asserts otherwise) but worth noting.

## Connections
- [[parproc-ch03-shared-memory-parallelism]] — §3.6.
- [[CacheCoherency]] — orthogonal layer; coherency operations gated by this layer.
- [[MESI]] — the gated protocol.
- [[FalseSharing]] — pathology that's *partially* mitigated by relaxed consistency (writes can batch).
- [[SoftwareDSM]] / [[JIAJIA]] — page-based SDSMs implement scope consistency at the page level.
- [[SharedMemoryArchitecture]] — substrate.
