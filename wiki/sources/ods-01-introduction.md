---
title: "ODS Ch.1: Introduction"
type: source
tags: [book, data-structures, algorithms, foundations]
date: 2026-05-10
source_file: raw/ods-python.pdf
book: "Open Data Structures (in pseudocode)"
author: "Pat Morin"
chapter: 1
pages: "1-30"
---

## Summary
Motivates the need for efficient data structures: a million-item dataset queried a million times naïvely takes ~1000s on a billion-ops/sec computer; carefully organized data lets a single search inspect on average two items, taking 2 ns even on billion-item structures. Introduces the book's core distinction between **interface** (what a data structure does — Queue, Stack, Deque, List, USet, SSet) and **implementation** (how it does it). Reviews mathematical background: exponentials, base-2 logarithms, factorials, Stirling's approximation, big-O notation, expected values, indicator random variables, and linearity of expectation. Defines the **w-bit word-RAM model** as the cost framework used throughout the book.

## Key Claims
- **Interfaces vs. implementations.** A Queue/Stack/Deque is defined by operations and queueing discipline (FIFO, priority, LIFO); a List adds get/set/add/remove at index; a USet is an unordered set with size/add/remove/find; an SSet adds total ordering and successor search.
- **The List interface subsumes Stack/Queue/Deque.** add_first/last and remove_first/last are sugar for add(0,x), add(size(),x), remove(0), remove(size()-1).
- **Always prefer USet over SSet unless successor search is needed** — SSet operations are typically Θ(log n) while USet operations are O(1) expected via [[ods-05-hash-tables|hashing]].
- **Big-O lets us compare algorithms above the constant-factor noise.** O(a) ⊂ O(log n) ⊂ O(n^b) ⊂ O(c^n) for constants a, b > 0, c > 1.
- **Indicator random variables + linearity of expectation** are the fundamental analysis tool for randomized structures used in [[ods-04-skiplists]] and [[ods-07-random-binary-search-trees]].
- **Word-RAM cost model.** Constant-time operations on w-bit words including `+ − × / mod`, comparisons, bitwise ops, and array indexing. All asymptotic claims in the book are in this model.

## Key Quotes
> "An interface describes what a data structure does, while an implementation describes how the data structure does it."
> "When choosing which of these structures to use, one should always use a USet unless the extra functionality offered by an SSet is truly needed."

## Connections
- [[ods-02-array-based-lists]] / [[ods-03-linked-lists]] — implement the List interface.
- [[ods-05-hash-tables]] — USet implementation.
- [[ods-06-binary-trees]] / [[ods-07-random-binary-search-trees]] / [[ods-08-scapegoat-trees]] / [[ods-09-red-black-trees]] / [[ods-13-data-structures-for-integers]] — SSet implementations.
- [[ods-10-heaps]] — priority Queue implementation.
- [[ods-11-sorting-algorithms]] — uses BinaryHeap and random binary search tree analysis.
- [[binomial-coefficient]] — used in expected-value derivations.
- [[factorial]] / [[logarithms]] / [[powers]] — mathematical primitives reviewed here.

## Contradictions
None.
