---
title: "Range expansion (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, parsing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Range_expansion
---

## Summary
The task is the inverse of range extraction: given a compact comma-separated range description string such as `-6,-3--1,3-5,7-11,14,15,17-20`, expand it into the full list of integers it represents. The key insight is parsing each comma-delimited chunk as either a single integer or a hyphenated `low-high` range, while correctly handling negative bounds where the leading minus sign is not a separator (e.g. `-3--1` means the range from minus three to minus one).

## Task Requirements
- Parse the input range string `-6,-3--1,3-5,7-11,14,15,17-20`.
- Treat each comma-separated element as either a standalone number or an inclusive numeric range.
- Disambiguate the hyphen used as a range separator from the minus sign of a negative number.
- Output the expanded, ordered sequence of all integers covered.

## Language Coverage
107 languages implement this task, reflecting very broad coverage across functional, imperative, scripting, and esoteric families. Representative implementations include Python, C, C++, Java, Haskell, Ruby, Perl, Rust, Go, and Scheme.

## Connections
- [[StringParsing]] — splitting and interpreting the delimited input
- [[RegularExpressions]] — a common technique for matching range tokens and negative bounds
- [[RangeExtraction]] — the explicit inverse companion task
- [[IntegerSequences]] — the expanded output is a contiguous integer enumeration

## Contradictions
- None — reference task page.
