---
title: "Display a linear combination (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, linear-algebra]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Display_a_linear_combination
---

## Summary
Given a finite list of scalars (α¹, α², …), the task is to write a function that produces a human-readable string for the linear combination Σ αⁱeᵢ in an infinite vector basis (e₁, e₂, …), formatted the way it would appear in a mathematics textbook. The core challenge is not the math but the string-formatting edge cases: suppressing zero terms, hiding coefficients of ±1, and turning leading minus signs into subtraction operators.

## Task Requirements
- Accept a finite list of scalars and emit a string representing Σ αⁱeᵢ, e.g. `e(1) + 2*e(2) + 3*e(3)`.
- Omit null (zero-coefficient) terms entirely, unless every coefficient is zero — in which case output `0`.
- Omit a coefficient when it equals 1 or -1 (show `e(3)`, never `1*e(3)`).
- Use subtraction instead of adding a negative term (`e(4) - e(5)`, never `e(4) + -e(5)`).
- Produce output for ten given test lists, including all-zero and single-element cases.

## Language Coverage
58 languages implement this task, spanning low-level assembly through high-level functional and array languages. Representative entries include C, C++, Rust, Go, Java, Python, Haskell, OCaml, F#, Julia, Perl, Raku, J, APL, and 8080 Assembly.

## Connections
- [[LinearCombination]] — the mathematical object being rendered.
- [[VectorSpace]] — basis vectors eᵢ and scalar coefficients live here.
- [[StringFormatting]] — the actual difficulty is conditional term assembly.
- [[ListProcessing]] — iterating and filtering the scalar list to build terms.

## Contradictions
- None — reference task page.
