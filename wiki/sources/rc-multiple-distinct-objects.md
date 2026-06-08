---
title: "Multiple distinct objects (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, memory-management, object-oriented]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Multiple_distinct_objects
---

## Summary
The task asks the programmer to build a sequence (array, list, etc.) of `n` distinct, fully initialized items of the same type, where `n` is determined at runtime. The crucial insight is that the items must be independent: mutating one must not affect the others, ruling out the common mistake of filling a collection with `n` references to a single shared mutable object. It is most relevant to pass-references-by-value languages (object-oriented, garbage-collected, or dynamic).

## Task Requirements
- Create a sequence of `n` items of the same type, with `n` decided at runtime.
- Items must be distinct: changes to one do not propagate to others, and they compare unequal under any appropriate equality operator.
- Items must be properly initialized to a well-defined state for their type, not merely zero-filled (unless the type meaningfully defines a "zero").
- Avoid numeric-range generators that do not generalize to arbitrary types.
- Optionally demonstrate the negative example: creating `n` references to the same mutable object, and when that is actually the desired behavior.

## Language Coverage
77 languages implement this task, spanning a broad mix of object-oriented, functional, dynamic, and low-level systems languages. Representative examples include Python, Java, C++, C#, Ruby, Haskell, Rust, Go, JavaScript, and Common Lisp.

## Connections
- [[ObjectOrientedProgramming]] — distinctness matters most for mutable reference types
- [[ReferenceSemantics]] — the task hinges on value-vs-reference copying behavior
- [[MemoryManagement]] — allocation and initialization of independent instances
- [[Closures]] — see also Closures/Value capture, a closely related pitfall

## Contradictions
- None — reference task page.
