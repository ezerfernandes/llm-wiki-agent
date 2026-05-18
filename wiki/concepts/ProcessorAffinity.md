---
title: "Processor Affinity"
type: concept
tags: [parallel-computing, performance, operating-system, cache, shared-memory]
sources: [parproc-ch03-shared-memory-parallelism]
last_updated: 2026-05-17
---

# Processor Affinity

The practice of binding (or hinting that the OS bind) a thread to a **preferred core**, so the thread tends to run on the same physical core across timeslices. The motivation is cache preservation. ([[parproc-ch03-shared-memory-parallelism|ParProcBook Ch3]] §3.10).

*"With a timesharing OS, a given thread may run on different cores during different timeslices. If so, the cache for a given core may need a lot of refreshing, each time a new thread runs on that core. To avoid this slowdown, one might designate a preferred core for each thread, in the hope of reusing cache contents."*

Setting affinity is OS- and chip-specific:

- **Linux**: `sched_setaffinity(2)`, `taskset(1)`.
- **OpenMP 3.1+**: `OMP_PROC_BIND` environment variable, `proc_bind(close|spread|master)` clause — *"OpenMP 3.1 has some facility for this."*

## Why it matters

Cache lines a thread loaded last timeslice are "free" memory accesses next timeslice — provided the thread runs on the same core. Migration forces a fresh load of the working set; cache misses, [[CacheCoherency|coherency]] traffic, and (on [[NUMA]]) remote-memory access penalties multiply.

## Caveats

- Pinning too aggressively defeats load balancing — if one core is busy with another process, your thread can't migrate to an idle core.
- On [[NUMA]], affinity should usually be paired with **memory affinity** (e.g. `numactl --membind`) so the thread's hot pages are on the local module.
- [[Multicore]] threads sharing an L2 (siblings on the same chip) benefit from being scheduled close together for shared-data workloads but far apart for memory-bandwidth-bound workloads — affinity tools usually expose both options.

## Connections
- [[parproc-ch03-shared-memory-parallelism]] — §3.10.
- [[Multicore]] — the architecture where affinity matters most.
- [[NUMA]] — affinity gains compound with memory-affinity.
- [[CacheCoherency]] — affinity reduces coherency-protocol traffic.
- [[FalseSharing]] — orthogonal cache-friendliness concern.
- [[OpenMP]] — `proc_bind` clause / `OMP_PROC_BIND`.
- [[LoadBalancing]] — affinity is a load-balancing knob (used cautiously).
