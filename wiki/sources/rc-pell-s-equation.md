---
title: "Pell's equation (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, diophantine-equation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Pell's_equation
---

## Summary
The task is to find the smallest positive-integer solution to Pell's equation (also called the Pell–Fermat equation), the Diophantine equation x² − ny² = 1, where n is a given non-square positive integer. The key insight is that the fundamental solution is derived from the continued-fraction expansion of √n, whose periodic convergents yield the minimal (x, y) pair. Because solutions can grow enormous very quickly, big-integer arithmetic is generally required.

## Task Requirements
- Find the smallest solution in positive integers to Pell's equation for each n in {61, 109, 181, 277}.
- For each n, report the minimal (x, y) satisfying x² − ny² = 1.

## Language Coverage
42 languages implement this task, giving broad coverage across systems, functional, and scripting families. Representative implementations include C, C++, Rust, Go, Haskell, Java, Julia, Python, Perl, Raku, and Wren, alongside math-oriented entries like Mathematica/Wolfram Language and J.

## Connections
- [[DiophantineEquation]] — Pell's equation is a classic Diophantine equation.
- [[ContinuedFractions]] — the standard solution method expands √n as a periodic continued fraction.
- [[NumberTheory]] — the problem lives in the theory of integer solutions to quadratic forms.
- [[ArbitraryPrecisionArithmetic]] — minimal solutions grow large, requiring big-integer support.

## Contradictions
- None — reference task page.
