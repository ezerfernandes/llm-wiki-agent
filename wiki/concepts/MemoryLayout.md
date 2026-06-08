---
title: "Memory Layout"
type: concept
tags: [frameworks, tensors, performance, hardware]
sources: [mlsysbook-ch07-ml-frameworks]
last_updated: 2026-06-05
---

# Memory Layout

**Memory layout** is how a multi-dimensional [[Tensor|tensor]] maps onto linear physical memory, encoded by [[Stride|stride]] patterns. The two canonical orderings are **row-major** (C-style, used by [[NumPy]] / [[PyTorch]] — consecutive row elements contiguous) and **column-major** (Fortran-style, used by some BLAS libraries). For a 2×3 tensor, row-major strides are `[3,1]`; element `[i,j]` lives at `base + i·stride[0] + j·stride[1]`.

Layout choices are performance choices. Optimal layouts reach **80–90%** of peak bandwidth (1.5–3.0 TB/s on A100/H100); suboptimal patterns achieve only **20–30%**. Choosing **NCHW** when the target accelerator prefers **NHWC** (or vice versa) can *halve* throughput by breaking hardware memory coalescing — the [[Kernel|kernel]] dispatch and the memory-abstraction layer transform layouts to match each backend (e.g. NCHW on NVIDIA GPUs, NHWC for Apple's Metal). Non-contiguous layouts (post-transpose) require explicit `.contiguous()` copies before some CUDA kernels can run.

## Connections

- [[mlsysbook-ch07-ml-frameworks]] — the abstraction problem; tensor data representation.
- [[Tensor]] / [[Stride]] — the abstraction and its index→address mapping.
- [[KernelFusion]] / [[GEMM]] — operations whose speed depends on layout.
- [[NumPy]] / [[PyTorch]] — row-major; [[MemoryWall]] — why bandwidth utilization matters.
