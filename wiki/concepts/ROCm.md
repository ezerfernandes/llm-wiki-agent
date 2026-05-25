---
title: "ROCm (Radeon Open Compute)"
type: concept
tags: [gpu, kernel, compiler, amd, infrastructure, open-source]
sources: [ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

# ROCm — Radeon Open Compute

**AMD's open-source GPU programming stack** — the AMD-GPU counterpart to NVIDIA's proprietary [[CUDA]]. Per [[ai-engineering-ch09-inference-optimization|*AI Engineering* Ch 9]]:

> *"This has led many AI researchers and engineers to become interested in GPU programming languages such as CUDA (originally Compute Unified Device Architecture), OpenAI's Triton, and ROCm (Radeon Open Compute). The latter is AMD's open source alternative to NVIDIA's proprietary CUDA."*

## Why ROCm matters

AMD GPUs (e.g. MI300 series) are the **primary CUDA alternative** for large-scale AI workloads. ROCm provides:
- HIP (Heterogeneous Interface for Portability) — CUDA-source-compatible API.
- Tooling, profilers, and library reimplementations of CUDA equivalents.
- Open source — both spec and implementation, unlike CUDA.

## Limitations vs CUDA in 2024

- **Ecosystem gap** — PyTorch, JAX, TensorFlow have CUDA paths first; ROCm support is slower / spottier.
- **Kernel availability** — many production kernels (FlashAttention-3, vendor optimized libraries) target NVIDIA H100 first.
- **Mind-share** — most AI-engineering tutorials assume CUDA.

But this gap is narrowing — major frontier labs (notably Meta) ship inference on AMD MI-series hardware.

## Where ROCm appears in Ch 9

Ch 9 mentions ROCm only in passing — as one of three GPU programming languages alongside [[CUDA]] and [[Triton]]. The chapter's actual kernel-writing examples are CUDA-centric (e.g. [[FlashAttention]] for NVIDIA A100; FlashAttention-3 for H100).

## Connections

- [[CUDA]] — the dominant proprietary counterpart.
- [[Triton]] — OpenAI's Python-like alternative.
- [[AMD]] — the vendor behind ROCm.
- [[GPU]] / [[AIAccelerator]] — the broader hardware family.
- [[Kernel]] — what ROCm enables developers to write.
- [[InferenceOptimization]] — broader discipline.
- [[ai-engineering-ch09-inference-optimization]] — primary source.
