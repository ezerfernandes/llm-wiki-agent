---
title: "Levenshtein distance/Alignment (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, dynamic-programming]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Levenshtein_distance/Alignment
---

## Summary
The Levenshtein distance gives the minimum number of insertions, deletions, and substitutions needed to turn one string into another, but reveals nothing about which operations were used or in what order. This task asks the programmer to produce an *alignment*: a two-line display of the strings with the minus character ('-') inserted to mark where a character must be added, making the edit operations visible. The key insight is that recovering the alignment requires backtracking through the dynamic-programming distance matrix rather than just reading off its final cell.

## Task Requirements
- Write a function that displays the alignment of two strings corresponding to their Levenshtein distance.
- Use the minus character ('-') to indicate where a character must be inserted in one of the strings.
- Demonstrate with the example words "rosettacode" and "raisethysword".
- Either implement the alignment algorithm directly or use a dedicated library, noting its name in the chosen language.

## Language Coverage
32 languages implement this task, spanning systems, functional, scripting, and array-oriented styles. Representative examples include C, C++, C#, Rust, Go, Java, Haskell, Python, Perl, Raku, Julia, J, and Wren.

## Connections
- [[LevenshteinDistance]] — the base edit-distance metric this task extends
- [[DynamicProgramming]] — the matrix-filling technique used to compute distance and recover the path
- [[EditDistance]] — the general family of string-difference measures
- [[SequenceAlignment]] — the broader bioinformatics/CS problem this notation comes from

## Contradictions
- None — reference task page.
