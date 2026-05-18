---
title: "SMP (Symmetric Multiprocessor)"
type: concept
tags: [parallel-computing, hardware, architecture, shared-memory]
sources: [parproc-ch01-intro-parallel-processing]
last_updated: 2026-05-17
---

# SMP

Symmetric Multiprocessor — a [[SharedMemoryArchitecture|shared-memory]] hardware topology in which several processors P and memory modules M are attached to a common bus. All processors see all memory modules symmetrically (no privileged path for any one processor to any one module).

[[parproc-ch01-intro-parallel-processing]] gives the canonical schematic ("P P P M M M attached to a `bus` line") and the operational rule: "to make sure only one processor uses the bus at a time, standard bus arbitration signals and/or arbitration devices are used."

Two notable extensions:
- **[[Multicore]] is "effectively the same as SMP, except that the processors are all on one chip, attached to the bus."** Modern CPUs are essentially SMPs in package form.
- **[[NUMA]] architectures** (Non-Uniform Memory Access) generalize SMP for larger systems by giving each processor a "closer" memory; cross-domain access is slower. The chapter forward-references this to chapter 3.

The book also discusses **[[CoherentCaches|coherent caches]]** as part of the SMP package — multiple processors caching the same memory line have to coordinate to avoid each seeing a stale copy.

Cost trajectory: "until recently, shared-memory systems cost hundreds of thousands of dollars and were affordable only by large companies, such as in the insurance and banking industries. The high-end machines are indeed still quite expensive, but now multicore machines, in which two or more CPUs share a common memory, are commonplace in the home and even in cell phones!"

## Connections
- [[parproc-ch01-intro-parallel-processing]] — introduces SMP topology with schematic.
- [[SharedMemoryArchitecture]] — the broader architectural category.
- [[Multicore]] — single-chip SMP.
- [[MIMD]] — SMP's execution model.
- [[NUMA]] — generalization for larger node counts; chapter 3 material.
- [[CoherentCaches]] — required for correct SMP semantics with caching.
