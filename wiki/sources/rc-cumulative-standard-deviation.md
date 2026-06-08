---
title: "Cumulative standard deviation (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, statistics, stateful-functions]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Cumulative_standard_deviation
---

## Summary
This task asks for a stateful construct (function, class, generator, or coroutine) that accepts floating-point numbers one at a time and returns the running standard deviation of the series seen so far. The key constraint is that the result must be the population standard deviation (no Bessel's correction), so the running sample is always treated as the entire population. It exists to showcase each language's most natural idiom for maintaining state across successive calls.

## Task Requirements
- Implement a stateful function/class/generator/coroutine that takes one floating-point number per invocation.
- Return the running standard deviation of all numbers received so far.
- Use the most natural stateful style for the implementation language, and state which style is used.
- Do not apply Bessel's correction — compute as population standard deviation, not sample.
- Test case: feed the set {2, 4, 4, 4, 5, 5, 7, 9}; the final standard deviation must equal 2.

## Language Coverage
97 languages implement this task, spanning imperative, functional, and object-oriented paradigms with their differing approaches to retaining state. Representative implementations include C, C++, C#, Java, Python, JavaScript, Haskell, OCaml, Common Lisp, Ruby, Rust, and Go.

## Connections
- [[StandardDeviation]] — the statistical measure being computed
- [[Variance]] — standard deviation is the square root of variance
- [[Statefulness]] — the task centers on retaining accumulated state between calls
- [[Closures]] — a common idiom for encapsulating running totals in functional languages
- [[Generators]] — coroutine/generator style is one of the listed natural implementations

## Contradictions
- None — reference task page.
