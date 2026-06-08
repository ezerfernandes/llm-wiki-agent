---
title: "Voronoi diagram (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, computational-geometry, graphics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Voronoi_diagram
---

## Summary
The task is to generate and display a Voronoi diagram from a set of points called sites. A Voronoi diagram partitions the plane into cells, one per site, where each cell contains exactly the points that are closer to its site than to any other. The simplest implementation insight is brute force: for every pixel, assign it the color of its nearest site, which directly visualizes the cells without computing analytic cell boundaries.

## Task Requirements
- Define a set of Voronoi sites (typically random points).
- For each location in the plane, determine the nearest site (its Voronoi cell).
- Generate and display the resulting diagram, usually as a colored image where each cell gets a distinct color.

## Language Coverage
48 languages implement this task, spanning systems, scripting, functional, and BASIC-family languages with graphics support. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Julia, Lua, and Racket.

## Connections
- [[VoronoiDiagram]] — the geometric structure the task constructs.
- [[NearestNeighborSearch]] — each pixel is assigned to its closest site.
- [[EuclideanDistance]] — the standard metric defining cell membership.
- [[KMeansClustering]] — the task references K-means++ as a related algorithm.
- [[DelaunayTriangulation]] — the geometric dual of the Voronoi diagram.

## Contradictions
- None — reference task page.
