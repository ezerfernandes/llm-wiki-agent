---
title: "Sorting algorithms/Shell sort (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, sorting, algorithms]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sorting_algorithms/Shell_sort
---

## Summary
The task asks the programmer to sort an array using Shell sort, a diminishing-increment sort invented by Donald Shell in 1959. The key insight is that Shell sort runs a sequence of interleaved insertion sorts over progressively smaller gap sizes; once the gap reaches 1 it becomes a plain insertion sort, but by then the data is nearly sorted, hitting insertion sort's best case. The choice of gap (increment) sequence strongly affects performance.

## Task Requirements
- Implement the Shell sort algorithm to sort an array of elements.
- Use a diminishing increment sequence that reduces the gap after each pass until the gap size reaches 1.
- Any sequence ending in 1 will correctly sort, though some sequences (e.g. a geometric ratio around 2.2) perform better in practice.

## Language Coverage
92 languages implement this task, spanning systems and scripting languages plus several assembly dialects, showing very broad coverage. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Perl, Ruby, and ARM Assembly.

## Connections
- [[InsertionSort]] — Shell sort generalizes insertion sort with gaps and degenerates into it at gap 1
- [[SortingAlgorithms]] — member of the comparison-sort family
- [[IncrementSequence]] — performance hinges on the chosen gap sequence
- [[TimeComplexity]] — running time depends on the gap sequence rather than a single fixed bound

## Contradictions
- None — reference task page.
