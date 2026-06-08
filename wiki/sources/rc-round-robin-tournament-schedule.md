---
title: "Round-robin tournament schedule (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, scheduling, combinatorics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Round-robin_tournament_schedule
---

## Summary
A round-robin (all-play-all) tournament is one where every participant plays every other participant exactly once. The task is to generate and print a complete schedule of rounds for 12 participants numbered 1 to 12. The key insight is the "circle method": fix one participant in place and rotate the rest around it each round to produce conflict-free pairings.

## Task Requirements
- Print a tournament schedule for 12 participants represented by the numbers 1 to 12.
- Each participant must play every other participant exactly once.
- For N participants there are N-1 rounds when N is even, and N rounds when N is odd (in which case one contestant gets a "bye" each round).

## Language Coverage
28 languages implement this task, giving broad coverage across procedural, functional, and array-oriented styles. Representative implementations include Ada, ALGOL 68, APL, C++, C#, Go, Java, Julia, Python, Perl, Raku, Ruby, Rust, and J.

## Connections
- [[CircleMethod]] — standard rotation algorithm for generating round-robin pairings
- [[Combinatorics]] — every pairing of N items taken 2 at a time is scheduled
- [[Scheduling]] — assigning matches to rounds without conflicts
- [[GraphTheory]] — equivalent to edge-coloring the complete graph K_N

## Contradictions
- None — reference task page.
