---
title: "Total circles area (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, computational-geometry, numerical-integration]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Total_circles_area
---

## Summary
Given a set of partially overlapping circles (disks) on the plane, compute the total area covered by their union, where regions covered by two or more disks are counted only once. The task supplies a standard 25-disk dataset (11 of which are fully contained inside others) and the known answer 21.56503660..., requested to four or six decimal digits. A key point of the task is comparing solution strategies, since some approaches are simple but slow (e.g. grid/Monte Carlo sampling) while others are fast but mathematically intricate (analytic union-of-circles via the Green's theorem / arc-integration approach).

## Task Requirements
- Compute and display the area of the union of a given set of circles to about four to six decimal digits of precision.
- Count any overlapping region only once, regardless of how many disks cover it.
- Solve against the provided standard dataset (25 disks with x, y center coordinates and radii).
- Verify the result against the expected value 21.56503660....
- Discuss relative merits of strategies (performance, precision, simplicity); keeping both slow and fast solutions per language is welcome.

## Language Coverage
38 languages implement this task, spanning systems languages, scripting languages, functional languages, and array/symbolic environments. Representative implementations include C, C++, C#, Java, Python, Go, Haskell, Julia, Perl, Raku, Fortran, and Mathematica/Wolfram Language.

## Connections
- [[ComputationalGeometry]] — the task is a union-of-disks area problem.
- [[NumericalIntegration]] — common solutions integrate covered area by scanning lines or sampling a grid.
- [[MonteCarloMethod]] — random-sampling approaches estimate the covered fraction of the bounding box.
- [[GreensTheorem]] — analytic solutions reduce the area to a contour integral over visible circular arcs.
- [[InclusionExclusionPrinciple]] — the conceptual basis for avoiding double-counting overlapping regions.

## Contradictions
- None — reference task page.
