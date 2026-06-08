---
title: "Tic-tac-toe (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, game, adversarial-search]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Tic-tac-toe
---

## Summary
The task is to implement a playable game of tic-tac-toe (noughts and crosses), where two players alternately place X and O marks on a 3x3 grid. The program must enforce that only legal moves are accepted and must detect and announce a winning line. The interesting design dimension is the opponent: implementations range from simple human-vs-human input to a computer player that uses minimax or heuristic logic to play optimally on the small, fully solvable game tree.

## Task Requirements
- Play a complete game of tic-tac-toe on a 3x3 board.
- Ensure that only legal moves are played (occupied or out-of-range cells rejected).
- Detect and notify when a winning position (three in a row, column, or diagonal) is reached.

## Language Coverage
78 languages implement this task, spanning a wide breadth from systems and functional languages to scripting and esoteric languages. Representative examples include C, C++, Java, Python, Go, Rust, Haskell, Common Lisp, Prolog, Ruby, and Befunge.

## Connections
- [[Minimax]] — the standard algorithm for an optimal AI opponent on this game tree.
- [[AdversarialSearch]] — the broader class of two-player game-search methods this task exemplifies.
- [[GameTree]] — tic-tac-toe's small, fully enumerable tree makes perfect play tractable.
- [[CombinatorialGameTheory]] — a solved game that always draws under optimal play.

## Contradictions
- None — reference task page.
