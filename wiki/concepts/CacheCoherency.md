---
title: "Cache Coherency"
type: concept
tags: [parallel-computing, hardware, cache, shared-memory]
sources: [parproc-ch03-shared-memory-parallelism, dis-11-6-cache-coherency]
last_updated: 2026-05-17
---

# Cache Coherency

Hardware protocol layer ensuring that, when multiple CPUs cache the same memory line, the value seen at each cache stays *consistent* — *"inconsistency between caches"* is the **cache coherency problem**. ([[parproc-ch03-shared-memory-parallelism|ParProcBook Ch3]] §3.5.1; [[dis-11-6-cache-coherency|DIS Ch 11.6]] states it as *"the value of a copy of a block of memory stored in one core's L1 cache is different than the value of a copy of the same block stored in another core's L1 cache"*).

## Multicore topology ([[dis-11-6-cache-coherency|DIS Ch 11.6]])

[[DiveIntoSystems|DIS]]'s pedagogical framing: each core owns a **private L1** (split I/D), with **L2/L3 shared** across cores. Coherency exists because per-core L1 beats a shared L1 — the added protocol complexity is the price for *"each core executes independent instruction streams"* with high local hit rates.

DIS introduces the simpler **MSI** (Modified / Shared / Invalid) variant — three states per cache line — as the pedagogical baseline; the [[MESI]] protocol used in production adds the **Exclusive** state to avoid broadcasts on first-write to an uncontested line.

Caches exist in [[SharedMemoryArchitecture|shared-memory]] systems because spinning on a [[TestAndSet|TAS]] lock variable without caches *"would be unthinkable"* — every spin generates bus traffic. But once each processor caches lock variables (and everything else), the question becomes: *when one processor writes L, how do the other caches find out?*

## Bus-based: snoopy protocols

On a bus, all caches *"snoop on"* — monitor — the bus, watching for transactions made by other caches. Two flavors:

- **Invalidate protocol**: when a CPU writes a cached variable, it first broadcasts an invalidation; other caches mark their copies invalid. Those caches re-fetch only when their own processor next accesses the line.
- **Update protocol**: the writing CPU broadcasts the new value, and all other caches immediately update their cached copies.

*"This relation between these two is somewhat analogous to the relation between **write-back** and **write-through** protocols for caches in uniprocessor systems."*

**Tradeoff**: invalidate wins when many writes happen before the next remote read (no wasted broadcasts). Update wins when the data is hot at many CPUs (no cache misses on the read). The chapter's worked counterexamples — a cacheable vector that's written sequentially, vs `Sum += X[I]` in a loop — show neither dominates. *"CPU designers must try to anticipate which protocol will work well across a broad mix of applications."* Some real protocols **dynamically switch modes** at runtime.

## Non-bus: directory-based protocols

For crossbar / omega networks, broadcasting to every cache is expensive (one copy per network path). Directory-based protocols maintain a **directory at memory** listing the *home* of each block and which caches currently have valid copies; invalidates/updates go only to those. A cache joining or leaving the "club" updates the directory.

## MESI (the example protocol)

Pentium's snoopy invalidate protocol; the chapter dedicates §3.5.2 to it. See [[MESI]] for the four-state machine.

## Coherency ≠ consistency

The chapter is careful to distinguish *coherency* (multi-cache, same address — "are the caches in agreement?") from *consistency* (single variable — "when does a new value become visible?"). [[MemoryConsistency]] addresses the latter; the two protocols compose, with cache coherency operations *postponed* until consistency-prescribed events (e.g. a write-buffer flush triggered by a `MEMBAR` or RELEASE) fire.

## Connections
- [[parproc-ch03-shared-memory-parallelism]] — §3.5.1.
- [[dis-11-6-cache-coherency]] — [[DiveIntoSystems|DIS]] Ch 11.6 introduction (MSI + snooping/directory framing).
- [[CoherentCaches]] — the same idea, framed as a Ch1 stub.
- [[MESI]] — the protocol exemplar.
- [[FalseSharing]] — the line-granularity pathology cache coherency introduces.
- [[MemoryConsistency]] — the sibling layer.
- [[TestAndSet]] — the synchronization primitive whose spin-traffic motivated caches in the first place.
- [[SharedMemoryArchitecture]] — substrate.
- [[Multicore]] — modern coherency implementations live in the on-chip cache hierarchy.
