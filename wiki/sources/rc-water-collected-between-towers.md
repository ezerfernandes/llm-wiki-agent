---
title: "Water collected between towers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, arrays, dynamic-programming]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Water_collected_between_towers
---

## Summary
Given an array of column heights forming a bar chart, compute how many unit cells of water would be trapped in the chart's concavities after rain. This is the classic "trapping rain water" problem: the water above any column equals the smaller of the tallest bars to its left and right, minus that column's own height. The key insight is that each position is bounded by the minimum of its left-max and right-max prefix/suffix heights.

## Task Requirements
- Write a function that takes an array of heights and returns the number of water units the corresponding bar chart can hold.
- Run it on seven given test series, e.g. `[5, 3, 7, 2, 6, 4, 5, 9, 1, 2]` should yield 14 units.
- The other test inputs include `[1, 5, 3, 7, 2]`, a 16-element series, `[5, 5, 5, 5]`, `[5, 6, 7, 8]`, `[8, 7, 7, 6]`, and `[6, 7, 10, 7, 6]`.

## Language Coverage
63 languages implement this task, spanning systems and functional styles as well as several assembly dialects. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Clojure, Ruby, and 8086 Assembly.

## Connections
- [[DynamicProgramming]] — precomputed left-max/right-max arrays give an O(n) solution
- [[ArrayProcessing]] — operates over an array of column heights
- [[TwoPointerTechnique]] — an alternative O(1)-space approach converging from both ends
- [[PrefixAndSuffixMaxima]] — water at each index depends on running maxima from each side

## Contradictions
- None — reference task page.
