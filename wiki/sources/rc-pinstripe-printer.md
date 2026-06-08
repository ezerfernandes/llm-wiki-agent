---
title: "Pinstripe/Printer (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graphics, printing, test-card]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Pinstripe/Printer
---

## Summary
The task asks the programmer to send a printer test card to an actual printer (or print-to-file equivalent). The pattern is a series of vertical pinstripes alternating one point of white and one point of black across the full page width. The key twist is that the stripe width grows by one point after each inch of vertical travel: 1-point stripes for the first inch, 2-point for the second, 3-point for the third, and so on for the page length (or 12 inches on continuous-roll stationery), after which the page is ejected.

## Task Requirements
- Produce vertical pinstripes 1 point wide, alternating white and black, spanning the full printed page width (last partial stripe excepted).
- After each inch of run length, widen the stripes by one more point (2 pt for the second inch, 3 pt for the third, etc.).
- Continue the trend for the full page length, or 12 inches on continuous-roll printers.
- Eject the page (or roll the pattern clear) after printing.
- Pixels may substitute for points where the printer cannot address points; smallest available marks are acceptable.
- Optionally prompt the user for printer resolution to compute point size when it cannot be auto-detected.

## Language Coverage
13 languages implement this task, a relatively small set reflecting that it requires real printer/device output rather than pure computation. Representative implementations include Ada, Go, Julia, Nim, Phix, PicoLisp, Racket, Raku, Tcl, and Wren, alongside several BASIC dialects (BBC BASIC, FreeBASIC, Liberty BASIC).

## Connections
- [[PrinterTestCard]] — this is the printer-output sibling of the screen-based pinstripe test pattern
- [[DeviceResolution]] — converting inches to printable points/pixels depends on the printer DPI
- [[GraphicsRendering]] — drawing alternating black/white vertical bars
- [[PostScript]] — common page-description language used to express such printer test patterns

## Contradictions
- None — reference task page.
