---
title: "Stem-and-leaf plot (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, statistics, data-visualization, text-formatting]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Stem-and-leaf_plot
---

## Summary
The task asks the programmer to produce a well-formatted stem-and-leaf plot from a given data set, splitting each number into a "stem" (its leading digits) and a "leaf" (its last digit). The key insight is that the plot groups values by stem and lists the trailing-digit leaves alongside, preserving the raw data while revealing its distribution like a sideways histogram. The emphasis is on clean presentation: monospaced text is acceptable, and the data set may be hardcoded.

## Task Requirements
- Build a stem-and-leaf plot from the provided ~120-element integer data set.
- Treat the last digit of each value as the leaf and the remaining leading digits as the stem.
- Produce well-aligned, readable output (monospaced plain text is acceptable; output need not be a bitmap image).
- It is acceptable to hardcode the data set or its characteristics (such as the stem range).

## Language Coverage
69 languages implement this task, showing broad coverage across general-purpose, functional, and array languages. Representative implementations include C, C++, C#, Java, Python, Haskell, Ruby, Rust, Go, J, and REXX.

## Connections
- [[DescriptiveStatistics]] — the plot summarizes a data distribution
- [[DataVisualization]] — a textual alternative to a histogram
- [[Histogram]] — closely related frequency-display technique
- [[TextFormatting]] — alignment and column layout drive the presentation
- [[IntegerDigitExtraction]] — splitting numbers into stem and leaf parts

## Contradictions
- None — reference task page.
