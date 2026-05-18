---
title: "Gaussian Elimination"
type: concept
tags: [linear-algebra, numerical-methods, parallel-computing, cuda]
sources: [parproc-ch11-parallel-matrix-operations]
last_updated: 2026-05-17
---

# Gaussian Elimination

A direct method for solving a system of linear equations $Ax = b$. The augmented matrix $C = (A \mid b)$ is reduced to echelon form through a sequence of row operations, then solved by back substitution.

This page supersedes the stub at `wiki/concepts/solvinglinearsystemsusinggaussianelimination.md`.

## Algorithm

Form $C = (A \mid b)$, an $n \times (n+1)$ matrix. The **reduced row echelon form** variant eliminates both above and below each pivot:

```
for ii = 0 to n-1:
    divide row ii by c[ii][ii]
    for r = 0 to n-1, r != ii:
        replace row r by row r - c[r][ii] * row ii
```

The result transforms A to the identity and b to the solution x. The **row echelon form** variant eliminates only below each pivot, producing an upper-triangular system solved by back substitution. When the pivot element $c_{ii}$ is zero or near zero, a **pivoting** operation swaps row $ii$ with a later row.

## CUDA Implementation

Matloff's CUDA implementation assigns one thread per row, using a single block to avoid inter-block synchronization. The pivot row is cached in `__shared__` memory (variable `iirow`) since it is read by every other thread in each elimination step. Each thread applies the `vplscu` helper (add a scaled vector) to its row.

### Limitations

- Single-block design caps at 512 threads → at most 512×512 matrices.
- With 4K shared memory in single precision, the shared pivot row limits practical size to approximately 30×30 matrices.
- Multi-block extension is possible at the cost of extra kernel launches for inter-block synchronization.

## Connections

- [[JacobiAlgorithm]] — iterative alternative for solving $Ax = b$; better suited to diagonally dominant large systems.
- [[CUDA]] — §11.5.2 implementation platform.
- [[SparseMatrix]] — sparse systems call for specialized solvers rather than dense Gaussian elimination.
- [[parproc-ch11-parallel-matrix-operations]] — §11.5.1–11.5.2 primary source.
