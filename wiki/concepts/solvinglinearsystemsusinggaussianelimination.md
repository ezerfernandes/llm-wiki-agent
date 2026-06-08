---
title: "Solving Linear Systems Using Gaussian Elimination"
type: concept
tags: [linear-algebra, numerical-methods]
sources: [mml-ch02-linear-algebra, mml-book]
last_updated: 2026-06-04
---

# Solving Linear Systems Using Gaussian Elimination

This page resolves to the canonical concept page **[[GaussianElimination]]** (see also the parallel-computing treatment there).

[[GaussianElimination|Gaussian elimination]] applies elementary row transformations to the augmented matrix $[\mathbf{A}\,|\,\mathbf{b}]$ to reach [[ReducedRowEchelonForm|reduced row-echelon form]], from which the particular and general solution of $\mathbf{A}\mathbf{x}=\mathbf{b}$ are read off ([[mml-ch02-linear-algebra|MML Ch 2]] §2.3). The general solution = a particular solution + the homogeneous solution set (the [[NullSpace|kernel]]).

## Connections

- [[GaussianElimination]] — canonical page (this slug is an alias).
- [[RowEchelonForm]] / [[ReducedRowEchelonForm]] / [[Pivot]] — the intermediate forms.
- [[SystemOfLinearEquations]] — what is being solved.
- [[mml-ch02-linear-algebra|MML Ch 2]] / [[mml-book]] — §2.3 reference.
