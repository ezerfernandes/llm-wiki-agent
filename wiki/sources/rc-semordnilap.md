---
title: "Semordnilap (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Semordnilap
---

## Summary
A semordnilap ("palindromes" spelled backward) is a word that spells a different valid word when reversed, such as *lager* and *regal*. This task asks the programmer to read the unixdict.txt word list and find all such pairs. The key insight is that a word is a semordnilap if its reversal is also in the dictionary but differs from the original (excluding palindromes).

## Task Requirements
- Read words only from the unixdict.txt word list.
- Count the total number of unique semordnilap pairs.
- Treat a matching pair (e.g. *lager* / *regal*) as a single unique pair, not two.
- Print 5 examples of the pairs found.
- Consider single words only, not phrases.

## Language Coverage
91 languages implement this task, showing very broad coverage across functional, imperative, and scripting paradigms. Representative implementations include Python, C, C++, Haskell, Ruby, Perl, Go, Rust, Java, and Common Lisp.

## Connections
- [[StringReversal]] — the core operation: reversing each word to test for a match
- [[HashSet]] — efficient membership testing of reversed words against the dictionary
- [[Palindrome]] — semordnilaps are explicitly the non-palindromic case of reversal-based word matching
- [[StringProcessing]] — the task is fundamentally text/word manipulation

## Contradictions
- None — reference task page.
