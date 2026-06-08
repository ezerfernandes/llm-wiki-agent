---
title: "Ulam spiral (for primes) (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, primes, spiral-matrix]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Ulam_spiral_(for_primes)
---

## Summary
The task asks the programmer to generate an Ulam (prime) spiral: integers are laid out on a square grid in an outward, counter-clockwise spiral starting from a center value (default 1), and then only the prime-valued cells are rendered with a glyph (e.g. a dot) while non-primes are left blank. The visual insight is that primes cluster along diagonal lines rather than scattering randomly, a pattern that becomes more striking as the grid grows. The implementation combines a spiral-coordinate walk with a primality test.

## Task Requirements
- For any N x N grid size, construct a counter-clockwise spiral of consecutive integers.
- Allow a specifiable starting number (default 1) at the center.
- Render primes with a "dotty" glyph and non-primes as blank/whitespace.
- Demonstrate the generator with a spiral large enough to (almost) fill the terminal screen.

## Language Coverage
56 languages implement this task, spanning systems, scripting, functional, and array languages. Representative examples include C, C++, Rust, Go, Java, Python, Haskell, J, Julia, Perl, and REXX.

## Connections
- [[PrimeNumbers]] — each cell is tested for primality before being drawn
- [[SpiralMatrix]] — the underlying coordinate-walk that fills the grid in a spiral
- [[NumberTheory]] — the diagonal clustering of primes is a number-theoretic phenomenon
- [[TrialDivision]] — a common primality-testing method used to classify each cell
- [[DataVisualization]] — the task is fundamentally about visualizing a numeric pattern

## Contradictions
- None — reference task page.
