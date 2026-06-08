---
title: "Chinese zodiac (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, calendars, modular-arithmetic]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Chinese_zodiac
---

## Summary
Given a Gregorian CE year, determine the Chinese lunisolar year's zodiac animal, its yin/yang aspect, and its associated wǔxíng element. The key insight is that the Chinese calendar advances two concurrent cycles each year — 10 celestial stems and 12 terrestrial branches — which interlock into a repeating 60-year sexagenary pattern. The branch maps to one of 12 animals, while consecutive pairs of stems map to one of 5 elements (yang then yin), so the computation reduces to modular indexing off a known anchor year (1984 = Wood Rat, yang).

## Task Requirements
- Return or output the animal, yin/yang aspect, and element for the lunisolar year beginning in a given CE year.
- Use the animal cycle (period 12): Rat, Ox, Tiger, Rabbit, Dragon, Snake, Horse, Goat, Monkey, Rooster, Dog, Pig.
- Use the element cycle (period 10 via stems, 5 elements each spanning two years): Wood, Fire, Earth, Metal, Water; each element covers a yang year followed by a yin year.
- Anchor the cycle at 1984 CE = Wood Rat, yang (start of the current 60-year cycle).
- Optionally report the year's position within the 60-year cycle and/or its stem-branch name in Han characters or Pinyin (e.g., 2025 = 乙巳, yǐ-sì, the yin Wood Snake, 42nd of the cycle).

## Language Coverage
83 languages implement this task, spanning systems languages, scripting, functional, and esoteric tongues. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Common Lisp, Raku, and even LOLCODE and Befunge.

## Connections
- [[ModularArithmetic]] — animal/stem/element indices derive from year modulo 12, 10, and 60
- [[Calendars]] — the lunisolar sexagenary calendar system
- [[CyclicSequences]] — interlocking cycles of unequal length forming a 60-year period
- [[UnicodeHandling]] — optional output of Han characters and Pinyin tone marks

## Contradictions
- None — reference task page.
