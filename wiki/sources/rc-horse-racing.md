---
title: "Horse racing (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, simulation, unit-conversion]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Horse_racing
---

## Summary
This task is a quantitative reasoning puzzle dressed as a horse-racing handicapping problem. Given the results of three separate one-mile races (each with three horses, their carried weights in stones/pounds, finishing distances in lengths, and the winner's time), the program must predict the full finishing order and winner's time of a fourth race in which all nine horses plus a new horse J compete head-to-head. The key insight is establishing a common performance scale by converting weight, distance, and time into a single comparable unit (lengths) using the stated conversion rules, then re-ranking every horse under the new race's weight assignments and trainer adjustments.

## Task Requirements
- Convert weights expressed in stones and pounds, where 1 stone = 14 pounds.
- Apply the rule that 2 pounds carried slows a horse by 1 length at the finish.
- Apply the rule that 1 second equals 5 lengths at the finish.
- Treat all races as run over 1 mile in similar conditions, with the listed time being the winner's time and listed distances the gaps between horses at the finish.
- Account for one-off adjustments: F was slowly away and lost 2 lengths; horse B improved 4 pounds; horse C is 4 pounds below best; horse H gains 3 pounds from the champion jockey; horse J (a filly) can run the mile in 1:35.8 carrying 8.11.
- In Race 4, colts carry 9.00 and fillies 8.11; produce the expected full finishing order plus the winner's predicted time.

## Language Coverage
16 languages implement this task, a modest count reflecting its niche, domain-specific nature. Representative implementations include C++, Go, Java, Julia, Python, Perl, Raku, Phix, Nim, and Wren.

## Connections
- [[UnitConversion]] — normalizes weight, distance, and time into a common length-based metric
- [[Simulation]] — models projected race outcomes from historical performance data
- [[Sorting]] — ranks horses by computed performance to produce the finishing order
- [[HandicappingModel]] — encodes the weight-for-length and time-for-length racing assumptions

## Contradictions
- None — reference task page.
