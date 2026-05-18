---
title: "Relaxed Consistency (OpenMP memory model)"
type: concept
tags: [openmp, parallel-computing, memory-consistency]
sources: [parproc-ch04-introduction-to-openmp, parproc-ch03-shared-memory-parallelism]
last_updated: 2026-05-17
---

# Relaxed Consistency

The [[OpenMP]] memory model. Memory updates are **not guaranteed visible to other threads between synchronization points** — between such points, the runtime may keep values in registers or write buffers indefinitely. This is the named position in [[MemoryConsistency|memory-consistency taxonomy]] that OpenMP picks.

[[parproc-ch04-introduction-to-openmp]] §4.6.2: *"OpenMP takes a **relaxed consistency** approach, meaning that it forces updates to memory ('flushes') at all synchronization points."*

## Synchronization points that flush

- `#pragma omp barrier`
- entry / exit of `#pragma omp critical`
- entry / exit of `#pragma omp ordered`
- entry / exit of `#pragma omp parallel`
- exit of `#pragma omp parallel for`
- exit of `#pragma omp parallel sections`
- exit of `#pragma omp single`

So the natural rhythm of OpenMP code (parallel block opens, work-sharing happens with implicit barriers, parallel block closes) automatically flushes at every step.

## Explicit flush

Between synchronization points, `#pragma omp flush(x)` ([[FlushPragma]]) forces a write-out. Architecture-dependent; falls back to a lock/unlock cycle on platforms without a dedicated flush instruction.

## Why relaxed

Strict ([[MemoryConsistency|sequential]]) consistency would require every write to be globally visible immediately — impossible to implement efficiently on modern out-of-order CPUs with write buffers and registers. The relaxed model lets the compiler / hardware reorder freely between sync points, paying the visibility cost only when explicitly asked.

## Connections
- [[OpenMP]] — parent.
- [[parproc-ch04-introduction-to-openmp]] — §4.6.2 source.
- [[parproc-ch03-shared-memory-parallelism]] — §3.6 hardware-consistency taxonomy.
- [[MemoryConsistency]] — the broader hardware-level concept (sequential / release / scope).
- [[FlushPragma]] — the explicit lever.
- [[CacheCoherency]] — independent but interacting layer.
- [[Barrier]] / [[CriticalSection]] — sync points that auto-flush.
