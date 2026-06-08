---
title: "Euler's sum of powers conjecture (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, brute-force-search]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Euler's_sum_of_powers_conjecture
---

## Summary
Euler conjectured that summing fewer than k positive k-th powers can never equal another k-th power (for k > 2). The conjecture stood for over two centuries until Lander and Parkin disproved it in 1966 with a brute-force computer search. The task asks the programmer to reproduce that disproof for the k=5 case by finding distinct positive integers satisfying x0^5 + x1^5 + x2^5 + x3^5 = y^5. The known counterexample is 27^5 + 84^5 + 110^5 + 133^5 = 144^5.

## Task Requirements
- Search for an integer solution to x0^5 + x1^5 + x2^5 + x3^5 = y^5.
- All x_i and y must be distinct integers strictly between 0 and 250.
- Display the found solution.

## Language Coverage
73 languages implement this task, spanning systems and assembly languages through scripting and functional ones. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Common Lisp, Fortran, and 360 Assembly.

## Connections
- [[NumberTheory]] — the problem concerns sums of integer powers.
- [[EulersSumOfPowersConjecture]] — the historical conjecture being disproved.
- [[BruteForceSearch]] — the solution strategy (with optimizations like precomputed power tables and binary search).
- [[DiophantineEquations]] — finding integer solutions to a polynomial equation.

## Contradictions
- None — reference task page.
