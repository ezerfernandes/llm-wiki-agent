---
title: "Partial function application (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, functional-programming, higher-order-functions]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Partial_function_application
---

## Summary
The task explores partial function application: taking a multi-parameter function and fixing some of its arguments to produce a new function that only needs the remaining arguments. The key distinction the task draws is that partially applying a parameter must not explicitly mention the other parameters (though introspecting the target function's signature is allowed), which separates true partial application from merely wrapping a function in a closure.

## Task Requirements
- Create a function `fs(f, s)` that takes a function `f(n)` of one value and a sequence `s`, returning the ordered results of applying `f` to each element of `s`.
- Create `f1` that returns its argument multiplied by 2, and `f2` that returns its argument squared.
- Partially apply `f1` to `fs` to form `fsf1(s)`, and `f2` to `fs` to form `fsf2(s)`.
- Test both with `s` = integers 0 to 3 inclusive, and even integers 2 to 8 inclusive.
- The partial application must avoid explicit mention of the other parameters of `fs`.

## Language Coverage
70 languages implement this task, spanning functional languages where partial application is idiomatic and imperative languages that simulate it with closures or binders. Representative examples include Haskell, OCaml, F#, Scala, Clojure, Common Lisp, Python, JavaScript, C++, and Racket.

## Connections
- [[PartialApplication]] — the core technique the task demonstrates
- [[Currying]] — closely related transformation of multi-argument functions
- [[HigherOrderFunction]] — `fs` takes a function as a parameter
- [[Closure]] — common implementation mechanism for capturing fixed arguments
- [[FunctionalProgramming]] — the paradigm where this idiom originates

## Contradictions
- None — reference task page.
