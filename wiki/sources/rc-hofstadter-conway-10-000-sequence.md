---
title: "Hofstadter-Conway $10,000 sequence (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, recursion, memoization]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Hofstadter-Conway_$10,000_sequence
---

## Summary
The task asks the programmer to generate the Hofstadter-Conway $10,000 sequence, a self-referential integer sequence defined by a(1)=a(2)=1 and a(n)=a(a(n-1))+a(n-a(n-1)). The key insight is that the recurrence indexes back into the sequence itself, so efficient computation relies on building up and memoizing earlier terms. The sequence is named after John Conway, who offered a $10,000 prize for finding the first position p beyond which a(n)/n stays below 0.55, later won by Colin Mallows.

## Task Requirements
- Create a routine to generate members of the Hofstadter-Conway $10,000 sequence.
- Use it to show the maxima of a(n)/n between successive powers of two, up to 2**20.
- Stretch goal: compute the value of n that would have won the $10,000 prize and confirm a(n)/n < 0.55 holds for all n up to 2**20.

## Language Coverage
70 languages implement this task, spanning systems, functional, scripting, and array languages. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Common Lisp, J, and REXX.

## Connections
- [[Recursion]] — the defining recurrence references the sequence at indices derived from its own values.
- [[Memoization]] — caching computed terms (the page is tagged Memoization) makes generation tractable.
- [[IntegerSequences]] — a member of the family of self-referential meta-Fibonacci sequences.
- [[NumberTheory]] — the analysis of a(n)/n asymptotics underlies Mallows' prize-winning proof.

## Contradictions
- None — reference task page.
