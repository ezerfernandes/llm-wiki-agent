---
title: "Box the compass (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, lookup-table, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Box_the_compass
---

## Summary
The task asks the programmer to write a function that converts a heading in degrees into the correct 32-point compass name (e.g. "North", "North by east", "North-northeast"). The key insight is that the 360-degree circle is divided into 32 equal sectors of 11.25 degrees each, so the point index is found by rounding the heading to the nearest sector. The program then prints a table of index, compass point name, and degree for 33 specified test headings spread across the acceptance ranges.

## Task Requirements
- Implement a function taking a heading in degrees and returning the matching 32-point compass heading.
- Print a table with columns Index, Compass point, and Degree.
- Use exactly the 33 given test headings as input (e.g. 0.0, 16.87, 16.88, 33.75, ... 354.38).
- Indices run 1..32, enumerating the cardinal points; names follow standard compass nomenclature.

## Language Coverage
97 languages implement this task, giving very broad coverage across systems, scripting, functional, and BASIC-family languages. Representative implementations include C, C++, Python, Java, Go, Rust, Haskell, Ruby, Perl, Raku, and Tcl.

## Connections
- [[CompassDirections]] — the 32-point compass rose being modeled
- [[LookupTable]] — names are typically stored in a fixed table indexed by sector
- [[ModularArithmetic]] — index computed via `(heading / 11.25) mod 32`
- [[Rounding]] — mapping a continuous heading to the nearest discrete sector
- [[StringProcessing]] — assembling and formatting the compass point names

## Contradictions
- None — reference task page.
