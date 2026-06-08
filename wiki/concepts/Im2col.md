---
title: "im2col (Image to Column)"
type: concept
tags: [deep-learning, cnn, systems, hardware, mlsysbook]
sources: [mlsysbook-ch06-network-architectures]
last_updated: 2026-06-05
---

# im2col (Image to Column)

An implementation technique that **converts a [[Convolution|convolution]] into a single [[GEMM|general matrix multiply]]** by unfolding overlapping input patches into the columns of a matrix, with filter kernels arranged as rows. Rather than a learning algorithm, im2col is a *lowering* used by CNN frameworks and libraries such as Caffe and cuDNN. Documented in [[mlsysbook-ch06-network-architectures]] (Reddi, *Machine Learning Systems* Vol 1, Ch 6) as the bridge that turns sliding-window locality into the mature matrix-multiply path.

## Why it matters

- **Speed via mature BLAS.** Decades of optimization went into GEMM (cuBLAS, Intel oneMKL, OpenBLAS); im2col lets [[CNN|CNNs]] reuse those libraries instead of writing convolution kernels from scratch per target, yielding **5–10× speedups** on CPUs and enabling [[TensorCore|Tensor Core]] utilization.
- **The memory tradeoff.** im2col *duplicates* data where windows overlap: in a fully materialized stride-1 $K{\times}K$ transform, interior elements can appear in up to $K^2$ columns (9× for 3×3 filters). Borders, stride, padding, and tiling reduce the realized expansion.
- **Data center vs mobile.** GPUs with abundant [[HBM]] favor GEMM-oriented lowering for throughput; memory-constrained mobile frameworks (TFLite, NNAPI) prefer *direct convolution* to avoid the duplication, which is also more energy-efficient for large kernels.

## Connections

- [[mlsysbook-ch06-network-architectures]] — presents im2col as the convolution→GEMM lowering and its memory-for-throughput tradeoff.
- [[Convolution]] / [[CNN]] — the operation being lowered.
- [[GEMM]] — the target dense primitive.
- [[SystolicArray]] — the alternative hardware path (direct dataflow reuse) used by TPUs.
- [[TensorCore]] / [[HBM]] — hardware that makes GEMM-oriented lowering attractive in the data center.
