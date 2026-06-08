---
title: "Horizontal sundial calculations (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, trigonometry, astronomy]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Horizontal_sundial_calculations
---

## Summary
This task asks the programmer to compute, for a user-entered location, the dial hour-line angles of a horizontal sundial across the daytime hours. Given a latitude, longitude, and legal (reference) meridian, the program prints for each hour from 6am to 6pm the hour value, the sun's hour angle, and the resulting dial line angle. The key insight is the gnomon-angle formula: a horizontal dial's hour-line angle equals arctan(sin(latitude) × tan(sun hour angle)), with the style tilted to the site's latitude.

## Task Requirements
- Prompt the operator for a location: latitude, longitude, and legal meridian (in degrees).
- For each hour from 6am to 6pm, compute and display three values per row: the hour, the sun hour angle, and the dial hour line angle.
- The sun hour angle accounts for the offset between the local longitude and the legal meridian (15° of hour angle per hour).
- Dial line angle uses the formula angle = atan(sin(lat) · tan(HRA)), reported in degrees.

## Language Coverage
67 languages implement this task, giving broad coverage across systems, functional, scripting, and legacy languages. Representative examples include C, C++, Java, Python, Haskell, Rust, Go, Fortran, Perl, Raku, and even calculator dialects such as МК-61/52 and x86 Assembly.

## Connections
- [[Trigonometry]] — relies on sine, tangent, and arctangent of angles
- [[DegreeRadianConversion]] — inputs are in degrees but math libraries use radians
- [[SolarHourAngle]] — converts clock time and meridian offset into the sun's angular position
- [[Latitude]] — sets both the gnomon style angle and scales the hour-line formula

## Contradictions
- None — reference task page.
