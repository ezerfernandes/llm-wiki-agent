---
title: "Pinstripe/Display (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graphics, test-pattern]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Pinstripe/Display
---

## Summary
This task asks the programmer to draw a series of vertical pinstripes spanning the entire width of the display, as a kind of test card. The screen is divided into four horizontal quarters, and the stripe width increases by one pixel in each successive quarter, alternating white and black bars. The key insight is mapping screen geometry (full display width and quarter-height bands) to a per-pixel toggle whose period changes by region.

## Task Requirements
- Cover the entire width of the display with vertical pinstripes.
- Top quarter: 1-pixel-wide stripes alternating white and black every pixel.
- Second quarter (from one quarter down): 2-pixel-wide stripes, alternating two white, two black.
- Third quarter (from halfway down): 3-pixel-wide stripes.
- Bottom quarter: 4-pixel-wide stripes.

## Language Coverage
45 languages implement this task, spanning low-level assembly, classic 8-bit BASIC dialects, and modern general-purpose languages. Representative implementations include 6502 Assembly, C, C++, C#, Java, Python, Go, Lua, Perl, Raku, and BBC BASIC.

## Connections
- [[ComputerGraphics]] — direct pixel-level rendering to the display
- [[TestCard]] — the pattern functions as a calibration / test image
- [[Rasterization]] — filling pixel rows and columns by coordinate
- [[ModularArithmetic]] — toggling color by pixel index modulo stripe width

## Contradictions
- None — reference task page.
