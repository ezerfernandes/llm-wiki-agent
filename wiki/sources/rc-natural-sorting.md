---
title: "Natural sorting (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, sorting]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Natural_sorting
---

## Summary
Natural sorting orders text the way a human reader expects rather than by raw character codes. The task asks the programmer to implement a sort routine that normalizes whitespace and case and treats embedded numbers as numeric values. The key insight is to split each string into alternating text and numeric fields, then compare fields positionally so that "foo9.txt" precedes "foo10.txt" instead of sorting lexically.

## Task Requirements
- Implement at least the first four of eight listed "natural" behaviors.
- Feature 1: ignore leading, trailing, and multiple adjacent spaces.
- Feature 2: treat all whitespace characters as equivalent.
- Feature 3: sort case-insensitively.
- Feature 4: sort numeric substrings in numeric order (split on numeric boundaries, integer fields compared as numbers, rightmost fields most significant).
- Test each feature separately against the provided sample input lists and match the reference (Python) output order; print results.
- Extra credit: implement further features (title sorts ignoring leading "The", accent folding, ligature splitting, character replacements such as ß → ss).

## Language Coverage
35 languages implement this task, spanning systems, scripting, and functional ecosystems. Representative entries include C, C++, Rust, Go, Java, Python, Perl, Raku, Haskell, Ruby, and JavaScript.

## Connections
- [[StringProcessing]] — core operation is tokenizing and normalizing text.
- [[SortingAlgorithms]] — implements a custom comparator over a standard sort.
- [[Tokenization]] — splitting strings into alternating text/number fields.
- [[UnicodeNormalization]] — accent folding, ligature splitting, and character replacements for extra credit.
- [[Collation]] — produces a human-friendly ordering distinct from code-point order.

## Contradictions
- None — reference task page.
