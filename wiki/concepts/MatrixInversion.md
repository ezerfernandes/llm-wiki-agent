---
title: "Matrix Inversion"
type: concept
tags: [linear-algebra, numerical-methods, parallel-computing]
sources: [parproc-ch11-parallel-matrix-operations]
last_updated: 2026-05-17
---

# Matrix Inversion

Computing $A^{-1}$ for a square matrix A. Direct methods (e.g., [[GaussianElimination|Gaussian elimination]] on the augmented matrix $(A \mid I)$) have $O(n^3)$ complexity, the same as matrix multiplication.

## Power Series Method

For an $n \times n$ matrix C with $\sum_{i,j} c_{ij}^2 < 1$:

$$(I - C)^{-1} = I + C + C^2 + \ldots$$

To invert A, set $C = I - dA$ for a scalar $d$ small enough that the convergence condition holds (possible when A has nonnegative entries). Then:

$$A^{-1} = (I - C)^{-1} / d = (I + C + C^2 + \ldots) / d$$

The sum is truncated when the partial sum stabilizes. Computing it reduces to repeated [[MatrixMultiplication|matrix multiplication]], which parallelizes more effectively than direct inversion — motivating this approach in parallel settings even though the asymptotic complexity is the same serially.

The repeated-squaring trick can accelerate the partial-sum computation.

## Appendix B Definition (Matloff)

Section B.5 of *Programming on Parallel Machines* ([[parproc-appB-matrix-algebra]]) gives the foundational definitions:

- The **identity matrix** I of size n has 1s on the diagonal and 0s off-diagonal; $AI = IA = A$.
- B is the **inverse** of square A (written $A^{-1}$) if $AB = I$; then $BA = I$ also holds.
- $A^{-1}$ exists iff the rows (or columns) of A are linearly independent, equivalently iff $\det(A) \neq 0$.
- For conformable invertible A and B: $(AB)^{-1} = B^{-1}A^{-1}$.
- An orthogonal matrix U satisfies $U^{-1} = U'$ (see [[MatrixTranspose]]).
- **QR method:** write $A = QR$ with Q orthogonal and R upper-triangular; then $A^{-1} = (QR)^{-1} = R^{-1}Q'$. The triangular inverse $R^{-1}$ is found by back substitution.

In R, `solve(a)` computes $A^{-1}$ directly (subject to roundoff); `qr.solve(a)` uses the QR route and is more numerically stable.

```r
minv <- solve(m)        # direct inverse
m %*% minv              # should recover I (with roundoff)
qr.solve(m)             # QR-based inverse
```

## Connections

- [[MatrixMultiplication]] — the power series approach reduces inversion to iterated multiplication.
- [[GaussianElimination]] — direct alternative for solving $Ax = b$.
- [[Determinant]] — $A^{-1}$ exists iff $\det(A) \neq 0$.
- [[LinearIndependence]] — $A^{-1}$ exists iff rows/columns of A are linearly independent.
- [[MatrixTranspose]] — orthogonal matrices satisfy $U^{-1} = U'$; QR formula uses $Q'$.
- [[GraphConnectedness]] — a related matrix-power application.
- [[FibonacciNumbers]] — another matrix-power application.
- [[parproc-ch11-parallel-matrix-operations]] — §11.4.3 primary source.
- [[parproc-appB-matrix-algebra]] — §B.5 formal definitions and QR route.
