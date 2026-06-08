---
title: "Levenshtein distance (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, dynamic-programming, edit-distance]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Levenshtein_distance
---

## Summary
The task asks the programmer to compute the Levenshtein distance between two strings — the minimum number of single-character edits (insertions, deletions, or substitutions) needed to transform one string into the other. The canonical example is that the distance between "kitten" and "sitting" is 3. The key insight is that this is an edit-distance string metric typically solved with a dynamic-programming table, and the distance is symmetric (reversing both strings yields the same result).

## Task Requirements
- Implement a Levenshtein distance function (or use a library function).
- The allowed edit operations are insertion, deletion, and substitution of a single character.
- Demonstrate it by showing the Levenshtein distance between "kitten" and "sitting" (which is 3).

## Language Coverage
122 languages implement this task, reflecting very broad coverage across mainstream, scripting, functional, and assembly languages. Representative implementations include C, C++, Python, Java, JavaScript, Haskell, Rust, Go, Ruby, and Common Lisp.

## Connections
- [[DynamicProgramming]] — the standard algorithmic technique used to compute the distance via a cost matrix.
- [[EditDistance]] — Levenshtein distance is the most common form of edit distance.
- [[StringMetric]] — it serves as a metric measuring the difference between two sequences.
- [[LongestCommonSubsequence]] — a related string-comparison task cross-referenced on the page.

## Contradictions
- None — reference task page.
