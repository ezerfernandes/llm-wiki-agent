---
title: "NUMA (Non-Uniform Memory Access)"
type: concept
tags: [parallel-computing, hardware, architecture, shared-memory]
sources: [parproc-ch01-intro-parallel-processing, parproc-ch03-shared-memory-parallelism]
last_updated: 2026-05-17
---

# NUMA

Non-Uniform Memory Access — a [[SharedMemoryArchitecture]] generalization for larger systems in which each processor has a "closer" (faster) memory and "farther" (slower) memory; the address space is still unified but access latency varies depending on which physical module holds the address. *"Today almost all high-end MIMD systems are NUMAs."* ([[parproc-ch03-shared-memory-parallelism|Ch3]] §3.3.2).

## Structure

Each P/M/R triple — a processor `P`, its local memory module `M`, and a router `R` — forms a **processing element (PE)**. Each PE has its own local bus (P↔M↔R) and is also wired into a global bus through `R`. A local memory access (P3 reads from M3) is served by the local bus and is fast; a remote access (P3 reads from M8) goes P3 → R3 → global bus → R8 → M8, then the response retraces the path — slow.

*"It should be obvious now where NUMA gets its name. P8 will have much faster access to M8 than P3 will to M8, if none of the buses is currently in use—and if say the global bus is currently in use, P3 will have to wait a long time to get what it wants from M8."*

## Interconnect topologies

The global interconnect is not necessarily a bus. NUMA systems frequently use a [[Crossbar|crossbar]] or an [[OmegaNetwork|omega/delta]] multistage network (see [[parproc-ch03-shared-memory-parallelism|Ch3]] §3.3.3 and the scaling table).

## Programming for NUMA

Exploit the nonuniformity. *"In matrix problems, for example, we can write our program so that, for example, P8 usually works on those rows of the matrix which are stored in M8, P3 usually works on those rows of the matrix which are stored in M3, etc. In order to do this, we need to make use of the C language's `&` address operator, and have some knowledge of the memory hardware structure, i.e. the interleaving."* See [[MemoryInterleaving]].

[[ProcessorAffinity]] is the standard tool for keeping a thread next to its hot memory.

## Cache coherency on NUMA

Bus-style snoopy [[CacheCoherency|coherency]] doesn't scale to NUMA — broadcasting on a multipath network requires extra copies. NUMA systems use **directory-based** coherency protocols instead ([[parproc-ch03-shared-memory-parallelism|Ch3]] §3.5.1).

## Connections
- [[parproc-ch01-intro-parallel-processing]] — forward-references NUMA to chapter 3.
- [[parproc-ch03-shared-memory-parallelism]] — §3.3.2 delivers the substantive treatment; §3.3.3 surveys the interconnect topologies.
- [[SMP]] — NUMA is the asymmetric generalization.
- [[SharedMemoryArchitecture]] — NUMA is a subclass.
- [[Crossbar]] / [[OmegaNetwork]] — typical global-interconnect topologies.
- [[CacheCoherency]] — directory-based protocols (not snoopy) on NUMA.
- [[MemoryInterleaving]] — exploited by NUMA-aware code.
- [[ProcessorAffinity]] — keeps threads near their hot memory.
