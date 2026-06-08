---
title: "Magic constant (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, sequences]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Magic_constant
---

## Summary
The task asks the programmer to compute the magic constant of an N x N magic square — the value to which every row, column, and main diagonal must sum. The key insight is that this value depends only on the order N via the closed form M(N) = N(N² + 1) / 2, so no actual square need be constructed. The sequence conventionally begins at order 3, skipping the trivial orders 0 and 1 and the impossible order 2.

## Task Requirements
- Starting at order 3, show the first 20 magic constants.
- Show the 1000th magic constant (which corresponds to order 1003).
- Find and show the order of the smallest N x N magic square whose constant exceeds each of 10¹ through 10¹⁰.
- Stretch: extend the threshold search to constants greater than 10¹¹ through 10²⁰ (requiring big-integer arithmetic).

## Language Coverage
43 languages implement this task, spanning systems languages, scripting languages, and array/functional languages. Representative examples include C, C++, C#, Go, Java, Python, Perl, Raku, Julia, J, and Wren.

## Connections
- [[MagicSquare]] — the combinatorial object whose row/column/diagonal sum this constant defines
- [[NumberTheory]] — the closed-form formula is a straightforward integer arithmetic identity
- [[IntegerSequence]] — the constants form an OEIS sequence (related to A006003)
- [[BigInteger]] — the stretch goal's 10²⁰ thresholds require arbitrary-precision arithmetic

## Contradictions
- None — reference task page.
