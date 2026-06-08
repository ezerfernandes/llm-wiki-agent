---
title: "Longest common substring (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, dynamic-programming]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Longest_common_substring
---

## Summary
The task asks the programmer to write a function returning the longest common substring of two strings, where a substring is a run of consecutive characters (unlike a subsequence, which may skip characters). The canonical demonstration finds the longest common substring of "thisisatest" and "testing123testing", which is "test". The key insight is the contrast with the longest common subsequence problem, which for the same inputs yields "tsitest".

## Task Requirements
- Implement a function that returns the longest common substring of two input strings.
- The substring must consist of consecutive characters in both strings.
- Demonstrate the function on the inputs "thisisatest" and "testing123testing", producing "test".

## Language Coverage
71 languages implement this task, spanning low-level systems languages, functional languages, scripting languages, and many BASIC dialects. Representative implementations include C, C++, Rust, Go, Java, Haskell, Python, Perl, Common Lisp, and Prolog.

## Connections
- [[DynamicProgramming]] — the standard quadratic-time table approach to finding common substrings.
- [[LongestCommonSubsequence]] — the closely related task this one is explicitly contrasted with.
- [[SuffixTree]] — a generalized suffix tree gives an asymptotically faster solution.
- [[StringMatching]] — the broader family of substring search and comparison problems.

## Contradictions
- None — reference task page.
