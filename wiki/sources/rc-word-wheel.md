---
title: "Word wheel (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, anagrams]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Word_wheel
---

## Summary
A "word wheel" is a newspaper puzzle in which nine letters are arranged in a 3×3 grid and the solver must find as many words as possible using only those letters, with every word required to contain the center letter. This task asks the programmer to solve a specific instance (letters `ndeokgelw`, center `k`) by filtering a dictionary, and the key insight is that each candidate word is valid only if its letter multiset is contained in the wheel's available-letter multiset.

## Task Requirements
- Find all words of 3 or more letters drawn only from the letters in the string `ndeokgelw`.
- Every valid word must contain the central letter `k`.
- Each letter may be used at most as many times as it appears in the source string.
- Use lowercase English letters only, validated against the `unixdict.txt` word list (or state an alternative dictionary).
- Optional extra: find the 3×3 grids that have at least one nine-letter solution and yield the largest number of words of three or more letters.

## Language Coverage
49 languages implement this task, spanning systems languages, scripting languages, and array/functional languages. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Perl, Raku, J, and APL.

## Connections
- [[StringProcessing]] — words are filtered and validated as character strings
- [[Multiset]] — letter-frequency containment is the core validity test
- [[Anagram]] — checking constructibility of a word from a fixed letter pool is closely related to anagram detection
- [[DictionaryLookup]] — candidate words are matched against an external word list

## Contradictions
- None — reference task page.
