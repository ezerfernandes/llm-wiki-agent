---
title: "TorchInductor"
type: concept
tags: [frameworks, pytorch, compilation, codegen]
sources: [mlsysbook-ch07-ml-frameworks]
last_updated: 2026-06-05
---

# TorchInductor

**TorchInductor** is the default code-generation backend of PyTorch 2.0's [[TorchCompile|torch.compile]]. It compiles [[FXGraph|FX graphs]] (captured by [[TorchDynamo]]) into optimized machine code: for CUDA GPUs it generates [[Triton]] kernels (which compile to [[PTX]]); for CPUs it generates C++ with vectorization (AVX2, AVX-512). It applies three key optimizations: **[[KernelFusion|kernel fusion]]** (combining operations to reduce memory traffic), **memory layout optimization**, and **autotuning** (benchmarking implementation variants to pick the fastest).

Using Triton is a deliberate trade-off: it prioritizes fast JIT compilation over peak hardware performance, making on-the-fly optimization practical even though resulting kernels are ~5–20% slower than hand-written CUDA. Generated code is cached on disk (TorchInductor's own cache plus Triton kernels in `~/.triton/cache/`), so subsequent same-shape runs skip compilation.

## Connections

- [[mlsysbook-ch07-ml-frameworks]] — the codegen stage of the torch.compile pipeline.
- [[TorchCompile]] / [[TorchDynamo]] / [[FXGraph]] — upstream stages.
- [[Triton]] / [[PTX]] / [[CUDA]] — the GPU codegen targets.
- [[KernelFusion]] — its primary optimization; [[PyTorch]] — the framework.
