---
title: "Last letter-first letter (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graph-search, combinatorics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Last_letter-first_letter
---

## Summary
Based on a children's word game where each player must say a word beginning with the last letter of the previous word, this task asks the programmer to find the longest possible non-repeating chain through a given set of 70 English Pokemon names, where each name's first letter matches the prior name's final letter. The key insight is that this is a longest-path problem over a directed graph whose nodes are words and whose edges link a word to any other word starting with its terminal letter — an NP-hard search typically solved by exhaustive backtracking with pruning.

## Task Requirements
- Take the supplied list of 70 English Pokemon names.
- Generate a sequence containing the maximum number of names such that each subsequent name begins with the final letter of the preceding name.
- No name may be repeated within the sequence.
- Extra credit for handling the full list of 646 Pokemon names.

## Language Coverage
56 languages implement this task, spanning systems, functional, scripting, and BASIC-family dialects. Representative implementations include C, C++, Rust, Go, Java, Haskell, Python, Perl, Ruby, Clojure, and Prolog.

## Connections
- [[GraphTheory]] — names form nodes; last-to-first letter matches form directed edges
- [[LongestPath]] — finding the maximal non-repeating chain is a longest-path search
- [[Backtracking]] — the common solution strategy with depth-first pruning
- [[NPHardProblems]] — longest simple path is NP-hard, motivating heuristics for the 646-name case
- [[StringProcessing]] — matching first and last characters of each word

## Contradictions
- None — reference task page.
