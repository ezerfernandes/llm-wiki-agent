---
title: "Range extraction (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Range_extraction
---

## Summary
This task asks the programmer to compress a sorted list of integers into a compact "range format" string. A run of three or more consecutive integers is collapsed into a `first-last` range, while shorter runs are listed individually, with all items joined by commas. The key insight is detecting maximal runs of consecutive values and only abbreviating those of length three or more (so a pair like `4,5` stays expanded, not `4-5`).

## Task Requirements
- Write a function that takes a list of integers in increasing order and returns the correctly formatted range string.
- A sequence of three or more successive integers `a, a+1, ..., b` is written as `a-b`; runs shorter than three are written out individually.
- Apply the function to the given 33-element list and verify it produces `0-2,4,6-8,11,12,14-25,27-33,35-39`.
- Print the program's output.

## Language Coverage
103 languages implement this task, spanning a very broad cross-section of the site — from systems and application languages like C, C++, Rust, Go, Java, and C# to scripting languages such as Python, Perl, Ruby, and Lua, plus functional languages like Haskell, OCaml, F#, and Scheme.

## Connections
- [[StringFormatting]] — assembling the comma-joined output and `first-last` range tokens
- [[RunLengthEncoding]] — collapsing consecutive runs is a form of run-length compression
- [[RangeExpansion]] — the inverse task that expands a range string back into a list
- [[IntegerSequences]] — operates on ordered sequences of integers

## Contradictions
- None — reference task page.
