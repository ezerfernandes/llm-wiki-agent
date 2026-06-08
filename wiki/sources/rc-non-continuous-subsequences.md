---
title: "Non-continuous subsequences (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, combinatorics, discrete-math]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Non-continuous_subsequences
---

## Summary
Given an ordered sequence of elements, the task is to enumerate all of its non-continuous subsequences — subsequences that preserve the original order but have at least one gap, i.e. at least one element of the original sequence missing between the chosen subsequence's first and last elements. The key insight is that subsequences are defined structurally (by which positions are kept) rather than by their values, so this reduces to filtering the power set of positions to those that skip an interior element. For the sequence 1,2,3,4 there are exactly five such subsequences: 1,3; 1,4; 2,4; 1,3,4; and 1,2,4.

## Task Requirements
- For a given sequence, find and list all of its non-continuous subsequences.
- Treat subsequences structurally (by position/ordering), not by element values.
- A subsequence is continuous if no element is missing between its first and last chosen elements; non-continuous ones have at least one such gap.
- Demonstrate one or more algorithms idiomatic to the language (e.g. power-set generation with a gap filter).

## Language Coverage
63 languages implement this task, spanning functional, imperative, array, and logic paradigms. Representative implementations include Haskell, Python, J, Common Lisp, Prolog, C, Rust, Ruby, Scala, and Wren.

## Connections
- [[Combinatorics]] — enumerating subsequences is a combinatorial selection problem.
- [[PowerSet]] — non-continuous subsequences are a filtered subset of the power set of positions.
- [[Subsequence]] — the core structural concept being enumerated.
- [[Recursion]] — many implementations generate subsequences recursively.

## Contradictions
- None — reference task page.
