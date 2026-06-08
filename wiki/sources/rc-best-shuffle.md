---
title: "Best shuffle (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, combinatorics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Best_shuffle
---

## Summary
The task is to shuffle the characters of a string so that as few characters as possible remain in their original position — ideally producing a derangement of the multiset of characters. Because repeated characters constrain how fully a string can be deranged, the goal is to minimize the count of fixed positions rather than guarantee zero. A randomized result among equally good choices is preferred, though a deterministic algorithm is acceptable.

## Task Requirements
- Rearrange a string's characters to maximize the number of positions whose character value changes.
- Compute a score equal to the number of positions where the character value did *not* change.
- Display output as: original string, shuffled string, (score).
- Handle the test cases: `abracadabra`, `seesaw`, `elk`, `grrrrrr`, `up`, and `a`.
- A randomized best-among-optimal result is preferred; a deterministic equivalent is acceptable.

## Language Coverage
79 languages implement this task, showing very broad coverage across systems, scripting, and functional families. Representative examples include C, C++, Rust, Go, Java, Python, Haskell, Perl, Raku, Common Lisp, and Tcl.

## Connections
- [[Derangement]] — the ideal shuffle is a derangement of the character multiset
- [[StringProcessing]] — operates on and rearranges characters in a string
- [[Combinatorics]] — concerns permutations and counting fixed points
- [[Permutation]] — the shuffled string is a permutation of the original

## Contradictions
- None — reference task page.
