---
title: "Zhang-Suen thinning algorithm (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, image-processing, morphology]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Zhang-Suen_thinning_algorithm
---

## Summary
The task asks the programmer to implement the Zhang-Suen thinning (skeletonization) algorithm, which reduces the black regions of a binary (one-bit-per-pixel) image to a one-pixel-wide skeleton. The key insight is that pixels are deleted iteratively based on local 8-neighbourhood conditions, and crucially the deletions are applied only after each full pass so that the order of pixel processing does not corrupt the result. The process alternates between two slightly different deletion sub-iterations and repeats until no pixel changes.

## Task Requirements
- Treat black pixels as 1 and white as 0 on a rectangular N-by-M matrix.
- For each interior black pixel P1 with its eight neighbours P2..P9, compute B(P1) (count of black neighbours) and A(P1) (number of 0→1 transitions around the circular sequence P2..P9,P2).
- Step 1: mark a black pixel for deletion if it has eight neighbours, 2 ≤ B(P1) ≤ 6, A(P1) = 1, at least one of P2/P4/P6 is white, and at least one of P4/P6/P8 is white; then set all marked pixels white.
- Step 2: repeat with the conditions changed to "at least one of P2/P4/P8 white" and "at least one of P2/P6/P8 white"; then set all marked pixels white.
- Repeat both steps until an iteration changes no pixels.
- Run the routine on the provided sample image and display the thinned output as a matrix or ASCII art.

## Language Coverage
37 languages implement this task, spanning systems languages, scripting languages, and array/functional languages. Representative implementations include C, C++, D, Go, Java, Python, Haskell, Julia, Ruby, Perl, Raku, and the array language J.

## Connections
- [[ImageProcessing]] — operates on binary raster images
- [[MathematicalMorphology]] — thinning is a classic morphological operation
- [[Skeletonization]] — Zhang-Suen produces a one-pixel-wide skeleton
- [[IterativeAlgorithm]] — repeats passes until a fixed point is reached
- [[BinaryImage]] — input is one bit per pixel

## Contradictions
- None — reference task page.
