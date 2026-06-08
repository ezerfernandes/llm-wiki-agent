---
title: "Triangular numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, combinatorics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Triangular_numbers
---

## Summary
A triangular number counts objects arranged in an equilateral triangle; the nth is the sum of the first n positive integers, given explicitly by n(n+1)/2, which equals the binomial coefficient "n+1 choose 2". The task generalizes this to higher dimensions — tetrahedral (r=3), pentatopic (r=4), and arbitrary r-simplex numbers — all unified by the single binomial formula (n+r-1 choose r). The key insight is that figurate/simplex numbers of any dimension are just binomial coefficients, and each has an invertible real "root" formula (e.g. the triangular root (√(8x+1)−1)/2) that tests membership.

## Task Requirements
- Display the first 30 triangular numbers (r = 2).
- Display the first 30 tetrahedral numbers (r = 3).
- Display the first 30 pentatopic numbers (r = 4).
- Display the first 30 12-simplex numbers (r = 12).
- Compute the triangular, tetrahedral, and pentatopic roots of the integers 7140, 21408696, 26728085384, and 14545501785001.

## Language Coverage
23 languages implement this task, a moderate spread of mathematical and general-purpose languages. Representative entries include Python, Go, Java, Julia, Perl, Raku, R, Mathematica/Wolfram Language, Maxima, PARI/GP, J, jq, and ALGOL 68.

## Connections
- [[BinomialCoefficient]] — every r-simplex number is the binomial (n+r−1 choose r)
- [[FigurateNumbers]] — the general class these numbers belong to
- [[TriangularNumber]] — the base r=2 case driving the task
- [[NumberTheory]] — integer roots determine membership in each figurate sequence
- [[PascalsTriangle]] — the binomial coefficients arrange directly into Pascal's triangle

## Contradictions
- None — reference task page.
