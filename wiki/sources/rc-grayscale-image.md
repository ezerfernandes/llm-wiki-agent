---
title: "Grayscale image (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graphics, image-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Grayscale_image
---

## Summary
This task extends the basic bitmap storage type to support grayscale images, requiring two conversion operations: color-to-grayscale and grayscale-to-color. The core insight is computing luminance using the CIE-recommended weighted formula L = 0.2126·R + 0.7152·G + 0.0722·B, which reflects the human eye's differing sensitivity to red, green, and blue. Care must be taken with rounding when storing the floating-point luminance back into an unsigned integer channel.

## Task Requirements
- Extend the bitmap storage type (from the Basic bitmap storage task) to hold grayscale images.
- Implement a function converting a color image to grayscale.
- Implement a function converting a grayscale image back to color.
- Compute luminance via L = 0.2126·R + 0.7152·G + 0.0722·B.
- Handle floating-point rounding so the stored unsigned-integer luminance is neither erroneous nor distorted.

## Language Coverage
63 languages implement this task, spanning systems languages, scripting languages, and math/array-oriented tools. Representative examples include C, C#, Java, Python, Go, Haskell, Ruby, Perl, OCaml, J, and MATLAB.

## Connections
- [[ImageProcessing]] — grayscale conversion is a foundational preprocessing step.
- [[Luminance]] — the perceptual brightness quantity being computed.
- [[ColorSpace]] — RGB-to-luminance is a projection within color-space transformations.
- [[RasterGraphics]] — operates on pixel-based bitmap storage.

## Contradictions
- None — reference task page.
