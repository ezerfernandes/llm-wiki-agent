---
title: "Row-Echelon Form"
type: concept
tags: [linear-algebra, numerical-methods]
sources: [mml-ch02-linear-algebra, mml-book]
last_updated: 2026-06-04
---

# Row-Echelon Form

**Definition 2.6** ([[mml-ch02-linear-algebra|MML Ch 2]] §2.3.2): a matrix is in *row-echelon form* (REF) if:

1. All rows containing only zeros are at the **bottom**; correspondingly, all rows with at least one non-zero element are above the all-zero rows.
2. Looking at non-zero rows only, the first non-zero entry from the left (the [[Pivot|pivot]] / *leading coefficient*) is **strictly to the right** of the pivot of the row above.

This produces a characteristic **"staircase" structure**. REF is obtained by applying *elementary transformations* — (i) swap two rows, (ii) multiply a row by $\lambda\neq0$, (iii) add a multiple of one row to another — which preserve the solution set.

## Basic and free variables

Variables corresponding to pivot columns are **basic variables**; the rest are **free variables** (MML Remark, p. 30). The free variables parameterize the infinitely many solutions of an underdetermined system.

## What REF is good for

- **Solving** $\mathbf{A}\mathbf{x}=\mathbf{b}$: REF gives an upper-triangular-like system solved by back substitution; a particular solution comes from expressing $\mathbf{b}$ via the pivot columns (MML Eq. 2.48).
- **Testing [[LinearIndependence|linear independence]]**: pivot columns are independent; non-pivot columns are combinations of pivot columns to their left.
- **Finding a [[Basis|basis]]** of a span (pivot columns) and the [[Rank|rank]] (number of pivots).

The stricter [[ReducedRowEchelonForm|reduced row-echelon form]] adds: every pivot is 1 and is the only non-zero entry in its column.

## Connections

- [[GaussianElimination]] — the algorithm that reaches (reduced) REF.
- [[ReducedRowEchelonForm]] — the canonical, stricter form.
- [[Pivot]] — the leading coefficients defining the staircase.
- [[Rank]] / [[Basis]] / [[LinearIndependence]] — read off the pivot columns.
- [[SystemOfLinearEquations]] — REF is the intermediate form for solving.
- [[mml-ch02-linear-algebra|MML Ch 2]] / [[mml-book]] — §2.3.2 canonical reference.
