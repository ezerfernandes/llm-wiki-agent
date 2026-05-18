---
title: "Jacobi Algorithm"
type: concept
tags: [linear-algebra, numerical-methods, parallel-computing, openmp, iterative]
sources: [parproc-ch11-parallel-matrix-operations]
last_updated: 2026-05-17
---

# Jacobi Algorithm

An iterative method for solving $Ax = b$. Rewrite each equation to isolate $x_i$:

$$x_i = \frac{1}{a_{ii}}\bigl[b_i - (a_{i0}x_0 + \ldots + a_{i,i-1}x_{i-1} + a_{i,i+1}x_{i+1} + \ldots + a_{i,n-1}x_{n-1})\bigr]$$

In matrix terms: $x^{(k+1)} = D^{-1}(b - Ox^{(k)})$ where D is the diagonal matrix of $a_{ii}$ values and O is A with diagonal zeroed.

## Convergence

The algorithm is guaranteed to converge when A is **diagonally dominant**: each diagonal element is larger in absolute value than the sum of absolute values of the other elements in its row. (This is sufficient but not strictly necessary.)

## Parallelization

**OpenMP:** Assign each thread a contiguous chunk of indices. Within each iteration, each thread updates its section of $x$. After updating, a barrier synchronizes threads so every thread reads the latest $x$ values. An `omp reduction` clause accumulates the convergence check (sum of $|x_i - x_i^{\text{old}}|$). Convergence is declared when this sum falls below $n \cdot \varepsilon$.

**R/gputools:** The R implementation directly uses `gpumatmult` for the $Ox^{(k)}$ step, delegating the matrix-vector product to the GPU.

## Connections

- [[GaussianElimination]] — direct alternative; Jacobi is preferred for large diagonally dominant systems where direct elimination is too costly.
- [[MatrixMultiplication]] — the Jacobi update reduces to a matrix-vector multiply $Ox^{(k)}$.
- [[OpenMP]] — §11.5.4 implementation.
- [[parproc-ch11-parallel-matrix-operations]] — §11.5.3–11.5.5 primary source.
