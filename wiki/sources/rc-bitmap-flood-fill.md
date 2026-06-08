---
title: "Bitmap/Flood fill (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graphics, algorithms, recursion]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Bitmap/Flood_fill
---

## Summary
This task asks the programmer to implement flood fill, an algorithm that fills a contiguous region of a bitmap starting from a seed pixel. Filling spreads from the seed to neighboring pixels that share a target color (or stay within color "banks"), behaving like water flowing through a valley until it hits boundaries. The key insight is that the region is defined by pixel connectivity and color matching, not by explicit geometry — and a tolerance parameter can extend the basic algorithm to truecolor images.

## Task Requirements
- Implement at least one flood fill algorithm (e.g., the recursive or queue/stack-based variants described on Wikipedia).
- Fill spreads outward from a seed point to connected pixels matching a target color or bounded by color banks.
- Variations are explicitly allowed, such as adding a tolerance parameter for color matching of the banks/target color (needed for truecolor images, where the naive algorithm is unsuitable).
- Test against a sample image (e.g., the unfilled-circle image), filling the white area or the inner black circle.

## Language Coverage
54 languages implement this task, spanning low-level systems languages, high-level scripting, and array/functional styles. Representative examples include C, C++, C#, Java, Rust, Go, Python, Ruby, Haskell, OCaml, and J.

## Connections
- [[FloodFill]] — the core algorithm this task implements
- [[Recursion]] — the classic four-way recursive fill formulation
- [[BreadthFirstSearch]] — queue-based fills are effectively a BFS over connected pixels
- [[RasterGraphics]] — the bitmap/pixel-grid domain the task operates on
- [[ConnectedComponents]] — flood fill identifies a connected region of like-colored pixels

## Contradictions
- None — reference task page.
