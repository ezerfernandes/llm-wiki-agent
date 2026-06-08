---
title: "Loops/Nested (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, control-flow, iteration]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Loops/Nested
---

## Summary
This task asks the programmer to write a nested loop that scans a two-dimensional array of random integers drawn uniformly from 1 to 20, printing each element as it iterates over rows and columns. The scan stops as soon as the value 20 is encountered. The key insight is demonstrating how to break cleanly out of *both* loop levels at once, which many languages handle differently (labeled breaks, flags, exceptions, or early returns).

## Task Requirements
- Build a two-dimensional array filled with random numbers uniformly distributed over [1, 20].
- Use a nested loop (rows × columns) to traverse the array, printing each element visited.
- Terminate the entire search the moment the value 20 is found.
- Show idiomatic technique for breaking out of nested loops, not just the inner one.

## Language Coverage
143 languages implement this task, reflecting that nested iteration and multi-level break are near-universal control-flow primitives. Representative implementations span systems languages (C, C++, Rust, Go, Zig), JVM languages (Java, Kotlin, Scala, Clojure), scripting languages (Python, Ruby, Perl, Lua, JavaScript), functional languages (Haskell, OCaml, F#, Racket), and many BASIC dialects.

## Connections
- [[ControlFlow]] — nested loops are a core control-flow construct.
- [[Iteration]] — the task is categorized under iteration patterns.
- [[BreakStatement]] — central challenge is breaking out of multiple loop levels.
- [[TwoDimensionalArray]] — the data structure being traversed.
- [[RandomNumberGeneration]] — array is populated with uniform random values.

## Contradictions
- None — reference task page.
