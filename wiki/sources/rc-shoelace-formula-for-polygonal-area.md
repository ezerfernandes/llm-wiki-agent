---
title: "Shoelace formula for polygonal area (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, computational-geometry]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Shoelace_formula_for_polygonal_area
---

## Summary
This task asks the programmer to implement the Shoelace formula (also called the surveyor's formula or Gauss's area formula), which computes the area of a simple polygon from the ordered coordinates of its vertices. The key insight is that the area equals half the absolute value of the sum of cross-products of consecutive vertex coordinates, walking around the polygon's boundary. It works for any simple (non-self-intersecting) polygon without needing to decompose it into triangles.

## Task Requirements
- Write a function/method/routine implementing the Shoelace formula.
- Compute area as `abs( sum(x[i]*y[i+1]) - sum(x[i+1]*y[i]) ) / 2`, wrapping the last vertex back to the first.
- Apply it to the specific polygon with vertices (3,4), (5,11), (12,8), (9,5), (5,6).
- Display the resulting area (the expected answer is 30).

## Language Coverage
63 languages implement this task, spanning systems, scripting, functional, and array languages as well as several historical and assembly dialects. Representative examples include C, C++, Rust, Go, Java, Python, Haskell, J, APL, and Fortran.

## Connections
- [[ShoelaceFormula]] — the named algorithm this task implements
- [[ComputationalGeometry]] — the field concerned with polygon area and related calculations
- [[Polygon]] — the geometric object whose area is measured
- [[CrossProduct]] — the pairwise term summed across consecutive vertices

## Contradictions
- None — reference task page.
