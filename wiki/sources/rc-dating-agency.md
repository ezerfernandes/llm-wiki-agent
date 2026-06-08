---
title: "Dating agency (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, object-modelling, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Dating_agency
---

## Summary
A lighthearted object-modelling exercise: a sailor signs up to a dating agency with 10 candidate ladies. The agency applies the rule "all the nice girls love a sailor" to pick which ladies to suggest, and the sailor applies a separate "lady is lovable" rule to decide whom to date. The key wrinkle is choosing some arbitrary, name-derived predicate for "nice" and "lovable" whose outcomes are roughly equally likely (e.g. parity of a character code or letter count).

## Task Requirements
- Model the scenario in the chosen language, giving the sailor and the ladies names.
- Use an arbitrary method based on each lady's name to decide whether she is *nice* and/or *lovable*, preferring a method with roughly 50/50 outcomes.
- Apply the agency's filter ("nice girls love a sailor") to determine which ladies are suggested.
- Apply the sailor's filter ("lady is lovable") to determine which suggested ladies he offers to date.

## Language Coverage
20 languages implement this task. Coverage is modest and spread across systems, scripting, and BASIC-family languages, including C++, Java, Rust, Nim, Python, Perl, Raku, Julia, Factor, and Wren.

## Connections
- [[ObjectModelling]] — the core purpose of the exercise is modelling entities and their relationships
- [[StringProcessing]] — niceness/lovability is derived from manipulating the ladies' names
- [[PredicateFiltering]] — two successive boolean filters narrow the candidate list

## Contradictions
- None — reference task page.
