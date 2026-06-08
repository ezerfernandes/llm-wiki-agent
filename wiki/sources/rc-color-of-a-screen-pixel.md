---
title: "Color of a screen pixel (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, gui, graphics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Color_of_a_screen_pixel
---

## Summary
This task asks the programmer to read color information from an arbitrary pixel on the screen, for example the pixel currently under the mouse cursor. The mouse cursor need not be active inside a GUI created by the program. The key insight is that screen-pixel reading is an OS-level operation requiring platform-specific APIs or windowing-system bindings rather than pure language features.

## Task Requirements
- Get the color of an arbitrary screen pixel (e.g., at the current mouse cursor location).
- The mouse cursor may or may not need to be active in a GUI created by the program.
- Recognize that these functions are OS-related and depend on the underlying platform.

## Language Coverage
50 languages implement this task, reflecting broad coverage but heavy reliance on OS- and toolkit-specific bindings. Representative implementations include C, C#, C++/CLI, Java, Python, Ruby, Perl, Go, Kotlin, AutoHotkey, and Tcl.

## Connections
- [[GraphicalUserInterface]] — pixel sampling typically goes through GUI/windowing APIs
- [[RasterGraphics]] — the screen is treated as a raster of addressable pixels
- [[ColorModel]] — sampled values are reported in an RGB color representation
- [[OperatingSystemAPI]] — the task is inherently platform-dependent

## Contradictions
- None — reference task page.
