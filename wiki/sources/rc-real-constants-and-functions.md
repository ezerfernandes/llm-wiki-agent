---
title: "Real constants and functions (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, mathematics, floating-point]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Real_constants_and_functions
---

## Summary
A basic language-learning task that asks the programmer to demonstrate access to a standard set of real-valued (floating-point) mathematical constants and functions in their language, noting any that are unavailable. The exercise surveys how each language exposes its math library, with care taken to distinguish similar-but-distinct operations (e.g. floor versus truncate, ceiling versus round-up).

## Task Requirements
- Constant `e` — base of the natural logarithm.
- Constant `pi` (π).
- Square root.
- Logarithm — any base is acceptable.
- Exponential — `e^x`.
- Absolute value (magnitude).
- Floor — largest integer ≤ the number (not the same as truncate or int).
- Ceiling — smallest integer ≥ the number (not the same as round-up).
- Power — `x^y`.
- Note explicitly any function or constant the language does not provide.

## Language Coverage
132 languages implement this task, reflecting that nearly every general-purpose language ships these primitives in a standard math library. Representative implementations include C, Python, Java, Haskell, Ada, Fortran, Common Lisp, Perl, Rust, and Scheme.

## Connections
- [[FloatingPointArithmetic]] — the constants and functions operate on real numbers
- [[StandardLibrary]] — these primitives live in each language's math module
- [[Logarithm]] — natural and arbitrary-base logarithms
- [[Exponentiation]] — power and exponential functions
- [[RoundingModes]] — floor and ceiling versus truncate and round

## Contradictions
- None — reference task page.
