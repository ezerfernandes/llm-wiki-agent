---
title: "Safe addition (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, floating-point, interval-arithmetic, numerical-analysis]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Safe_addition
---

## Summary
The task asks the programmer to implement directed-rounding addition operators — a downward-rounding `+↓` and an upward-rounding `+↑` — such that `a +↓ b ≤ a + b ≤ a +↑ b`. These form the basis of interval arithmetic, where each operation returns an interval guaranteed to contain the exact mathematical result rather than a single (possibly inaccurate) floating-point value. The key insight is trading precision for accuracy: the result is wider but provably encloses the true answer, ideally within one machine epsilon of width.

## Task Requirements
- Show how `+↓` (round toward negative infinity) and `+↑` (round toward positive infinity) can be implemented using the language's standard floating-point type.
- Define an interval type based on the standard floating-point type.
- Implement interval-valued addition of two floats treated as exact, yielding the interval `[a +↓ b, a +↑ b]`.
- The interval width should be on the order of machine epsilon (after removing the exponent part).

## Language Coverage
31 languages implement this task, spanning systems languages, functional languages, and scripting languages. Representative implementations include Ada, C, C++, D, Go, Java, Julia, Python, Perl, Raku, Racket, and Wren — many relying on FPU rounding-mode control or `nextafter`-style nudging to construct the bounds.

## Connections
- [[IntervalArithmetic]] — the technique this task underpins
- [[FloatingPointArithmetic]] — directed rounding modes and machine epsilon
- [[NumericalAnalysis]] — accurate-but-imprecise enclosure of exact results
- [[FuzzyNumbers]] — generalization mentioned as a motivating use case

## Contradictions
- None — reference task page.
