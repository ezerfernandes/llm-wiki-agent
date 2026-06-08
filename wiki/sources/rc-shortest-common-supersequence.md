---
title: "Shortest common supersequence (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, dynamic-programming]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Shortest_common_supersequence
---

## Summary
The task asks the programmer to compute the shortest common supersequence (SCS) of two strings u and v: the shortest string s such that both u and v are subsequences of s. The key insight is that the SCS is closely tied to the longest common subsequence (LCS) — once the LCS is known, it can be interleaved with the leftover characters of each input, giving length |u| + |v| − |LCS|. The result is not necessarily unique.

## Task Requirements
- Given two strings u and v, find the shortest sequence s that contains both u and v as subsequences.
- May reuse a longest-common-subsequence routine as a helper.
- Demonstrate by printing s for u = "abcbdab" and v = "bdcaba".

## Language Coverage
32 languages implement this task, spanning systems, functional, scripting, and array styles. Representative entries include C, C++, C#, Java, Go, Rust-adjacent D, Haskell, Python, Ruby, Perl, Raku, JavaScript, Julia, Kotlin, Phix, and Wren.

## Connections
- [[LongestCommonSubsequence]] — the SCS is derived directly from the LCS of the two inputs.
- [[DynamicProgramming]] — both LCS and SCS are classic DP table problems.
- [[Subsequence]] — u and v must each embed in s as subsequences.
- [[StringAlgorithms]] — sequence alignment / edit-style string manipulation.

## Contradictions
- None — reference task page.
