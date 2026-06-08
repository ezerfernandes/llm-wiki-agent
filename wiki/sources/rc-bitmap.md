---
title: "Bitmap (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graphics, data-structures]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Bitmap
---

## Summary
This task asks the programmer to define a basic in-memory storage type for a simple RGB raster image plus the primitive operations that act on it. The key insight is that almost all raster graphics work reduces to a 2D array of color triples, so a clean bitmap abstraction (allocate, fill, set-pixel, get-pixel) becomes the shared foundation for every higher-level drawing task.

## Task Requirements
- Define a storage type capable of holding a simple RGB raster image.
- Provide a function to allocate an uninitialised image given its width and height.
- Provide a function to fill the whole image with a single plain RGB color.
- Provide a function to set a given pixel to a color.
- Provide a function to get the color of a given pixel.
- Explain any specificities of the chosen storage or allocation scheme.

## Language Coverage
95 languages implement this task, reflecting its role as the base type for the entire raster graphics category; coverage spans systems languages (C, C++, Rust, Zig, Ada), managed/functional languages (Java, C#, Haskell, OCaml, Scala, Racket), scripting languages (Python, Ruby, Perl, Lua, JavaScript), and many BASIC dialects.

## Connections
- [[RasterGraphics]] — the bitmap is the foundational storage type for this category of tasks.
- [[RGBColorModel]] — each pixel is stored as a red/green/blue triple.
- [[TwoDimensionalArray]] — the image is conceptually a 2D grid of pixels.
- [[WritePpmFile]] — companion task that outputs a bitmap so results can be verified.

## Contradictions
- None — reference task page.
