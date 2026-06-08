---
title: "OpenGL (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graphics, 3d-rendering, gpu]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/OpenGL
---

## Summary
This task asks the programmer to use the OpenGL API to display a single triangle whose interior is smooth (Gouraud) shaded — each vertex is given a distinct color and OpenGL interpolates the colors across the face. The key insight is that smooth shading is achieved by assigning per-vertex color attributes and letting the rasterizer blend them, rather than filling the polygon with a single flat color.

## Task Requirements
- Use OpenGL to render a triangle.
- Apply smooth (per-vertex interpolated) shading rather than flat shading.
- Typically involves setting up a window/context (often via a toolkit such as GLUT/freeglut), defining three vertices with associated colors, and drawing the triangle primitive.

## Language Coverage
49 languages implement this task, spanning systems languages, scripting languages, and BASIC dialects, since OpenGL has bindings almost everywhere. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, OCaml, Common Lisp, and Lua.

## Connections
- [[OpenGL]] — the cross-platform graphics API the task exercises
- [[GouraudShading]] — the per-vertex color interpolation technique requested
- [[Rasterization]] — how the triangle's pixels are generated and shaded
- [[3DRendering]] — the broader graphics domain this task belongs to
- [[GLUT]] — the windowing toolkit commonly used to create the context

## Contradictions
- None — reference task page.
