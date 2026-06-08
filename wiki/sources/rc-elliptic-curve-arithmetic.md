---
title: "Elliptic curve arithmetic (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, elliptic-curves, cryptography, group-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Elliptic_curve_arithmetic
---

## Summary
This task asks the programmer to implement a simplified (non-modular) version of the point arithmetic used on elliptic curves, the same arithmetic that underpins the elliptic curve DSA protocol. The curve is defined by y² = x³ + ax + b, using the secp256k1 parameters a=0 and b=7. The key insight is that points on the curve form a group under a geometric "addition" rule: three collinear points sum to the infinity point (the identity element), so adding two points means drawing the line through them, finding the third intersection, and reflecting it across the x-axis.

## Task Requirements
- Define a point addition function that, given any two curve points, returns their sum on the curve y² = x³ + 0x + 7.
- Handle the infinity point as the neutral (identity) element of the addition.
- Pick two random points on the curve, compute their sum, and demonstrate that the reflection of the sum is collinear with the two original points.
- Likely define a "doubling" function returning P+P (needed when the two points coincide).
- Extra credit: implement scalar "multiply" returning P added to itself n times.

## Language Coverage
35 languages implement this task, spanning systems languages, functional languages, and computer-algebra-oriented tools. Representative implementations include C, C++, Rust, Go, Zig, Haskell, OCaml, Python, Julia, Raku, and PARI/GP.

## Connections
- [[EllipticCurves]] — the geometric object whose points form the underlying set
- [[GroupTheory]] — point addition gives the curve an abelian group structure with the infinity point as identity
- [[EllipticCurveCryptography]] — this arithmetic is the basis of ECDSA and related protocols
- [[Secp256k1]] — the specific curve parameters (a=0, b=7) used here

## Contradictions
- None — reference task page.
