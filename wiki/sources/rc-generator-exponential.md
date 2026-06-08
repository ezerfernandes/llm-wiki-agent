---
title: "Generator/Exponential (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, generators, lazy-evaluation, coroutines]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Generator/Exponential
---

## Summary
This task demonstrates generators — executable entities that yield a sequence of values one at a time, holding internal state between calls so the next value is produced on demand. The key insight is composability over potentially infinite sequences: build a generator of m'th powers, instantiate it for squares and cubes, then compose those two generators into a third that lazily filters all cubes out of the squares. Generators let this run without any stated upper bound, limited only by integer size or time.

## Task Requirements
- Create a function returning a generator of the m'th powers of the positive integers starting from zero, in order, with no explicit upper limit (bounds should come only from the language's natural integer size or compute limits).
- Use it to instantiate a generator of squares and a generator of cubes.
- Create a new generator that filters all cubes out of the generator of squares.
- Drop the first 20 values from this filtered generator, then show the next 10 values.
- The use of generators in computing the result is mandatory.

## Language Coverage
69 languages implement this task, spanning languages with native generator/coroutine support and those that emulate them via closures or lazy lists. Representative implementations include Python, Haskell, JavaScript, C#, Ruby, Racket, Go, Julia, Rust, and Common Lisp.

## Connections
- [[Generators]] — the central abstraction this task exercises
- [[LazyEvaluation]] — values produced on demand from a potentially infinite sequence
- [[Coroutines]] — a common substrate for implementing stateful generators
- [[HigherOrderFunctions]] — composing one generator (filter) on top of others
- [[Iterators]] — the closely related interface for stepwise sequence consumption

## Contradictions
- None — reference task page.
