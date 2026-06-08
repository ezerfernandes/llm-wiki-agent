---
title: "Sokoban (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, search-algorithms, puzzle-solving, state-space-search]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Sokoban
---

## Summary
The task is to find a solution to a given Sokoban puzzle level, in which a player pushes boxes onto designated goal squares within a walled grid. Solving Sokoban is formally PSPACE-complete, so any method is allowed, though move-optimal or push-optimal solutions are preferred. The key insight is that the puzzle reduces to a search over board states, where the state is the player position plus the set of box positions.

## Task Requirements
- Read a level encoded as a character grid using the standard symbols: space (empty), `#` (wall), `@` (player), `$` (box), `.` (goal), `+` (player on goal), `*` (box on goal).
- Compute a sequence of moves that pushes every box onto a goal square.
- Output the solution in LURD format, where lowercase `l/u/r/d` denote moves (left, up, right, down) and uppercase `L/U/R/D` denote pushes; state explicitly if a different input/output format is used and why.
- Prefer optimal solutions (move-optimal, push-optimal, or otherwise), though any working method is acceptable.

## Language Coverage
29 languages implement this task, spanning systems languages, functional languages, and scripting languages. Representative implementations include C, C++, Rust, Go, Java, Haskell, OCaml, Python, Ruby, Perl, Racket, and Julia.

## Connections
- [[BreadthFirstSearch]] — typical approach for finding a move-optimal solution over board states
- [[StateSpaceSearch]] — the puzzle is solved by exploring reachable configurations of player and boxes
- [[PSPACECompleteness]] — Sokoban solving is a canonical PSPACE-complete problem
- [[HashSet]] — visited-state tracking commonly uses a hashed set of board configurations

## Contradictions
- None — reference task page.
