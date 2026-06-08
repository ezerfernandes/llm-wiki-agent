---
title: "O'Halloran numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/O'Halloran_numbers
---

## Summary
O'Halloran numbers are even integers that cannot be the surface area of any cuboid (rectangular box) with positive integer side lengths. A cuboid's surface area is 2 × (lw + wh + hl), which is always even with a minimum of 6 (for the 1×1×1 unit cube). The task asks the programmer to find the sixteen even integers greater than 6 and less than 1000 that can never arise as such a surface area; it is conjectured (but unproven) that no others exist beyond 1000.

## Task Requirements
- Compute surface areas 2 × (lw + wh + hl) for cuboids with positive integer dimensions.
- Identify which even integers in the range (6, 1000) are never produced as a surface area.
- Find and display the sixteen even values that cannot be a cuboid surface area.

## Language Coverage
47 languages implement this task, spanning systems, scripting, and functional styles. Representative examples include C, C++, Rust, Go, Java, Python, Julia, Raku, Haskell-adjacent OCaml/Racket, and Wren.

## Connections
- [[NumberTheory]] — classifying integers by a geometric/arithmetic property
- [[SurfaceArea]] — the cuboid surface-area formula 2(lw + wh + hl)
- [[SieveTechnique]] — marking achievable areas and finding the gaps
- [[IdonealNumbers]] — a related set referenced by the task
- [[OEIS]] — sequence A072843 catalogs these numbers

## Contradictions
- None — reference task page.
