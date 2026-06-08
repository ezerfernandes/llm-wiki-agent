---
title: "System of Linear Equations"
type: concept
tags: [linear-algebra, foundational]
sources: [mml-ch02-linear-algebra, mml-book]
last_updated: 2026-06-04
---

# System of Linear Equations

A finite collection of linear equations in shared unknowns. In general form ([[mml-ch02-linear-algebra|MML Ch 2]] §2.1, Eq. 2.3):

$$a_{11}x_1+\cdots+a_{1n}x_n=b_1,\quad\ldots,\quad a_{m1}x_1+\cdots+a_{mn}x_n=b_m$$

with $a_{ij},b_i\in\mathbb{R}$. An $n$-tuple $(x_1,\ldots,x_n)$ satisfying all equations is a *solution*. Compactly, $\mathbf{A}\mathbf{x}=\mathbf{b}$, where $\mathbf{A}\mathbf{x}$ is a **linear combination of the columns** of $\mathbf{A}$ (each $x_j$ scales column $j$).

## Solution trichotomy

A real system has exactly one of three outcomes — **no solution**, a **unique solution**, or **infinitely many solutions** (never any other count). The infinite case is parameterized by *free variables*, e.g. $\{(\tfrac52-\tfrac32 a,\ \tfrac12+\tfrac12 a,\ a):a\in\mathbb{R}\}$ ([[mml-ch02-linear-algebra|MML Ch 2]] Eq. 2.7).

## Geometric reading

With two unknowns each equation is a *line* in the plane; the solution set is the intersection (point / line / empty). With three unknowns each equation is a *plane*; intersections give a plane / line / point / empty set ([[mml-ch02-linear-algebra|MML Ch 2]] §2.1 Remark).

## Homogeneous vs inhomogeneous

- **Homogeneous** ($\mathbf{b}=\mathbf{0}$): the solution set is a [[VectorSubspace|vector subspace]] of $\mathbb{R}^n$ of dimension $n-\operatorname{rk}(\mathbf{A})$ — the [[NullSpace|kernel/null space]].
- **Inhomogeneous** ($\mathbf{b}\neq\mathbf{0}$): the solution set is **not** a subspace (no $\mathbf{0}$); it is an [[AffineSubspace|affine subspace]] (particular solution + homogeneous solutions).
- **Solvability**: $\mathbf{A}\mathbf{x}=\mathbf{b}$ has a solution iff $\operatorname{rk}(\mathbf{A})=\operatorname{rk}(\mathbf{A}|\mathbf{b})$.

## Connections

- [[GaussianElimination]] — the constructive algorithm for solving via [[ReducedRowEchelonForm]].
- [[Matrix]] / [[MatrixMultiplication]] — the compact $\mathbf{A}\mathbf{x}=\mathbf{b}$ representation.
- [[Rank]] — controls solvability and the dimension of the solution space.
- [[VectorSubspace]] / [[AffineSubspace]] — the geometry of solution sets.
- [[LinearRegression]] — solves a least-squares relaxation of $\mathbf{A}\mathbf{x}=\mathbf{b}$ when no exact solution exists (MML Ch 9).
- [[mml-ch02-linear-algebra|MML Ch 2]] / [[mml-book]] — §2.1, §2.3 canonical reference.
