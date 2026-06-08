---
title: "Order by pair comparisons (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, sorting, comparison-sort, interactive]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Order_by_pair_comparisons
---

## Summary
Given a set of items whose order is known only to the user, write a function that interactively asks the user to compare two items at a time (reporting less-than, equal-to, or greater-than) and uses those answers to return the items fully sorted. The key constraint is to minimise the number of comparison questions asked, which makes this a comparison-sort problem where the comparator is the human rather than a fixed predicate.

## Task Requirements
- Implement a function that, given an unordered set of items, asks the user to compare pairs of items and sorts them based on the responses.
- Each comparison query returns whether one item is less than, equal to, or greater than another.
- Soliciting and receiving the user's comparison answers is an explicit part of the task (no built-in ordering may be assumed).
- Inputs must not encode any pre-existing order.
- Minimise the number of comparison questions (e.g., the seven rainbow colours form twenty-one possible pairs, but a good routine asks far fewer).
- Demonstrate by ordering the rainbow colours `violet red green indigo blue yellow orange` into `red orange yellow green blue indigo violet`.

## Language Coverage
36 languages implement this task, spanning systems, functional, scripting, and BASIC-family languages. Representative implementations include C, C++, Go, Rust-adjacent Crystal, Haskell, OCaml, F#, Julia, Python, Ruby, Perl, Raku, Prolog, and Wren.

## Connections
- [[SortingAlgorithm]] — the task is fundamentally an interactive sort.
- [[ComparisonSort]] — the human acts as the comparator function.
- [[InsertionSort]] — a common minimal-comparison strategy used in solutions.
- [[BinarySearch]] — inserting each item via binary search reduces the number of questions asked.

## Contradictions
- None — reference task page.
