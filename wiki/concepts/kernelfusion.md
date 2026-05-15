---
title: "Kernel Fusion"
type: concept
tags: [gpu, systems, compiler]
sources: [2205.14135-flashattention]
last_updated: 2026-05-10
---

# Kernel Fusion

A GPU optimization that combines a chain of element-wise or otherwise small operations into a **single kernel launch**, so intermediate values stay in registers / on-chip SRAM and are never spilled to HBM. Eliminates the dominant cost of memory-bound op pipelines: redundant HBM reads/writes between successive small kernels.

## In Transformer attention

Standard PyTorch attention runs as separate kernels — matmul, mask, softmax, dropout, matmul — each loading from HBM and writing back to HBM. [[2205.14135-flashattention]] fuses all five into one CUDA kernel: inputs load from HBM once, intermediates live in SRAM, only the final output is written back. The fusion is enabled by the tiling reformulation of softmax — without that, the softmax dependency on the full row would block fusion.

Compilers (XLA, TorchInductor, Triton) can fuse many element-wise chains automatically. **Reduction operations (softmax, layer norm) and operations that need cross-block communication generally need hand-written fused kernels**, which is what FlashAttention provides.

## See also
- [[FlashAttention]]
- [[IOComplexity]]
- [[GpuMemoryHierarchy]]
