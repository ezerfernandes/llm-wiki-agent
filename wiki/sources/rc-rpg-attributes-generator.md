---
title: "RPG attributes generator (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, random-numbers, simulation, dice]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/RPG_attributes_generator
---

## Summary
The task models the classic tabletop RPG character-creation method of "roll 4d6, drop the lowest" to generate each of the six core attributes (strength, dexterity, constitution, intelligence, wisdom, charisma). The key insight is rejection sampling: keep regenerating the full set of six attributes until both fairness constraints are met, rather than trying to construct a valid set directly.

## Task Requirements
- Generate 4 random whole values between 1 and 6 (simulating four d6 rolls).
- Save the sum of the 3 largest of those 4 values as one attribute.
- Repeat to produce a total of 6 attribute values, preserving generation order.
- The total of all 6 values must be at least 75.
- At least 2 of the values must be 15 or more.
- Display the total and all 6 values once a valid set is found.

## Language Coverage
88 languages implement this task, spanning systems languages, scripting languages, and many BASIC dialects. Representative examples include C, C++, Rust, Go, Java, Python, Haskell, Perl, Raku, and Common Lisp.

## Connections
- [[RejectionSampling]] — re-rolling until the total and minimum-count constraints hold
- [[RandomNumberGeneration]] — simulating dice via uniform integers in [1,6]
- [[MonteCarloMethod]] — repeated random trials to satisfy probabilistic criteria
- [[Sorting]] — selecting the three highest of four rolls

## Contradictions
- None — reference task page.
