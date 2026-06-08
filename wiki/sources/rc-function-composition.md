---
title: "Function composition (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, functional-programming, higher-order-functions]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Function_composition
---

## Summary
The task asks the programmer to write a higher-order function `compose` that takes two one-argument functions `f` and `g` and returns a new one-argument function which applies `g` first and then `f` to the result, i.e. `compose(f, g)(x) = f(g(x))`. The key insight is that in many languages a correct implementation requires capturing `f` and `g` in a closure so the returned function remembers them.

## Task Requirements
- Define `compose` taking two arguments `f` and `g`, both functions of one argument.
- The result must itself be a function of one argument `x`.
- That result function must compute `f(g(x))` — apply `g` to `x`, then apply `f` to the output.
- Where the language has no first-class functions, implementing `compose` correctly may require building a closure.

## Language Coverage
144 languages implement this task, showing very broad coverage since function composition is a foundational functional-programming idiom. Representative examples include Haskell, OCaml, Standard ML, Scheme, Common Lisp, Python, JavaScript, Clojure, Rust, and Erlang.

## Connections
- [[HigherOrderFunctions]] — `compose` takes functions as arguments and returns a function.
- [[Closure]] — capturing `f` and `g` for the returned function typically needs a closure.
- [[FunctionalProgramming]] — composition is a core idiom of the functional paradigm.
- [[FirstClassFunctions]] — the task presupposes functions can be passed and returned as values.

## Contradictions
- None — reference task page.
