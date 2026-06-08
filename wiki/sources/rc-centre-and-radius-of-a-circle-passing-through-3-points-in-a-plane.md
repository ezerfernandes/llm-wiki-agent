---
title: "Centre and radius of a circle passing through 3 points in a plane (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, computational-geometry, analytic-geometry]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Centre_and_radius_of_a_circle_passing_through_3_points_in_a_plane
---

## Summary
The task asks the programmer to write a function that, given three points in a plane, returns the centre and radius of the unique circle passing through all three (the circumcircle of the triangle they form). The key insight is that the centre — the circumcentre — is equidistant from all three points and can be found as the intersection of the perpendicular bisectors of two of the chords, with the radius then being its distance to any point. Collinear points (or coincident points) yield no valid finite circle and must be handled as an edge case.

## Task Requirements
- Implement a function that takes three planar points and returns the centre (x, y) and radius of the circle through them.
- Demonstrate the function on the points (22.83, 2.07), (14.39, 30.24), and (33.65, 17.31).

## Language Coverage
32 languages implement this task, spanning systems, scripting, functional, and array-oriented styles. Representative implementations include Ada, C++, C#, Go, Java, Julia, Python, Perl, Raku, Rust, Wren, and Uiua.

## Connections
- [[Circumcircle]] — the circle through three points is the triangle's circumcircle, centred on the circumcentre.
- [[PerpendicularBisector]] — the centre lies at the intersection of the perpendicular bisectors of the chords.
- [[AnalyticGeometry]] — the solution is set up via coordinate equations and determinants.
- [[LinearSystems]] — solving for the centre reduces to a small linear system / determinant computation.
- [[CollinearityTest]] — degenerate (collinear) inputs must be detected as having no finite circle.

## Contradictions
- None — reference task page.
