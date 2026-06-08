---
title: "Sierpinski carpet (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, fractals, recursion]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sierpinski_carpet
---

## Summary
The task asks the programmer to produce a graphical or ASCII-art rendering of a Sierpinski carpet of order N. The carpet is a self-similar fractal built by repeatedly subdividing a square into a 3x3 grid and removing the central cell, leaving the other eight to recurse. The key insight is that a cell is filled only when, for every base-3 digit pair of its (x, y) coordinates, no pair is simultaneously the center digit (1, 1) — equivalent to recursive subdivision.

## Task Requirements
- Generate a Sierpinski carpet of arbitrary order N.
- Output may be graphical or ASCII art.
- The `#` character is not mandatory; any non-whitespace marker is acceptable.
- The essential requirement is the correct placement of whitespace versus non-whitespace cells, matching the recursive 3x3 hole pattern.

## Language Coverage
100 languages implement this task, spanning systems and assembly languages, functional languages, scripting languages, and array/math languages. Representative implementations include Python, C, C++, Java, Haskell, Rust, Go, Ruby, Perl, J, and X86 Assembly.

## Connections
- [[Fractal]] — the carpet is a classic self-similar fractal.
- [[Recursion]] — the natural construction subdivides each square recursively.
- [[SierpinskiTriangle]] — closely related fractal and Rosetta Code companion task.
- [[BaseConversion]] — a non-recursive solution tests base-3 digits of coordinates.
- [[SelfSimilarity]] — defines the fractal's scale-invariant structure.

## Contradictions
- None — reference task page.
