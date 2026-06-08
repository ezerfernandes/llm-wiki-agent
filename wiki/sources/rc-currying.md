---
title: "Currying (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, functional-programming, higher-order-functions]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Currying
---

## Summary
This task asks the programmer to write a simple, demonstrative example of currying in their chosen language, and to note any historical detail about how the feature entered that language. Currying transforms a function taking multiple arguments into a chain of functions that each take a single argument, so that supplying fewer arguments than the original arity yields a new specialized function (partial application). The key insight is that this is trivial in languages with first-class functions and closures, but requires explicit machinery in languages without them.

## Task Requirements
- Create a simple demonstrative example of currying in a specific language.
- Add any historic details as to how the feature made its way into the language.

## Language Coverage
89 languages implement this task, reflecting broad cross-paradigm interest because currying is central to functional programming yet expressible almost anywhere with closures. Representative implementations include Haskell, OCaml, Standard ML, F#, Scala, Clojure, JavaScript, Python, Ruby, and C++.

## Connections
- [[FunctionalProgramming]] — currying is a foundational idea in this paradigm
- [[HigherOrderFunctions]] — currying both produces and consumes functions as values
- [[Closures]] — capturing the first argument in a returned function is how most languages implement it
- [[PartialApplication]] — the practical effect of supplying fewer than all arguments
- [[LambdaCalculus]] — currying is the standard way to model multi-argument functions in this formalism

## Contradictions
- None — reference task page.
