---
title: "Polyspiral (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graphics, geometry, animation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Polyspiral
---

## Summary
A polyspiral is a spiral built from a sequence of connected line segments, where each successive segment grows (or shrinks) by a fixed amount and turns by a fixed incremental angle. The task is to animate a family of polyspirals by drawing a full spiral, slightly increasing the turn-angle increment, clearing the screen, and redrawing — each spiral forming one animation frame. The key insight is that compounding a constant angular increment per segment produces the characteristic curling spiral form, and slowly sweeping that increment yields a continuously morphing animation.

## Task Requirements
- Draw a spiral from multiple line segments where each segment's length changes by a fixed delta and its heading rotates by a per-segment angle.
- Per the pseudocode: start length 5, grow length by 3 each segment, iterate ~150 segments, accumulating the angle modulo 360.
- Animate by incrementing the base angle (e.g. by 0.05, mod 360) each frame, clearing the background between frames; the animation may loop once full-circle or run indefinitely.
- If animation is impractical in the environment, a single static frame is acceptable.

## Language Coverage
43 languages implement this task, spanning native graphics toolkits, canvas/web rendering, and turtle-style drawing. Representative implementations include C, C++, C#, Java, JavaScript, Python, Haskell, Go, Lua, Processing, and SVG.

## Connections
- [[Spiral]] — the geometric figure being constructed
- [[TurtleGraphics]] — the move-and-turn drawing model the pseudocode follows
- [[ComputerAnimation]] — frame-by-frame redraw with background clearing
- [[ParametricCurve]] — segment endpoints derived from accumulated angle and length
- [[ModularArithmetic]] — angles tracked modulo 360 degrees

## Contradictions
- None — reference task page.
