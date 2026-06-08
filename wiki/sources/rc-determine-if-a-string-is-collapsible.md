---
title: "Determine if a string is collapsible (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Determine_if_a_string_is_collapsible
---

## Summary
The task asks the programmer to detect whether a string is "collapsible" (contains immediately repeated characters) and, if so, to collapse it by deleting every run of duplicates down to a single character. Each maximal run of identical adjacent characters is reduced to one instance; characters that repeat non-adjacently are left untouched. The key insight is that this is purely a single-pass adjacent-deduplication, independent of which characters are involved or whether they appear elsewhere.

## Task Requirements
- Write a routine that locates immediately repeated characters and collapses (deletes) them, keeping only the first character of each run.
- The string may be processed from either direction.
- For each test string, show the original string with its length and the resultant string with its length.
- Bracket displayed strings with `<<<` and `>>>` (or guillemets) so leading/trailing blanks are visible.
- Test with the five given strings, including a null (empty) string and a string with many repeated blanks.

## Language Coverage
84 languages implement this task, a very broad cross-section spanning systems, scripting, functional, and assembly languages. Representative implementations include C, C++, Rust, Go, Python, Java, JavaScript, Haskell, Perl, REXX, and even 8080 Assembly and sed.

## Connections
- [[StringProcessing]] — core operation on character sequences
- [[RunLengthEncoding]] — collapsing adjacent runs is the deletion half of RLE
- [[Deduplication]] — removes immediately repeated elements
- [[FiniteStateMachine]] — a single-pass scan comparing each character to the previous one

## Contradictions
- None — reference task page.
