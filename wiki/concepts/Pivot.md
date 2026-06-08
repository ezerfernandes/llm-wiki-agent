---
title: "Pivot"
type: concept
tags: [linear-algebra, numerical-methods]
sources: [mml-ch02-linear-algebra, mml-book]
last_updated: 2026-06-04
---

# Pivot

The *pivot* (also *leading coefficient*) of a row is the first non-zero number from the left ([[mml-ch02-linear-algebra|MML Ch 2]] §2.3.2, Remark on Pivots and Staircase Structure). In a matrix in [[RowEchelonForm|row-echelon form]], each pivot lies **strictly to the right** of the pivot of the row above — giving the "staircase" structure. (In some texts the pivot is required to be 1; in [[ReducedRowEchelonForm|reduced row-echelon form]] MML requires every pivot to equal 1 and to be the only non-zero entry in its column.)

## Pivot columns carry the structure

- **Basic vs free variables**: variables of pivot columns are *basic variables*; the others are *free variables* (MML p. 30).
- **[[LinearIndependence|Independence]]**: pivot columns are linearly independent; non-pivot columns are linear combinations of pivot columns to their left. All columns are independent **iff** all columns are pivot columns.
- **[[Basis|Basis]] & [[Rank|rank]]**: the pivot columns give a basis of the [[ColumnSpace|column space]]; the number of pivots equals the rank.

## Pivoting (numerical)

When a pivot element is zero or near-zero, a **pivoting** operation swaps the row with a later row to obtain a usable pivot — essential for numerical stability in [[GaussianElimination|Gaussian elimination]].

## Connections

- [[RowEchelonForm]] / [[ReducedRowEchelonForm]] — pivots define the staircase.
- [[GaussianElimination]] — produces and may need to swap pivots.
- [[LinearIndependence]] / [[Rank]] / [[Basis]] — read off from pivot columns.
- [[mml-ch02-linear-algebra|MML Ch 2]] / [[mml-book]] — §2.3.2 canonical reference.
