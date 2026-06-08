---
title: "Matrix Multiplication"
type: concept
tags: [linear-algebra, parallel-computing, algorithms]
sources: [parproc-ch11-parallel-matrix-operations, mml-ch02-linear-algebra, mml-book, mlsysbook-ch05-neural-computation]
last_updated: 2026-06-05
---

# Matrix Multiplication

The computation $C = AB$ for matrices A ($n \times k$) and B ($k \times n$), where $C_{ij} = \sum_l A_{il} B_{lj}$. Sequential matrix multiplication has time complexity $O(n^3)$ for square $n \times n$ matrices.

Parallel matrix multiplication is a central problem in parallel computing: many other matrix algorithms (eigenvalue computation, matrix inversion, graph connectivity) reduce to it.

## From [[mml-ch02-linear-algebra|MML Ch 2]]

(This page is parallel-computing-focused; the LA-canonical definition is added here.) **Definition** (§2.2.1, Eq. 2.13): for $\mathbf{A}\in\mathbb{R}^{m\times n},\mathbf{B}\in\mathbb{R}^{n\times k}$, the product $\mathbf{C}=\mathbf{AB}\in\mathbb{R}^{m\times k}$ has $c_{ij}=\sum_{l=1}^n a_{il}b_{lj}$ — the [[DotProduct|dot product]] of row $i$ of $\mathbf{A}$ and column $j$ of $\mathbf{B}$. Key facts:

- **Neighbouring dimensions must match** ($n\times k$ times $k\times m$); $\mathbf{BA}$ need not be defined even when $\mathbf{AB}$ is, and the two products can have different shapes (Fig. 2.5).
- **Not commutative**: $\mathbf{AB}\neq\mathbf{BA}$ in general (Example 2.3).
- **Associative** and **distributive** (Eqs. 2.18–2.19); the [[IdentityMatrix|identity]] is the neutral element (Eq. 2.20).
- Matrix multiplication is **not** element-wise — the element-wise product $c_{ij}=a_{ij}b_{ij}$ is the distinct **Hadamard product** (a common cause of bugs when array libraries overload `*`).
- A [[SystemOfLinearEquations|system]] $\mathbf{A}\mathbf{x}=\mathbf{b}$ writes the equations compactly; $\mathbf{A}\mathbf{x}$ is a [[LinearCombination|linear combination]] of the columns of $\mathbf{A}$.
- Composition of [[LinearMapping|linear mappings]] corresponds to the product of [[TransformationMatrix|transformation matrices]]: $\mathbf{A}_{\Psi\circ\Phi}=\mathbf{A}_\Psi\mathbf{A}_\Phi$.

## Parallel Strategies

### Message-Passing (MPI)

[[FoxAlgorithm|Fox's algorithm]] distributes A, B, and C as block partitions across $\sqrt{p} \times \sqrt{p}$ nodes. Each node broadcasts its diagonal block of A across its block row, accumulates the subproduct, then shifts its block of B down. Cannon's algorithm is similar but rotates in both dimensions.

### Shared-Memory (OpenMP)

The outer loop over rows of A can be parallelized with `#pragma omp parallel for`. Deeper nesting levels can also be parallelized if profitable.

### GPU (CUDA)

A natural assignment is one thread per output element $c_{ij}$, each computing a full inner product. A more efficient approach tiles A and B into BLOCK_SIZE×BLOCK_SIZE submatrices in `__shared__` memory — described in the Prof. Edgar algorithm — extending speedup from 20× to 500× over a serial baseline. CUBLAS provides highly tuned closed-source implementations.

### R Interfaces

R [[Snow]] parallelizes matrix-matrix products by the same row-chunk tiling used for matrix-vector products (§1.6.3.1). The `gputools` library exposes `gpuMatMult()` for GPU-accelerated multiplication from R.

## As the neural-network workload (mlsysbook Ch 5)

[[mlsysbook-ch05-neural-computation|mlsysbook Vol 1 Ch 5]] frames matmul as *the* deep-learning workload: a layer's `xW` is a [[GEMM]] kernel, and matmul accounts for **>90% of NN floating-point operations**. Its high [[ArithmeticIntensity|arithmetic intensity]] (N×N matmul = 2N³ FLOPs / ~3N²s bytes ≈ 2N/(3s) FLOP/byte) is what saturates [[ComputeBound|compute-bound]] [[GPU|GPUs]]/[[TensorCore|Tensor Cores]] — whereas element-wise ops stay [[MemoryBound|memory-bound]] at ~0.125 FLOP/byte (FP32). This is *why* dense layers are preferred over custom element-wise logic, and why blocking/tiling for cache reuse is essential against the [[MemoryWall|memory wall]].

## Connections

- [[GEMM]] / [[MultiplyAccumulate]] — the NN kernel and its atomic op.
- [[ArithmeticIntensity]] / [[RooflineModel]] / [[ComputeBound]] / [[MemoryBound]] — why matmul fits accelerators.
- [[ForwardPropagation]] / [[WeightMatrix]] / [[mlsysbook-ch05-neural-computation]] — the neural-computation framing.
- [[PartitionedMatrix]] — algebraic basis for block algorithms.
- [[FoxAlgorithm]] — MPI block multiplication algorithm.
- [[MatrixVectorMultiply]] — simpler related operation; row-chunk pattern transfers directly to matrix-matrix case.
- [[CUBLAS]] — production-quality GPU matrix multiplication library.
- [[OpenMP]] — shared-memory parallelization via `#pragma omp parallel for`.
- [[CUDA]] — GPU implementation; tiling with shared memory is key to performance.
- [[Snow]] — R distributed-memory interface.
- [[MatrixInversion]] — reduces to repeated matrix multiplication via power series.
- [[GraphConnectedness]] — computing adjacency matrix powers via repeated multiplication.
- [[FibonacciNumbers]] — Fibonacci recurrence expressed as matrix power.
- [[Matrix]] / [[IdentityMatrix]] / [[DotProduct]] — LA fundamentals (MML §2.2).
- [[LinearMapping]] / [[TransformationMatrix]] — composition = matrix product.
- [[mml-ch02-linear-algebra|MML Ch 2]] / [[mml-book]] — §2.2.1 LA definition.
- [[parproc-ch11-parallel-matrix-operations]] — §11.3 primary source.
