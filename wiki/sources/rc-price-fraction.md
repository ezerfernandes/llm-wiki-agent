---
title: "Price fraction (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, lookup-table, financial]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Price_fraction
---

## Summary
The task asks the programmer to map a floating point currency value between 0.00 and 1.00 onto a fixed, government-regulated replacement value drawn from a 20-row lookup table. The motivating scenario is a pharmacy dispensary application that rescales a price fraction to a standard value. The core insight is that this is a piecewise-constant step function: each half-open input interval (e.g. >= 0.06 and < 0.11) maps to a single output (0.18).

## Task Requirements
- Accept a floating point input in the range 0.00 to 1.00.
- Rescale it according to the 20-entry table of half-open intervals to its mapped output value.
- The intervals are inclusive on the lower bound and exclusive on the upper bound; the final bucket (>= 0.96, < 1.01) maps to 1.00.

## Language Coverage
91 languages implement this task, reflecting broad coverage typical of a simple lookup/branching exercise. Representative implementations include C, C++, Python, Java, JavaScript, Haskell, Perl, Ruby, Rust, Go, and Common Lisp.

## Connections
- [[LookupTable]] — the mapping is naturally expressed as a table of thresholds and outputs.
- [[StepFunction]] — the rescaling is a piecewise-constant function over input intervals.
- [[FloatingPoint]] — care is needed comparing decimal currency values represented in binary floating point.
- [[ConditionalLogic]] — a chain of range comparisons is the straightforward implementation.

## Contradictions
- None — reference task page.
