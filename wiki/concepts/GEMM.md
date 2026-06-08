---
title: "GEMM (General Matrix Multiply)"
type: concept
tags: [hardware, ml-systems, matrix-multiplication, compute, kernels]
sources: [mlsysbook-ch05-neural-computation, mlsysbook-ch07-ml-frameworks, mlsysbook-ch11-hardware-acceleration]
last_updated: 2026-06-05
---

# GEMM (General Matrix Multiply)

The hardware kernel that implements the matrix expression **xW** at the heart of every neural-network layer. Per [[mlsysbook-ch05-neural-computation|mlsysbook Vol 1 Ch 5]], GEMM is "the most optimized routine in all of computing" and accounts for **over 90% of the floating-point operations** in most neural networks.

## Why GEMM dominates

[[ForwardPropagation|Forward propagation]] is a chain of matrix multiplications interleaved with [[ActivationFunction|activations]]. GEMM has high [[ArithmeticIntensity|arithmetic intensity]] — for an N×N multiply it does ~2N³ FLOPs while moving only ~3N²s bytes, so intensity ≈ 2N/(3s) FLOP/byte and grows with N. This lets it saturate [[ComputeBound|compute-bound]] accelerators ([[GPU|GPUs]], [[TensorCore|Tensor Cores]], TPUs), unlike element-wise ops ([[ReLU]] ≈ 0.125 FLOP/byte for FP32) which leave them [[MemoryBound|memory-starved]]. This is *why* "fully connected" and "convolutional" layers are preferred over custom element-wise logic.

To hit peak performance, engineers use **blocking and tiling** so data fits into L1/L2 caches and is reused as long as possible (maximizing [[ArithmeticIntensity|data reuse]] against the [[MemoryWall|memory wall]]). Designing architectures around large dense matmuls that specialized accelerators execute at exaflop scale is the hardware–software co-design principle that makes modern deep learning physically possible.

## Connections

- [[MatrixMultiplication]] / [[MultiplyAccumulate]] — the operation GEMM implements.
- [[ForwardPropagation]] — the pass dominated by GEMM.
- [[ArithmeticIntensity]] / [[RooflineModel]] / [[ComputeBound]] / [[MemoryBound]] — why GEMM is the preferred workload.
- [[TensorCore]] / [[GPU]] / [[NVIDIA]] — hardware tuned for GEMM (e.g. the H100).
- [[mlsysbook-ch07-ml-frameworks]] — Ch 7 makes GEMM the bottom rung of the framework [[LadderOfAbstraction|Ladder of Abstraction]] (BLAS/LAPACK delegate `C = A @ B` to vendor-tuned [[CUBLAS|cuBLAS]]); a ResNet-50 forward pass ≈ 4.1 GFLOP, "nearly all of which reduce to GEMM," with convolutions lowered via [[Im2col|im2col]].
- [[mlsysbook-ch05-neural-computation]] — source of the >90%-of-FLOPs claim.
- [[mlsysbook-ch11-hardware-acceleration]] — "modern AI accelerators are essentially specialized GEMM engines" ([[TensorCore|tensor cores]], [[SystolicArray|systolic arrays]], AMX all exist to accelerate GEMM); cuBLAS/oneDNN reach 80–95% of peak; a square FP16 GEMM has [[ArithmeticIntensity|arithmetic intensity]] $n/3$, so small multiplies fall below the ridge point; GEMM performance is the most reliable predictor of end-to-end training throughput.
