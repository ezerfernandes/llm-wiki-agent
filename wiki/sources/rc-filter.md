---
title: "Filter (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, higher-order-functions, collections]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Filter
---

## Summary
The task asks the programmer to select certain elements from an array into a new array in a generic way, demonstrated by picking all even numbers from an array. The key insight is the filter operation as a fundamental higher-order pattern: applying a predicate to each element and keeping only those that satisfy it.

## Task Requirements
- Select certain elements from an array into a new array, in a generic (reusable) way.
- Demonstrate by selecting all even numbers from a given array.
- Optionally provide a second solution that filters destructively, modifying the original array in place rather than allocating a new one.

## Language Coverage
187 languages implement this task, showing extremely broad coverage since filtering is a core operation in nearly every paradigm. Representative implementations include Python, Haskell, JavaScript, C++, Ruby, Clojure, Rust, APL, Scheme, and Java.

## Connections
- [[HigherOrderFunctions]] — filter takes a predicate function as an argument
- [[Predicate]] — the boolean test determining which elements are kept
- [[ListComprehension]] — a common syntactic form for expressing filters
- [[MapFilterReduce]] — filter is one of the three canonical collection operations
- [[Iteration]] — traversing the array element by element

## Contradictions
- None — reference task page.
