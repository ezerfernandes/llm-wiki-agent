---
title: "Honeycombs (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, graphics, gui]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Honeycombs
---

## Summary
This GUI task asks the programmer to render 20 hexagon-shaped widgets in a honeycomb layout: five columns of four hexagons, where the odd-numbered columns are aligned horizontally and the even-numbered columns sit lower so the cells interlock. Each hexagon shows a unique randomly assigned capital letter, and the user picks hexagons one at a time (via pointer or keyboard) until all are chosen, with each picked cell changing colour. The interesting part is laying out a tessellating hex grid and wiring both mouse and keyboard hit-testing to the same selection logic.

## Task Requirements
- Draw 20 hexagons arranged as five columns of four, with columns 2 and 4 offset to a lower vertical position.
- All hexagons start the same colour; each displays a unique randomly chosen single capital letter.
- Let the user select a hexagon by clicking it or by pressing the matching letter key; support both where the platform allows.
- Mark the selected letter (with a comment at the point of determination), recolour the chosen hexagon, and keep the new colour permanently.
- Each letter is selectable only once; the program ends when every letter has been chosen.
- Optional extras: print the list of selected letters and the last one, allow a different grid size, and support two players with distinct colours and separate selection records.

## Language Coverage
34 languages implement this task, spanning desktop GUI toolkits and BASIC dialects. Representative entries include C, C++, C#, Java, Python, Go, Haskell, Ruby, Tcl, and Mathematica / Wolfram Language.

## Connections
- [[HexagonalGrid]] — the offset tessellation that defines the honeycomb layout
- [[EventDrivenProgramming]] — the mouse/keyboard selection loop driving the UI
- [[HitTesting]] — mapping a click coordinate to the containing hexagon
- [[GUIProgramming]] — the rendering and widget framework the task exercises

## Contradictions
- None — reference task page.
