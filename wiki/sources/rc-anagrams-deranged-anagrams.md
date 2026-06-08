---
title: "Anagrams/Deranged anagrams (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, anagrams, derangement]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Anagrams/Deranged_anagrams
---

## Summary
The task is to find the longest pair of "deranged anagrams" in the unixdict word list: two words made of the same multiset of characters where no character occupies the same position in both words. It combines anagram detection (grouping words by their sorted-character signature) with the derangement constraint (no fixed points when comparing the two strings position by position). The key insight is to group candidates by sorted-letter key, then check pairs within each group for a position-wise mismatch.

## Task Requirements
- Read the word list from the unixdict.txt word file.
- Identify anagrams: words sharing the same characters in any order.
- Restrict to deranged anagram pairs, where the same character never appears at the same index in both words.
- Display the longest such deranged anagram pair found.

## Language Coverage
85 languages implement this task, reflecting broad coverage across functional, imperative, scripting, and assembly languages. Representative implementations include Python, Haskell, C, C++, Rust, Go, Java, Perl, Ruby, and Racket.

## Connections
- [[Anagram]] — words composed of the same characters in different order.
- [[Derangement]] — a permutation with no element left in its original position.
- [[StringProcessing]] — sorting, grouping, and comparing character sequences.
- [[HashingByKey]] — grouping words by their sorted-character signature.

## Contradictions
- None — reference task page.
