---
title: "Monads/List monad (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, functional-programming, monads]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Monads/List_monad
---

## Summary
This task asks the programmer to implement the List monad: a list data type paired with two helper functions, `pure` (a.k.a. `return`/`unit`, mathematically eta) and `bind` (mathematically mu/flatMap). The key insight is that `bind` for lists is the composition of `concat` and `map`, so chaining two list-returning computations produces a Cartesian product — and returning an empty list signals failure, which also enables filtering alongside mapping.

## Task Requirements
- Construct a List monad by writing its `bind` function and `pure`/`return` function (or use the language's built-in equivalent).
- Define two functions that each take a number and return a monadic value, e.g. `Int -> List Int` and `Int -> List String`.
- Compose those two functions together using `bind`.

## Language Coverage
32 languages implement this task, spanning functional, imperative, and array-oriented styles. Representative examples include Haskell, F#, OCaml, Clojure, Racket, and Raku among the functional languages, plus Python, JavaScript, Java, Go, Ruby, and J.

## Connections
- [[Monad]] — the abstraction this task demonstrates concretely
- [[FunctionalProgramming]] — the paradigm in which monads originate
- [[ListComprehension]] — desugars to the same concat-map (bind) over lists
- [[CartesianProduct]] — what chaining two list-monad computations yields
- [[FunctionComposition]] — bind is used to compose the two monadic functions

## Contradictions
- None — reference task page.
