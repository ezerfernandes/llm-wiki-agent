---
title: "Angles (geometric), normalization and conversion (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, geometry, unit-conversion, modular-arithmetic]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Angles_(geometric),_normalization_and_conversion
---

## Summary
This task asks the programmer to normalize and convert geometric angles across four common angular scales: degrees, gradians, mils, and radians. A full turn equals 360 degrees, 400 gradians, 6400 mils, or 2π radians, so conversion between any pair is a simple proportional scaling. The key subtlety is normalization: an angle is reduced in magnitude to less than a full circle while preserving its sign, so -45° stays -45° rather than wrapping to 315°.

## Task Requirements
- Write normalization functions for each scale (suggested names d2d, g2g, m2m, r2r) that reduce magnitude below one full turn while keeping the sign.
- Write conversion functions between every pair of scales (d2g, d2m, d2r, g2d, g2m, g2r, m2d, m2g, m2r, r2d, r2g, r2m).
- Treat 0°, +0°, and -0° all as 0°.
- Apply the dozen test inputs: -2, -1, 0, 1, 2, 6.2831853, 16, 57.2957795, 359, 399, 6399, 1000000.
- Normalize every angle except the original base value, then display each input in all four scales converted to all others.

## Language Coverage
48 languages implement this task, spanning systems, scripting, functional, and BASIC-family languages. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Common Lisp, Perl, Raku, Julia, and REXX.

## Connections
- [[UnitConversion]] — proportional scaling between angular units
- [[ModularArithmetic]] — sign-preserving reduction modulo a full turn
- [[Radian]] — the natural angular unit tied to 2π
- [[FloatingPointArithmetic]] — handling of large inputs like 1000000 and signed zero

## Contradictions
- None — reference task page.
