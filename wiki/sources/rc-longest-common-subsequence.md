---
title: "Longest common subsequence (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, dynamic-programming, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Longest_common_subsequence
---

## Summary
The task asks the programmer to write a function returning a longest common subsequence (LCS) of two case-sensitive strings, where a subsequence is any string formed by deleting zero or more symbols (preserving order) and the LCS is the longest such string common to both inputs. The key insight is that an LCS corresponds to a maximum-cardinality chain over the set of matches (i, j) where A[i] = B[j], which the classic dynamic-programming solution computes in O(m*n) time. The problem underlies practical applications such as file-diff comparison and bioinformatics sequence alignment.

## Task Requirements
- Implement a function that takes two strings and returns one longest common subsequence of them.
- Comparison is case-sensitive.
- Only a single LCS need be returned; enumerating all LCSs is not required.
- The code only needs to handle strings (not arbitrary sequences).
- Example: LCS of "1234" and "1224533324" is "1234"; LCS of "thisisatest" and "testing123testing" is "tsitest".

## Language Coverage
77 languages implement this task, giving broad coverage across functional, imperative, array, and esoteric paradigms. Representative implementations include Python, C, C++, Java, Haskell, Rust, Go, Common Lisp, Prolog, APL, J, and Raku.

## Connections
- [[DynamicProgramming]] — the standard O(m*n) LCS table-filling technique
- [[Memoization]] — recursive formulation cached to avoid recomputation
- [[Recursion]] — naive divide-on-last-character definition of LCS
- [[StringProcessing]] — operating over sequences of symbols
- [[EditDistance]] — closely related sequence-alignment measure used in diffs

## Contradictions
- None — reference task page.
