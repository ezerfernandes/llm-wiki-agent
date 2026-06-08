---
title: "Jaro-Winkler distance (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, edit-distance, spell-checking]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Jaro-Winkler_distance
---

## Summary
The task asks the programmer to implement the Jaro-Winkler distance, a string similarity metric that extends the Jaro similarity by boosting the score for strings sharing a common prefix. The Jaro similarity counts matching characters (within a sliding window) and transpositions, while the Winkler modification adds a bonus weighted by the length of the shared prefix (up to 4 characters, multiplier 0.1). The distance is simply 1 minus the similarity, so identical strings score 0. The key application motivating the metric is spell checking, since transposition and mid-word errors are common typing mistakes.

## Task Requirements
- Implement the Jaro similarity: count matching characters (same character within max(|s1|, |s2|)/2 − 1 positions) and t = half the number of transpositions.
- Apply the Winkler modification: add l·p·(1 − sim_j), where l is the common-prefix length capped at 4 and p = 0.1.
- Compute the distance as d_w = 1 − sim_w.
- Using a dictionary of choice and a fixed list of 9 commonly misspelled words ("accomodate", "definately", "goverment", "occured", "publically", "recieve", "seperate", "untill", "wich"), find at least two close dictionary alternatives per misspelled word.
- Display the computed distances between each misspelled word and its suggested replacements.

## Language Coverage
26 languages implement this task, spanning systems, functional, scripting, and array-oriented styles. Representative solutions include C++, Rust, Go, Swift, Java, JavaScript/TypeScript, Python, Perl, Raku, Julia, J, and Wren.

## Connections
- [[EditDistance]] — Jaro-Winkler is a string edit-distance metric.
- [[LevenshteinDistance]] — the more basic edit distance it is contrasted against.
- [[StringSimilarity]] — the broader family of string comparison measures.
- [[SpellChecking]] — primary application for suggesting word replacements.

## Contradictions
- None — reference task page.
