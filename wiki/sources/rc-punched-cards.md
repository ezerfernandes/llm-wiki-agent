---
title: "Punched cards (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, text-encoding, ascii-art]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Punched_cards
---

## Summary
This task asks the programmer to render text as an ASCII-art representation of an 80-column IBM punched card, where each character of an input string is encoded as a column of holes according to the Hollerith punched card code. The key insight is mapping each printable character to its specific combination of zone punches (rows 12, 11, 0) and digit punches (rows 0-9), then drawing the resulting grid of holes. As a test, the program prints the punched cards encoding its own language's hello-world program.

## Task Requirements
- Print a representation of one or more 80-column punched cards.
- Encode each character of the input text using the Hollerith punched card code (zone and digit row punches).
- Draw the card outline including the clipped top-left corner and the row of printed characters across the top.
- Non-graphic characters and the special IBM zero (the "0" with a dot inside) may be omitted.
- Demonstrate by punching the source/text of the language's hello-world program.

## Language Coverage
17 languages implement this task, a modest spread covering systems, scripting, and functional styles. Representative implementations include Ada, ALGOL 68, AWK, C, Fortran, Java, Julia, Perl, Raku, and Wren.

## Connections
- [[CharacterEncoding]] — Hollerith code is a character-to-hole encoding scheme
- [[HollerithCode]] — the specific zone/digit punch mapping defined by IBM
- [[AsciiArt]] — the card is rendered as a fixed grid of text characters
- [[LookupTable]] — character-to-punch mapping is typically driven by a table

## Contradictions
- None — reference task page.
