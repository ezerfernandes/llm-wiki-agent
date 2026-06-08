---
title: "Colour pinstripe/Printer (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graphics, printing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Colour_pinstripe/Printer
---

## Summary
The task is to send a colour test pattern to a graphics printer, drawing 1-point-wide vertical pinstripes that cycle through each ink cartridge and ink pair plus black and white (e.g. black, red, green, blue, magenta, cyan, yellow, white), repeated across the full page width. After the first inch the stripe width grows to 2 points, then 3, then 4, and so on for each successive inch down the page, after which the page is ejected. The key insight is mapping logical "points" to whatever marking resolution the language/printer exposes, falling back to the smallest available mark or prompting for resolution when native DPI is unknown.

## Task Requirements
- Draw 1-point-wide vertical colour pinstripes spanning the full printer width.
- Cycle stripe colours through each individual ink and ink pair, including black and white (typical sequence: black, red, green, blue, magenta, cyan, yellow, white).
- After the first inch, increase stripe width to 2 points; widen by one more point for each subsequent inch.
- Continue for the full page length (or 12 inches on continuous-roll printers), then eject/advance the page clear.
- Acceptable to use the smallest marks the language offers rather than native printer resolution.
- Optionally prompt the user for printer resolution where it cannot be detected, allowing fractional point sizes.

## Language Coverage
14 languages implement this task, mostly via OS print APIs, PostScript generation, or printer device contexts rather than direct hardware control. Representative implementations include Ada, Go, Julia, Nim, Phix, PicoLisp, Python, Racket, Raku, and Tcl.

## Connections
- [[ColourPinstripeDisplay]] — companion screen-based variant of the same colour-bar pattern
- [[RGBColorModel]] — the additive ink/colour combinations defining the stripe sequence
- [[PostScript]] — common output target for sending the vector pinstripe pattern to a printer
- [[RasterGraphics]] — mapping logical points onto printer dots/marks
- [[DotsPerInch]] — resolution conversion driving stripe width per inch

## Contradictions
- None — reference task page.
