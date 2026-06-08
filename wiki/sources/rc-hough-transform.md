---
title: "Hough transform (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, image-processing, computer-vision, graphics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Hough_transform
---

## Summary
This task asks the programmer to implement the Hough transform, a feature-extraction technique that detects straight lines in a digital image regardless of their orientation. Each point in the output accumulator corresponds to polar line parameters (rho, theta), and is filled with the accumulated/averaged intensity of source pixels lying on the line defined by x·cos(theta) + y·sin(theta) = rho. The key insight is that collinear edge points in image space map to a single bright spot in (rho, theta) parameter space, so peak detection there recovers the lines.

## Task Requirements
- Implement the Hough transform for identifying straight lines in a source image (e.g., the sample Pentagon.png).
- Map each point of the target image (rho, theta) to the accumulated/average color of source pixels on the corresponding line x·cos(theta) + y·sin(theta) = rho.
- Use polar coordinates for the target/parameter space, conventionally displayed on rectangular axes with one axis for theta and the other for rho.
- Take the center of the source image as the origin (no exact polar-to-flat mapping is mandated).

## Language Coverage
27 languages implement this task, spanning systems and scientific languages alongside scripting and functional ones. Representative implementations include C, D, Rust, Go, Java, Haskell, Python, Ruby, MATLAB, and Mathematica / Wolfram Language.

## Connections
- [[HoughTransform]] — the named feature-extraction algorithm this task implements
- [[FeatureExtraction]] — broader computer-vision goal the transform serves
- [[PolarCoordinates]] — parameter space (rho, theta) used to represent lines
- [[EdgeDetection]] — typical preprocessing that supplies the edge points fed into the transform
- [[ImageProcessing]] — domain category of the task

## Contradictions
- None — reference task page.
