---
title: "Simultaneous Multithreading (SMT)"
type: concept
tags: [computer-architecture, cpu, parallelism, multithreading, smt, superscalar]
sources: [dis-5-9-modern]
last_updated: 2026-05-17
---

# Simultaneous Multithreading (SMT)

**Simultaneous multithreading (SMT)** is the [[HardwareMultithreading|hardware-multithreading]] variant that **issues instructions from multiple threads in the same clock cycle** — using the wide-issue capability of [[Superscalar|superscalar]] hardware to fill issue slots that a single thread alone could not. [[dis-5-9-modern|Ch 5.9]] introduces it as the second hardware-multithreading variant, sharply distinguished from interleaved multithreading.

## The mechanism

- The core has [[Superscalar|superscalar]] issue width *W* (multiple pipelines, ALUs, load/store units).
- Multiple architectural thread contexts (PC, register file, status) sit on the same core.
- Each cycle, the issue logic picks the best-ready *W* instructions from **whichever threads have them ready** — possibly drawing from several threads at once.
- Steady-state **IPC exceeds 1** because cross-thread ready instructions cover for any single thread's dependency bubbles.

## SMT vs interleaved multithreading

| Property | Interleaved | **SMT** |
|---|---|---|
| Threads issued per cycle | 1 (alternating) | **Many (up to issue width)** |
| Pipelines | Shared, time-sliced | Replicated / wide |
| Max IPC | 1 | **> 1** |
| Requires [[Superscalar]] | No | **Yes** |

Per Ch 5.9: **Intel's [[HyperThreading|Hyper-Threading]] implements interleaved multithreading — not true SMT.**

## Worked examples (Ch 5.9 chip tables)

- **IBM Power 9** (supercomputers): up to 24 cores × **8-way SMT** → per-chip IPC ceiling of **192**.
- **Oracle SPARC M7**: 32 cores × 8 threads/core → IPC 64.
- Mainstream desktop AMD Zen / Intel Core / Xeon: 2–8 cores × 2 threads/core.

## Connections

- [[HardwareMultithreading]] — the umbrella family.
- [[Superscalar]] — the hardware substrate SMT requires (you cannot co-issue without multi-issue hardware).
- [[HyperThreading]] — Intel's *interleaved* multithreading product (per Ch 5.9, **not** SMT).
- [[MulticoreProcessor]] — the orthogonal between-core parallelism axis.
- [[InstructionThroughput]] / [[CyclesPerInstruction]] — the metrics SMT pushes past 1.
- [[PowerWall]] — the constraint that made cross-thread ILP attractive.
- [[CPU]] — the device class.
- [[dis-5-9-modern]] — primary source.
