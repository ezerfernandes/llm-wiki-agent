---
title: "Taxicab numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Taxicab_numbers
---

## Summary
A taxicab number is a positive integer expressible as the sum of two positive cubes in more than one way. The canonical example is 1729 = 1³ + 12³ = 9³ + 10³, famously called the Hardy–Ramanujan number. The task is to generate these numbers in order along with the cube pairs that produce them. The key insight is that searching over pairs (a, b) with a ≤ b and bucketing their cube sums lets you detect any sum that arises from two or more distinct pairs.

## Task Requirements
- Compute and display the lowest 25 taxicab numbers in numeric order, in a human-readable format.
- For each taxicab number, show the number itself plus its constituent cube pairs.
- Extra credit: show the 2,000th taxicab number plus roughly a half dozen more beyond it.

## Language Coverage
55 languages implement this task, spanning systems, scripting, functional, and array languages. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, J, Julia, Perl, Raku, and REXX.

## Connections
- [[NumberTheory]] — taxicab numbers are a classic integer-sequence problem
- [[SumOfTwoCubes]] — the defining decomposition each number must admit twice
- [[HardyRamanujanNumber]] — 1729, the first and namesake taxicab number
- [[OEIS]] — catalogued as sequence A001235
- [[HashMap]] — typical solutions bucket cube sums in a map keyed by sum

## Contradictions
- None — reference task page.
