---
title: "Boyer-Moore string search (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, algorithms]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Boyer-Moore_string_search
---

## Summary
The task asks the programmer to implement the Boyer-Moore string-search algorithm, which locates a pattern within a larger text. Its key insight is to compare the pattern against the text from right to left (highest position backward) and, on a mismatch, skip ahead by a precomputed amount rather than advancing one character at a time. This makes it efficient and well suited to backtracking-unfriendly storage such as tape and hard disks, since whole segments can be skipped without rescanning.

## Task Requirements
- Implement the Boyer-Moore algorithm to search for a pattern inside a text.
- Match the pattern from its highest (rightmost) position backward to the lowest; on failure, advance the start pointer to skip data guaranteed not to match, repeating until a match is found or the pointer exceeds the data length.
- Test with a pattern containing repeated subsequences, e.g. `alfalfa`.
- The searched text should include a real match preceded by partial near-matches such as `alfredo`, `behalf`, `calfskin`, `halfhearted`, `malfunction`, or `severalfold`.

## Language Coverage
30 languages implement this task, spanning systems, scripting, and functional styles. Representative examples include C++, Rust, Go, Java, Python, JavaScript, Perl, Raku, Julia, and Fortran.

## Connections
- [[StringSearchingAlgorithm]] — Boyer-Moore is a classic exact substring-search method.
- [[BadCharacterRule]] — heuristic for computing safe skip distances on mismatch.
- [[GoodSuffixRule]] — second skip heuristic exploiting matched suffixes.
- [[KnuthMorrisPratt]] — alternative linear-time string search for comparison.
- [[StringProcessing]] — the broader domain this task belongs to.

## Contradictions
- None — reference task page.
