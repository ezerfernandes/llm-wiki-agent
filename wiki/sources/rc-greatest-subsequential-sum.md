---
title: "Greatest subsequential sum (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, dynamic-programming, arrays]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Greatest_subsequential_sum
---

## Summary
Given a sequence of integers, find a contiguous subsequence whose elements sum to the maximum possible value, with no other contiguous subsequence summing higher. This is the classic maximum subarray problem, optimally solved in linear time by Kadane's algorithm. The key insight: an empty subsequence has sum 0, so if every element is negative the answer is the empty sequence.

## Task Requirements
- Take a sequence of integers as input.
- Return a continuous (contiguous) subsequence whose element sum is maximal.
- Treat the empty subsequence as having sum 0.
- If all elements are negative, the result must be the empty sequence.

## Language Coverage
103 languages implement this task, spanning systems languages, functional languages, scripting languages, and BASIC dialects. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, OCaml, Clojure, Ruby, and Perl.

## Connections
- [[KadanesAlgorithm]] — the canonical linear-time solution
- [[MaximumSubarrayProblem]] — the formal name of this problem
- [[DynamicProgramming]] — the paradigm underlying the optimal solution
- [[PrefixSums]] — an alternative O(n) framing via running totals

## Contradictions
- None — reference task page.
