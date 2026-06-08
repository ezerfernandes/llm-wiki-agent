---
title: "Weiler-Atherton polygon clipping (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, computational-geometry, graphics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Weiler-Atherton_polygon_clipping
---

## Summary
The task is to implement the Weiler-Atherton algorithm, which clips a subject polygon against a clip polygon to produce their intersection (one or more output polygons). Unlike the simpler Sutherland-Hodgman algorithm, it handles arbitrary non-convex polygons. The key insight is to find all edge intersection points, splice them into linked vertex lists for both polygons with cross-pointers, then walk the boundaries — switching between the subject and clip polygons at intersections to trace out each closed result region.

## Task Requirements
- Find all intersection points where subject polygon edges cross clip polygon edges.
- Insert those intersection points into both polygons' vertex lists between the appropriate vertices, with pointers linking each occurrence across the two lists.
- Traverse boundaries starting at an intersection: follow the subject polygon while inside the clip region, switch to the clip polygon when crossing from inside to outside, and continue until returning to the start.
- Repeat for each unvisited intersection point to emit multiple closed output polygons when they exist.
- Algorithm cost is O(n × m) for n and m vertices.

## Language Coverage
13 languages implement this task, reflecting moderate coverage typical of a more involved computational-geometry problem. Representative implementations include C#, C++, Fortran, Go, Java, JavaScript, Julia, Rust, Scala, and Wren.

## Connections
- [[ComputationalGeometry]] — the broader field this clipping task belongs to
- [[PolygonClipping]] — the general operation being performed
- [[SutherlandHodgmanAlgorithm]] — simpler convex-only clipping algorithm contrasted here
- [[GreinerHormannClipping]] — related extension with improved numerical robustness
- [[LineSegmentIntersection]] — core primitive for finding the crossing points

## Contradictions
- None — reference task page.
