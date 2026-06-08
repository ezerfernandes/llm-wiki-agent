---
title: "Factorize string into Lyndon words (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, combinatorics-on-words]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Factorize_string_into_Lyndon_words
---

## Summary
The task asks the programmer to decompose an input string into its unique factorization as a non-decreasing sequence of Lyndon words. A Lyndon word is a non-empty string strictly smaller in lexicographic order than all of its circular rotations. The Chen–Fox–Lyndon theorem guarantees that every string factors uniquely into such words in non-decreasing order, and Duval's algorithm produces this factorization in O(n) time and O(1) extra space.

## Task Requirements
- Implement a factorization that splits any input string into a sequence of Lyndon words.
- The output sequence of factors must be non-decreasing in lexicographic order, per the Chen–Fox–Lyndon theorem.
- Use a lexicographic comparison where shorter strings are padded on the right with the smallest letter (a total preorder).
- The expected approach is Duval's algorithm for linear-time, constant-space computation.

## Language Coverage
23 languages implement this task, spanning systems, functional, scripting, and array languages. Representative examples include C++, Rust, Go, Java, Python, Perl, Raku, Julia, JavaScript, and Wren.

## Connections
- [[LyndonWord]] — the central object the factorization produces
- [[DuvalsAlgorithm]] — the O(n) time, O(1) space method specified by the task
- [[ChenFoxLyndonTheorem]] — guarantees unique non-decreasing factorization
- [[LexicographicOrder]] — defines the comparison used to order rotations and factors
- [[CombinatoricsOnWords]] — the broader field studying Lyndon words and string factorizations

## Contradictions
- None — reference task page.
