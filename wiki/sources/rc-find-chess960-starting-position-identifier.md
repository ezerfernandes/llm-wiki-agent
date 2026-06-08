---
title: "Find Chess960 starting position identifier (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, combinatorics, enumeration]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Find_Chess960_starting_position_identifier
---

## Summary
Chess960 (Fischer Random Chess) randomizes the back-rank piece arrangement, and each of the 960 legal setups has a unique Starting Position Identifier (SP-ID). This task is the inverse of generating a position from a number: given a back-rank array of eight pieces, compute its SP-ID. The key insight is a mixed-radix encoding that decomposes the position into independent sub-choices (knights, queen, and the two color-bound bishops) and combines them with the formula 96N + 16Q + 4D + L.

## Task Requirements
- Accept a starting array of the eight back-rank pieces in any representation (string, list, letters, or Unicode chess symbols), read left to right from White's side.
- Derive the unique SP-ID number and return it (e.g. QNRBBNKR yields 105; the standard chess setup RNBQKBNR yields 518).
- Knight step: ignoring queen and bishops, find the two knights' combination index N among the five remaining squares.
- Queen step: ignoring bishops, find the queen's index Q among the six remaining squares.
- Bishop step: find the dark-square bishop index D and light-square bishop index L within their respective four like-colored squares (leftmost square is dark).
- Combine via 4(4(6N + Q) + D) + L = 96N + 16Q + 4D + L.
- Validating the input (illegal characters, same-color bishops, king not between rooks) is optional.

## Language Coverage
22 languages implement this task, spanning systems, functional, and scripting families. Representative examples include C++, D, Go, Java, Nim, Rust-adjacent V (Vlang), Python, Ruby, Perl, Raku, Julia, Common Lisp, Factor, J, jq, and Wren.

## Connections
- [[Chess960]] — the chess variant whose positions are being identified.
- [[MixedRadixNumber]] — the SP-ID is a mixed-radix encoding of independent piece-placement choices.
- [[Combinatorics]] — counting and indexing knight placements among remaining squares.
- [[Enumeration]] — assigning each of 960 valid arrangements a unique ordinal index.

## Contradictions
- None — reference task page.
