---
title: "Sparkline in unicode (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, data-visualization, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sparkline_in_unicode
---

## Summary
The task asks the programmer to build a tiny inline bar graph — a sparkline — using the eight Unicode block characters U+2581 through U+2588 (▁▂▃▄▅▆▇█). Given a list of numbers separated by whitespace and/or commas, the program scales each value into one of eight height bins and prints the corresponding glyphs on a single line. The core insight is the binning: each value is mapped via its position between the data minimum and maximum, with care needed at the bin boundaries so that edge cases (e.g. evenly spaced values) use the intended number of distinct levels.

## Task Requirements
- Parse a series of numbers separated by one or more whitespace or comma characters (mixed separators allowed).
- Map each value to one of the eight characters ▁▂▃▄▅▆▇█ proportional to its magnitude.
- Emit the sparkline as a single line of output, with no space characters in the bar graph itself.
- Demonstrate on the inputs `1 2 3 4 5 6 7 8 7 6 5 4 3 2 1` and `1.5, 0.5 3.5, 2.5 5.5, 4.5 7.5, 6.5`.
- Optionally show simple statistics such as the data range.
- Suggested edge cases for correct bin bounds: `"0, 1, 19, 20" -> ▁▁██` and `"0, 999, 4000, 4999, 7000, 7999" -> ▁▁▅▅██`.

## Language Coverage
57 languages implement this task, spanning systems languages, functional languages, and scripting tools. Representative implementations include C, C++, Rust, Go, Java, Haskell, Python, Perl, Raku, Ruby, Clojure, and J.

## Connections
- [[DataVisualization]] — sparklines are a compact glyph-based chart form
- [[UnicodeBlockCharacters]] — the eight U+2581–U+2588 glyphs supply the bar heights
- [[LinearScaling]] — values are normalized between min and max before binning
- [[StringParsing]] — handling mixed whitespace/comma delimiters in the input

## Contradictions
- None — reference task page.
