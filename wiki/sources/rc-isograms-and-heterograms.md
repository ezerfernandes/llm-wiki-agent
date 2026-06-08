---
title: "Isograms and heterograms (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Isograms_and_heterograms
---

## Summary
The task asks the programmer to classify dictionary words by the frequency of their letters. An *n-isogram* is a word in which every distinct character appears exactly n times, and a *heterogram* (equivalently a 1-isogram) is a word with no repeated characters. The key insight is that both properties reduce to counting character occurrences and checking that the set of counts is uniform.

## Task Requirements
- Read words from `unixdict.txt`, ignoring capitalization.
- Find all words that are n-isograms with n > 1 (every present character used exactly n times, n at least 2).
- Sort that list by decreasing n, then decreasing word length, then ascending lexicographic order, and present as one list.
- Separately, find all heterograms longer than 10 characters.
- Sort the heterogram list by decreasing word length then ascending lexicographic order.

## Language Coverage
27 languages implement this task, spanning systems, scripting, functional, and array languages. Representative implementations include C, C++, C#, Java, Python, Perl, Raku, Julia, J, and Wren.

## Connections
- [[StringProcessing]] — the task is fundamentally about analyzing characters within strings.
- [[FrequencyCounting]] — solving it relies on tallying per-character occurrence counts.
- [[Sorting]] — results require multi-key ordering (by n, length, and lexicographic value).
- [[Anagram]] — closely related word-structure property based on letter multisets.

## Contradictions
- None — reference task page.
