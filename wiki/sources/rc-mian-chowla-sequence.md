---
title: "Mian-Chowla sequence (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory, integer-sequence]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Mian-Chowla_sequence
---

## Summary
The task asks the programmer to generate the Mian–Chowla sequence, a recursively defined integer sequence that is an infinite instance of a Sidon (B₂) sequence. Starting from a₁ = 1, each subsequent term is the smallest positive integer such that all pairwise sums aᵢ + aⱼ (for i, j ≤ n) remain distinct. The key insight is greedily testing candidate values while maintaining a set of already-seen pairwise sums to detect collisions.

## Task Requirements
- Compute and display the first 30 terms of the Mian–Chowla sequence.
- Compute and display the 91st through 100th terms of the sequence.
- For each candidate term, ensure every pairwise sum with prior terms (and itself) is unique before accepting it.

## Language Coverage
42 languages implement this task, spanning systems, scripting, functional, and BASIC-family languages. Representative implementations include C, C++, C#, Go, Haskell, Java, JavaScript, Python, Julia, Perl, Raku, and Wren.

## Connections
- [[SidonSequence]] — the Mian–Chowla sequence is an infinite Sidon (B₂) sequence
- [[IntegerSequence]] — a recursively defined sequence catalogued as OEIS A005282
- [[GreedyAlgorithm]] — terms are chosen greedily as the smallest valid candidate
- [[SetMembership]] — distinctness of pairwise sums is tracked via a set/hash lookup

## Contradictions
- None — reference task page.
