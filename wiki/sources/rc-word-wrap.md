---
title: "Word wrap (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, text-layout]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Word_wrap
---

## Summary
The task is to wrap a paragraph of text so that no line exceeds a specified column width, breaking only at word boundaries. The basic version implements the greedy minimum-length algorithm (fill each line with as many words as fit, then start a new line). The key insight is the contrast with the more sophisticated Knuth–Plass line-breaking algorithm used by TeX, which minimizes a global "badness" cost rather than making locally greedy choices.

## Task Requirements
- Wrap a paragraph of text at a specified column width.
- If a built-in or standard-library facility exists, demonstrate it; otherwise implement the greedy minimum-length word-wrap algorithm.
- Show the routine working on a sample of text at two different wrap columns.
- Extra credit: implement a more advanced algorithm (e.g., Knuth–Plass), reference documentation showing it is better than greedy, and show an input where the two algorithms produce different output.

## Language Coverage
93 languages implement this task, reflecting broad coverage across general-purpose, scripting, and assembly languages. Representative implementations include C, C++, Python, Java, JavaScript, Haskell, Rust, Go, Perl, Raku, and REXX.

## Connections
- [[GreedyAlgorithm]] — the basic minimum-length line-fill strategy.
- [[DynamicProgramming]] — underlies the optimal Knuth–Plass approach.
- [[KnuthPlassLineBreaking]] — the TeX algorithm cited for extra credit.
- [[StringProcessing]] — tokenizing and reassembling text.
- [[TextLayout]] — the typesetting domain this task addresses.

## Contradictions
- None — reference task page.
