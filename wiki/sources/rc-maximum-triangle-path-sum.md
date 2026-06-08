---
title: "Maximum triangle path sum (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, dynamic-programming, recursion]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Maximum_triangle_path_sum
---

## Summary
Given a triangle of numbers, you walk from the top down to the bottom row, stepping diagonally left or right at each level, and sum the values visited. The task is to find the maximum possible sum over all top-to-bottom paths for a specific 18-row triangle. The key insight is to solve it bottom-up: collapse each pair of adjacent values in a row by adding the larger one to the value above, avoiding the exponential cost of enumerating every path.

## Task Requirements
- Walk down a numeric triangle from the apex to the base, moving one step left or right at each row.
- Compute the total of all numbers visited along a path.
- Find the maximum such total among all possible paths for the given 18-row triangle.
- The triangle data may be embedded in the source code or read from a `triangle.txt` file.

## Language Coverage
69 languages implement this task, spanning systems, functional, scripting, and assembly families. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Common Lisp, Perl, Raku, and even 360 Assembly and Z80 Assembly.

## Connections
- [[DynamicProgramming]] — the efficient bottom-up reduction is a textbook DP problem.
- [[Recursion]] — naive top-down solutions express the path search recursively.
- [[ProjectEuler]] — this task is derived from Project Euler Problem #18.
- [[GreedyAlgorithm]] — a naive greedy descent fails here, motivating the DP approach.

## Contradictions
- None — reference task page.
