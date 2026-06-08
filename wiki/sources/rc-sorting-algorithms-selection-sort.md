---
title: "Sorting algorithms/Selection sort (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, sorting, algorithms]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sorting_algorithms/Selection_sort
---

## Summary
This task asks the programmer to sort an array or list using the selection sort algorithm. The method repeatedly finds the smallest remaining element and swaps it into the next position, growing a sorted prefix one element at a time. Its key property is that it performs the minimum possible number of swaps (at most n-1), making it useful when writing data is far more expensive than reading it, such as with flash memory or EEPROM.

## Task Requirements
- Sort an array (or list) of elements using selection sort.
- Find the smallest element and exchange it with the element in the first position, then the second smallest with the second position, and so on until sorted.
- Understand its asymptotic complexity is O(n^2), making it inefficient on large arrays.
- Note that no other sorting algorithm performs less data movement.

## Language Coverage
107 languages implement this task, spanning systems languages, scripting languages, functional languages, and several assembly dialects. Representative examples include C, C++, Rust, Go, Java, Python, Haskell, Common Lisp, ALGOL 68, and ARM Assembly.

## Connections
- [[SelectionSort]] — the algorithm this task implements
- [[SortingAlgorithms]] — the broader family of in-place comparison sorts
- [[BigONotation]] — characterizing the O(n^2) time complexity
- [[InPlaceAlgorithm]] — selection sort minimizes data movement and sorts in place

## Contradictions
- None — reference task page.
