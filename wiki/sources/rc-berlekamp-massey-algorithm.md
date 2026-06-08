---
title: "Berlekamp–Massey algorithm (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, finite-fields, coding-theory, cryptography]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Berlekamp–Massey_algorithm
---

## Summary
The task is to implement the Berlekamp–Massey algorithm, which finds the shortest linear feedback shift register (LFSR) that generates a given sequence over a finite field. Equivalently, it computes the minimal connection polynomial of a linearly recurrent sequence, whose degree L is the sequence's linear complexity. The key insight is that the algorithm builds this polynomial iteratively, correcting it with a stored backup polynomial only when a discrepancy appears, achieving O(n²) time.

## Task Requirements
- Implement the algorithm to compute the connection polynomial C(x) = 1 + c₁x + ... + c_Lx^L for an input sequence over a finite field.
- Initialize C(x) = 1, L = 0, and a backup polynomial B(x) = 1, then process each element.
- At each step compute the discrepancy Δ = sᵢ + Σ cₖ·sᵢ₋ₖ; when Δ ≠ 0, update C(x) ← C(x) − Δ·x·B(x), and when 2L ≤ i, increase L and refresh B(x).
- Output both the connection polynomial and the linear complexity L; e.g. for the GF(2) sequence 0,0,1,1,0,1,0 the result is C(x) = 1 + x + x³ with complexity 3.

## Language Coverage
19 languages implement this task, spanning systems, functional, scientific, and BASIC-family languages. Representative entries include C++, C#, Java, Go, Rust, Python, Julia, R, Raku, and Mathematica/Wolfram Language.

## Connections
- [[FiniteField]] — the sequence elements and arithmetic live in a finite field such as GF(2)
- [[LinearFeedbackShiftRegister]] — the algorithm finds the shortest LFSR generating the sequence
- [[LinearComplexity]] — the polynomial degree L is the sequence's linear complexity
- [[ErrorCorrectingCodes]] — used to decode Reed–Solomon and BCH codes
- [[Cryptography]] — assesses the security of stream-cipher keystreams

## Contradictions
- None — reference task page.
