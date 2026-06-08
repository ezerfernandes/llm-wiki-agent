---
title: "Jaro similarity (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, edit-distance]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Jaro_similarity
---

## Summary
This task asks the programmer to implement the Jaro similarity, a normalized measure of how alike two strings are, scoring 0 for no similarity and 1 for an exact match. The metric combines the count of matching characters (characters that are equal and within a bounded window of each other) with the number of transpositions (matched characters that appear in a different order). The key insight is the matching window: two characters only count as matching if they are no farther apart than floor(max(len)/2) - 1 positions.

## Task Requirements
- Implement the Jaro algorithm following the definition: d_j = 0 if m = 0, otherwise (1/3)(m/|s1| + m/|s2| + (m-t)/m), where m is matching characters and t is half the transpositions.
- Count two characters as matching only if equal and within floor(max(|s1|,|s2|)/2) - 1 positions of each other.
- Compute t as half the number of common characters occupying different positions.
- Show similarity scores for the pairs ("MARTHA","MARHTA"), ("DIXON","DICKSONX"), and ("JELLYFISH","SMELLYFISH").

## Language Coverage
64 languages implement this task, spanning systems and scripting languages as well as several BASIC and assembly dialects. Representative implementations include C, C++, Rust, Go, Java, Python, Haskell, Perl, Ruby, and ARM Assembly.

## Connections
- [[EditDistance]] — Jaro is a variant in the family of string edit-distance measures.
- [[StringMetric]] — it is a normalized similarity metric over pairs of strings.
- [[JaroWinklerDistance]] — the closely related extension that boosts scores for common prefixes.
- [[StringMatching]] — used for fuzzy matching and record linkage.

## Contradictions
- None — reference task page.
