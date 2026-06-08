---
title: "Abelian sandpile model/Identity (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, cellular-automata, abstract-algebra, simulation]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Abelian_sandpile_model/Identity
---

## Summary
The task asks the programmer to model "sandpiles" on a 3x3 grid where each cell holds 0-3 grains of sand. Addition is cell-wise, and any cell reaching 4 or more grains "topples," shedding one grain to each orthogonal neighbor (grains at the edge are lost), which can cascade into an "avalanche" until the pile stabilizes. The key insight is that stable sandpiles under this stabilizing addition form an abelian group: order of topplings never changes the result, and a particular identity sandpile `s3_id` acts as the additive identity for the all-3s configuration.

## Task Requirements
- Create a class or data structure plus functions to represent and operate on sandpiles.
- Confirm the worked avalanche example reaches the shown stable result.
- Confirm commutativity: `s1 + s2 == s2 + s1`, showing the stable results.
- Given `s3` (all cells = 3) and the identity pile `s3_id` (2 1 2 / 1 0 1 / 2 1 2), show that `s3 + s3_id == s3`.
- Show that `s3_id + s3_id == s3_id` (idempotent identity element).
- Print confirming output with the examples.

## Language Coverage
35 languages implement this task, spanning systems, scripting, functional, and even hand-written assembly. Representative implementations include C++, Rust, Go, Zig, Python, Ruby, Haskell, OCaml, F#, Julia, J, and ARM/AArch64 Assembly.

## Connections
- [[CellularAutomata]] — toppling is a local update rule applied until a fixed point.
- [[AbelianGroup]] — stable sandpiles form a commutative group with `s3_id` as identity.
- [[FixedPointIteration]] — stabilization repeatedly applies toppling until no cell exceeds 3.
- [[Idempotence]] — the identity sandpile satisfies `s3_id + s3_id == s3_id`.
- [[GridSimulation]] — state evolves over a 2D lattice of cells.

## Solved in (Rosetta Code languages)
Solved in **32** of the wiki's catalogued languages (Rosetta Code shows 35 language sections for this task). (3 further RC language section(s) are outside the wiki's popularity-list language set.)

[[11l]], [[AArch64 Assembly]], [[Ada]], [[ALGOL 68]], [[ARM Assembly]], [[C++]], [[Crystal]], [[EasyLang]], [[Factor]], [[Fortran]], [[FreeBASIC]], [[FutureBasic]], [[Go]], [[Haskell]], [[J]], [[Java]], [[Julia]], [[Lua]], [[Nim]], [[OCaml]], [[Phix]], [[Pluto]], [[Python]], [[Raku]], [[Rebol]], [[Red]], [[REXX]], [[Ruby]], [[Rust]], [[V (Vlang)]], [[Wren]], [[Zig]]

## Contradictions
- None — reference task page.
