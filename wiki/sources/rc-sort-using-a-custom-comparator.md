---
title: "Sort using a custom comparator (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, sorting, string-processing, comparator]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sort_using_a_custom_comparator
---

## Summary
The task asks the programmer to sort an array or list of strings using a two-level ordering rule: primarily by descending string length, and secondarily by ascending lexicographic (case-insensitive) order for strings of equal length. The key requirement is to use the language's built-in sort facility combined with a user-supplied callback comparison function, demonstrating how to inject custom ordering logic into a standard sort routine.

## Task Requirements
- Sort a collection of strings by descending length as the primary key.
- For strings of equal length, order them in ascending lexicographic order.
- Lexicographic comparison must be case-insensitive.
- Use the language's library sort facility, supplying your own comparator callback rather than reimplementing the sort.

## Language Coverage
104 languages implement this task, spanning functional, imperative, object-oriented, and esoteric paradigms. Representative implementations include C, C++, Java, Python, Haskell, JavaScript, Ruby, Rust, Go, Common Lisp, and Scala.

## Connections
- [[SortingAlgorithm]] — the task relies on a library sort routine driven by custom criteria
- [[Comparator]] — the core technique is passing a comparison callback to the sort
- [[HigherOrderFunction]] — sort facilities accept the comparator as a function argument
- [[LexicographicOrder]] — the secondary tie-breaking ordering for equal-length strings
- [[StringProcessing]] — operates on length and case-insensitive content of strings

## Contradictions
- None — reference task page.
