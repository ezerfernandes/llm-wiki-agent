---
title: "P-Adic square roots (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, p-adic, modular-arithmetic]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/P-Adic_square_roots
---

## Summary
The task asks the programmer to compute the approximate p-adic square root of a rational number a/b. The root is built iteratively by Hensel lifting: first solve x² ≡ a/b modulo p, then refine the solution one p-adic digit at a time so that f(x) = bx² − a is congruent to 0 modulo successively higher powers of p. To verify, the root is squared and the original rational a/b is recovered from the p-adic expansion via rational reconstruction (Lagrange lattice basis reduction). Built-in big-integer support is essential, since the lifted values overflow fixed-width types.

## Task Requirements
- Convert a rational a/b into its approximate p-adic square root.
- Find the initial root x₁ modulo p, then lift it through the recurrence x_{k+1} = x_k + d_k·p^k.
- Compute each p-adic digit via d_k = −(f(x_k)/p^k) / f′(x₁) (mod p), where f(x) = bx² − a.
- Square the resulting root and reconstruct a rational m/n to compare against the radicand a/b.
- Use Lagrange's lattice basis reduction for the rational reconstruction step.
- Use arbitrary-precision integers to avoid overflow truncating the expansion.

## Language Coverage
13 languages implement this task, a modest set reflecting its mathematical specialization and reliance on big-integer arithmetic. Representative implementations include C++, Go, Haskell, Java, JavaScript, Julia, Python, Rust, Nim, and Wren.

## Connections
- [[PAdicNumbers]] — the number system whose square roots are being computed
- [[HenselsLemma]] — the lifting principle that refines the root modulo increasing powers of p
- [[ModularArithmetic]] — initial root and digit computations are done mod p
- [[LatticeBasisReduction]] — Lagrange's algorithm used for rational reconstruction
- [[NumberTheory]] — the broader domain of the task

## Contradictions
- None — reference task page.
