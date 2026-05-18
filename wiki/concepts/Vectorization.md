---
title: "Vectorization (SIMD)"
type: concept
tags: [hardware, cpu, gpu, performance]
sources: [d2l-computational-performance]
last_updated: 2026-05-16
---

# Vectorization (SIMD)

Performing the same arithmetic operation on multiple data elements in a single clock cycle. The **SIMD** (Single Instruction Multiple Data) paradigm that makes modern CPUs and GPUs throughput-competitive for dense linear algebra ([[d2l-computational-performance]] §`hardware`).

## On CPUs

Names vary by ISA:

- **ARM NEON** — 128-bit registers (8× 16-bit ints, 4× 32-bit floats, etc.).
- **x86 AVX2** — 256-bit registers (8× FP32 or 4× FP64).
- **x86 AVX-512** — 512-bit registers (16× FP32 or 8× FP64). Up to 64 INT8 ops per cycle.
- **Fused multiply-add (FMA)** — `a*b + c` in one instruction; doubles throughput.

> *"Deep learning is extremely compute-hungry. Hence, to make CPUs suitable for machine learning, one needs to perform many operations in one clock cycle. This is achieved via vector units."* — [[d2l-computational-performance]]

Intel OpenVINO and oneDNN exploit AVX-512 for respectable server-CPU DL inference.

## On GPUs

A consumer NVIDIA GPU like the RTX 2080 Ti has 4,352 CUDA cores, each performing one FMA per cycle — the entire GPU is a giant SIMD engine. Even at modest 1.5 GHz this delivers tens of TFLOPs at FP32, hundreds at FP16 ([[TensorCore|tensor-cores]]).

> *"This number is entirely dwarfed by what GPUs are capable of achieving. For instance, NVIDIA's RTX 2080 Ti has 4,352 CUDA cores, each of which is capable of processing such an operation at any time."* — [[d2l-computational-performance]]

## When vectorization fails

- Memory-bound code — kernel waits for [[gpumemoryhierarchy|HBM]] bandwidth, vector units idle.
- Branch divergence — different lanes need different code paths.
- Misaligned data — partial loads kill throughput; 64-bit boundary alignment is the cheap fix.

## See also
- [[TensorCore]] — matrix-level extension of SIMD on NVIDIA GPUs.
- [[gpumemoryhierarchy]] — the memory side of the throughput equation.
- [[GPU]] — the consumer of massive vectorization.
- [[d2l-computational-performance]] §`hardware`.
