---
title: "Animated Spinners (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graphics, animation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Animated_Spinners
---

## Summary
The task is to create and display five animated spinners on screen — one centered with four surrounding it. Each spinner is rendered by drawing radius lines emanating from a center axis, then repeatedly redrawing the figure with the active "clock hand" advanced around the circle. When this loop runs fast enough, persistence of vision produces the illusion of a smooth spinning motion. The key insight is that animation is achieved purely by looping the draw routine quickly rather than by any special motion primitive.

## Task Requirements
- Create and display five spinners: one in the middle and four surrounding it.
- Draw each spinner as radius lines arranged around a center axis.
- Loop through the drawing to animate a moving clock-hand effect; faster loops give a better illusion.
- Stretch goal: offset the spinners in response to mouse movement (extra credit).

## Language Coverage
17 languages implement this task, spanning systems, scripting, and BASIC-family languages with graphics support. Representative implementations include Ada, C, Go, Java, Julia, Nim, Perl, Python, Raku, and Wren.

## Connections
- [[ComputerGraphics]] — the task is fundamentally a 2D rendering exercise.
- [[Animation]] — the moving illusion is produced by a fast redraw loop.
- [[PolarCoordinates]] — radius lines around a center axis are naturally expressed via angle/radius.
- [[GameLoop]] — the repeated draw-and-advance cycle is a classic frame loop.
- [[EventHandling]] — the stretch goal requires capturing mouse-movement input.

## Contradictions
- None — reference task page.
