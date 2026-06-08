---
title: "Cantor set (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, fractals, recursion]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Cantor_set
---

## Summary
The task asks the programmer to draw a Cantor set, the classic fractal formed by repeatedly removing the open middle third of each line segment. The key insight is that the construction is naturally recursive: at each level every remaining segment is split into thirds and only the outer two are kept, so a simple recursive or iterative routine reproducing this rule generates the figure.

## Task Requirements
- Draw a representation of the Cantor set (typically as text/ASCII rows or a graphical rendering).
- Reproduce the construction rule: remove the middle third of each segment at every iteration.
- See the linked Wikipedia article for mathematical details.

## Language Coverage
70 languages implement this task, spanning systems and scripting languages, BASIC dialects, and functional and array languages. Representative examples include C, C++, Rust, Go, Python, Haskell, Java, JavaScript, Lua, Perl, Raku, Scheme, and J.

## Connections
- [[Fractal]] — the Cantor set is a canonical self-similar fractal.
- [[Recursion]] — the middle-third removal rule maps directly onto recursive subdivision.
- [[CantorSet]] — the named mathematical object with measure zero yet uncountably many points.
- [[SelfSimilarity]] — each subsegment is a scaled copy of the whole.

## Contradictions
- None — reference task page.
