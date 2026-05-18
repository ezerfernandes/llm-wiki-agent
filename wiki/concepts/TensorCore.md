---
title: "Tensor Core"
type: concept
tags: [hardware, gpu, nvidia, deep-learning]
sources: [d2l-computational-performance]
last_updated: 2026-05-16
---

# Tensor Core

Specialized matrix-multiply-accumulate units inside modern NVIDIA GPUs (Volta and later). A tensor core performs a small (typically $4{\times}4$ to $16{\times}16$) matrix-multiply-add **in a single clock**, dramatically accelerating the GEMMs that dominate deep-learning workloads ([[d2l-computational-performance]] §`hardware`).

## Why specialized

> *"What if we added operations that optimized not just operations between vectors but also between matrices? This strategy led to tensor cores."* — [[d2l-computational-performance]]

Standard CUDA cores compute one FP scalar op per cycle. A vector unit (SIMD) does e.g. 16 ops per cycle. A tensor core does a $4{\times}4{\times}4$ FMA (= 64 FMAs = 128 FLOPs) per cycle — orders of magnitude denser.

## Numerical formats per generation

| Architecture | Card | Year | Tensor-core formats |
|---|---|---|---|
| Volta | V100 | 2017 | FP16 |
| Turing | T4, RTX 20-series | 2018 | FP16, INT8, INT4 |
| Ampere | A100 | 2020 | FP16, BF16, TF32, INT8/4, FP64 |
| Hopper | H100 | 2022 | FP8 (E4M3 / E5M2) + above (Transformer Engine) |
| Blackwell | B200 | 2024 | FP4 + above |

## Trade-offs ([[d2l-computational-performance]])

- **Training accelerators** (V100, A100, H100) need FP16/BF16 + FP32 mixed precision and lots of HBM — tensor cores at training-friendly precision.
- **Inference accelerators** (T4, L4) lean on INT8 / FP8 with much smaller memory.
- *"NVIDIA's Turing T4 GPUs are optimized for inference whereas the V100 GPUs are preferable for training."*

Going from 8-bit to 16-bit data types **increases silicon by ~4×** (multiplier circuit area scales quadratically) — which is why NVIDIA exposed INT4 on Turing and FP4 on Blackwell: trade precision for throughput.

## See also
- [[GPU]] / [[NVIDIA]] / [[CUDA]] — the substrate.
- [[Vectorization]] — the SIMD predecessor of matrix units.
- [[HBM]] — feeds the tensor cores.
- [[d2l-computational-performance]] §`hardware`.
