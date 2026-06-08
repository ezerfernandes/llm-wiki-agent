---
title: "Letter frequency (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, file-io]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Letter_frequency
---

## Summary
This task asks the programmer to open a text file and count how often each letter (or character) appears in it. The core technique is a single pass over the file's contents while tallying occurrences into a map or array keyed by character. Implementations vary on whether they count only the letters A–Z or every character including punctuation and whitespace.

## Task Requirements
- Open a text file and read its contents.
- Count the occurrences of each letter.
- Counting all characters (including punctuation) or restricting to letters A–Z are both acceptable.

## Language Coverage
143 languages implement this task, making it one of the broadly covered string-processing exercises spanning systems languages, scripting languages, and array languages. Representative implementations include C, Python, Java, Haskell, Perl, Ruby, Rust, Go, J, and Common Lisp.

## Connections
- [[FrequencyDistribution]] — the task builds a count of each distinct symbol
- [[HashMap]] — letters are typically tallied into an associative map
- [[FileIO]] — requires reading a text file from disk
- [[StringProcessing]] — iterating over and classifying characters
- [[Histogram]] — the resulting per-letter counts form a histogram

## Contradictions
- None — reference task page.
