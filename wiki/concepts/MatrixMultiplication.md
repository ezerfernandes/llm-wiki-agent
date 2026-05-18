---
title: "Matrix Multiplication"
type: concept
tags: [linear-algebra, parallel-computing, algorithms]
sources: [parproc-ch11-parallel-matrix-operations]
last_updated: 2026-05-17
---

# Matrix Multiplication

The computation $C = AB$ for matrices A ($n \times k$) and B ($k \times n$), where $C_{ij} = \sum_l A_{il} B_{lj}$. Sequential matrix multiplication has time complexity $O(n^3)$ for square $n \times n$ matrices.

Parallel matrix multiplication is a central problem in parallel computing: many other matrix algorithms (eigenvalue computation, matrix inversion, graph connectivity) reduce to it.

## Parallel Strategies

### Message-Passing (MPI)

[[FoxAlgorithm|Fox's algorithm]] distributes A, B, and C as block partitions across $\sqrt{p} \times \sqrt{p}$ nodes. Each node broadcasts its diagonal block of A across its block row, accumulates the subproduct, then shifts its block of B down. Cannon's algorithm is similar but rotates in both dimensions.

### Shared-Memory (OpenMP)

The outer loop over rows of A can be parallelized with `#pragma omp parallel for`. Deeper nesting levels can also be parallelized if profitable.

### GPU (CUDA)

A natural assignment is one thread per output element $c_{ij}$, each computing a full inner product. A more efficient approach tiles A and B into BLOCK_SIZE×BLOCK_SIZE submatrices in `__shared__` memory — described in the Prof. Edgar algorithm — extending speedup from 20× to 500× over a serial baseline. CUBLAS provides highly tuned closed-source implementations.

### R Interfaces

R [[Snow]] parallelizes matrix-matrix products by the same row-chunk tiling used for matrix-vector products (§1.6.3.1). The `gputools` library exposes `gpuMatMult()` for GPU-accelerated multiplication from R.

## Connections

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
- [[parproc-ch11-parallel-matrix-operations]] — §11.3 primary source.
