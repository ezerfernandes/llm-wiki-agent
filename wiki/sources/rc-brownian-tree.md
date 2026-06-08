---
title: "Brownian tree (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, fractals, graphics, simulation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Brownian_tree
---

## Summary
The task asks the programmer to generate and draw a Brownian tree, a fractal-like aggregate produced by simulating diffusion-limited aggregation. The key insight is that a single fixed "seed" point grows into a branching structure as randomly wandering particles drift across the field and freeze in place the moment they touch the existing tree. Because particle placement and motion are random, every resulting tree differs in shape and no two are alike.

## Task Requirements
- Place an initial seed somewhere in the field (fixed or randomized position).
- Inject particles into the field, each following a typically random motion pattern.
- When a particle collides with the seed or the existing tree, fix its position so it becomes part of the tree.
- Render the resulting tree as a raster image.

## Language Coverage
65 languages implement this task, spanning systems languages, scripting languages, math/plotting environments, and many vintage BASIC dialects. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Lua, Mathematica/Wolfram Language, and Processing.

## Connections
- [[DiffusionLimitedAggregation]] — the physical process the simulation models
- [[RandomWalk]] — governs each particle's wandering motion
- [[Fractal]] — the self-similar branching structure produced
- [[RasterGraphics]] — the field and final tree are drawn as a pixel image
- [[CollisionDetection]] — particles freeze when they contact the tree

## Contradictions
- None — reference task page.
