---
title: "Colour pinstripe/Display (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graphics, color]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Colour_pinstripe/Display
---

## Summary
The task asks the programmer to fill the graphics display with vertical coloured pinstripes that cycle through a fixed colour sequence (black, red, green, blue, magenta, cyan, yellow, white) or the system palette. The display is divided into four horizontal bands: the stripe width grows from 1 pixel in the top quarter, to 2, then 3, and finally 4 pixels wide in the bottom quarter. The key insight is mapping a horizontal pixel position to a colour index based on the band's current stripe width.

## Task Requirements
- Draw 1-pixel-wide coloured vertical pinstripes spanning the full display width.
- Cycle stripe colours through the system palette or the sequence: black, red, green, blue, magenta, cyan, yellow, white.
- After the top quarter, switch to 2-pixel-wide stripes.
- Halfway down, switch to 3-pixel-wide stripes.
- For the final (bottom) quarter, use 4-pixel-wide stripes.

## Language Coverage
51 languages implement this task, spanning low-level assembly (6502 Assembly, ARM Assembly, MIPS Assembly), systems languages (C, C++, Ada, Go, Nim), JVM/scripting languages (Java, Kotlin, Scala, Python, Perl, Lua, Tcl), and several BASIC dialects (FreeBASIC, PureBasic, Yabasic, SmileBASIC), reflecting broad coverage across graphics-capable platforms.

## Connections
- [[ComputerGraphics]] — the task is fundamentally about drawing to a raster display.
- [[ColorPalette]] — stripes cycle through a fixed or system colour palette.
- [[RasterScan]] — colours are assigned per pixel column across the screen width.
- [[ModularArithmetic]] — stripe colour index is the column position modulo the palette size.

## Contradictions
- None — reference task page.
