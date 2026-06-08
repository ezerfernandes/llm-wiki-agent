---
title: "Fivenum (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, statistics, descriptive-statistics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Fivenum
---

## Summary
The task asks the programmer to compute Tukey's five-number summary for an array of numbers: the minimum, lower hinge, median, upper hinge, and maximum. This compact representation captures a distribution's shape and is the basis for drawing boxplots, making it a memory-efficient stand-in for very large data arrays. The key subtlety is that statistical packages disagree on exactly how the hinges (quartiles) are computed, so implementations should match R's `fivenum` convention.

## Task Requirements
- Given an array of numbers, compute its five-number summary.
- The five numbers are the sample minimum, the lower hinge, the median, the upper hinge, and the sample maximum.
- Follow the hinge/quartile computation used by R's `fivenum` function (interpolation based on a half-position index over the sorted data).
- The summary is intended to support boxplot construction, though the task notes whisker definitions vary across packages.

## Language Coverage
55 languages implement this task, spanning systems languages, functional languages, statistical environments, and scripting languages. Representative examples include C, C++, Rust, Go, Java, Haskell, Python, R, Julia, Perl, and Wren.

## Connections
- [[FiveNumberSummary]] — the statistical concept the task computes
- [[Median]] — central value, and the basis for the lower and upper hinges
- [[Quartiles]] — the hinges approximate the first and third quartiles
- [[BoxPlot]] — the visualization the summary feeds into
- [[DescriptiveStatistics]] — broader family of summary measures

## Contradictions
- None — reference task page.
