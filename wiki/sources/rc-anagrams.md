---
title: "Anagrams (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, hashing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Anagrams
---

## Summary
The task asks the programmer to read a standard word list (unixdict.txt) and find the sets of words that are anagrams of one another — words built from exactly the same multiset of letters in a different order — reporting the group(s) containing the most words. The key insight is that all anagrams of a word share an identical canonical form (typically the sorted sequence of their letters), so sorting each word's characters and grouping words by that sorted key reduces the problem to a single grouping pass over the dictionary.

## Task Requirements
- Read the word list from unixdict.txt (provided URL or mirror).
- Identify sets of words composed of the same characters in different orders (anagrams).
- Find and report the anagram set(s) that contain the most words.

## Language Coverage
137 languages implement this task, giving very broad coverage across functional, imperative, scripting, and assembly families. Representative implementations include Python, C, C++, Java, Haskell, Perl, Ruby, Go, Rust, and Common Lisp.

## Connections
- [[Anagram]] — the core concept the task detects.
- [[StringProcessing]] — words are normalized and compared as character sequences.
- [[Sorting]] — sorting a word's letters yields its canonical anagram key.
- [[HashTable]] — grouping words by canonical key is typically done with a dictionary/map.
- [[CanonicalForm]] — the sorted-letter signature that makes anagrams collapse to one key.

## Contradictions
- None — reference task page.
