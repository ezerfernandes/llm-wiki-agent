---
title: "Specific characters (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Specific_characters
---

## Summary
Given a list of ASCII strings, a character is "specific" if it appears exactly twice within its own string and appears in no other string in the list. The task asks for the count of distinct specific characters across the whole list (each qualifying character counted once). The key insight is combining a per-string frequency check (exactly two occurrences) with a global uniqueness check (the character belongs to only one string).

## Task Requirements
- For each string, identify characters that occur exactly twice in that string.
- Among those, keep only characters that do not appear in any other string.
- Report how many distinct specific characters exist in the list (per the example ["ahwiueshaiu","ajxxfioaaf","ajrdsfroiwr"] yields [2, 1, 0]).
- Assume all inputs are ASCII.
- Extra credit: count the distinct characters in each string that do NOT satisfy the condition (example yields [5, 5, 9]).

## Language Coverage
17 languages implement this task, a modest spread of mainstream and niche languages. Representative entries include C++, Java, Python, Rust, Perl, Raku, Julia, Nim, Crystal, and the historical ALGOL 68.

## Connections
- [[StringProcessing]] — operates on per-character contents of strings
- [[FrequencyCounting]] — relies on tallying character occurrences within and across strings
- [[HashTable]] — character-to-count maps are the natural data structure
- [[SetOperations]] — distinct-character and cross-string uniqueness use set logic

## Contradictions
- None — reference task page.
