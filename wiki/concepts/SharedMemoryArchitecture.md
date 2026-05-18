---
title: "Shared-Memory Architecture"
type: concept
tags: [parallel-computing, hardware, architecture]
sources: [parproc-ch01-intro-parallel-processing]
last_updated: 2026-05-17
---

# Shared-Memory Architecture

Parallel hardware paradigm in which many CPUs share a single physical memory address space. [[parproc-ch01-intro-parallel-processing]] introduces it as the first of three dominant architectures (the others being [[MessagePassingArchitecture]] and [[SIMD]]).

The canonical topology is the [[SMP|Symmetric Multiprocessor]]: processors P and memory modules M attached to a shared bus, with bus-arbitration signals ensuring only one processor uses the bus at a time. **[[Multicore]] is "effectively the same as SMP except that the processors are all on one chip, attached to the bus."** Larger systems may use [[NUMA]] designs (forward-referenced to chapter 3).

The book's footnote on terminology: "the term *processor* will generally include cores, e.g. a dual-core chip will be considered to have two processors" (footnote 1, p. 3).

Memory addressing two ways (in an N-module system):
- **High-order interleaving** — consecutive addresses live in the same module; address bits split with the high-order bits selecting the module. Example with four modules over addresses 0–1023: M0 holds 0–255, M1 holds 256–511, etc.
- **Low-order interleaving** — consecutive addresses live in consecutive modules; the low-order bits select the module. Better for spreading contention because parallel sequential accesses hit different modules.

The chapter's stock real-world example: "the Registrar's Office at [[UCDavis|UC Davis]] uses shared-memory multiprocessors for processing its on-line registration work … the database field has contributed greatly to the commercial success of large shared-memory machines."

Programming model implications (developed throughout Chapter 1):
- All threads/processors see a single address space — `Y[3] = 12;` on one node is visible to subsequent reads from `Y[3]` on any other node.
- Race conditions exist; locks ([[CriticalSection]] / [[Mutex]]) are required for invariants spanning multiple operations.
- [[CoherentCaches|Coherent caches]] (forward-referenced) and bus contention are the central performance considerations.

## Connections
- [[parproc-ch01-intro-parallel-processing]] — introduces all three architectures including this one.
- [[SMP]] — the canonical shared-memory topology.
- [[Multicore]] — single-chip SMP.
- [[MIMD]] — most shared-memory systems are MIMD.
- [[CriticalSection]] — the central concurrency hazard.
- [[Pthreads]] / [[OpenMP]] / [[Rdsm]] — software interfaces for shared-memory parallelism.
- [[MessagePassingArchitecture]] — the contrasting paradigm.
- [[SIMD]] — the third paradigm (lockstep execution).
- [[NUMA]] — non-uniform memory access; forward-referenced as chapter 3 material.
