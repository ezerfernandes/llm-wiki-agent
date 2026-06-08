---
title: "Fractal tree (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, fractals, recursion, graphics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Fractal_tree
---

## Summary
The task asks the programmer to generate and draw a fractal tree: start by drawing a trunk, then at the end of each branch split off by some fixed angle into two new branches, recursing until a chosen depth is reached. The key insight is that a self-similar branching structure emerges naturally from a simple recursive routine that shortens each successive segment and rotates left and right by a constant angle.

## Task Requirements
- Draw the trunk.
- At the end of the trunk, split by some angle and draw two branches.
- Repeat at the end of each branch until a sufficient level of branching is reached.

## Language Coverage
83 languages implement this task, showing very broad coverage across general-purpose, functional, and graphics-oriented environments. Representative implementations include C, C++, Java, JavaScript, Python, Haskell, Lua, Go, Rust, Scheme, and PostScript.

## Connections
- [[Recursion]] — each branch recursively spawns two shorter branches.
- [[Fractals]] — the tree is self-similar across scales.
- [[Turtle Graphics]] — many solutions advance and rotate a pen by a fixed angle.
- [[Pythagoras Tree]] — a closely related fractal branching task.

## Contradictions
- None — reference task page.
