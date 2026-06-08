---
title: "Closures/Value capture (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, closures, functional-programming]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Closures/Value_capture
---

## Summary
The task asks the programmer to build a list of ten functions (anonymous functions encouraged) where the function at index `i` returns `i` squared when called. The crux is that each closure must capture the *value* of the loop variable at creation time rather than a shared mutable reference; otherwise every function would see the final loop value when later invoked. This exposes the difference between value capture and reference capture across languages.

## Task Requirements
- Create a list of ten functions in the simplest way possible.
- The function at index `i` (starting from 0 or 1) must return `i` squared when run.
- Run any function except the last and display its result, proving each one remembers its own captured value.
- Demonstrate independent closures from a shared template, each holding a separate copy of the closed-over variable.

## Language Coverage
96 languages implement this task. Coverage is broad, spanning functional languages where closures are idiomatic, imperative languages that must work around shared loop variables, and Lisp dialects; representative examples include Haskell, Scheme, Common Lisp, Python, JavaScript, Ruby, Rust, Swift, Go, and OCaml.

## Connections
- [[Closure]] — the core concept being exercised
- [[FunctionalProgramming]] — anonymous functions and first-class function values
- [[VariableScope]] — value capture versus reference capture and binding lifetime
- [[HigherOrderFunctions]] — functions stored in and returned from collections

## Contradictions
- None — reference task page.
