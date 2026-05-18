---
title: "MIMD (Multiple Instruction Multiple Data)"
type: concept
tags: [parallel-computing, hardware, architecture]
sources: [parproc-ch01-intro-parallel-processing]
last_updated: 2026-05-17
---

# MIMD

Multiple Instruction, Multiple Data — the standard execution model for [[SharedMemoryArchitecture|shared-memory]] multiprocessors and most non-GPU parallel machines.

From [[parproc-ch01-intro-parallel-processing]]: "this kind of architecture is sometimes called MIMD, standing for Multiple Instruction (different CPUs are working independently, and thus typically are executing different instructions at any given instant), Multiple Data (different CPUs are generally accessing different memory locations at any given time)."

Contrast with [[SIMD]]: SIMD processors execute the *same* instruction at every clock tick, just on different data; MIMD processors execute *independent* instruction streams. Almost all modern CPUs in shared-memory configurations ([[SMP]], [[Multicore]]) are MIMD; [[GPU|GPUs]] are SIMD in their execution lanes but "fundamentally shared-memory" in their storage.

## Connections
- [[parproc-ch01-intro-parallel-processing]] — introduces the MIMD/SIMD distinction.
- [[SharedMemoryArchitecture]] — typical MIMD context.
- [[SMP]] — canonical MIMD topology.
- [[Multicore]] — single-chip MIMD.
- [[SIMD]] — the contrasting execution model.
