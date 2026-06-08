---
title: "First-class functions/Use numbers analogously (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, higher-order-functions, closures]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/First-class_functions/Use_numbers_analogously
---

## Summary
This task is a deliberate parallel to the original First-class functions task, asking the programmer to perform the same manipulations on plain numbers instead of functions, so the two solutions can be compared side by side. The key insight is that a language treating functions as first-class values should let function code look structurally close to the equivalent number-handling code. The exercise centers on a `multiplier` function that returns a closure capturing two factors.

## Task Requirements
- Build an ordered collection mixing literal real numbers and numbers produced by expressions (x = 2.0, y = 4.0, z = x + y), and a second ordered collection of their multiplicative inverses (xi = 0.5, yi = 0.25, zi = 1/(x+y)).
- Define a function `multiplier(n1, n2)` that returns a new function; calling that returned function with argument `m` yields `n1 * n2 * m`.
- Pair each number with its inverse across the two collections, apply the resulting multiplier function, and show each result equals one.
- Compare and contrast the program with the corresponding First-class functions entry; they should be close.

## Language Coverage
63 languages implement this task, spanning functional, object-oriented, scripting, and array languages. Representative entries include Haskell, OCaml, Scheme, Common Lisp, Python, Ruby, JavaScript, Clojure, Rust, and J.

## Connections
- [[FirstClassFunctions]] — the companion task this one mirrors with numbers
- [[Closures]] — `multiplier` returns a function capturing its two arguments
- [[HigherOrderFunctions]] — a function that returns another function
- [[MultiplicativeInverse]] — each number paired with its reciprocal yields one

## Contradictions
- None — reference task page.
