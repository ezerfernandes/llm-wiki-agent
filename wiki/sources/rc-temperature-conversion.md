---
title: "Temperature conversion (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, units-conversion, arithmetic]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Temperature_conversion
---

## Summary
This task asks the programmer to accept a temperature value in Kelvin and convert it into the three other well-known temperature scales: Celsius, Fahrenheit, and Rankine, then print all results. The key insight is that Celsius/Kelvin and Fahrenheit/Rankine each share a magnitude but differ in null point, while the two pairs are related by a fixed 5:9 ratio.

## Task Requirements
- Accept an input value expressed in Kelvin.
- Convert it to Celsius (subtract 273.15), to Rankine (multiply by 9/5), and to Fahrenheit (Rankine minus 459.67).
- Print the converted values for all three target scales.

## Language Coverage
123 languages implement this task, reflecting its status as a beginner-friendly arithmetic exercise across nearly every language family. Representative implementations include C, C++, Java, Python, Haskell, Rust, Go, JavaScript, Lua, Ruby, and APL.

## Connections
- [[UnitConversion]] — the task is a canonical units-of-measure conversion problem.
- [[LinearTransformation]] — each scale relates to Kelvin via an affine (scale-and-offset) mapping.
- [[FloatingPointArithmetic]] — conversions rely on non-integer constants like 273.15 and 459.67.

## Contradictions
- None — reference task page.
