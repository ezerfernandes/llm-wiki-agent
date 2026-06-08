---
title: "Pancake numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, combinatorics, sorting, search]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Pancake_numbers
---

## Summary
The pancake number p(n) is the minimum number of prefix-reversal "flips" needed to sort the worst-case arrangement of a stack of n distinct-sized pancakes into ascending order, where each flip inserts a spatula at some point and reverses every pancake above it. The task asks the programmer to compute p(n) for n = 1 to 9 and exhibit, for each n, a stack that actually requires p(n) flips. The key insight is that p(n) is a maximin quantity — the maximum over all permutations of the minimum number of flips to sort that permutation — so finding it generally requires searching the space of stacks rather than just sorting one.

## Task Requirements
- Determine p(n) for n = 1 through 9.
- For each n, show one example arrangement that requires exactly p(n) flips.
- Optionally compare the results against the flip counts produced by an actual pancake sort ([[PancakeSort]]).
- Extra credit for computing p(n) beyond p(16); a stated caveat is that p(19) = 22, so any algorithm disagreeing with known OEIS values (A058986) is suspect.

## Language Coverage
37 languages implement this task, spanning low-level assembly through high-level scripting and functional languages. Representative entries include C, C++, C#, Java, JavaScript, Python, Rust, Go, Julia, Raku, and ARM Assembly.

## Connections
- [[PancakeSort]] — the sorting procedure whose worst-case flip count this task quantifies.
- [[BreadthFirstSearch]] — the standard way to find the minimum flips for a given stack and thus the maximin p(n).
- [[Combinatorics]] — p(n) is a maximin over the n! permutations of pancake stacks.
- [[Permutation]] — each candidate stack is a permutation searched or generated.
- [[IntegerSequence]] — the values form OEIS sequence A058986.

## Contradictions
- None — reference task page.
