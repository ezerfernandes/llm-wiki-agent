---
title: "List comprehensions (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, list-comprehension, functional-programming]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/List_comprehensions
---

## Summary
A list comprehension is dedicated syntax in some languages for describing lists, modeled on the mathematical set-builder notation. The task asks the programmer to use this syntax — distinct from nested for-loops or map/filter calls, and yielding a list or iterator — to build all Pythagorean triples whose elements lie between 1 and n. Where a language offers multiple forms (e.g. eager comprehensions and lazy generators), each should be shown.

## Task Requirements
- Use a true list comprehension, distinct from nested for loops and from explicit map/filter functions.
- The construct must return a list or an iterator over successive members.
- Its syntax should mirror set-builder notation (generators, filters/conditions, output expression).
- Build the list of all Pythagorean triples with elements in the range 1..n.
- If the language has several such constructs (e.g. comprehensions vs. generators), provide one example each.

## Language Coverage
86 languages implement this task, spanning functional, multi-paradigm, and array languages that natively support comprehensions, plus imperative ones that emulate them. Representative entries include Python, Haskell, Erlang, Clojure, F#, Scala, Racket, JavaScript, Ruby, and Julia.

## Connections
- [[ListComprehension]] — the language construct the task showcases
- [[SetBuilderNotation]] — the mathematical notation it mirrors
- [[PythagoreanTriples]] — the concrete data the comprehension generates
- [[FunctionalProgramming]] — paradigm where comprehensions and generators originate
- [[LazyEvaluation]] — relevant to the generator/iterator variants

## Contradictions
- None — reference task page.
