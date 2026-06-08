---
title: "Sort numbers lexicographically (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, sorting, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sort_numbers_lexicographically
---

## Summary
Given an integer n, return the sequence of integers from 1 to n (inclusive) ordered lexicographically rather than numerically. The key insight is that the numbers must be compared as if they were strings, so for n=13 the result is [1,10,11,12,13,2,3,4,5,6,7,8,9] because "10" sorts before "2".

## Task Requirements
- Take an integer n.
- Produce all integers from 1 through n inclusive.
- Order them in lexicographical (dictionary/string) order, not numeric order.
- Show the output on the page; the canonical example is n=13 yielding [1,10,11,12,13,2,3,4,5,6,7,8,9].

## Language Coverage
72 languages implement this task, spanning functional, imperative, array, and stack-based paradigms. Representative implementations include Python, C, C++, Java, Haskell, Rust, Go, Ruby, Perl, APL, and Wren.

## Connections
- [[Sorting]] — the task is a specialized ordering problem.
- [[LexicographicalOrder]] — the defining comparison rule.
- [[StringComparison]] — numbers are compared by their string representations.
- [[RadixSort]] — lexicographic ordering relates to digit-by-digit traversal of a trie of decimal strings.

## Contradictions
- None — reference task page.
