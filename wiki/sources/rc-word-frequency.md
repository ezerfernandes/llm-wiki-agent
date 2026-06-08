---
title: "Word frequency (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, text-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Word_frequency
---

## Summary
The task asks the programmer to read a text file and print the n most common words along with their occurrence counts, ordered by decreasing frequency. A word is defined loosely as a sequence of one or more contiguous letters, with case folded to lowercase, leaving the handling of apostrophes, hyphens, and accented characters to the implementer's discretion. The classic illustration is finding the top 10 words in Les Misérables, and the task's history traces to a famous Knuth-vs-McIlroy comparison where McIlroy solved it in a six-line Unix pipeline.

## Task Requirements
- Read a text file and an integer n.
- Tokenize the text into words (a word being one or more contiguous letters; letter definition is up to the implementer).
- Treat uppercase letters as equivalent to their lowercase counterparts.
- Treat distinct spellings (e.g. color vs colour) as separate words; no normalization.
- Count occurrences of each word.
- Display the n most frequent words with their counts in decreasing frequency; ties may be in any order.
- Demonstrate output using Les Misérables from Project Gutenberg with the top 10 words.

## Language Coverage
83 languages implement this task, reflecting broad coverage across scripting, functional, and systems languages well-suited to text munging. Representative implementations include Python, Perl, Raku, Ruby, Haskell, Go, Rust, C++, AWK, and the UNIX Shell (echoing McIlroy's original pipeline).

## Connections
- [[StringProcessing]] — tokenizing text into words
- [[Tokenization]] — splitting input on non-letter boundaries
- [[HashTable]] — accumulating word counts in a map/dictionary
- [[Sorting]] — ordering words by descending frequency
- [[FrequencyAnalysis]] — counting and ranking element occurrences

## Contradictions
- None — reference task page.
