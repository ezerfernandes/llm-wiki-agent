---
title: "MESI Cache Coherency Protocol"
type: concept
tags: [parallel-computing, hardware, cache, shared-memory, protocol]
sources: [parproc-ch03-shared-memory-parallelism]
last_updated: 2026-05-17
---

# MESI

A widely-used invalidate-style [[CacheCoherency|cache-coherency]] protocol for snoopy-bus systems; *"for example the protocol used in the Pentium series."* ([[parproc-ch03-shared-memory-parallelism|ParProcBook Ch3]] §3.5.2).

The four-letter name is the alphabet of states a *(cache, memory-block)* pair can occupy:

| state | meaning |
|---|---|
| **M** odified | written to more than once; no other copy valid |
| **E** xclusive | valid; no other cache copy valid; memory copy valid |
| **S** hared | valid; at least one other cache copy valid |
| **I** nvalid | block not in cache, or present but incorrect |

Each memory block has a **separate state at each cache**. For instance, block 88 may be S at P5's and P12's caches but I at P1's.

## Transition tables

In addition to the familiar `read hit / read miss / write hit / write miss` events, MESI distinguishes **read snoop** and **write snoop**: an event our cache observes on the bus when *another* CPU's read or write misses and that CPU's cache requests the block. If we have a valid copy, we must supply it.

**Reads:**

| present | event | new |
|---|---|---|
| M | read hit | M |
| E | read hit | E |
| S | read hit | S |
| I | read miss; no other valid cache copy | E |
| I | read miss; ≥1 other valid cache copy | S |

**Writes:**

| present | event | new |
|---|---|---|
| M | write hit; no invalidate bus signal; no memory update | M |
| E | same as M above | M |
| S | write hit; put invalidate signal on bus; update memory | E |
| I | write miss; update memory but do nothing else | I |

**Snoops:**

| present | event | new |
|---|---|---|
| M | read snoop; write line back to memory, picked up by other CPU | S |
| M | write snoop; write line back, signal other CPU OK to write | I |
| E | read snoop; put shared signal on bus; no memory action | S |
| E | write snoop; no memory action | I |
| S | read snoop | S |
| S | write snoop | I |
| I | any snoop | I |

## Notable transitions

- A **write miss does NOT bring the block in from memory** — *"Note that a write miss does NOT result in the associated block being brought in from memory."* The block stays I locally; the write goes to memory.
- A **write hit on Shared** transitions both: the writing cache to E (since it now has the only valid copy), other caches to I (via the invalidate broadcast).
- **Worked example**: block in state M at A, state I at B. B issues a write. B broadcasts intent; A intercepts, writes its own M copy back to memory, then signals B to proceed; A's state becomes I; B's stays I (write miss); memory is updated. Net: every cache state is I, memory holds B's new value.

## What MESI does not address

MESI is a **coherency** protocol (multiple caches, one address). It says nothing about the **timing** at which a write reaches the cache from a CPU's write buffer — that's the job of the [[MemoryConsistency|consistency model]]. Cache coherency operations are *postponed* until the consistency model says they fire.

## Connections
- [[parproc-ch03-shared-memory-parallelism]] — §3.5.2.
- [[CacheCoherency]] — the parent concept.
- [[FalseSharing]] — what MESI invalidations cause when unrelated variables sit on one cache line.
- [[MemoryConsistency]] — the orthogonal model that gates *when* MESI transitions actually execute.
- [[SharedMemoryArchitecture]] — substrate.
