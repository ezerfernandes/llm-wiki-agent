---
title: "Order disjoint list items (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, sorting, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Order_disjoint_list_items
---

## Summary
Given a list M of items and a second list N of items drawn from M, produce M' by reordering only the relevant occurrences in M so they follow the order given in N, while leaving every other item in its original position. Items in N are matched against M without replacement: the first occurrences in M of each item in N are collected, then those slots are refilled in N's order. The key insight is that the set of positions being permuted stays fixed; only the contents of those positions are reshuffled to mirror N's sequence.

## Task Requirements
- Match each item of N to its first available occurrence in M, consuming matches without replacement (duplicates only up to as many as appear in N).
- Record the indices in M that get matched; these positions form the slots to be rewritten.
- Fill those slots with N's items in N's given order, leaving all unmatched positions untouched.
- Demonstrate the output for the seven specified M/N input pairs (e.g. M='the cat sat on the mat', N='mat cat' -> 'the mat sat on the cat').

## Language Coverage
43 languages implement this task, showing broad reach across functional, imperative, and scripting families. Representative implementations include Python, Haskell, Common Lisp, C++, Go, Java, JavaScript, Perl, Raku, Ruby, and J.

## Connections
- [[Permutation]] — the matched positions are permuted into N's order
- [[StringProcessing]] — inputs are typically word lists parsed from strings
- [[Multiset]] — without-replacement matching treats N as a multiset against M
- [[SortDisjointSublist]] — the closely related companion Rosetta Code task

## Contradictions
- None — reference task page.
