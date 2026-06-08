---
title: "Smith–Waterman algorithm (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, dynamic-programming, bioinformatics, sequence-alignment]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Smith–Waterman_algorithm
---

## Summary
The task asks the programmer to implement the Smith–Waterman algorithm, a dynamic programming method for optimal *local* sequence alignment that finds the highest-scoring aligned substrings of two sequences. The key insight is that, unlike global alignment, the scoring matrix is clamped at zero so any cell can restart an alignment; the best local match is found by tracing back from the matrix's maximum value until a zero is reached. It is a foundational technique in bioinformatics for comparing DNA, RNA, or protein sequences.

## Task Requirements
- Build an `(m+1) × (n+1)` scoring matrix `H` for sequences `A` and `B`, with the first row and column initialized to 0.
- Fill each cell `H(i,j)` as the max of: 0, the diagonal cell plus match/mismatch score, the cell above minus the gap penalty, and the cell to the left minus the gap penalty.
- Use a scoring system: `+s` for a match, `-d` for a mismatch (substitution), `-g` for a gap (insertion/deletion).
- Perform traceback from the cell with the maximum value, stopping when a cell with value 0 is reached.
- Output the highest alignment score, the aligned substrings of `A` and `B`, and the alignment path.
- Example: `A = "ACACACTA"`, `B = "AGCACACA"` with match `+2`, mismatch `-1`, gap `-2` yields an optimal local alignment with score 14.

## Language Coverage
8 languages implement this task, a relatively small set reflecting its specialized bioinformatics niche. Implementations include Fortran, FreeBASIC, Go, JavaScript, Julia, Phix, Raku, and Wren.

## Connections
- [[DynamicProgramming]] — the matrix-filling recurrence is a classic dynamic programming formulation
- [[SequenceAlignment]] — the algorithm computes optimal local alignment between two sequences
- [[Bioinformatics]] — primary application domain for DNA, RNA, and protein comparison
- [[NeedlemanWunschAlgorithm]] — closely related dynamic programming method for global (rather than local) alignment

## Contradictions
- None — reference task page.
