---
title: "Textonyms (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, hashing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Textonyms
---

## Summary
A textonym is a set of distinct words that map to the same sequence of digits on a phone's number pad under the standard mapping (2→ABC, 3→DEF, 4→GHI, 5→JKL, 6→MNO, 7→PQRS, 8→TUV, 9→WXYZ). The task is to scan a word list, convert each word to its digit sequence, and find which digit combinations are produced by more than one word. The key insight is grouping words by a derived key, which reduces to building a multimap from digit-string to the list of words sharing it.

## Task Requirements
- Map each letter to its phone-keypad digit; words containing non-mappable characters are skipped.
- Process a word list such as the Rosetta `Textonyms/wordlist` or unixdict.txt.
- Produce a report stating: the number of representable words, the wordlist URL, the number of distinct digit combinations needed, and how many of those combinations represent more than one word (the textonyms).
- Optionally show example textonyms, e.g. `2748424767 -> "Briticisms", "criticisms"`.
- Extra credit: use a non-English word list and keypad mapping.

## Language Coverage
43 languages implement this task, showing broad coverage across functional, imperative, and scripting families. Representative implementations include Python, C, C++, Go, Rust, Haskell, Java, Perl, Raku, Ruby, Julia, and Clojure.

## Connections
- [[HashTable]] — grouping words by their digit-key into a multimap
- [[StringProcessing]] — letter-to-digit transformation of each word
- [[Anagrams]] — a structurally similar "group words by a canonical key" pattern
- [[FrequencyCounting]] — counting how many words share each digit combination

## Contradictions
- None — reference task page.
