---
title: "Power set (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, set-theory, combinatorics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Power_set
---

## Summary
The task asks the programmer to write a function that, given a set S, returns its power set 2^S — the set of all subsets of S, including the empty set and S itself. The key insight is that a set of n elements has exactly 2^n subsets, so each subset can be enumerated by treating the bits of an n-bit number as a membership mask, or built recursively. Edge cases include the power set of the empty set (which equals {∅}) and the power set of {∅} (which equals {∅, {∅}}).

## Task Requirements
- Using a library/built-in set type or a custom set type with the necessary operations, write a function taking a set S and yielding the power set 2^S.
- The result for an n-element set must contain all 2^n subsets, including the empty set.
- Extra credit: demonstrate the power set of the empty set is {∅}, and the power set of {∅} is {∅, {∅}}.

## Language Coverage
111 languages implement this task, reflecting very broad coverage from functional and array languages to mainstream and scripting languages — including Haskell, Python, C, Java, JavaScript, Scheme, Common Lisp, APL, J, Rust, and Ruby.

## Connections
- [[SetTheory]] — the power set is a fundamental construction on sets.
- [[Combinatorics]] — enumerating all subsets of a finite set.
- [[Subset]] — each element of the power set is a subset of the input.
- [[BitmaskEnumeration]] — common technique mapping integers 0..2^n-1 to subsets.
- [[Recursion]] — alternate construction by recursively combining subsets with and without each element.

## Contradictions
- None — reference task page.
