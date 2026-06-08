---
title: "Faces from a mesh (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, computational-geometry, graph-traversal]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Faces_from_a_mesh
---

## Summary
The task deals with two ways of representing polygonal faces of a 3D mesh: the "perimeter format" (an ordered, cyclic list of vertex numbers traced around the face) and the "edge format" (an unordered set of edges, each edge being a vertex pair listed in ascending order). The programmer must (1) determine whether two perimeter-formatted faces describe the same face, accounting for rotation and direction reversal, and (2) reconstruct an ordered perimeter from an unordered set of edges by chaining the edges together.

## Task Requirements
- Write a routine that checks whether two perimeter-formatted faces have the same perimeter, treating any rotation or reversal (anti-clockwise vs clockwise traversal) as equal; test it on the pairs Q/R and U/V.
- Write a routine that converts faces from edge format to perimeter format by walking the edges and ordering the vertices into a closed loop; test it on faces E, F, G, and H.
- Show the program's output.

## Language Coverage
17 languages implement this task, a moderate-sized set spanning systems, functional, and scripting languages. Representative implementations include C++, Go, Haskell, Java, Julia, Python, Perl, Raku, Nim, Lua, J, and Wren.

## Connections
- [[PolygonMesh]] — the underlying surface data structure being described
- [[ComputationalGeometry]] — the broader domain of representing and manipulating geometric primitives
- [[GraphTraversal]] — edge-to-perimeter conversion is effectively walking a cycle in an adjacency structure
- [[CyclicSequenceComparison]] — perimeter equality requires matching under rotation and reversal

## Contradictions
- None — reference task page.
