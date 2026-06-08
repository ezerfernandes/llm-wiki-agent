---
title: "Bitmap/Bresenham's line algorithm (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graphics, raster-graphics, algorithm]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Bitmap/Bresenham's_line_algorithm
---

## Summary
This task asks the programmer to draw a straight line between two given points on a raster bitmap using Bresenham's line algorithm. Bresenham's method is notable because it determines which pixels to plot using only integer addition, subtraction, and comparison (via an accumulated error term), avoiding floating-point arithmetic and division entirely. It builds on the bitmap storage type defined on the companion Bitmap task.

## Task Requirements
- Use the raster image storage type defined on the [[Bitmap]] page.
- Draw a line between two supplied endpoints.
- Implement the plotting decisions using Bresenham's line algorithm.

## Language Coverage
81 languages implement this task, reflecting both the algorithm's foundational role in computer graphics and broad raster-drawing support across ecosystems. Representative implementations include C, C++, C#, Java, Python, Go, Rust, Haskell, Ada, Fortran, JavaScript, and Common Lisp.

## Connections
- [[BresenhamsLineAlgorithm]] — the core line-rasterization technique implemented here
- [[RasterGraphics]] — the pixel-grid drawing model the task operates on
- [[Bitmap]] — the underlying image storage type reused by this task
- [[IntegerArithmetic]] — Bresenham avoids floating point via integer error accumulation
- [[ComputerGraphics]] — broader field this primitive belongs to

## Contradictions
- None — reference task page.
