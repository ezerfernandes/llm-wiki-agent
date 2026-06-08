---
title: "Find the intersection of two lines (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, geometry, computational-geometry]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Find_the_intersection_of_two_lines
---

## Summary
The task asks the programmer to compute the single point where two lines in a 2D plane cross. Each line is defined by two points it passes through, and the goal is to find their intersection coordinates. This is a foundational primitive in collision detection and computational geometry; the key insight is converting each point-pair into a line equation (or slope-intercept form) and solving the resulting system, while guarding against parallel lines where no unique intersection exists.

## Task Requirements
- Find the point of intersection of two lines given in 2D.
- Line 1 passes through (4,0) and (6,10).
- Line 2 passes through (0,3) and (10,7).
- Report the resulting intersection point.

## Language Coverage
65 languages implement this task, showing very broad coverage spanning systems, scripting, functional, and array languages. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Common Lisp, APL, Fortran, Julia, and Wren.

## Connections
- [[ComputationalGeometry]] — line-line intersection is a core primitive of the field
- [[CollisionDetection]] — the task is framed as an introduction to detecting overlaps
- [[LinearEquations]] — solving for the intersection means solving a 2x2 linear system
- [[Slope]] — many solutions derive each line's slope and intercept from its two points

## Contradictions
- None — reference task page.
