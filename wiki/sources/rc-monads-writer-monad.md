---
title: "Monads/Writer monad (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, functional-programming, monads]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Monads/Writer_monad
---

## Summary
This task asks the programmer to implement the Writer monad, a design pattern that composes functions which each return a value paired with a log string. As composed functions run, their values flow through while their logs are accumulated by concatenation, so the final result carries both an output value and a complete trace of every step. The key insight is that `bind` threads the value forward while transparently appending each function's log, keeping the logging concern separate from the computation.

## Task Requirements
- Construct a Writer monad by implementing its `bind` function and its `unit` (a.k.a. `return`) function, or reuse what the language already provides.
- Write three simple plain functions: `root`, `addOne`, and `half`.
- Derive Writer monad versions of each of those functions (returning a value paired with a log entry).
- Apply a composition of the Writer versions of `root`, `addOne`, and `half` to the integer 5, producing both a value approximating the Golden Ratio φ and a concatenated log of the function applications, starting with the initial value.

## Language Coverage
28 languages implement this task, with broad representation across functional, multiparadigm, and imperative styles. Representative entries include Haskell, F#, Scheme, EchoLisp, Koka, J, Factor, Python, JavaScript, Kotlin, Ruby, and C++.

## Connections
- [[Monad]] — the Writer monad is one canonical instance of this abstraction.
- [[FunctionComposition]] — the task chains Writer-wrapped functions together.
- [[FunctionalProgramming]] — the pattern originates from and is idiomatic to this paradigm.
- [[GoldenRatio]] — the composed computation converges on φ from the seed value 5.

## Contradictions
- None — reference task page.
