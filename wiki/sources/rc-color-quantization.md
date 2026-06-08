---
title: "Color quantization (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, image-processing, clustering]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Color_quantization
---

## Summary
Color quantization reduces the number of distinct colors in an image while preserving its visual appearance. Treating each RGB pixel as a point in 3D color space, the problem becomes one of cluster analysis: finding a small representative palette that best approximates the original colors. The task highlights that the palette must be derived adaptively from the image rather than chosen from a fixed predefined set.

## Task Requirements
- Take an RGB color image as input (the canonical "frog" test image).
- Reduce the image's colors to a smaller number, fewer than 256 (specifically 16 for this task).
- The palette must be adaptive to the input image, not a fixed palette like Web colors or the Windows system palette.
- Output the resulting set of chosen colors.
- Dithering is not required.

## Language Coverage
25 languages implement this task, a moderate breadth reflecting that it requires both image I/O and a clustering algorithm. Representative implementations include C, Python, Go, Rust, Haskell, Java, OCaml, Julia, Racket, and Wren.

## Connections
- [[ColorQuantization]] — the core image-processing technique this task names
- [[ClusterAnalysis]] — quantization is framed as clustering RGB points in 3D color space
- [[KMeansClustering]] — a common adaptive-palette method for choosing representative colors
- [[MedianCut]] — a classic adaptive color-quantization algorithm
- [[RasterGraphics]] — the broader category of raster image operations this task belongs to

## Contradictions
- None — reference task page.
