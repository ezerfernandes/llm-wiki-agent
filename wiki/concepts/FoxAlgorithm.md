---
title: "Fox's Algorithm"
type: concept
tags: [parallel-computing, matrix, mpi, distributed-memory]
sources: [parproc-ch11-parallel-matrix-operations]
last_updated: 2026-05-17
---

# Fox's Algorithm

A distributed-memory algorithm for parallel [[MatrixMultiplication|matrix multiplication]] of two $n \times n$ matrices A and B stored in a partitioned, distributed manner across $p$ MPI nodes arranged in a $\sqrt{p} \times \sqrt{p}$ logical mesh.

## Algorithm

Assume $m = n/\sqrt{p}$ (so $\sqrt{p}$ divides $n$). Each node holds one block of A, one of B, and accumulates one block of C.

The node computing $C_{ij}$ needs:

$$\sum_{k=0}^{m-1} A_{i,(i+k) \bmod m} \; B_{(i+k) \bmod m,\, j}$$

Over $m$ steps indexed by $k$:

1. **Broadcast** block $A_{i,(i+k) \bmod m}$ to all nodes in block row $i$.
2. Each node **accumulates**: $C_{i,j} \mathrel{+}= A_{i,km} \times B_{km,j}$.
3. **Shift** B downward by one block row (send $B[km,j]$ to the node handling $C[i_{\text{down}},j]$).

The computation and communication can be overlapped (broadcast while the previous multiply proceeds) for better efficiency. Using MPI communicators to group block rows makes the broadcast convenient.

## Comparison with Cannon's Algorithm

Cannon's algorithm performs cyclic rotation in **both** rows and columns, while Fox's rotates only in columns and broadcasts within rows.

## Connections

- [[PartitionedMatrix]] — the algebraic substrate.
- [[MatrixMultiplication]] — the operation being parallelized.
- [[MPI]] — the communication model (broadcast + send/receive).
- [[parproc-ch11-parallel-matrix-operations]] — §11.3.1 primary source.
