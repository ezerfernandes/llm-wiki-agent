---
title: "Compare a list of strings (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, comparison]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Compare_a_list_of_strings
---

## Summary
Given a list of arbitrarily many strings stored in a variable named `strings`, the task asks the programmer to write two expressions that each yield a single boolean: one testing whether all strings are lexically equal, and one testing whether the list is in strict ascending order (every string lexically less than the one after it). The key insight is reducing a pairwise relation across a sequence into a single truth value, ideally via short-circuiting and without mutating the original list. Lists with fewer than two elements should return true for both tests.

## Task Requirements
- Test whether all strings in the list are lexically equal, returning a single true/false value.
- Test whether every string is lexically less than its successor (strict ascending order), returning a single true/false value.
- For lists of fewer than two elements, both tests must return true.
- Assume the strings live in a variable named `strings`; show only the expressions plus any needed includes or helper functions.
- Prefer solutions that do not modify the original list; note any that do.

## Language Coverage
108 languages implement this task, spanning a very broad cross-section from low-level assembly to functional and array languages. Representative implementations include C, C++, Java, Python, Haskell, Rust, Go, Ruby, Perl, Raku, J, and Common Lisp.

## Connections
- [[StringComparison]] — relies on lexicographic ordering of strings
- [[LexicographicOrder]] — the ascending-order test is a strict lexical sort check
- [[FoldReduce]] — collapsing a pairwise relation across a sequence into one boolean
- [[ShortCircuitEvaluation]] — idiomatic solutions use short-circuiting `all`/`every` constructs

## Contradictions
- None — reference task page.
