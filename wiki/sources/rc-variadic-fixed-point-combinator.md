---
title: "Variadic fixed-point combinator (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, functional-programming, recursion, higher-order-functions]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Variadic_fixed-point_combinator
---

## Summary
A fixed-point combinator is a higher-order function `fix` that returns the fixed point of its argument, satisfying `fix f = f (fix f)`. This task generalizes the idea to a system of n mutually-referencing functions: implement a variadic combinator `fix*` that takes functions f1..fn and returns the n simultaneous fixed points, where each result may depend on all the others. The key insight is that this enables mutual recursion (e.g. mutually recursive `even`/`odd`) to be expressed without explicit recursion, ideally built atop a plain fixed-point combinator like the Y combinator.

## Task Requirements
- Implement a variadic fixed-point combinator `fix*` that accepts an arbitrary number of functions f1..fn and returns all of their simultaneous fixed points.
- Each fixed point is defined so that `fix_{i,n} f1..fn = f_i (fix_{1,n} f1..fn) .. (fix_{n,n} f1..fn)`, allowing each function to reference every fixed point.
- The variadic input and output may be represented with any language feature (e.g. lists or tuples).
- Prefer avoiding explicit recursion: derive the variadic combinator from a fixed-point combinator such as the Y combinator.
- Provide an example demonstrating a genuinely useful application (e.g. a set of mutually recursive functions).

## Language Coverage
15 languages implement this task, spanning lambda-calculus dialects and mainstream functional and imperative languages. Representative entries include Haskell, F#, Julia, Python, Perl, Raku, Java, Wren, Phix, and the esoteric Binary Lambda Calculus and Bruijn.

## Connections
- [[YCombinator]] — the canonical fixed-point combinator this task extends
- [[FixedPointCombinator]] — the underlying concept being generalized
- [[MutualRecursion]] — the primary use case enabled by simultaneous fixed points
- [[HigherOrderFunctions]] — combinators take and return functions
- [[LambdaCalculus]] — the theoretical setting for fixed-point combinators

## Contradictions
- None — reference task page.
