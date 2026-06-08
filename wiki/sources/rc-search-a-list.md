---
title: "Search a list (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, searching, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Search_a_list
---

## Summary
This task asks the programmer to find the index of a target string (the "needle") within an ordered, indexable collection of strings (the "haystack"). When the needle occurs more than once, the smallest matching index must be returned, and an exception should be raised if the needle is absent. The key insight is that most languages expose this directly through a built-in collection method, so the exercise highlights how each language signals "not found" (return value vs. exception).

## Task Requirements
- Find the index of a string (needle) within an indexable, ordered collection of strings (haystack).
- Raise an exception if the needle is missing.
- If the needle occurs multiple times, return the smallest index.
- Extra credit: return the largest index for a needle that appears multiple times.

## Language Coverage
124 languages implement this task, reflecting that linear/collection search is a universal operation across paradigms. Representative implementations include C, C++, Java, Python, Ruby, Haskell, Go, Rust, Common Lisp, and Perl.

## Connections
- [[LinearSearch]] — the underlying algorithm for locating an element by scanning positions.
- [[StringProcessing]] — the haystack consists of strings to be compared and matched.
- [[ExceptionHandling]] — the missing-needle case must raise an exception.
- [[ArrayIndexing]] — results are expressed as positions within an ordered collection.

## Contradictions
- None — reference task page.
