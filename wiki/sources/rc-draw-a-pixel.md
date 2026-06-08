---
title: "Draw a pixel (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graphics, gui]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Draw_a_pixel
---

## Summary
This task asks the programmer to open a graphical window and set a single pixel within it to a specific color. The key insight is that it exercises the most minimal possible graphics operation, forcing each language to demonstrate how it creates a window/canvas and addresses individual pixels through whatever graphics library or framebuffer it has available.

## Task Requirements
- Create a window sized 320 x 240.
- Draw a single pixel colored red, with RGB value (255, 0, 0).
- Position the pixel at coordinates x = 100, y = 100.

## Language Coverage
72 languages implement this task, spanning systems languages, scripting languages, and a wide variety of BASIC dialects. Representative implementations include C, Rust, Go, Java, Python, OCaml, Lua, Ruby, Perl, and FreeBASIC, alongside assembly versions (ARM Assembly, X86 Assembly) showing direct framebuffer manipulation.

## Connections
- [[RasterGraphics]] — addressing individual pixels in a 2D bitmap
- [[GraphicalUserInterface]] — creating and displaying a window
- [[ColorModel]] — specifying color via an RGB triple
- [[CoordinateSystem]] — locating the pixel by (x, y)

## Contradictions
- None — reference task page.
