---
title: "Plasma effect (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graphics, trigonometry]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Plasma_effect
---

## Summary
The plasma effect is a classic demoscene visual produced by summing several sine and cosine functions of a pixel's x and y coordinates (and optionally time) to compute a smoothly varying value, which is then mapped to a color. The key insight is that overlapping periodic functions create organic, fluid-looking color gradients without any underlying physical simulation. When the functions are offset by an animated time term, the static gradient appears to flow like a colorful liquid.

## Task Requirements
- Create a plasma effect by applying functions such as sine and cosine to pixel color values across the screen.
- Animation is explicitly noted as not a requirement; a single static plasma image suffices.

## Language Coverage
35 languages implement this task, spanning systems and graphics-capable languages alongside scripting and functional ones. Representative implementations include C, C++, Rust, Go, Java, JavaScript, Python, Lua, Processing, Raku, and Racket.

## Connections
- [[Trigonometry]] — sine and cosine functions drive the pixel value computation
- [[ProceduralGeneration]] — texture/color fields generated algorithmically rather than stored
- [[ColorMapping]] — scalar field values are mapped to RGB colors, often via HSV or a palette
- [[Demoscene]] — the effect originates from real-time graphics demos
- [[RasterGraphics]] — operates per-pixel over a 2D bitmap

## Contradictions
- None — reference task page.
