---
title: "Deconvolution/2D+ (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, linear-algebra, signal-processing, numerical-methods]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Deconvolution/2D+
---

## Summary
This task generalizes one-dimensional deconvolution to arbitrary dimensions, where the 1D case applies to audio signals and the 2D case to images. Given the discrete convolution `g = f * h` of two finite multi-dimensional arrays, the goal is to implement a `deconv` function that recovers `h` given `f` and `g` (the inverse of convolution). The key insight is that each output element of the convolution is a linear combination of the unknowns, so deconvolution reduces to solving a (typically overdetermined) system of linear equations.

## Task Requirements
- Implement a `deconv` function that solves for `h` given `f` and `g`.
- Work for `g` of arbitrary length in each dimension (not hard-coded), and `f` of any length up to that of `g` per dimension.
- Parameterize by dimension `d`, unless the dimension can be inferred from the data structures.
- Handle the overdetermined case: either use a library that finds a best-fit / least-squares solution, or prune equations and solve via reduced row echelon form.
- Verify both directions: deconvolving `g` with `f` yields `h`, and deconvolving `g` with `h` yields `f`.
- Display results in human-readable form for the three-dimensional case only, using the provided test data.

## Language Coverage
19 languages implement this task, a moderate spread covering systems, numerical, and array-oriented languages. Representative examples include C, C++, D, Go, Java, JavaScript, Julia, Python, Perl, Rust, and the array language J, plus Mathematica/Wolfram Language and Wren.

## Connections
- [[Convolution]] — deconvolution is the inverse operation this task reverses.
- [[LinearAlgebra]] — each convolution output element is a linear equation in the unknowns.
- [[LeastSquares]] — recommended approach for the overdetermined system.
- [[ReducedRowEchelonForm]] — alternative Gaussian-elimination solving method when pruning equations.
- [[SignalProcessing]] — the 1D/2D motivation (audio signals and images).

## Contradictions
- None — reference task page.
