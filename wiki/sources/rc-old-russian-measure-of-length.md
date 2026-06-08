---
title: "Old Russian measure of length (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, unit-conversion, linear-transformation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Old_Russian_measure_of_length
---

## Summary
The task asks the programmer to convert between the obsolete Russian units of length and the metric system in both directions. Given a single input value in one chosen unit, the program returns the equivalent value expressed in all the other units. Because every unit relates to the others by a fixed scale factor, the conversion reduces to a simple linear transformation through a common base unit (typically meters).

## Task Requirements
- Accept a single numeric value together with a selected source unit of measurement.
- Convert and return that value expressed in every other supported unit.
- Support these units: vershoks, arshins, sazhens, versts, meters, centimeters, and kilometers.
- Handle conversion in both directions (old Russian units to metric and metric to old Russian units).

## Language Coverage
47 languages implement this task, giving broad coverage across imperative, functional, and scripting paradigms. Representative implementations include Python, C, C++, Java, Go, Rust, Haskell, Perl, Ruby, Julia, and REXX.

## Connections
- [[UnitConversion]] — the core problem of mapping a quantity between measurement systems.
- [[LinearTransformation]] — each unit relates to the others by a constant scaling factor, making the conversion linear.
- [[DimensionalAnalysis]] — uses a common base unit (meters) as the pivot for all conversions.
- [[ScaleFactor]] — fixed ratios between vershoks, arshins, sazhens, and versts drive the arithmetic.

## Contradictions
- None — reference task page.
