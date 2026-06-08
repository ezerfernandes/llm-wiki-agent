---
title: "String matching (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/String_matching
---

## Summary
This task asks the programmer to demonstrate three basic string predicates given two strings: whether the first starts with the second, whether it contains the second anywhere, and whether it ends with the second. The key point is that most languages provide these as built-in methods or operators, so the exercise highlights each language's idiomatic substring API. Optional extensions ask for reporting the match position and finding all occurrences.

## Task Requirements
- Determine if the first string starts with the second string (prefix test).
- Determine if the first string contains the second string at any location (substring search).
- Determine if the first string ends with the second string (suffix test).
- Optional: print the location/index of the match for the "contains" case.
- Optional: handle and report multiple occurrences of the substring.

## Language Coverage
143 languages implement this task, reflecting that prefix/substring/suffix testing is a near-universal standard-library feature. Representative implementations include Python, Java, C, C++, Go, Rust, Ruby, Perl, Haskell, and JavaScript.

## Connections
- [[StringProcessing]] — the broader category of operations on text sequences this task belongs to.
- [[SubstringSearch]] — the core algorithmic problem behind the "contains" requirement.
- [[StringMatchingAlgorithms]] — named techniques (e.g. Knuth-Morris-Pratt, Boyer-Moore) underlying efficient substring search.
- [[PrefixAndSuffix]] — the starts-with / ends-with predicates exercised here.

## Contradictions
- None — reference task page.
