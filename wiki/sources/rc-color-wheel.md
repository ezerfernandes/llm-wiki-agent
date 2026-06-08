---
title: "Color wheel (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graphics, color]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Color_wheel
---

## Summary
The task asks the programmer to write a function that procedurally draws a complete HSV color wheel entirely in code. The key insight is mapping each pixel inside a circle to a color: the angle around the center determines the hue, and the distance from the center determines the saturation, while value (brightness) is typically held constant. The page notes this is purely educational, since real applications should use a precomputed image because per-pixel procedural drawing is slow.

## Task Requirements
- Write a function that draws a full HSV color wheel.
- Compute each color from polar coordinates: hue from the angle, saturation from the radius.
- Convert the resulting HSV values to RGB for display.
- Intended strictly for learning how color wheels and color-from-position lookups work.

## Language Coverage
47 languages implement this task, spanning systems languages, scripting languages, BASIC dialects, and even pure HTML/CSS, reflecting its appeal as a graphics learning exercise. Representative implementations include C, C++, C#, Go, Rust, Java, Python, Julia, Perl, Raku, Lua, and Processing.

## Connections
- [[HSVColorModel]] — the color space the wheel visualizes
- [[HSVtoRGBConversion]] — needed to render computed colors to a display
- [[PolarCoordinates]] — angle and radius map to hue and saturation
- [[RasterGraphics]] — per-pixel drawing technique used to fill the wheel

## Contradictions
- None — reference task page.
