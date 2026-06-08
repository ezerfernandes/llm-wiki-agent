---
title: "Bitmap/Histogram (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, image-processing, histogram]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Bitmap/Histogram
---

## Summary
This task extends the basic bitmap storage type to compute an image histogram: for each luminance value, the count of pixels having that luminance. The key practical consideration is choosing a count data type with a range of at least 0..N×M (width times height), since every pixel could share one luminance. The histogram is then applied to a black-and-white conversion that thresholds each pixel against the median luminance.

## Task Requirements
- Extend basic bitmap storage to produce an image histogram (per-luminance pixel counts).
- Use a count type whose range covers at least 0..N×M for an N-by-M image.
- As a test, convert an image to black-and-white art: convert to grayscale, compute the histogram, find the median luminance (equal pixel counts below and above), then map pixels below the median to black and the rest to white.
- Reuse the read/write PPM and grayscale-image solutions.

## Language Coverage
37 languages implement this task, spanning systems languages, functional languages, and scripting/array languages. Representative implementations include C, Ada, Rust, Go, D, Java, Kotlin, Scala, Haskell, OCaml, Common Lisp, Racket, Python, Ruby, J, and Forth.

## Connections
- [[Histogram]] — the core data structure being computed.
- [[ImageProcessing]] — the broader domain this task belongs to.
- [[Grayscale]] — luminance conversion is a prerequisite step.
- [[Thresholding]] — median-based black-and-white conversion is a thresholding operation.
- [[Median]] — the median luminance is the threshold value.

## Contradictions
- None — reference task page.
