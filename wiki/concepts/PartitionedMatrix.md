---
title: "Partitioned Matrix"
type: concept
tags: [linear-algebra, parallel-computing, matrix]
sources: [parproc-ch11-parallel-matrix-operations]
last_updated: 2026-05-17
---

# Partitioned Matrix

A matrix divided into rectangular submatrices called **blocks** (or **tiles**). If matrices A, B, and C = AB are partitioned into blocks of compatible sizes, the block product obeys the same summation formula as scalar multiplication: $C_{ij} = \sum_k A_{ik} B_{kj}$, where each term is now a submatrix product.

This algebraic property is the foundation of all block-parallel matrix algorithms. Each block can be assigned to a different processing element, which computes its portion of C by performing a sequence of smaller matrix multiplications and additions.

The standard partition for an $n \times n$ matrix with $p$ processes assumes $\sqrt{p}$ evenly divides $n$, yielding $m = n/\sqrt{p}$ blocks per dimension, so each block is of size $m \times m$.

## Connections

- [[MatrixMultiplication]] — partitioned matrices enable parallel matrix multiplication.
- [[FoxAlgorithm]] — Fox's and Cannon's algorithms both rely on a compatible block partition of A, B, and C.
- [[CUDA]] — BLOCK_SIZE tiles in the Edgar shared-memory kernel exploit the partitioned-matrix multiply rule.
- [[parproc-ch11-parallel-matrix-operations]] — §11.2 primary source.
