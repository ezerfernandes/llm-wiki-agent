---
title: "Ranking methods (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, ranking, sorting]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Ranking_methods
---

## Summary
This task asks the programmer to assign numerical ranks to competitors given an ordered list of scores, where ties must be handled consistently. The key insight is that there are several distinct, well-defined conventions for resolving ties, each producing a different rank sequence for the same data. The implementation must produce all five standard ranking variants over the same example dataset.

## Task Requirements
- Implement a function/procedure for each of five ranking methods that takes a best-first ordered list of scores with scorers.
- **Standard** ("1224"): tied competitors share what would have been their first ordinal number.
- **Modified** ("1334"): tied competitors share what would have been their last ordinal number.
- **Dense** ("1223"): tied competitors share the next available integer, with no gaps.
- **Ordinal** ("1234"): each competitor takes the next available integer; ties are not specially treated.
- **Fractional** ("1 2.5 2.5 4"): tied competitors share the mean of what would have been their ordinal numbers.
- Show the ranking of the provided test scores (Solomon 44, Jason 42, Errol 42, Garry 41, Bernard 41, Barry 41, Stephen 39) under each method.

## Language Coverage
47 languages implement this task, spanning systems, scripting, functional, and array languages. Representative implementations include C, C++, C#, Go, Rust-adjacent Nim, Haskell, Java, JavaScript, Python, Ruby, Perl, Raku, Julia, and the array language J.

## Connections
- [[Ranking]] — the core concept of ordering and tie resolution this task implements
- [[SortingAlgorithm]] — input is assumed pre-sorted in best-first order
- [[TieBreaking]] — the distinguishing dimension across the five methods
- [[Statistics]] — fractional ranking underlies rank-based statistical measures

## Contradictions
- None — reference task page.
