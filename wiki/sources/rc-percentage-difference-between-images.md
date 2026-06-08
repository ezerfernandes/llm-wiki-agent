---
title: "Percentage difference between images (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, image-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Percentage_difference_between_images
---

## Summary
This task asks the programmer to compute a single percentage value expressing how different two same-size images are. The core idea is to sum the absolute differences of every color channel across all pixels, then normalize that total against the maximum possible difference (every pixel maximally different on every channel). It is presented as useful for quantifying the loss introduced when re-saving a JPEG at a lower compression quality.

## Task Requirements
- Compare two images (e.g. JPEGs, or two bitmaps as defined in basic bitmap storage) of identical dimensions.
- For each pixel, accumulate the absolute difference of each color component.
- Normalize the accumulated difference to a percentage of the theoretical maximum difference.
- For the supplied 50%-quality and 100%-quality Lenna test images, the expected result is 1.62125%.

## Language Coverage
45 languages implement this task, spanning systems languages, functional languages, and scripting/math environments. Representative examples include C, C++, C#, D, Go, Rust, Java, Python, Haskell, OCaml, Common Lisp, and Mathematica/Wolfram Language.

## Connections
- [[ImageProcessing]] — the task is a basic image-analysis operation
- [[BasicBitmapStorage]] — the referenced pixel-storage model the comparison runs over
- [[MeanAbsoluteError]] — the underlying metric being computed and normalized
- [[Normalization]] — scaling the summed difference to a 0–100% range

## Contradictions
- None — reference task page.
