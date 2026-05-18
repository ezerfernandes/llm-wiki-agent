---
title: "False Sharing"
type: concept
tags: [parallel-computing, performance, cache, shared-memory]
sources: [parproc-ch03-shared-memory-parallelism]
last_updated: 2026-05-17
---

# False Sharing

A performance pathology of [[CacheCoherency|cache-coherent]] [[SharedMemoryArchitecture|shared-memory]] systems: two **unrelated** variables sit on the same cache line, so a write to one *appears* (to the coherency protocol) to invalidate the other at remote caches even though no read-write dependency actually exists. ([[parproc-ch03-shared-memory-parallelism|ParProcBook Ch3]] §3.5.3).

## Canonical example

```c
int W, Z;
```

Most compilers lay these out adjacently; both end up on the same cache line. Under an [[MESI|invalidate]] protocol, a write to `Z` invalidates other CPUs' copies of `W`. *"This is the **false sharing** problem, alluding to the fact that the two variables are sharing a cache line even though they are not related."*

Worse — under workloads that alternate writes to `W` and `Z` at different CPUs, the line ping-pongs invalidation messages between caches: *"this can lead to a 'ping-pong' effect, in which alternate writing to two variables leads to a cyclic pattern of coherency transactions."*

## Mitigation: padding

Force the variables onto separate cache lines:

```c
int W, U[1000], Z;
```

The compiler must actually honor the layout — verify with a `printf("%x %x\n", &W, &Z);` that the addresses are far enough apart given the line size (typically 64 bytes; the chapter uses 512-byte blocks as an upper bound for the hardware-cache case).

## Why this matters in software DSM, too

[[SoftwareDSM]] systems share at **page** granularity, not cache-line granularity — and pages are 4 KB vs the typical 64 B cache line, so the false-sharing surface is **~64×–8× larger** depending on the comparison. [[JIAJIA]]'s *multiple-writers* mechanism (each node's writes are diffed against a saved page twin at the next barrier) is specifically designed to mitigate page-level false sharing.

## Connections
- [[parproc-ch03-shared-memory-parallelism]] — §3.5.3.
- [[CacheCoherency]] — the protocol that turns line co-residence into pathological traffic.
- [[MESI]] — the example invalidate protocol.
- [[ProcessorAffinity]] — orthogonal cache-friendliness tool.
- [[JIAJIA]] — multi-writer SDSM, motivated in part by page-level false sharing.
- [[SoftwareDSM]] — false sharing scales up to page granularity here.
