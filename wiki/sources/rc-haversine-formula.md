---
title: "Haversine formula (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, geometry, trigonometry, geospatial]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Haversine_formula
---

## Summary
The task asks the programmer to implement a great-circle distance function (or call a library) that computes the shortest distance between two points on a sphere given their latitude and longitude. The canonical example computes the distance between Nashville (BNA) and Los Angeles (LAX) airports. The key insight is the haversine formula, a numerically stable special case of the law of haversines from spherical trigonometry that avoids precision loss at small distances.

## Task Requirements
- Implement (or use a library for) a great-circle distance function.
- Compute the distance between Nashville International Airport (36.12, -86.67) and Los Angeles International Airport (33.94, -118.40).
- Use an Earth radius constant; the task notes 6372.8 km (Kaimbridge's recommended quadratic-mean value) versus the more defensible mean radius of 6371 km, which minimizes RMS error against geodesic distance.

## Language Coverage
133 languages implement this task, reflecting very broad coverage spanning systems, scripting, functional, and database/query languages. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Common Lisp, Fortran, MySQL, and Wolfram/Mathematica.

## Connections
- [[GreatCircleDistance]] — the quantity the formula computes.
- [[SphericalTrigonometry]] — the haversine formula is a special case of the law of haversines.
- [[Trigonometry]] — relies on sine, cosine, and arcsine of angular coordinates.
- [[NumericalStability]] — haversine avoids catastrophic cancellation for nearly antipodal/small distances.
- [[Geodesy]] — Earth-radius choices (authalic, mean, quadratic-mean) affect accuracy.

## Contradictions
- None — reference task page.
