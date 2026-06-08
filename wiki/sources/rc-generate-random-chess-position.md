---
title: "Generate random chess position (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, randomness, board-games, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Generate_random_chess_position
---

## Summary
The task is to generate a random legal-ish chess position and emit it as a Forsyth–Edwards Notation (FEN) string. The position need not be realistic or balanced, but it must satisfy a handful of validity constraints, and the generator must sample broadly rather than always producing degenerate boards. The core challenge is placing pieces on an 8x8 grid under a few coupled rules and then serializing the board into FEN's rank-by-rank, run-length-encoded format.

## Task Requirements
- Exactly one king of each color (one white, one black).
- The two kings must not occupy adjacent squares.
- No pawn on its promotion rank (no white pawn on rank 8, no black pawn on rank 1).
- At most 32 pieces total, kings included; no material balance required.
- Piece counts need not match a real chess set (e.g. five knights, twenty rooks are allowed).
- It is white's turn to move.
- Both sides have lost castling rights and en passant is impossible — the FEN must end in `w - - 0 1`.
- The sampling method should span a representative range of positions (not always tiny or corner-locked).

## Language Coverage
37 languages implement this task, spanning systems, scripting, functional, and BASIC-family languages. Representative implementations include C, C++, Rust, Go, Java, JavaScript, Python, Haskell, Julia, Perl, Raku, and Wren.

## Connections
- [[ForsythEdwardsNotation]] — the FEN target encoding for the board
- [[RunLengthEncoding]] — FEN compresses consecutive empty squares as digit counts per rank
- [[RandomNumberGeneration]] — uniform sampling of squares and piece types
- [[Chess]] — the domain rules constraining valid placements
- [[ConstraintSatisfaction]] — adjacency and promotion-rank rules the generator must respect

## Contradictions
- None — reference task page.
