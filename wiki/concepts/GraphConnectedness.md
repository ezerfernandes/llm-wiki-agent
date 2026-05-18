---
title: "Graph Connectedness"
type: concept
tags: [graph-theory, linear-algebra, parallel-computing]
sources: [parproc-ch11-parallel-matrix-operations]
last_updated: 2026-05-17
---

# Graph Connectedness

A graph is **connected** if there is a path between every pair of vertices. Testing connectivity and computing reachability can be reduced to matrix power computations over the adjacency matrix.

## Adjacency Matrix Approach

Let A be the $n \times n$ adjacency matrix of a graph: $a_{ij} = 1$ if there is an edge from $i$ to $j$, 0 otherwise.

**Theorem (Matloff Ch11, Theorem 1):**
- The number of r-step paths from vertex $i$ to vertex $j$ equals the $(i,j)$ element of $A^r$.
- The graph is connected if and only if each of the **reachability matrices** $R^{(1)}, \ldots, R^{(n-1)}$ has all off-diagonal elements equal to 1, where $R^{(k)} = b(A^k)$ and $b(\cdot)$ replaces nonzero entries with 1.
- For undirected graphs, since cycles allow revisiting vertices, connectivity holds if and only if **some** $R^{(k)}$ among $R^{(1)}, \ldots, R^{(n-1)}$ has all off-diagonal elements equal to 1.

Once a fully-1 (off-diagonal) reachability matrix is found, computation can stop.

## Parallel Computation

Computing $A^k$ reduces to repeated [[MatrixMultiplication|matrix multiplication]], which parallelizes well. The repeated-squaring trick (compute $A^2$, then $A^4$, $A^8$, ...) reduces $k$ multiplications to $\log_2 k$.

## Connections

- [[MatrixMultiplication]] — powers of A computed via parallel matrix multiplication.
- [[MatrixInversion]] — another application of matrix powers.
- [[FibonacciNumbers]] — another application of the matrix-power technique.
- [[SparseMatrix]] — real-world graphs are often sparse; CSR format applies.
- [[parproc-ch11-parallel-matrix-operations]] — §11.4.1 primary source.
