---
title: "Kronecker product based fractals (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, fractals, linear-algebra, recursion]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Kronecker_product_based_fractals
---

## Summary
This task asks the programmer to generate self-similar fractals by taking repeated Kronecker products (a "Kronecker power") of a small 0/1 seed matrix. Because the Kronecker product tiles a copy of one matrix scaled by each element of the other, raising a 0/1 matrix to the nth Kronecker power yields a block matrix whose 1-cells form a fractal pattern. Plotting that resulting matrix renders an order-n fractal — the key insight being that self-replication emerges naturally from the Kronecker product's structure.

## Task Requirements
- Implement a Kronecker power function such as `matkronpow(M, n)`, building it from a Kronecker product routine if the language lacks one built in.
- Use the recurrence R2 = M ⊗ M and Rn = R(n-1) ⊗ M to reach the nth order.
- Build and display two named fractals, each at order/power 4 or higher: the Vicsek fractal and the Sierpinski carpet.
- Use the two specified 3x3 seed matrices (a plus/cross shape for Vicsek, a ring-with-corners shape for the carpet).
- Output may be graphical or ASCII-art (printing only practical up to order 4); orientation/distortion is implementation-specific. Optionally show one extra fractal of the author's choice.

## Language Coverage
38 languages implement this task, spanning systems languages, scientific/array languages with native Kronecker support, and functional languages. Representative entries include C, C++, Rust, Go, Java, Python, Haskell, J, Julia, R, PARI/GP, and Mathematica/Wolfram Language.

## Connections
- [[KroneckerProduct]] — the core matrix operation the fractal is built from
- [[VicsekFractal]] — one of the two required output fractals
- [[SierpinskiCarpet]] — the other required output fractal
- [[Recursion]] — the order-by-order recurrence Rn = R(n-1) ⊗ M
- [[SelfSimilarity]] — the structural property that makes the output fractal

## Contradictions
- None — reference task page.
