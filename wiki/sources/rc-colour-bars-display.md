---
title: "Colour bars/Display (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graphics, color]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Colour_bars/Display
---

## Summary
This task asks the programmer to draw a series of vertical colour bars spanning the full width of the display, similar to a television test pattern. The bars must use either the host system's palette or a fixed eight-colour sequence (black, red, green, blue, magenta, cyan, yellow, white). The core challenge is accessing the display surface and dividing its width evenly into coloured regions.

## Task Requirements
- Display vertical colour bars across the entire width of the screen.
- Use either the system palette, or the explicit sequence: black, red, green, blue, magenta, cyan, yellow, white.
- Bars should fill the display vertically and be distributed across its horizontal extent.

## Language Coverage
55 languages implement this task, spanning low-level assembly, classic BASIC dialects, functional languages, and modern general-purpose languages — reflecting the variety of graphics and terminal APIs available. Representative implementations include 6502 Assembly, C, C++, Go, Java, Python, Haskell, Racket, Rust, Lua, Perl, and Processing.

## Connections
- [[ComputerGraphics]] — rendering coloured regions to a display surface
- [[ColorModels]] — the RGB primaries and secondaries used for the bar sequence
- [[ColorPalette]] — the alternative of using the host system palette
- [[TestPattern]] — colour bars are a classic video/TV calibration pattern

## Contradictions
- None — reference task page.
