---
title: "Fibonacci Numbers"
type: concept
tags: [mathematics, linear-algebra, parallel-computing]
sources: [parproc-ch11-parallel-matrix-operations]
last_updated: 2026-05-17
---

# Fibonacci Numbers

The sequence defined by $f_0 = f_1 = 1$ and $f_n = f_{n-1} + f_{n-2}$ for $n > 1$.

## Matrix Formulation

The recurrence can be expressed in matrix form:

$$\begin{pmatrix} f_{n+1} \\ f_n \end{pmatrix} = A \begin{pmatrix} f_n \\ f_{n-1} \end{pmatrix}, \quad A = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$$

It follows that:

$$\begin{pmatrix} f_{n+1} \\ f_n \end{pmatrix} = A^{n-1} \begin{pmatrix} 1 \\ 1 \end{pmatrix}$$

Computing Fibonacci numbers thus reduces to finding powers of A. Using the repeated-squaring trick, $A^{n-1}$ can be found in $O(\log n)$ matrix multiplications, each parallelizable.

## Connections

- [[MatrixMultiplication]] — computing $A^k$ via parallel matrix multiplication.
- [[GraphConnectedness]] — another application of the matrix-power technique.
- [[MatrixInversion]] — a third matrix-power application in the same chapter.
- [[parproc-ch11-parallel-matrix-operations]] — §11.4.2 primary source.
