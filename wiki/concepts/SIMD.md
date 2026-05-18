---
title: "SIMD (Single Instruction Multiple Data)"
type: concept
tags: [parallel-computing, hardware, architecture, gpu, vectorization]
sources: [parproc-ch01-intro-parallel-processing]
last_updated: 2026-05-17
---

# SIMD

Single Instruction, Multiple Data — the third of the three parallel-hardware paradigms in [[parproc-ch01-intro-parallel-processing]] (alongside [[SharedMemoryArchitecture]] / [[MIMD]] systems and [[MessagePassingArchitecture]]).

"In contrast to MIMD systems, processors in SIMD … systems execute in lockstep. At any given time, all processors are executing the same machine instruction on different data."

Historical examples cited in the chapter: the ILLIAC, [[ThinkingMachines|Thinking Machines Corporation]]'s **CM-1** and **CM-2**. Digital-signal-processing (DSP) chips "tend to have a SIMD architecture."

Modern prominent example: **[[GPU|GPUs]]**. "Today the most prominent example of SIMD is that of GPUs — graphics processing units. In addition to powering your PC's video cards, GPUs can now be used for general-purpose computation. The architecture is fundamentally shared-memory, but the individual processors do execute in lockstep, SIMD-fashion." This single sentence is Matloff's anchor for the GPU sections of his book — the GPGPU programming model treats SIMD lanes as the basic execution primitive while still relying on a shared-memory substrate.

## Connections
- [[parproc-ch01-intro-parallel-processing]] — introduces SIMD as the third architecture.
- [[GPU]] — modern dominant SIMD platform; "fundamentally shared-memory" + "lockstep SIMD-fashion."
- [[CUDA]] — programming layer for [[NVIDIA]] GPUs; bridges SIMD execution to shared-memory programming.
- [[MIMD]] — the contrasting execution model (different instructions on different data).
- [[ThinkingMachines]] — historical SIMD vendor (CM-1, CM-2).
- [[SharedMemoryArchitecture]] — GPUs are SIMD-executing but shared-memory in storage layout.
- [[MessagePassingArchitecture]] — the third paradigm.
