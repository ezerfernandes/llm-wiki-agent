---
title: "Count occurrences of a substring (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Count_occurrences_of_a_substring
---

## Summary
This task asks the programmer to write (or demonstrate a built-in) function that counts how many times a substring appears inside a larger string, returning an integer. The crucial constraint is that matches must be **non-overlapping**: once a substring is matched, the search resumes after it rather than within it. The key insight is that scanning consistently left-to-right (or right-to-left) yields the maximum number of non-overlapping matches.

## Task Requirements
- Create or show a function taking two arguments: the string to search and the substring to find.
- Return an integer count of occurrences.
- Count only non-overlapping matches — e.g. `countSubstring("ababababab","abab")` is 2, not 3.
- `countSubstring("the three truths","th")` should return 3.
- The matching should maximize the number of non-overlapping matches (achieved by consistent directional scanning).

## Language Coverage
154 languages implement this task, reflecting that string searching is a near-universal primitive. Representative implementations span C, C++, Java, Python, JavaScript, Go, Rust, Haskell, Perl, and Ruby, with many leaning on built-in count/find methods.

## Connections
- [[StringSearching]] — the underlying problem of locating a pattern within text
- [[SubstringMatching]] — overlapping vs. non-overlapping match semantics
- [[StringProcessing]] — broader category of text manipulation tasks
- [[PatternMatching]] — general technique this task specializes

## Contradictions
- None — reference task page.
