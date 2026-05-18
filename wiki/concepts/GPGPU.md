---
title: "GPGPU (General-Purpose GPU Computing)"
type: concept
tags: [computer-architecture, gpu, parallelism, accelerator, vector-processor]
sources: [dis-5-9-modern]
last_updated: 2026-05-17
---

# GPGPU (General-Purpose GPU Computing)

**GPGPU** — *general-purpose computing on graphics processing units* — is the use of GPUs as massively-parallel compute accelerators for workloads beyond rendering. [[dis-5-9-modern|Ch 5.9]] names GPU accelerators as **the modern home of the [[VectorProcessor|vector-processor]] [[InstructionLevelParallelism|ILP]] model** — the architectural lineage that started with the [[Cray1|Cray-1]] (1976) and ceded the general-purpose CPU market over the following decades has not disappeared, it has *migrated*: *"vector processors today primarily appear in GPU accelerators."*

## The architectural through-line (Ch 5.9 framing)

| Era | Where vector-style ILP lives |
|---|---|
| 1976+ | Standalone vector supercomputers ([[Cray1|Cray-1]] etc.) |
| 1990s–2000s | Pushed out of mainstream CPUs by [[Superscalar|superscalar]] designs |
| Today | **GPU accelerators (GPGPU)** |

A modern GPU's streaming multiprocessor is, at its core, a wide vector machine: many lanes executing the same instruction on different data — a generalization of the [[VectorProcessor|vector-processor]] model adapted for graphics-shader workloads and now reused for everything from physics simulation to neural-network inference.

## Scope note

Ch 5.9 introduces GPGPU only as the modern instantiation of the vector-processor lineage. The page does **not** cover CUDA, OpenCL, GPU memory hierarchies, warp/wavefront scheduling, or specific accelerator products. The wider wiki has [[GpuMemoryHierarchy]] and related pages that go deeper.

## Connections

- [[VectorProcessor]] — the architectural ancestor.
- [[Cray1]] — the founding example.
- [[InstructionLevelParallelism]] — the umbrella family.
- [[Superscalar]] — the rival ILP family GPUs do **not** primarily use.
- [[ParallelComputing]] — the broader programming paradigm GPGPU serves.
- [[GpuMemoryHierarchy]] — adjacent existing page on GPU memory architecture.
- [[dis-5-9-modern]] — primary source.
