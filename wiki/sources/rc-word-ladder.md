---
title: "Word ladder (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graph-search, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Word_ladder
---

## Summary
Given two words of equal length, transform the first into the second by changing one letter at a time, where every intermediate string must itself be a valid word in the unixdict word list. The goal is to find a transformation chain using the minimum number of intermediate words, which is fundamentally a shortest-path problem on a graph whose nodes are words and whose edges connect words differing by exactly one letter.

## Task Requirements
- Read the dictionary from the `unixdict.txt` word list.
- Given two equal-length words, find a sequence transposing the first into the second.
- Change only one letter at a time; each intermediate result must be a dictionary word.
- Use the minimum number of intermediate words (shortest path).
- Demonstrate the given examples: boy -> man, girl -> lady, john -> jane.
- Report that child cannot be turned into adult (no path exists).

## Language Coverage
29 languages implement this task, spanning systems, functional, scripting, and array families. Representative implementations include C++, Go, Rust, Haskell, F#, Python, Perl, Ruby, Julia, Java, JavaScript, and APL.

## Connections
- [[BreadthFirstSearch]] — the standard technique for finding the minimum-length ladder
- [[ShortestPath]] — the task is explicitly a shortest-path problem
- [[GraphTheory]] — words as nodes, single-letter edits as edges
- [[HammingDistance]] — adjacency is defined by a Hamming distance of one
- [[StringProcessing]] — comparing and mutating fixed-length words

## Contradictions
- None — reference task page.
