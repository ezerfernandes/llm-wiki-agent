---
title: "Bioinformatics/Sequence mutation (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, bioinformatics, string-processing, randomness]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Bioinformatics/Sequence_mutation
---

## Summary
The task models random point mutations on a DNA sequence represented as a string over the alphabet {A, C, G, T}. A routine picks a random position and applies one of three mutation operations — swap (substitution), delete, or insert — then reports how the sequence changes. The key insight is that mutation is a stochastic edit applied repeatedly, and that base composition can be tracked before and after to observe the drift.

## Task Requirements
- Implement a routine that mutates a DNA string by choosing a random base position and then performing one of: Swap (change the base to one of A/C/G/T, possibly the same), Delete the base at that position, or Insert a randomly chosen base at that position.
- Randomly generate a test DNA sequence of at least 200 bases.
- "Pretty print" the sequence along with its total length and a per-base count (A, C, G, T).
- Apply ten mutations to the sequence.
- Pretty print the sequence again afterward, with its new length and per-base counts.
- Extra credit: report details of each individual mutation applied, and allow mutation types to be weighted or selected.

## Language Coverage
37 languages implement this task, spanning systems, scripting, functional, and BASIC-family languages. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Common Lisp, Julia, Raku, and Wren.

## Connections
- [[StringProcessing]] — the core operation is editing a character string.
- [[RandomNumberGeneration]] — positions, bases, and mutation choices are drawn at random.
- [[Bioinformatics]] — models DNA sequence mutation over the nucleotide alphabet.
- [[WeightedRandomChoice]] — the extra-credit variant selects mutation types by weight.

## Contradictions
- None — reference task page.
