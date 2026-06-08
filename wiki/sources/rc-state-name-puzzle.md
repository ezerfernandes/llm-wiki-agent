---
title: "State name puzzle (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, anagrams, combinatorics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/State_name_puzzle
---

## Summary
The task asks the programmer to find all pairs of U.S. state names whose combined letters can be rearranged to spell a different pair of state names, where all four names are distinct. The key insight is that this is an anagram-equivalence problem: pooling the letters of one pair and matching that multiset against the pooled letters of every other pair, which can be made efficient via canonical letter signatures (e.g. sorted-letter keys or Gödel numbering).

## Task Requirements
- Solve the puzzle on the original list of 50 U.S. states and again on the list extended with fictitious states.
- Find two-state pairs whose merged letters can be rearranged into two other, different state names (all four distinct).
- Treat case and spacing as insignificant — compare letters only, after harmonizing case.
- Do not assume the input list is sorted, and eliminate duplicate state names before processing.

## Language Coverage
35 languages implement this task, spanning systems and functional styles. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Perl, Ruby, Julia, and Wren.

## Connections
- [[Anagrams]] — the core operation is detecting anagram equivalence between letter multisets
- [[StringProcessing]] — normalization, letter counting, and canonical-key construction
- [[GoedelNumbering]] — suggested encoding to map letter multisets to comparable numbers
- [[EquivalenceClasses]] — grouping pairs by their canonical letter signature
- [[Combinatorics]] — enumerating distinct unordered pairs of state names

## Contradictions
- None — reference task page.
