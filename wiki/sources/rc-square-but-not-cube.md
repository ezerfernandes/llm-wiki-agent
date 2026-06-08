---
title: "Square but not cube (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Square_but_not_cube
---

## Summary
This task asks the programmer to find and display the first 30 positive integers that are perfect squares but not perfect cubes. The key insight is that an integer is both a square and a cube exactly when it is a perfect sixth power (since lcm(2,3) = 6), so those values must be filtered out of the sequence of squares.

## Task Requirements
- Show the first 30 positive integers that are squares but not cubes of integers.
- Optionally, also show the first 3 positive integers that are both squares and cubes (perfect sixth powers), marking them as such.

## Language Coverage
86 languages implement this task, reflecting broad coverage across systems, scripting, functional, and assembly languages. Representative implementations include C, C++, Python, Java, Haskell, Rust, Go, REXX, APL, and 8080 Assembly.

## Connections
- [[PerfectSquare]] — the base sequence being generated
- [[PerfectCube]] — the values to exclude
- [[PerfectPower]] — squares-and-cubes overlap are sixth powers
- [[NumberTheory]] — the underlying mathematical domain

## Contradictions
- None — reference task page.
