---
title: "World Cup group stage (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, combinatorics, enumeration, statistics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/World_Cup_group_stage
---

## Summary
This task models the group stage of a football/soccer World Cup, where four teams each play the other three once in a round-robin (six games total). Each game is a win (3 points), draw (1 point), or loss (0 points). The programmer enumerates all 3^6 = 729 possible result combinations, tallies each team's standings points, and reports a histogram showing how often each final point total occurs. The key insight is that exhaustive enumeration of the small outcome space cleanly answers "given x points, where might a team finish?" — including curiosities like 8 points being unreachable.

## Task Requirements
- Generate all possible outcome combinations for the six group-stage games (3^6 = 729 total).
- Calculate standings points for each of the four teams under every combination.
- Show a histogram (graphical, ASCII art, or raw counts) of standings points across all teams over all outcomes.
- Ignore tiebreakers; the goal is the distribution of final positions versus points earned.

## Language Coverage
34 languages implement this task, spanning systems, functional, scripting, and BASIC-family languages. Representative implementations include C, C++, C#, Go, Java, Python, Ruby, Perl, Raku, Elixir, Common Lisp, and Wren.

## Connections
- [[Combinatorics]] — enumerating 3^6 outcome combinations
- [[BruteForceEnumeration]] — exhaustively iterating the full result space
- [[RoundRobinTournament]] — the six-game four-team scheduling structure
- [[Histogram]] — tabulating frequency of standings-point totals
- [[CartesianProduct]] — combining three outcomes across six independent games

## Contradictions
- None — reference task page.
