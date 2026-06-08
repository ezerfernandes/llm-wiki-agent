---
title: "Odd and square numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Odd_and_square_numbers
---

## Summary
This task asks the programmer to find and list all numbers greater than 99 and less than 1000 that are simultaneously odd and perfect squares. The key insight is that a perfect square is odd exactly when its integer root is odd, so the solution reduces to squaring odd integers whose squares fall within the bounded range (121, 169, 225, ... up to 961).

## Task Requirements
- Find all numbers greater than 99 and under 1000.
- Each number must be both odd and a perfect square.
- Output the matching numbers.

## Language Coverage
77 languages implement this task, spanning a very broad mix from modern high-level languages to assembly and historic dialects. Representative implementations include Python, Haskell, Rust, Go, Java, C++, Perl, Ruby, Fortran, and 8080 Assembly.

## Connections
- [[PerfectSquare]] — the task filters for perfect squares within a range.
- [[NumberTheory]] — concerns properties (parity, squareness) of integers.
- [[Parity]] — selects odd numbers, equivalently odd-rooted squares.
- [[IntegerSquareRoot]] — squareness testing relies on integer roots.

## Contradictions
- None — reference task page.
