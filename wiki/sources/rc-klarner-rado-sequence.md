---
title: "Klarner-Rado sequence (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, integer-sequences]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Klarner-Rado_sequence
---

## Summary
The Klarner-Rado sequence (OEIS A002977) is the thinnest strictly ascending integer sequence starting at 1 such that whenever an element n is present, both 2n+1 and 3n+1 also appear somewhere in the sequence. The task is to generate this sequence efficiently. The key insight noted by the problem is to build it without over-generating candidates and sorting; a clean approach is a min-heap (priority queue) that lazily emits the next smallest element while pushing its two successors, deduplicating along the way.

## Task Requirements
- Find and display the first 100 elements of the sequence.
- Find and display the 1,000th and 10,000th elements.
- Preferably do so without generating an over-abundance of candidates and sorting them.
- Stretch goal: find and display the 100,000th and 1,000,000th elements.

## Language Coverage
38 languages implement this task, spanning systems, functional, scripting, and array paradigms. Representative implementations include C, C++, C#, Rust, Java, Haskell, F#, Python, Perl, Raku, Julia, J, and Wren.

## Connections
- [[IntegerSequences]] — the task generates terms of a defined integer sequence (OEIS A002977)
- [[NumberTheory]] — the rule 2n+1 / 3n+1 places this among arithmetic generative sequences
- [[PriorityQueue]] — a min-heap is the natural structure to emit ordered elements without sorting
- [[Deduplication]] — distinct generated values must be merged since 2n+1 and 3n+1 collisions occur

## Contradictions
- None — reference task page.
