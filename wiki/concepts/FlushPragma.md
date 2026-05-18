---
title: "OpenMP flush Pragma"
type: concept
tags: [openmp, parallel-computing, pragma, memory-consistency]
sources: [parproc-ch04-introduction-to-openmp, parproc-ch03-shared-memory-parallelism]
last_updated: 2026-05-17
---

# OpenMP flush Pragma

`#pragma omp flush(x)` ([[OpenMP]] §4.6.2) forces a memory flush of variable `x`: any pending writes are pushed out to memory so other threads can observe them, and any cached / register-resident value of `x` is reloaded.

```c
#pragma omp flush (x)
```

## Why it exists

OpenMP takes a **[[RelaxedConsistency|relaxed consistency]]** approach to shared memory — between synchronization points, a thread's write to `x` is allowed to live in a register or write buffer indefinitely, invisible to other threads. The chapter (§4.6.2) walks through the consequence: *"the cache will be unaware of the new value, which thus will not be visible to other threads."*

To make a write visible without a heavier sync construct, programmers can issue an explicit `flush`.

## Synchronization points that flush automatically

OpenMP forces flushes at every synchronization point:
- `barrier`
- entry / exit of `critical`
- entry / exit of `ordered`
- entry / exit of `parallel`
- exit of `parallel for`
- exit of `parallel sections`
- exit of `single`

So `flush` is only needed *between* such points — most well-structured OpenMP code never calls it.

## Architecture dependence

[[parproc-ch04-introduction-to-openmp]]: *"The flush operation is obviously architecture-dependent. OpenMP compilers will typically have the proper machine instructions available for some common architectures. For the rest, it can force a flush at the hardware level by doing lock/unlock operations, though this may be costly in terms of time."*

This connects directly to [[parproc-ch03-shared-memory-parallelism]] §3.6's [[MemoryConsistency|memory consistency models]] taxonomy — `flush` is the OpenMP-level lever over what SPARC's `MEMBAR` is at the hardware level.

## Connections
- [[OpenMP]] — parent.
- [[parproc-ch04-introduction-to-openmp]] — §4.6.2 source.
- [[parproc-ch03-shared-memory-parallelism]] — §3.6 memory-consistency substrate.
- [[RelaxedConsistency]] — OpenMP's named memory model.
- [[MemoryConsistency]] — hardware-level taxonomy.
- [[Barrier]] — implicit flushes at barriers cover most use cases.
- [[CriticalSection]] — entry/exit of `critical` also flushes.
- [[CacheCoherency]] — the substrate underneath `flush`.
