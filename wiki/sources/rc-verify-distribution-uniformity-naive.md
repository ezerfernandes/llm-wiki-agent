---
title: "Verify distribution uniformity/Naive (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, probability-statistics, random-number-generation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Verify_distribution_uniformity/Naive
---

## Summary
This task asks the programmer to write a function that empirically checks whether a small-integer random generator produces a uniform (flat) distribution. The naive approach simply tallies how often each value appears over many calls and verifies that every count stays within a given tolerance ("delta") of the expected flat frequency, rather than using a formal statistical test. The key insight is that with enough samples, a uniform generator's per-bucket counts should all hover near total/buckets, so deviations beyond delta signal non-uniformity.

## Task Requirements
- Implement a function taking three arguments: the integer-generating function/object, the number of times to call it, and a delta indicating how close to flat is acceptable.
- The function must report some indication of the achieved distribution (the bucket counts).
- It must raise or signal an "error" when the distribution is not flat enough.
- Demonstrate the checker on both a sufficiently-flat distribution and a non-flat one, using a generator from the Seven-sided dice from five-sided dice task.

## Language Coverage
52 languages implement this task. Coverage is broad across functional, imperative, and scripting families, including C, C++, C#, Java, JavaScript, Python, Haskell, Go, Julia, Ruby, Perl, and Tcl.

## Connections
- [[UniformDistribution]] — the property being verified
- [[RandomNumberGeneration]] — the generator under test
- [[StatisticalHypothesisTesting]] — the naive alternative to a formal goodness-of-fit test
- [[ChiSquaredTest]] — the rigorous counterpart referenced by the companion task
- [[SevenSidedDiceFromFiveSidedDice]] — supplies the generator to validate

## Contradictions
- None — reference task page.
