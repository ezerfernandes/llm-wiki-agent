---
title: "Old lady swallowed a fly (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, cumulative-song]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Old_lady_swallowed_a_fly
---

## Summary
The task is to emit the lyrics of the cumulative children's song "I Knew an Old Lady Who Swallowed a Fly" while exploiting the repetitive structure of the verses. Each verse adds a new animal and then recites the chain of previously swallowed animals back down to the fly, so the natural solution is data-driven: store the animals plus their per-verse comment lines and generate the accumulating refrain in a loop rather than hard-coding every line. The song has several lyric variants, so outputs across implementations need not match exactly.

## Task Requirements
- Output the full lyrics of the song.
- Take advantage of the repetitive, cumulative structure rather than writing each verse out literally.
- Acknowledge that multiple lyric versions exist, so exact output may differ between programs.

## Language Coverage
94 languages implement this task, spanning everything from low-level assembly to high-level functional and scripting languages. Representative entries include C, C++, Python, Java, JavaScript, Haskell, Ruby, Rust, Perl, several BASIC dialects, and even Scratch and multiple assembly variants (8080, 8086, ARM, Z80).

## Connections
- [[CumulativeSong]] — the song belongs to the cumulative/chain-song genre this task exemplifies
- [[StringFormatting]] — building each verse from reusable text fragments and interpolation
- [[Iteration]] — looping over the accumulating list of swallowed animals
- [[DataDrivenProgramming]] — driving output from a table of animals and comment lines instead of literal verses

## Contradictions
- None — reference task page.
