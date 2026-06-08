---
title: "Benford's law (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, statistics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Benford's_law
---

## Summary
Benford's law (the "first-digit law") describes the frequency distribution of leading significant digits in many real-world data sets, where the digit 1 leads about 30% of the time and 9 leads under 5%. The task asks the programmer to compute the actual distribution of first significant (non-zero) digits in a collection of numbers and compare it against the expected distribution given by P(d) = log10(1 + 1/d). The key insight is that data spanning many orders of magnitude tends to follow this logarithmic distribution.

## Task Requirements
- Write a routine to calculate the distribution of the first significant (non-zero) digit across a collection of numbers.
- Display the actual versus expected distribution in any convenient form (table, graph, or histogram).
- Use the first 1000 numbers of the Fibonacci sequence as the data set (generated or loaded; no need to show how).
- Expected probability per leading digit d (1-9): P(d) = log10(d+1) - log10(d) = log10(1 + 1/d).
- Extra credit: show the distribution for another data set sourced from a Wikipedia page, naming the page and what the numbers enumerate.

## Language Coverage
94 languages implement this task, a broad spread covering systems, scripting, functional, statistical, and BASIC-family languages. Representative examples include C, C++, Rust, Go, Python, Haskell, Julia, R, Java, and Perl.

## Connections
- [[BenfordsLaw]] — the statistical phenomenon the task verifies
- [[FibonacciSequence]] — the prescribed input data set
- [[Logarithm]] — base-10 logarithm defines the expected probabilities
- [[FrequencyDistribution]] — actual vs. expected histogram comparison
- [[NumberTheory]] — domain of the leading-digit distribution result

## Contradictions
- None — reference task page.
