---
title: "Monads/Maybe monad (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, functional-programming, type-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Monads/Maybe_monad
---

## Summary
This task asks the programmer to implement the Maybe monad, a structure that encapsulates the possibility of an undefined or missing value. The core work is defining two operations: `unit` (also called `return`), which wraps a plain value into the monad, and `bind`, which chains monadic computations while short-circuiting on the absent (Nothing) case. The key insight is that `bind` propagates failure automatically, eliminating repetitive null/undefined checks when composing functions.

## Task Requirements
- Construct a Maybe monad by writing its `bind` function and `unit`/`return` function (or reuse a built-in implementation).
- Define two functions that each take a number and return a monadic number, e.g. `Int -> Maybe Int` and `Int -> Maybe String`.
- Compose the two functions using `bind`.

## Language Coverage
38 languages implement this task, spanning functional, object-oriented, and procedural styles. Representative entries include Haskell, F#, OCaml, Clojure, Racket, Scala-adjacent Kotlin, plus Python, JavaScript, C++, Rust, and Swift.

## Connections
- [[Monad]] — the general functional-programming abstraction this task instantiates
- [[OptionType]] — the Maybe/Option pattern for representing optional values
- [[FunctionComposition]] — bind chains computations together
- [[TypeTheory]] — monads formalize sequencing of typed computations
- [[NullHandling]] — Maybe is a type-safe alternative to null references

## Contradictions
- None — reference task page.
