---
title: "Cistercian numerals (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, numeral-systems, ascii-art, graphics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Cistercian_numerals
---

## Summary
Cistercian numerals are a medieval European notation that encodes any integer from 0 to 9999 in a single glyph built around one vertical stem. The task is to write a routine that renders a given number as its Cistercian glyph, typically as ASCII/text art or an image. The key insight is that each of the four quadrants around the stem independently encodes one decimal digit place (ones, tens, hundreds, thousands), so a four-digit number is the visual superposition of four mirrored digit marks on a shared stem.

## Task Requirements
- Write a function/procedure that displays any given Cistercian numeral (via drawing, image generation, or a reasonable text facsimile).
- The bare vertical stem alone represents 0; digit glyphs 1-9 attach to quadrants.
- Quadrant-to-place mapping: upper-right = ones, upper-left = tens, lower-right = hundreds, lower-left = thousands (with horizontal mirroring of the basic glyph shapes).
- Use the routine to render: 0, 1, 20, 300, 4000, 5555, 6789, plus one number of the implementer's choice.

## Language Coverage
44 languages implement this task, spanning systems and assembly (68000 Assembly, C, Rust, Ada), scripting and functional languages (Python, Perl, Raku, Haskell, F#, Julia), and array/stack/BASIC dialects (J, Uiua, Quackery, FreeBASIC, REXX), reflecting broad interest in rendering this unusual numeral system.

## Connections
- [[NumeralSystems]] — Cistercian numerals are an alternative base-10 positional encoding
- [[PositionalNotation]] — each quadrant carries one decimal digit place
- [[AsciiArt]] — most implementations render the glyph as a text grid
- [[RomanNumerals]] — the historical alternative the system competed with

## Contradictions
- None — reference task page.
