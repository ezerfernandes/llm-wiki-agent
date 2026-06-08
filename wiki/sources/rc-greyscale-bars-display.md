---
title: "Greyscale bars/Display (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graphics, test-card]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Greyscale_bars/Display
---

## Summary
The task asks the programmer to render a display-spanning test card composed of four horizontal quarters, each filled with vertical greyscale (contrast) bars. The number of bars doubles per quarter (8, 16, 32, 64), and each row alternates its gradient direction so that adjacent quarters meet at opposite shades. The key insight is mapping a bar's index to an evenly spaced grey level between black and white, then flipping the direction (ascending vs. descending) on alternating rows.

## Task Requirements
- Fill the display with vertical greyscale bars spanning its full width.
- Top quarter: 8 bars, left black stepping through six greys to white on the right.
- Second quarter: 16 bars, starting white and darkening to black on the right.
- Third quarter (halfway down): 32 bars, starting black and ending white.
- Bottom quarter: 64 bars, starting white and ending black in the bottom-right corner.

## Language Coverage
54 languages implement this task, spanning native GUI/canvas toolkits, BASIC dialects, and functional languages. Representative implementations include C, C++, C#, Java, JavaScript, Python, Haskell, OCaml, Go, Lua, Processing, and several BASIC variants such as FreeBASIC and ZX Spectrum Basic.

## Connections
- [[ComputerGraphics]] — rendering bars to a raster display surface
- [[TestCard]] — the greyscale contrast bars are a classic calibration pattern
- [[LinearInterpolation]] — evenly spacing grey levels across each row
- [[ColorQuantization]] — discretizing the black-to-white range into N steps

## Contradictions
- None — reference task page.
