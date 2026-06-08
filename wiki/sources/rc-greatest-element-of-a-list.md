---
title: "Greatest element of a list (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, reduction]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Greatest_element_of_a_list
---

## Summary
This task asks the programmer to write a function that returns the maximum value from an arbitrary set of values, where the count of values is not known until run time. The key insight is that this is a classic fold/reduction over a variable-length collection, often expressible with a built-in `max` over a list or via variadic arguments.

## Task Requirements
- Create a function that returns the maximum value in a provided set of values.
- The number of values may not be known until run-time (i.e. handle a variable-length collection or variadic input).

## Language Coverage
228 languages implement this task, making it one of the most broadly covered entries on the site, spanning everything from assembly to high-level functional languages. Representative implementations include Python, Haskell, C, Java, JavaScript, Ruby, Rust, Common Lisp, APL, and Go.

## Connections
- [[Reduction]] — finding a maximum is a fold/reduce over the collection
- [[Maximum]] — the core operation the task computes
- [[VariadicFunction]] — handling an unknown number of arguments at run-time
- [[ListProcessing]] — operating over an arbitrary-length sequence

## Contradictions
- None — reference task page.
