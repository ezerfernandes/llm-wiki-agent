---
title: "Harmonic series (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, series-summation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Harmonic_series
---

## Summary
The n-th harmonic number H_n is the sum of the reciprocals of the first n natural numbers (1 + 1/2 + 1/3 + ... + 1/n). The task is to write a routine that generates harmonic numbers and use it to explore the series. The key insight is that the harmonic series diverges to infinity, but does so extremely slowly — it grows roughly like the natural logarithm plus the Euler–Mascheroni constant γ — so reaching even modest integer thresholds requires a surprisingly large number of terms.

## Task Requirements
- Write a function/procedure to generate harmonic numbers.
- Show the values of the first 20 harmonic numbers.
- Find and show the position in the series of the first value greater than each of the integers 1 through 5.
- Stretch goal: find and show the position of the first value greater than the integers 6 through 10.

## Language Coverage
52 languages implement this task, spanning systems and functional languages as well as data-query and esoteric ones. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Julia, Perl, Raku, COBOL, and the database-oriented DuckDB.

## Connections
- [[HarmonicNumber]] — the quantity being computed
- [[DivergentSeries]] — the harmonic series diverges despite shrinking terms
- [[NaturalLogarithm]] — H_n is approximated by ln(n)
- [[EulerMascheroniConstant]] — the limiting difference between H_n and ln(n)
- [[RiemannZetaFunction]] — closely related to harmonic numbers

## Contradictions
- None — reference task page.
