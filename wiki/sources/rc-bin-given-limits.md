---
title: "Bin given limits (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, histogram, binary-search]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Bin_given_limits
---

## Summary
Given a list of n ascending, unique limit values, the task is to classify a large stream of input numbers into n+1 bins and count how many inputs land in each bin's half-open range. The first bin counts inputs below the smallest limit, each interior bin counts inputs in `[limit[i-1], limit[i])`, and the last bin counts inputs at or above the largest limit. The key insight is that this is a histogram-with-given-edges problem; because the limits are sorted, each input can be placed via binary search rather than a linear scan, and the data never needs to be sorted.

## Task Requirements
- Write a function that takes the ascending limits plus a stream/list of numbers and returns the bin counts.
- Write a second function that, given the same limits and the resulting bins, prints each bin's range limit together with its count.
- Assume the input numbers are too large to practically sort.
- Demonstrate on two provided datasets: one with 6 limits over 50 values, and one with 10 limits over 200 values.

## Language Coverage
47 languages implement this task, spanning systems and functional styles. Representative implementations include C, C++, C#, Rust, Go, Java, Python, Haskell, Julia, Perl, Raku, Ada, and Wren.

## Connections
- [[Histogram]] — binning counts inputs into fixed ranges, the defining operation here.
- [[BinarySearch]] — sorted limits let each value be placed in O(log n) per input.
- [[Counting]] — the bins are integer tallies over a data stream.
- [[Streaming]] — the task frames the data as too large to sort, favoring single-pass classification.

## Contradictions
- None — reference task page.
