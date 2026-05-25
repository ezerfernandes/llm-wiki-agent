---
title: "XDNA2"
type: concept
tags: [hardware, npu, amd, ai-accelerator]
sources: [2507.19457-gepa]
last_updated: 2026-05-22
---

# XDNA2

**AMD's second-generation NPU architecture** (Advanced Micro Devices, 2025). The on-chip AI accelerator integrated into AMD Ryzen AI processors for AI PCs. Successor to XDNA (the first-gen AMD NPU shipped in Ryzen 7040 series).

The architecture is a tiled array of **AIE-ML** (AI Engine for Machine Learning) compute tiles, each with a vector processing unit, scalar unit, and local memory; tiles communicate via on-chip interconnect. Programming targets vector kernels (compiled C++ subset) and uses a tile-graph scheduler.

Used as the target architecture for the [[NPUEval]] benchmark which [[2507.19457-gepa|GEPA]] exercises as an [[InferenceTimeSearch|inference-time search]] task. Manual ML-kernel porting to XDNA2 is expensive due to limited tooling and documentation maturity vs. mature CUDA on NVIDIA — automated kernel discovery from compiler-error feedback (the GEPA approach) is a partial closure of that gap.

## Connections
- [[2507.19457-gepa]] — uses XDNA2 (via [[NPUEval]]) as inference-time-search target.
- [[NPUEval]] — the benchmark.
- [[NPU]] — the hardware class.
- [[GPU]] — the contrast point; CUDA NVIDIA is the mature alternative, XDNA2 the emerging one.
- [[AMD]] — the manufacturer.
