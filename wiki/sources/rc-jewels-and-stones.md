---
title: "Jewels and stones (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, set-membership]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Jewels_and_stones
---

## Summary
The task asks for a function taking two strings, `stones` and `jewels`, that returns how many characters in `stones` also appear in `jewels`. The letters in `jewels` are guaranteed distinct, so the natural approach is to load them into a set and count set membership while iterating over `stones`. It was inspired by a LeetCode problem of the same name.

## Task Requirements
- Implement a function with two string parameters (`stones`, `jewels`) returning an integer count.
- Both strings may hold any mix of upper- and lower-case letters; `jewels` letters are all distinct.
- Count how many characters of `stones` are also present in `jewels`.
- Only ISO basic Latin letters (A-Z, a-z) need be considered.
- Matching is case-sensitive: 'a' is distinct from 'A'.
- No argument validation is required; e.g. stones="aAAbbbb", jewels="aA" returns 3.

## Language Coverage
97 languages implement this task, spanning low-level assembly through high-level and functional languages. Representative examples include C, C++, Rust, Go, Python, Java, JavaScript, Haskell, Ruby, and APL.

## Connections
- [[SetMembership]] — counting via membership tests against the jewel set
- [[StringProcessing]] — character-level iteration over the input strings
- [[HashSet]] — typical data structure for O(1) jewel lookups
- [[LinearSearch]] — naive alternative scanning jewels per stone character

## Contradictions
- None — reference task page.
