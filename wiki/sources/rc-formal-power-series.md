---
title: "Formal power series (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, lazy-evaluation, numeric-types]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Formal_power_series
---

## Summary
The task asks the programmer to implement formal power series — infinite sums of the form a₀ + a₁x + a₂x² + ... treated as an abstract numeric type without regard to convergence — supporting addition, multiplication, division, differentiation, and integration (integration constant zero). The central challenge is handling a potentially infinite sequence of coefficients, which naturally pushes toward lazy or delayed evaluation. The canonical demonstration defines sine and cosine mutually recursively via integration (sin x = ∫cos, cos x = 1 − ∫sin).

## Task Requirements
- Implement formal power series as a numeric type whose coefficients follow the usual arithmetic rules.
- Support at least addition, multiplication, and division of series.
- Support the non-numeric operations differentiation and integration (with integration constant of zero).
- Cope with the potentially infinite number of coefficients.
- As a demonstration, define the sine and cosine series in terms of each other using integration.
- Goal: showcase how the language handles new numeric types and lazy/delayed evaluation.

## Language Coverage
31 languages implement this task, spanning functional, lazy, and imperative paradigms — the problem is a favorite stress test for lazy evaluation. Representative entries include Haskell, Scheme, Common Lisp, Clojure, Racket, J, Python, Julia, Go, and Wren.

## Connections
- [[LazyEvaluation]] — infinite coefficient streams require delayed/on-demand computation
- [[PowerSeries]] — the underlying mathematical object being modeled
- [[OperatorOverloading]] — defining arithmetic on a custom numeric type
- [[Corecursion]] — sine and cosine defined mutually via integration over infinite streams
- [[SymbolicDifferentiation]] — coefficient-wise differentiation and integration of the series

## Contradictions
- None — reference task page.
