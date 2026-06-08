---
title: "Kernel Fusion"
type: concept
tags: [gpu, systems, compiler]
sources: [2205.14135-flashattention, mlsysbook-ch07-ml-frameworks, mlsysbook-ch11-hardware-acceleration]
last_updated: 2026-06-05
---

# Kernel Fusion

A GPU optimization that combines a chain of element-wise or otherwise small operations into a **single kernel launch**, so intermediate values stay in registers / on-chip SRAM and are never spilled to HBM. Eliminates the dominant cost of memory-bound op pipelines: redundant HBM reads/writes between successive small kernels.

## In Transformer attention

Standard PyTorch attention runs as separate kernels — matmul, mask, softmax, dropout, matmul — each loading from HBM and writing back to HBM. [[2205.14135-flashattention]] fuses all five into one CUDA kernel: inputs load from HBM once, intermediates live in SRAM, only the final output is written back. The fusion is enabled by the tiling reformulation of softmax — without that, the softmax dependency on the full row would block fusion.

Compilers (XLA, TorchInductor, Triton) can fuse many element-wise chains automatically. **Reduction operations (softmax, layer norm) and operations that need cross-block communication generally need hand-written fused kernels**, which is what FlashAttention provides.

## Why it is *the* memory-wall optimization ([[mlsysbook-ch07-ml-frameworks|mlsysbook Vol 1 Ch 7]])

Ch 7 positions fusion as the key lever for memory-bound ops: most individual op *types* (activations, normalizations, element-wise) are memory-bound, achieving <1% of peak compute on an A100. Fusing LayerNorm+Dropout+ReLU into one kernel yields ~5× speedup; matmul+bias+ReLU fusion gives 2–3× (registers/L1 deliver 10–100× HBM bandwidth). Crucially, **a framework can only fuse operations it can see together** — which is why [[StaticGraph|static graphs]] and [[JITCompilation|JIT]] capture (vs [[EagerExecution|eager]]) determine whether fusion is even possible. [[FlashAttention]] is fusion taken to its extreme, shifting attention from memory-bound to compute-bound.

## See also
- [[mlsysbook-ch07-ml-frameworks]] — fusion as the answer to the memory wall; visibility prerequisite.
- [[FlashAttention]]
- [[OperatorFusion]] / [[MemoryWall]] / [[RooflineModel]]
- [[IOComplexity]]
- [[GpuMemoryHierarchy]]
- [[mlsysbook-ch11-hardware-acceleration]] — Ch 11 quantifies fusion: combining ReLU+BatchNorm+scale on a 1024² FP32 tensor cuts the footprint 4× (16.8 MB → 4.2 MB); fused LayerNorm+GELU can hit 10× on very-low-AI ops. It is the prescribed lever for memory-bound [[RooflineModel|roofline]] regimes, paired with [[Tiling|tiling]], and bounded by register pressure.
