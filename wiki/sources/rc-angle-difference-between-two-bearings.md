---
title: "Angle difference between two bearings (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, geometry, modular-arithmetic]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Angle_difference_between_two_bearings
---

## Summary
The task asks the programmer to compute the signed angular difference `b2 - b1` between two compass bearings, where both inputs and the result are normalized to the range -180 to +180 degrees. The key insight is that a naive subtraction can yield values outside this range, so the result must be wrapped (e.g. by adding or subtracting 360, or using a modulo-based normalization) to keep it in the canonical interval.

## Task Requirements
- Compute `b2 - b1` for given pairs of bearings.
- Inputs are in the range -180 to +180 degrees; the result must also be expressed in -180 to +180 degrees.
- Process eight required test pairs (e.g. 20 and 45, -45 and 145, 29.4803 and -88.6381).
- Optional extra: accept any finite input value (large magnitudes such as -70099.74 and 29840.67), still producing a normalized result.

## Language Coverage
90 languages implement this task, showing very broad coverage spanning systems, scripting, functional, and array languages. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, APL, Raku, and Wren.

## Connections
- [[ModularArithmetic]] — wrapping the difference back into a 360-degree cycle
- [[AngleNormalization]] — canonicalizing an angle into a fixed interval
- [[CompassBearing]] — the navigation concept the task models
- [[FloatingPointArithmetic]] — handling finite real-valued inputs in the extra cases

## Contradictions
- None — reference task page.
