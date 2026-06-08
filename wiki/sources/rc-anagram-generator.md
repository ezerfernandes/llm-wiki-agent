---
title: "Anagram generator (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, combinatorics, dictionary-search]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Anagram_generator
---

## Summary
This task asks the programmer to write a routine that *creates* anagrams of a given seed word or phrase, in contrast to the related tasks that merely *find* existing anagrams. Given a word list and a seed, the program rearranges the seed's letters into one or more valid dictionary words or phrases. The key insight is that the search reduces to a recursive/multiset-subset problem: repeatedly pick a dictionary word whose letters are a sub-multiset of the remaining letters, then recurse on the leftover letters until none remain.

## Task Requirements
- Write an anagram generator program (not an anagram finder).
- Use a publicly and freely available word file as the word list (e.g. unixdict.txt or words_alpha.txt).
- Ignore letter case, whitespace, punctuation, and symbols; numerics are best avoided.
- Anagrams need not be semantically meaningful; prefer phrases made of longer words.
- Generate anagrams for a few chosen words/phrases and show the seed plus one or two of the best results (output may be very large, so no need to show all).

## Language Coverage
17 languages implement this task, a moderate spread across systems, scripting, and functional languages. Representative implementations include Ada, C++, Go, Java, Julia, Nim, Rust, Raku, J, and Wren.

## Connections
- [[Anagrams]] — the sibling task of finding existing anagrams rather than generating them
- [[Multiset]] — letter-frequency bags drive the sub-word matching test
- [[Recursion]] — the leftover-letters search is naturally recursive
- [[Combinatorics]] — enumerating letter rearrangements into word combinations
- [[StringProcessing]] — normalizing case, whitespace, and punctuation before matching

## Solved in (Rosetta Code languages)
Solved in **16** of the wiki's catalogued languages (Rosetta Code shows 17 language sections for this task). (1 further RC language section(s) are outside the wiki's popularity-list language set.)

[[Ada]], [[C++]], [[Crystal]], [[Fortran]], [[FreeBASIC]], [[Go]], [[J]], [[Java]], [[Julia]], [[Nim]], [[Phix]], [[Pluto]], [[Raku]], [[Rebol]], [[Rust]], [[Wren]]

## Contradictions
- None — reference task page.
