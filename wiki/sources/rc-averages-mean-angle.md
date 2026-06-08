---
title: "Averages/Mean angle (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, trigonometry, geometry, statistics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Averages/Mean_angle
---

## Summary
The task asks for a function that computes the mean of a list of angles given in degrees, correctly handling the fact that angles wrap around (any angle plus a multiple of 360 degrees is the same direction). The key insight is that you cannot arithmetically average angles directly — instead you treat each angle as a unit vector (point on the unit circle), sum or average those vectors, and take the phase of the result. Equivalently, the mean equals atan2 of the average sine over the average cosine.

## Task Requirements
- Write a function/method that, given a list of angles in degrees, returns their mean angle (using a built-in if available).
- Compute the mean angle for these lists: [350, 10]; [90, 180, 270, 360]; [10, 20, 30].
- Show the output. (Note: [350, 10] should yield 0 degrees, not 180, demonstrating correct wraparound handling.)

## Language Coverage
89 languages implement this task, reflecting very broad coverage across general-purpose and mathematical languages. Representative implementations include C, C++, Python, Java, JavaScript, Haskell, Rust, Go, Julia, Fortran, and MATLAB/Octave.

## Connections
- [[CircularMean]] — the statistical technique this task implements
- [[Atan2]] — the function used to recover the angle from sine and cosine sums
- [[ComplexNumbers]] — angles are treated as unit-circle complex numbers, summed, then converted to polar form
- [[UnitCircle]] — the geometric basis for representing each angle as a vector
- [[Trigonometry]] — sine and cosine decomposition underlies the computation

## Contradictions
- None — reference task page.
