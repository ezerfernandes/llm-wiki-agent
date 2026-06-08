---
title: "Bioinformatics/Global alignment (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, bioinformatics, string-processing, np-hard]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Bioinformatics/Global_alignment
---

## Summary
The task asks the programmer to reconstruct a long DNA sequence from a set of N shorter fragments (strings over the alphabet A, C, G, T) by finding their shortest common superstring — the briefest sequence that contains every fragment intact and in order. The key insight is that DNA sequencers produce many overlapping fragments, and assembly works by greedily merging fragments on their longest shared suffix/prefix overlaps. This shortest-common-superstring formulation is NP-hard and differs from the classic shortest common supersequence problem because here each fragment must appear as a contiguous substring rather than as a (possibly interleaved) subsequence.

## Task Requirements
- Given N non-identical DNA strings, find the shortest sequence that contains all N of them as contiguous substrings.
- Correctly handle duplicate fragments and fragments fully contained within another.
- Print the resulting superstring, its length (base count), and a per-base count for A, C, G, T.
- Solve four provided example fragment sets, ranging from tiny ("TA", "AAG", ...) up to a large 13-fragment set.

## Language Coverage
17 languages implement this task, a moderate spread reflecting its specialized bioinformatics flavor. Representative implementations include 11l, C++, Crystal, Go, Haskell, Java, Julia, Nim, Perl, Python, Raku, Rust, and Wren.

## Connections
- [[ShortestCommonSuperstring]] — the core combinatorial structure the task computes.
- [[SequenceAlignment]] — global alignment as the underlying bioinformatics technique.
- [[NPHardProblems]] — the assembly problem is NP-hard, motivating greedy heuristics.
- [[GreedyAlgorithm]] — the typical strategy of repeatedly merging the largest-overlap pair.
- [[StringOverlap]] — detecting maximal suffix/prefix overlaps between fragments.

## Contradictions
- None — reference task page.
