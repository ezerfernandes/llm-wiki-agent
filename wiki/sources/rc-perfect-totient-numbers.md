---
title: "Perfect totient numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, totient]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Perfect_totient_numbers
---

## Summary
This task asks the programmer to generate and display the first twenty perfect totient numbers (OEIS A082897). A perfect totient number is an integer n equal to the sum of its iterated totients: repeatedly apply Euler's totient function starting from n until the value reaches 1, summing each result. The key insight is that the answer reuses a standard totient implementation chained on its own output.

## Task Requirements
- Compute the iterated totient chain of a number: φ(n), φ(φ(n)), … down to 1.
- A number is perfect-totient if it equals the sum of that chain of iterated totients.
- Generate and show the first twenty perfect totient numbers.

## Language Coverage
63 languages implement this task, spanning low-level assembly through high-level functional and array languages. Representative entries include C, C++, Rust, Go, Java, Python, Haskell, Julia, Perl, Raku, APL, and ARM Assembly.

## Connections
- [[EulerTotientFunction]] — the core function iterated to build the sum
- [[NumberTheory]] — the mathematical domain of the task
- [[IntegerSequences]] — corresponds to OEIS A082897
- [[GreatestCommonDivisor]] — underlies the standard totient computation

## Contradictions
- None — reference task page.
