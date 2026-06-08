---
title: "Tupper's self-referential formula (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, bignum, graphics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Tupper's_self-referential_formula
---

## Summary
The task asks the programmer to plot Tupper's self-referential formula, an inequality involving two variables x and y that, when graphed over a specific 106-by-17 region, draws a bitmap of the formula itself. The key insight is that the enormous constant k encodes the image as a binary bitmap: each bit of `floor(y/17)` selected by the modular/floor expression turns a pixel on or off, so the formula is really a compact way of decoding and rendering a stored bitmap.

## Task Requirements
- Implement the inequality `1/2 < floor(mod(floor(y/17) * 2^(-17*floor(x) - mod(floor(y),17)), 2))`.
- Plot it over the integer ranges 0 ≤ x ≤ 106 and k ≤ y ≤ k+17, using the given 543-digit constant k.
- Output the result as text, a matrix, or an image.
- Use arbitrary-precision (bignum) integer arithmetic, via a library if the language lacks it natively.

## Language Coverage
23 languages implement this task, spanning systems and scripting languages with strong bignum support; representative entries include C++, C#, Java, Rust, Python, Julia, Perl, Raku, Common Lisp, Nim, and Wren.

## Connections
- [[ArbitraryPrecisionArithmetic]] — the 543-digit k requires bignum integers
- [[ModularArithmetic]] — the formula relies on mod and floor operations
- [[BitManipulation]] — k encodes a bitmap decoded bit by bit
- [[NumberTheory]] — bit extraction via division by powers of two
- [[RasterGraphics]] — the output is a 106x17 pixel bitmap

## Contradictions
- None — reference task page.
