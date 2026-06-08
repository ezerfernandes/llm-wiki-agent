---
title: "Extreme floating point values (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, floating-point, ieee-754, numerical-computing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Extreme_floating_point_values
---

## Summary
This task asks the programmer to produce the IEEE 754 "extreme" floating point values — negative zero (-0.0, distinct from +0.0), Not-a-Number (NaN), and positive/negative infinity — using ordinary arithmetic expressions on normal floats (e.g. `1.0/0.0` for infinity, `0.0/0.0` for NaN). The key insight is that these special values arise naturally from the IEEE 754 representation and propagate through arithmetic in well-defined ways, and that languages differ in whether they let you type such literals directly versus computing them.

## Task Requirements
- Compute extreme IEEE 754 values (minus zero, NaN, plus/minus infinity, and optionally others) from expressions over normal floating point values, assigning them to variables.
- Print the values of these variables where possible.
- Demonstrate some arithmetic involving these special values and variables.
- If the language supports entering these extreme values as literals directly, show that too.

## Language Coverage
66 languages implement this task, spanning systems languages, scripting languages, and functional languages, reflecting how broadly IEEE 754 floating point is supported. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, OCaml, Fortran, and Julia.

## Connections
- [[FloatingPointArithmetic]] — the task exercises the core arithmetic behavior of floats
- [[IEEE754]] — the standard defining these special values
- [[NotANumber]] — NaN generation and its non-reflexive comparison semantics
- [[Infinity]] — positive and negative infinity from division by zero
- [[SignedZero]] — the distinction between +0.0 and -0.0

## Contradictions
- None — reference task page.
