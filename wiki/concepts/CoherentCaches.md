---
title: "Coherent Caches"
type: concept
tags: [parallel-computing, hardware, cache, shared-memory]
sources: [parproc-ch01-intro-parallel-processing, parproc-ch03-shared-memory-parallelism]
last_updated: 2026-05-17
---

# Coherent Caches

In a [[SharedMemoryArchitecture]] system where multiple processors cache the same memory locations, **cache coherence** protocols ensure that all processors see a consistent value: when one processor writes a memory line, other processors' cached copies must be invalidated or updated.

[[parproc-ch01-intro-parallel-processing]] mentions coherent caches as part of the [[SMP]] memory-issues discussion: "there may also be coherent caches, which we will discuss later." Full treatment arrives in [[parproc-ch03-shared-memory-parallelism|Ch3]] §3.5, which lays out snoopy invalidate / update protocols, directory-based protocols for non-bus systems, the [[MESI]] state machine as the exemplar, [[FalseSharing]] as the cache-line-granularity pathology, and the consistency-vs-coherency distinction ([[MemoryConsistency]]).

## Connections
- [[parproc-ch01-intro-parallel-processing]] — flags coherent caches as a major performance consideration.
- [[parproc-ch03-shared-memory-parallelism]] — §3.5 delivers the full treatment.
- [[CacheCoherency]] — the protocol-layer concept page.
- [[MESI]] — Pentium's invalidate protocol.
- [[FalseSharing]] — pathology at cache-line granularity.
- [[MemoryConsistency]] — sibling layer.
- [[SMP]] / [[SharedMemoryArchitecture]] — the topology that necessitates coherence.
- [[Multicore]] — modern coherence implementation typically lives in the on-chip cache hierarchy.
