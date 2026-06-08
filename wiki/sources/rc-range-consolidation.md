---
title: "Range consolidation (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, interval-merging, sorting]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Range_consolidation
---

## Summary
The task asks the programmer to merge a collection of numeric ranges (closed intervals defined by two bounds) into the minimal set of non-overlapping ranges. Two ranges consolidate into one when either contains the other, or when they touch or overlap; otherwise both are kept. For N ranges, consolidation is applied repeatedly across all pairs until no further merges are possible. The key insight is that sorting the intervals by lower bound first reduces the otherwise pairwise problem to a single linear sweep.

## Task Requirements
- Represent a range as a pair of bounds covering all values between and including them; bound order is not fixed, so `[b0, b1]` equals `[b1, b0]`.
- Consolidate two ranges: encompassing range if one contains the other; a single merged range if they touch or intersect; both ranges unchanged otherwise.
- Generalize to N ranges by repeated pairwise consolidation until stable; for N < 2, return the input as-is.
- Normalize output: each range shows its smaller bound on the left, and ranges are ordered by ascending lower bound.
- Produce normalized output for five given input sets and display all results.

## Language Coverage
38 languages implement this task, spanning systems and functional languages alongside scripting and query languages. Representative implementations include C, C++, Rust, Go, Java, Haskell, Python, Perl, Raku, Julia, Clojure, and even SQL.

## Connections
- [[IntervalMerging]] — the canonical algorithm this task implements
- [[SortingAlgorithms]] — sorting by lower bound enables a linear merge sweep
- [[SetConsolidation]] — the discrete-set analogue referenced by the task
- [[ClosedInterval]] — the mathematical structure each range represents

## Contradictions
- None — reference task page.
