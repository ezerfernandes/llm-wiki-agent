---
title: "Hamming numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Hamming_numbers
---

## Summary
The task asks the programmer to generate Hamming numbers — positive integers of the form 2^i × 3^j × 5^k (i, j, k ≥ 0), also called ugly numbers or 5-smooth numbers because their only prime factors are 2, 3, and 5. The key insight is producing them in strictly increasing order without gaps or duplicates; the canonical solution merges three lazy streams (the sequence times 2, times 3, and times 5) rather than testing each integer for smoothness, which scales far better.

## Task Requirements
- Generate the sequence of Hamming numbers in increasing order.
- Show the first twenty Hamming numbers.
- Show the 1691st Hamming number (the last one below 2^31).
- Show the one millionth Hamming number, where the language or a convenient library supports arbitrary-precision integers.

## Language Coverage
106 languages implement this task, spanning low-level assembly, functional, and scripting paradigms — with notably elegant lazy-stream solutions in functional languages. Representative implementations include Haskell, Python, C, Java, Scheme, Clojure, OCaml, Rust, J, and REXX.

## Connections
- [[NumberTheory]] — Hamming numbers are defined by their prime factorization
- [[SmoothNumbers]] — they are exactly the 5-smooth numbers
- [[LazyEvaluation]] — canonical solutions use lazy infinite streams merged together
- [[DynamicProgramming]] — the merge-of-three-pointers approach is a classic DP technique
- [[ArbitraryPrecisionArithmetic]] — the one-millionth value requires bignum support

## Contradictions
- None — reference task page.
