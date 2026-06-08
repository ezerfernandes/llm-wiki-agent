---
title: "Nim game (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, game-theory, combinatorics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Nim_game
---

## Summary
This task is a simplified single-heap variant of Nim: starting from 12 tokens, two players alternately remove 1, 2, or 3 tokens, and whoever takes the last token wins. The key insight is that the second player can force a win by always taking enough tokens to bring the running total of each round up to 4 (i.e. taking `4 - n` after the human takes `n`). The programmer must implement a game where the human moves first and the computer, exploiting this strategy, wins every time.

## Task Requirements
- Start with 12 tokens.
- Each player removes 1, 2, or 3 tokens per turn.
- The player who takes the last token wins.
- The human player goes first; the computer always wins.
- The implementation must enforce the rules (valid move counts, turn order).

## Language Coverage
70 languages implement this task, spanning low-level assembly to high-level functional and scripting languages. Representative examples include C, C++, Rust, Go, Python, Java, Haskell, Common Lisp, Prolog, and Z80 Assembly.

## Connections
- [[Nim]] — the classical mathematical game this task simplifies to a single heap
- [[GameTheory]] — analysis of optimal strategies in turn-based games
- [[CombinatorialGameTheory]] — framework for impartial games like Nim
- [[ModularArithmetic]] — the winning move keeps tokens congruent to 0 mod 4

## Contradictions
- None — reference task page.
