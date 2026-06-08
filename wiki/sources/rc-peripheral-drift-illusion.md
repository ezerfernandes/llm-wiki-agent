---
title: "Peripheral drift illusion (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graphics, optical-illusion]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Peripheral_drift_illusion
---

## Summary
The task asks the programmer to generate and display a peripheral drift illusion: a perfectly static image that appears to move when viewed, particularly with peripheral vision. The key insight is that the illusory motion arises from carefully ordered gradients of luminance (typically repeating sequences such as black–dark–white–light tiles) arranged so the eye perceives drift even though no pixel ever changes.

## Task Requirements
- Generate and render a static image that produces the peripheral drift illusion (the image seems to move while remaining perfectly static).
- Provide a link to the output via an online run or an uploaded screenshot demonstrating the effect.

## Language Coverage
18 languages implement this task, spanning compiled, scripting, and graphics-oriented environments. Representative implementations include Java, Python, Julia, Perl, Raku, Nim, FreeBASIC, Phix, Wren, and Octave.

## Connections
- [[ComputerGraphics]] — the task is fundamentally a 2D rendering exercise.
- [[OpticalIllusion]] — the perceived motion is a visual perception phenomenon, not real movement.
- [[LuminanceGradient]] — ordered luminance steps in each tile drive the illusory drift.
- [[ColorModel]] — assembling the repeating black/dark/light/white palette relies on color value manipulation.

## Contradictions
- None — reference task page.
