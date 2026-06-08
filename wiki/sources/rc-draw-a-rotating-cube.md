---
title: "Draw a rotating cube (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graphics, 3d-rendering, animation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Draw_a_rotating_cube
---

## Summary
This task asks the programmer to render and animate a cube spinning in 3D space. The cube must be oriented along its main diagonal — one vertex pointing straight up and the diametrically opposite vertex pointing straight down — then continuously rotated. The key insight is reorienting the cube onto its body diagonal (a rotation onto the [1,1,1] axis) before applying the spin, and projecting the rotating 3D vertices down to a 2D display each frame.

## Task Requirements
- Draw a cube and animate it rotating.
- Orient it with one vertex pointing straight up and the opposite (main-diagonal) vertex straight down.
- Rendering may be solid or wire-frame; ASCII art is acceptable if the language lacks graphics.
- Perspective projection is optional.

## Language Coverage
44 languages implement this task, spanning compiled, scripting, and graphics-oriented languages as well as ASCII-only fallbacks. Representative implementations include C, C#, Go, Haskell, Java, JavaScript, Julia, Python, Perl, Raku, Processing, and PostScript.

## Connections
- [[RotationMatrix]] — applying 3D rotation matrices to vertices each frame
- [[3DProjection]] — mapping rotating 3D points onto a 2D screen
- [[LinearAlgebra]] — vector and matrix math underpinning the transforms
- [[ComputerGraphics]] — wire-frame/solid rendering and animation loop
- [[DrawACuboid]] — closely related Rosetta Code drawing task

## Contradictions
- None — reference task page.
