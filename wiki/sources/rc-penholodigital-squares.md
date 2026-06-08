---
title: "Penholodigital squares (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, combinatorics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Penholodigital_squares
---

## Summary
A penholodigital square is a perfect square whose representation in a given base contains every nonzero digit of that base ("1 through base-1") exactly once. For example, in base 10 the number 139854276 = 11826² uses each digit 1-9 once. The key insight is that such squares are constrained to a known digit-count, so candidate integers can be enumerated within a bounded range and tested via a digit-frequency check.

## Task Requirements
- Define a penholodigital square: a perfect square containing all nonzero digits of its base exactly once.
- For bases 9, 10, 11, and 12, find and display the total count of penholodigital squares, plus each square and the integer that was squared, all expressed in that base.
- Stretch: for bases 13, 14, 15, and beyond, display the total count and the first and last penholodigital squares (with their square roots) in each base.

## Language Coverage
21 languages implement this task, spanning systems, scripting, functional, and array languages. Representative implementations include C++, Go, Java, Python, Julia, Perl, Raku, Nim, J, jq, and Wren.

## Connections
- [[PerfectSquares]] — the task hunts perfect squares satisfying a digit constraint.
- [[NumberBases]] — penholodigitality is defined relative to an arbitrary radix.
- [[Pandigitalism]] — closely related to pandigital numbers, omitting only the zero digit.
- [[DigitFrequencyCounting]] — the core test counts each base digit's occurrences.
- [[BruteForceSearch]] — solutions enumerate candidate integers within a bounded range.

## Contradictions
- None — reference task page.
