---
title: "Sorting algorithms/Gnome sort (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, sorting, algorithms]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sorting_algorithms/Gnome_sort
---

## Summary
The task asks the programmer to implement gnome sort to order an array or list of numbers. Gnome sort is a simple comparison sort akin to insertion sort, but it relocates an out-of-place element through a series of adjacent swaps in the manner of bubble sort. The key insight is its single index pointer: when neighbors are in order the pointer advances, otherwise it swaps and steps back, so the algorithm needs no nested loops.

## Task Requirements
- Implement gnome sort in the chosen language.
- Sort an array (or list) of numbers using it.
- Follow the given pseudocode behavior: walk forward while ordered pairs are found, and swap-and-backtrack on disordered pairs (with an optional `>=` comparison for descending order).

## Language Coverage
100 languages implement this task, spanning assembly, functional, scripting, and mainstream imperative languages. Representative entries include C, C++, C#, Java, Python, Haskell, Rust, Go, Ruby, Common Lisp, and 360 Assembly.

## Connections
- [[GnomeSort]] — the algorithm this task implements
- [[InsertionSort]] — closely related sort gnome sort resembles
- [[BubbleSort]] — supplies the swap-based element movement idea
- [[SortingAlgorithms]] — the broader family of comparison sorts
- [[InPlaceAlgorithm]] — gnome sort sorts the array in place with O(1) extra space

## Contradictions
- None — reference task page.
