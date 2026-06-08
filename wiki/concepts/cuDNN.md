---
title: "cuDNN"
type: concept
tags: [gpu, nvidia, kernels, deep-learning]
sources: [mlsysbook-ch07-ml-frameworks]
last_updated: 2026-06-05
---

# cuDNN

**cuDNN** (CUDA Deep Neural Network library) is [[NVIDIA]]'s library of hand-tuned GPU [[Kernel|kernels]] for deep-learning primitives — convolutions, pooling, normalization, activations, and especially their backward passes. Frameworks ([[PyTorch]], [[TensorFlow]]) dispatch to cuDNN (alongside [[CUBLAS|cuBLAS]] for GEMM) rather than implementing these operations from scratch, exploiting memory-access patterns and hardware capabilities of modern accelerators. The framework's [[AutomaticDifferentiation|autodiff]] backward pass benefits from cuDNN's specialized backward kernels rather than a direct translation of the mathematical gradient definition.

## Connections

- [[mlsysbook-ch07-ml-frameworks]] — named as a GPU backend library frameworks rely on.
- [[CUBLAS]] — companion GEMM library; [[CUDA]] / [[NVIDIA]] — the platform.
- [[Kernel]] / [[KernelFusion]] — the hardware-execution layer.
- [[PyTorch]] / [[TensorFlow]] — frameworks that dispatch to it.
