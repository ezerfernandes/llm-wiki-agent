---
title: "Tropical algebra overloading (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, abstract-algebra, operator-overloading]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Tropical_algebra_overloading
---

## Summary
This task asks the programmer to implement the max-plus tropical semiring, where "addition" is the max function (x ⊕ y = max(x, y)) and "multiplication" is ordinary addition (x ⊗ y = x + y), over the reals augmented with negative infinity. The pedagogical point is to model this exotic algebra by overloading the host language's operators (or defining named functions where overloading is unsupported), so that familiar syntax like `+`, `*`, and `^` carries the tropical meaning.

## Task Requirements
- Define ⊕ (tropical add = max) and ⊗ (tropical multiply = real addition), either as new operators, as overloads of `+`/`*` on a custom type, or as ordinary functions like `tropicalAdd`/`tropicalMul`.
- Verify: 2 ⊗ -2 = 0; -0.001 ⊕ -Inf = -0.001; 0 ⊗ -Inf = -Inf; 1.5 ⊕ -1 = 1.5; -0.5 ⊗ 0 = -0.5.
- Note the identities: -Inf for ⊕ and 0 for ⊗.
- Define exponentiation as repeated ⊗ (so a^b = a*b for real a and positive integer b), ideally overloading `^` or an up-arrow operator; compute 5 ↑ 7.
- Demonstrate distributivity (⊗ binds tighter than ⊕): show 5 ⊗ (8 ⊕ 7) equals 5 ⊗ 8 ⊕ 5 ⊗ 7.

## Language Coverage
23 languages implement this task, spanning systems and functional languages as well as scientific and esoteric ones. Representative entries include C++, C#, Java, Rust, Go, Nim, Haskell, Julia, Python, Raku, and Wolfram Language.

## Connections
- [[TropicalSemiring]] — the algebraic structure being modeled
- [[OperatorOverloading]] — the language feature this task exercises
- [[AbstractAlgebra]] — the broader field of semirings and rings
- [[Distributivity]] — the law demonstrated for ⊗ over ⊕

## Contradictions
- None — reference task page.
