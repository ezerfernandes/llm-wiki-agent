---
title: "Systolic Array"
type: concept
tags: [hardware, accelerators, systems, tpu, mlsysbook]
sources: [mlsysbook-ch06-network-architectures, mlsysbook-ch11-hardware-acceleration]
last_updated: 2026-06-05
---

# Systolic Array

A grid of processing elements through which data flows in lockstep "pulses" (named for the heart's rhythmic contraction), directly implementing the **data reuse** required by [[GEMM|matrix multiplication]] and sliding-window [[Convolution|convolution]]. Each input value is passed between neighboring processors and reused across many multiply-accumulates *without repeated off-chip memory access*. Described in [[mlsysbook-ch06-network-architectures]] (Reddi, *Machine Learning Systems* Vol 1, Ch 6) as the core data-reuse primitive behind the [[GoogleTPU|TPU]].

## Why it matters

- **It avoids the dominant energy cost.** A single off-chip DRAM access can cost over **100×** the energy of a floating-point multiply-accumulate (~4.6 pJ at 45 nm vs hundreds of pJ for a 32-bit DRAM fetch, Horowitz 2014). By keeping operands moving between adjacent PEs, the systolic array avoids a DRAM round-trip per multiplication.
- **TPU embodiment.** Google's TPU maps GEMM onto a large systolic array executing thousands of MACs per clock, sacrificing general-purpose flexibility (caches, complex control) for domain-specific efficiency: TPU v1 delivered ~92 TOPS (INT8) at 40 W vs an NVIDIA K80's ~8.7 TFLOP/s (FP32) at 300 W — about 80× higher peak ops/W (with an INT8-vs-FP32 caveat).
- **The design principle:** dedicating silicon to a dominant primitive can outperform general-purpose flexibility.

## Connections

- [[mlsysbook-ch06-network-architectures]] — introduces systolic arrays as the sliding-window/GEMM data-reuse hardware primitive.
- [[GoogleTPU]] — the canonical systolic-array accelerator.
- [[GEMM]] / [[Convolution]] — the operations the array accelerates.
- [[Im2col]] — the alternative software lowering (convolution→GEMM) versus direct dataflow reuse.
- [[TensorCore]] / [[GPU]] / [[HBM]] — adjacent accelerator hardware motivated by the same primitives.
- [[ArithmeticIntensity]] — high-intensity workloads (weight reuse) are exactly what systolic arrays exploit.
- [[mlsysbook-ch11-hardware-acceleration]] — the deepest treatment: Kung & Leiserson 1979 origin, the cardiac *systole* etymology, the ~107× energy advantage of pulsing data (2 loads amortized across 128 ops vs 4 DRAM accesses/MAC), the [[Tiling|tiling principle]] (4096-wide layer → 1,024 tiles, 128× reuse) and "fringe tax," and the [[WeightStationary|weight-]]/[[OutputStationary|output-]]/row-stationary dataflow choice that hard-codes an accelerator's workload affinity.
