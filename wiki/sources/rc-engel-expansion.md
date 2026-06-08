---
title: "Engel expansion (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, rational-numbers, series]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Engel_expansion
---

## Summary
The task asks the programmer to compute the Engel expansion of a positive real number: the unique non-decreasing sequence of positive integers whose successive reciprocal cumulative products sum to the number. The key insight is that rational numbers yield finite expansions while irrationals yield infinite ones, and tiny rounding errors compound dramatically in the later (rapidly growing) terms, making numerical precision the central challenge.

## Task Requirements
- Write a routine to convert a rational number into its Engel expansion (sequence of integers).
- Write the inverse routine to reconstruct a rational number from an Engel expansion.
- Demonstrate the round trip on rational approximations of 𝜋, 𝑒, and √2.
- Stretch goal: repeat using high-precision rational arithmetic, limiting display to the first ~30 terms.

## Language Coverage
24 languages implement this task, spanning systems, scripting, functional, and array/math-oriented styles. Representative entries include C++, C#, Java, JavaScript, Python, Rust, Perl, Raku, Julia, J, and Wren.

## Connections
- [[EngelExpansion]] — the named series representation this task defines.
- [[RationalNumbers]] — exact arithmetic needed for correct finite expansions.
- [[ArbitraryPrecisionArithmetic]] — required for the high-precision stretch goal.
- [[NumberTheory]] — the broader field of integer-sequence representations of reals.

## Contradictions
- None — reference task page.
