---
title: "Burrows–Wheeler transform (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, data-compression]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Burrows–Wheeler_transform
---

## Summary
The task asks the programmer to implement the Burrows–Wheeler transform (BWT), a reversible string permutation that clusters identical characters into runs. The key insight is that although BWT alone does not compress data, the resulting runs are highly amenable to follow-on techniques like move-to-front transform and run-length encoding, and the original string can be perfectly recovered without storing extra side data.

## Task Requirements
- Implement the forward Burrows–Wheeler transform of an input string.
- Implement the inverse transform to recover the original string exactly.
- Handle the bookkeeping needed for reversibility, typically by appending a unique end-of-text sentinel character (commonly STX/ETX or `$`) and rejecting input that already contains it.
- Sort all rotations of the (sentinel-terminated) string and emit the last column as the transformed output.

## Language Coverage
46 languages implement this task, showing broad reach across compiled, scripting, functional, and array-oriented paradigms. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Julia, Perl, Raku, J, and Wren.

## Connections
- [[StringRotation]] — the transform is built from all cyclic rotations of the input
- [[SuffixArray]] — efficient BWT construction is closely tied to suffix sorting
- [[MoveToFrontTransform]] — common downstream stage that exploits BWT runs
- [[RunLengthEncoding]] — compresses the repeated-character runs BWT produces
- [[DataCompression]] — the broader domain motivating the transform

## Contradictions
- None — reference task page.
