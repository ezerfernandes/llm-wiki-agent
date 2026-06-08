---
title: "Paraffins (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, combinatorics, tree-enumeration, graph-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Paraffins
---

## Summary
The task is to enumerate, without repetition and in order of increasing size, all distinct paraffin (alkane) molecules with a given number `n` of carbon atoms. Chemically, alkanes share the formula C(n)H(2n+2), but for `n >= 4` multiple structural isomers exist. The key insight is that this is really a tree-enumeration problem: each molecule is an unrooted tree where carbon nodes have degree at most 4, and bond rotations or re-orientations must not be counted as distinct, so isomorphic trees collapse to a single isomer.

## Task Requirements
- Take `n`, the number of carbon atoms, as input.
- Count the number of distinct paraffin isomers with `n` carbons (e.g. `n=17` yields 24,894), ignoring stereo-isomerism.
- Treat the molecule as an unrooted tree of carbons with max degree 4; no double bonds and no cycles are allowed.
- Avoid double-counting molecules that differ only by rotation or re-orientation (graph isomorphism).
- Results should match OEIS A000602 (1, 1, 1, 1, 2, 3, 5, 9, 18, 35, 75, 159, 355, ...).
- Extra credit: display the paraffins via a 1D list representation or a 2D ASCII-art structure.

## Language Coverage
33 languages implement this task, a moderately broad set reflecting its algorithmic depth. Representative implementations include C, C++, D, Go, Haskell, J, Java, JavaScript, Julia, Python, Raku, and Wren.

## Connections
- [[TreeEnumeration]] — counting non-isomorphic trees is the core of the task
- [[GraphIsomorphism]] — distinct isomers correspond to non-isomorphic carbon trees
- [[Combinatorics]] — the rapidly growing isomer counts are a counting problem
- [[Recursion]] — solutions build larger molecules recursively from smaller centered/bicentered trees
- [[GeneratingFunctions]] — the classic functional solution uses generating-function-style recurrences

## Contradictions
- None — reference task page.
