---
title: "AI Accelerator"
type: concept
tags: [hardware, gpu, tpu, inference, training]
sources: [ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

# AI Accelerator

**A chip designed to accelerate a specific type of AI computational workload** — typically dense matrix multiplication (which accounts for **> 90% of all floating-point operations in a neural network** per Ivanov et al. arXiv 2021). Per [[ai-engineering-ch09-inference-optimization|*AI Engineering* Ch 9]]:

> *"An accelerator is a chip designed to accelerate a specific type of computational workload. An AI accelerator is designed for AI workloads. The dominant type of AI accelerator is GPUs, and the biggest economic driver during the AI boom in the early 2020s is undoubtedly NVIDIA."*

## CPU vs GPU (the foundational contrast)

| Aspect | CPU | GPU |
|---|---|---|
| Core count | ~64 (high-end consumer) | thousands |
| Per-core power | High (single-thread perf) | Lower |
| Workload | OS, I/O, sequential | Parallel: matmul, graphics |
| Memory tech | DDR SDRAM (2D) | HBM (3D-stacked) |
| Memory bandwidth | 25–50 GB/s | 256 GB/s – 1.5+ TB/s |

Matrix multiplication is "highly parallelizable" — which is why GPUs dominate.

## The AI-accelerator zoo (Ch 9's list)

- **[[NVIDIA]] GPUs** — economic dominant; CUDA is the *de facto* substrate.
- **[[AMD]] GPUs** — primary GPU competitor; uses [[ROCm]].
- **[[GoogleTPU|Google TPU]]** — Tensor Processing Unit (TPU v3 / v4 / v5).
- **Intel Habana Gaudi** — Intel's AI training/inference chip family.
- **[[Graphcore]] IPU** — Intelligent Processing Unit.
- **[[Groq]] LPU** — Language Processing Unit.
- **[[Cerebras]] Wafer-Scale QPU** — Quant Processing Unit.

### Inference-specialized accelerators

> *"While many chips can handle both training and inference, one big theme emerging is specialized chips for inference."*

- **[[AppleNeuralEngine|Apple Neural Engine]]** — on-device inference (iPhone, Mac).
- **AWS [[Inferentia]]** — AWS inference accelerator.
- **[[MTIA]]** — Meta Training and Inference Accelerator.

### Edge-inference chips

- **Google Edge TPU**.
- **NVIDIA Jetson Xavier**.

### Architecture-specialized

Some chips target a specific architecture (e.g. transformer-specialized chips). The reverse is also true: **the transformer was originally designed by Google to run fast on TPUs** and only later optimized on GPUs (Ch 9 footnote).

## Compute primitives

A chip mixes compute units optimized for different data shapes (Figure 9-6 in Ch 9):

- **Scalar units** — single number at a time.
- **Vector units** — 1D arrays (SIMD).
- **Tensor units** — 2D/3D matrix and tensor operations. NVIDIA Volta added [[TensorCore|Tensor Cores]]; TPUs use tensor ops as primary primitive.

## Three big numbers when evaluating an accelerator

> *"FLOP/s, memory size, and memory bandwidth are the three big numbers that help you answer the first two questions [Can the hardware run your workloads? How long does it take?]."*

Plus power consumption (TDP or max power draw) for cost-of-ownership.

## Why inference is now > 90% of ML cost

Desislavov et al. (2023) found inference can exceed training cost in deployed systems, accounting for **up to 90% of ML costs**. Inference workloads differ from training:
- Lower precision is tolerable.
- Memory capacity matters less than bandwidth.
- Latency-bounded (vs throughput-bounded for training).

This justifies dedicated inference accelerators.

## Connections

- [[GPU]] — the dominant subclass.
- [[GoogleTPU]] / [[AMD]] / [[Graphcore]] / [[Groq]] / [[Cerebras]] / [[Inferentia]] / [[MTIA]] / [[AppleNeuralEngine]] — specific instances.
- [[CUDA]] / [[ROCm]] / [[Triton]] — programming languages.
- [[TensorCore]] — modern GPU compute primitive.
- [[HBM]] / [[SRAM]] — memory hierarchy.
- [[MatrixMultiplication]] — the >90% workload accelerators are tuned for.
- [[InferenceOptimization]] — broader discipline.
- [[ai-engineering-ch09-inference-optimization]] — primary source.
