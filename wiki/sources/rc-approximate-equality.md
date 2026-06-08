---
title: "Approximate equality (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, floating-point, numerical-methods]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Approximate_equality
---

## Summary
The task asks the programmer to write a function that returns true when two floating point numbers are approximately equal, accounting for the fact that calculations differ across implementations (e.g. 32-bit vs 64-bit) by roughly the 8th significant digit. The key insight is that a fixed absolute tolerance is wrong: the comparison must scale with the magnitude of the operands (a relative tolerance), so that 100000000000000.01 ≈ 100000000000000.011 while 100.01 is not ≈ 100.011. Languages with a built-in (e.g. Python's `math.isclose`) may use it instead of a custom routine.

## Task Requirements
- Implement a function returning true if two floats are approximately equal.
- The comparison must allow for differences in number magnitude (relative, not purely absolute, tolerance).
- Simply rounding to a fixed number of decimals must not suffice: the function must return true for the first test pair and false for the second.
- Demonstrate results on the eight given value pairs, including sqrt(2)*sqrt(2) vs 2.0 and a value compared against 0.0.

## Language Coverage
57 languages implement this task, spanning systems, scripting, functional, and BASIC-family languages. Representative examples include C, C++, Rust, Go, Java, Haskell, OCaml, Julia, Python, Perl, Raku, and Common Lisp.

## Connections
- [[FloatingPointArithmetic]] — the underlying representation that makes exact equality unreliable
- [[RelativeTolerance]] — the magnitude-scaled comparison the task requires
- [[NumericalStability]] — broader concern this task illustrates
- [[MachineEpsilon]] — the precision limit driving the choice of tolerance

## Contradictions
- None — reference task page.
