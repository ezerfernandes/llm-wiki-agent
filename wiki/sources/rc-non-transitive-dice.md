---
title: "Non-transitive dice (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, probability, combinatorics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Non-transitive_dice
---

## Summary
This task asks the programmer to discover sets of "non-transitive" dice — ordered lists where each die beats the next (S < T, T < U) yet the cycle closes paradoxically (S > U), breaking the expected transitivity of comparison. Two dice are compared by enumerating all face combinations and counting wins; the die winning more equally-likely combinations is statistically stronger. The key insight is that "beats more often" is not a transitive relation, mirroring rock-paper-scissors among dice.

## Task Requirements
- Define fair dice (each face equally likely), allowing any number of faces and repeated face values.
- Compare two dice X and Y by enumerating all face pairings, counting wins to yield X > Y, X < Y, or X = Y.
- Treat dice as multisets: only show faces in lowest-first sorted order and remove permutation duplicates.
- Generate all four-faced dice with face values from 1 to 4, then test all ordered triples for non-transitivity (S < T, T < U, S > U).
- Show all such non-transitive triples on the page.
- Optional stretch goal: find lists of four non-transitive dice from the same pool of dice.

## Language Coverage
20 languages implement this task, a moderate breadth typical of combinatorial puzzle tasks. Representative implementations include C++, Go, Haskell, Java, Julia, Python, Perl, Raku, Wren, and the constraint-solver-oriented MiniZinc.

## Connections
- [[Probability]] — win likelihood derived from equally-likely face combinations.
- [[Combinatorics]] — generating dice as multisets and enumerating ordered triples.
- [[Transitivity]] — the broken relational property at the heart of the task.
- [[BruteForceSearch]] — exhaustively generating and testing all candidate dice.

## Contradictions
- None — reference task page.
