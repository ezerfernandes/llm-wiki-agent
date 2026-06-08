---
title: "Ordered words (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Ordered_words
---

## Summary
An "ordered word" is a word whose letters appear in non-decreasing alphabetic order (e.g. "abbey", "dirt"). The task is to read the unixdict.txt word list, identify every ordered word, and display those that tie for the longest length. The key insight is that detecting an ordered word reduces to checking whether the string already equals its own sorted-character version.

## Task Requirements
- Read the dictionary file unixdict.txt.
- Determine which words are "ordered" (letters in alphabetic order).
- Among the ordered words, find the maximum word length.
- Display all ordered words that share that longest length.

## Language Coverage
136 languages implement this task, reflecting its popularity as an introductory text-processing and filtering exercise. Representative implementations include Python, C, C++, Java, Haskell, Ruby, Rust, Go, Perl, APL, and Common Lisp.

## Connections
- [[StringProcessing]] — core domain of reading and filtering words
- [[Sorting]] — the canonical test compares a word against its sorted characters
- [[Filtering]] — selecting words matching a predicate, then by maximum length
- [[FileIO]] — reading the external dictionary word list

## Contradictions
- None — reference task page.
