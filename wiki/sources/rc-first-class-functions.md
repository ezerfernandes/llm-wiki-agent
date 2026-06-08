---
title: "First-class functions (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, functional-programming, higher-order-functions]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/First-class_functions
---

## Summary
This task demonstrates whether a language treats functions as first-class values — meaning functions can be created at runtime, stored in data structures, passed as arguments, and returned as results, all without invoking a compiler or metaprogramming. The concrete exercise builds a collection of functions (e.g. sine, cosine, cubing) plus a parallel collection of their inverses, composes each function with its inverse, and shows that the composition is the identity (within floating-point tolerance).

## Task Requirements
- Build an ordered collection A of functions of a real number, mixing built-in functions (sine, cosine) with at least one user-defined function (cubing).
- Build a second collection B holding the inverse of each function in A (arcsine, arccosine, cube root).
- Implement function composition as a higher-order function returning a new function.
- Apply each composed function (f from A composed with its inverse from B) to a value and show the result equals the original input, within computational accuracy.

## Language Coverage
104 languages implement this task, spanning functional, object-oriented, scripting, and stack-based paradigms. Representative entries include Haskell, OCaml, Scheme, Common Lisp, Python, Ruby, JavaScript, Clojure, F#, and Rust.

## Connections
- [[FirstClassFunctions]] — the core language property being tested
- [[HigherOrderFunctions]] — passing and returning functions as values
- [[FunctionComposition]] — combining two functions into one
- [[FunctionalProgramming]] — the paradigm where this is idiomatic
- [[Closures]] — runtime-created functions that capture environment

## Contradictions
- None — reference task page.
