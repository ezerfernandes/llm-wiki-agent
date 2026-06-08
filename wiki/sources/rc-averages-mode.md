---
title: "Averages/Mode (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, statistics, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Averages/Mode
---

## Summary
This task asks the programmer to compute the statistical mode — the most frequently occurring value — of a collection of values. The key insight is that the mode is not necessarily unique: when several values tie for the highest frequency, the program must return all of them rather than picking one arbitrarily. The empty-collection case may be ignored.

## Task Requirements
- Write a program that finds the mode value(s) of a collection.
- Handle the non-unique case: if multiple values share the maximum frequency, all should be reported.
- The empty-collection case may be ignored.
- If a general collection is impractical, an array/vector may be used; if an arbitrary value type is impractical, integers may be used.

## Language Coverage
113 languages implement this task, spanning a very broad range from systems and application languages to array, functional, and statistical languages. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, R, J, APL, Julia, and Common Lisp.

## Connections
- [[Mode]] — the central statistical measure being computed
- [[DescriptiveStatistics]] — mode is one of the core measures of central tendency
- [[FrequencyCounting]] — the standard implementation tallies occurrences per value
- [[HashTable]] — a common data structure for accumulating value counts efficiently

## Contradictions
- None — reference task page.
