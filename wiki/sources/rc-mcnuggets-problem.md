---
title: "McNuggets problem (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/McNuggets_problem
---

## Summary
A McNugget number is any total reachable as a non-negative combination of boxes of 6, 9, and 20 nuggets. The task asks to find, over the range 0 to 100, the largest number that *cannot* be expressed as 6x + 9y + 20z with natural-number coefficients. This is a concrete instance of the Frobenius coin problem; the answer for the {6, 9, 20} set is 43.

## Task Requirements
- Search numbers from 0 up to a limit of 100.
- Identify which values can be written as 6x + 9y + 20z where x, y, z are natural numbers (non-negative integers).
- Report the largest non-representable (non-McNuggets) number found.

## Language Coverage
89 languages implement this task, showing broad coverage across systems, scripting, functional, and constraint-solving paradigms. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Julia, Raku, and the constraint solver MiniZinc.

## Connections
- [[FrobeniusNumber]] — the largest unrepresentable value is exactly the Frobenius number of the set
- [[CoinProblem]] — the McNuggets problem is the canonical McDonald's framing of this problem
- [[NumberTheory]] — concerns representability of integers as linear combinations
- [[BruteForceSearch]] — the typical solution iterates over candidate sums up to the limit

## Contradictions
- None — reference task page.
