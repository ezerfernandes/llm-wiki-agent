---
title: "Galton box animation (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, animation, probability, simulation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Galton_box_animation
---

## Summary
The task is to build an animated simulation of a Galton box (a "bean machine" or "quincunx"), where balls drop through a triangular grid of pins, deflecting left or right at each pin until they settle into collection bins at the bottom. The key insight is that the accumulated ball heights in the bins approximate a normal distribution (a bell curve), with the number of paths to each bin matching Pascal's triangle. The challenge combines randomness, real-time animation, and managing multiple balls in flight without collisions.

## Task Requirements
- The box must have at least 5 pins on the bottom row.
- The solution may use graphics or ASCII animation.
- Provide a sample of the output/display (e.g. a screenshot).
- One or more balls may be in flight simultaneously.
- If multiple balls are in flight, they must not interfere with each other.
- Allow the user to specify the number of balls, or run until full / a preset limit.
- Optionally display the number of balls.

## Language Coverage
39 languages implement this task, spanning systems languages, scripting languages, functional languages, and many BASIC dialects. Representative implementations include C, C++, Go, Java, JavaScript, Python, Haskell, Clojure, Lua, and Wren.

## Connections
- [[NormalDistribution]] — the limiting shape of the ball heights in the bins
- [[PascalsTriangle]] — counts the number of paths to each bin
- [[BinomialDistribution]] — exact distribution of left/right deflections
- [[RandomNumberGeneration]] — drives each pin's left/right deflection
- [[Animation]] — the simulation must be rendered frame-by-frame over time

## Contradictions
- None — reference task page.
