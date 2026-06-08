---
title: "Gaussian Elimination"
type: concept
tags: [linear-algebra, numerical-methods, parallel-computing, cuda]
sources: [parproc-ch11-parallel-matrix-operations, mml-ch02-linear-algebra, mml-book]
last_updated: 2026-06-04
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

## From [[mml-ch02-linear-algebra|MML Ch 2]]

MML **defines** Gaussian elimination (§2.3.2 Remark) as "an algorithm that performs elementary transformations to bring a system of linear equations into [[ReducedRowEchelonForm|reduced row-echelon form]]." The three *elementary transformations* (which preserve the solution set) are: (i) swap two rows; (ii) multiply a row by $\lambda\neq0$; (iii) add a multiple of one row to another. They are applied to the *augmented matrix* $[\mathbf{A}\,|\,\mathbf{b}]$.

**Solution structure** (§2.3.1): the general solution = a *particular solution* of $\mathbf{A}\mathbf{x}=\mathbf{b}$ plus all solutions of the homogeneous system $\mathbf{A}\mathbf{x}=\mathbf{0}$. The three-step recipe: (1) find a particular solution; (2) find all solutions of $\mathbf{A}\mathbf{x}=\mathbf{0}$ (e.g. the *Minus-1 Trick*, §2.3.3); (3) combine. A particular solution is read off by expressing $\mathbf{b}$ via the [[Pivot|pivot]] columns.

**Many uses beyond solving** (§2.3.4): Gaussian elimination also computes the [[MatrixInverse|inverse]] (bring $[\mathbf{A}\,|\,\mathbf{I}]$ to RREF → $[\mathbf{I}\,|\,\mathbf{A}^{-1}]$), the [[Determinant|determinant]] (§4.1), tests [[LinearIndependence|linear independence]] (§2.5), computes the [[Rank|rank]] (§2.6.2), and finds a [[Basis|basis]] (§2.6.1). It is intuitive and works for thousands of variables, but scales **cubically**; for millions of variables, iterative methods (Jacobi, Gauss–Seidel, conjugate gradients, GMRES) of the form $\mathbf{x}^{(k+1)}=\mathbf{C}\mathbf{x}^{(k)}+\mathbf{d}$ are used instead.

## Connections

- [[RowEchelonForm]] / [[ReducedRowEchelonForm]] / [[Pivot]] — the forms it produces (MML §2.3).
- [[SystemOfLinearEquations]] / [[MatrixInverse]] / [[Rank]] / [[Determinant]] / [[Basis]] — its many applications.
- [[mml-ch02-linear-algebra|MML Ch 2]] / [[mml-book]] — §2.3 canonical reference.
- [[JacobiAlgorithm]] — iterative alternative for solving $Ax = b$; better suited to diagonally dominant large systems.
- [[CUDA]] — §11.5.2 implementation platform.
- [[SparseMatrix]] — sparse systems call for specialized solvers rather than dense Gaussian elimination.
- [[parproc-ch11-parallel-matrix-operations]] — §11.5.1–11.5.2 primary source.
