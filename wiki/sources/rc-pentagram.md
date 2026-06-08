---
title: "Pentagram (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, computational-geometry, graphics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Pentagram
---

## Summary
The task is to draw or print a regular pentagram — a five-pointed star polygon formed by a central pentagon with an isosceles triangle on each of its sides, where each star-point vertex measures 36 degrees. The key idea is computing the five vertex coordinates (typically by stepping around a circle in 144-degree increments so the connecting edges trace the star) and rendering them with distinct stroke, fill, and background colors or tokens.

## Task Requirements
- Draw (or print) a regular pentagram in any orientation.
- Use a different color (or token) for the stroke, the fill, and the background.
- For the fill, treat all points inside the triangles and the central pentagon as inside the pentagram.

## Language Coverage
41 languages implement this task, spanning graphical/turtle approaches and ASCII/text renderings. Representative implementations include C, Java, Python, Go, Haskell, Perl, Raku, Lua, PostScript, and Processing.

## Connections
- [[StarPolygon]] — a pentagram is the {5/2} star polygon this task constructs.
- [[RegularPolygon]] — the star is built around a central regular pentagon.
- [[GoldenRatio]] — pentagram segment lengths divide in the golden ratio.
- [[ComputationalGeometry]] — vertex coordinates come from points evenly spaced on a circle.
- [[TurtleGraphics]] — a common rendering technique stepping by the 144-degree exterior angle.

## Contradictions
- None — reference task page.
