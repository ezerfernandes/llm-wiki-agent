---
title: "Mayan numerals (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-systems, ascii-art, base-conversion]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Mayan_numerals
---

## Summary
The task asks the programmer to render decimal numbers in the Mayan numbering system, a vigesimal (base-20) positional numeral system, and to display each glyph inside a cartouche (a box drawn with ASCII or Unicode characters). The key insight is that each base-20 digit is itself built from sub-glyphs: dots for units (1-4), horizontal bars for fives, and a shell/egg glyph (rendered as Θ) for zero. Numbers are laid out left-to-right (one box per base-20 place) rather than the traditional vertical orientation, purely for readability.

## Task Requirements
- Convert a number to its base-20 digits and render each digit as a stacked arrangement of dots (units), bars (each worth five), and a zero glyph (Θ) when the place is empty.
- Enclose each base-20 numeral in a cartouche (box) using suitable ASCII/Unicode characters.
- Use the vertical glyph form (dots and bars stacked), not the horizontal form.
- Convert and display the decimal numbers 4,005; 8,017; 326,205; and 886,205.
- Show one additional unique/interesting Mayan number of the programmer's choosing.
- Print all output.

## Language Coverage
44 languages implement this task, reflecting broad coverage spanning systems, scripting, and functional languages. Representative implementations include C, C++, Rust, Go, Java, JavaScript, Python, Haskell, Perl, Raku, REXX, and Wren.

## Connections
- [[VigesimalNumberSystem]] — the base-20 positional system underlying Mayan numerals
- [[PositionalNotation]] — the place-value principle that maps each digit to a power of 20
- [[BaseConversion]] — the core algorithm of repeatedly dividing by 20 to extract digits
- [[AsciiArt]] — the rendering technique used to draw glyphs and cartouches
- [[RomanNumerals]] — a related numeral-encoding task linked from the page

## Contradictions
- None — reference task page.
