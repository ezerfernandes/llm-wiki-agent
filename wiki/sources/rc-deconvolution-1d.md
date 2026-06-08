---
title: "Deconvolution/1D (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, linear-algebra, signal-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Deconvolution/1D
---

## Summary
The task asks the programmer to implement `deconv`, the inverse of one-dimensional discrete convolution: given sequences `g` and `f` (where `g = f * h`), recover the third sequence `h`. The key insight is that convolution `g = A·h` can be written as a linear system whose matrix `A` is built from the entries of `f` arranged in banded/Toeplitz fashion, so deconvolution reduces to solving (or least-squares fitting) that overdetermined system, with `|h| = |g| - |f| + 1`.

## Task Requirements
- Implement a `deconv` function that constructs and solves the linear system `g = A·h` to recover `h` from given `f` and `g`.
- Work for `g` of arbitrary length and `f` of any length up to that of `g`; nothing hard-coded. Compute `|h| = |g| - |f| + 1`.
- Handle the case of more equations than unknowns: either use a least-squares solver for the overdetermined system, or prune equations and solve via Gaussian elimination / reduced row echelon form.
- Verify symmetry: `deconv(g, f) = h` and `deconv(g, h) = f`, and display results in human-readable form.
- Test against the provided fixed `h`, `f`, and `g` data vectors.

## Language Coverage
41 languages implement this task, spanning systems and numerical languages alongside array- and math-oriented ones; representative entries include C, C++, Rust, Go, Java, Python, Haskell, J, Julia, MATLAB, Fortran, and Wren.

## Connections
- [[Convolution]] — deconvolution is its inverse operation.
- [[ToeplitzMatrix]] — the system matrix `A` has banded Toeplitz structure built from `f`.
- [[LinearLeastSquares]] — recommended approach for the overdetermined system.
- [[GaussianElimination]] — alternative exact solver after pruning equations.
- [[ReducedRowEchelonForm]] — referenced fallback method for solving the system.

## Contradictions
- None — reference task page.
