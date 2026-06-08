---
title: "Lyndon word (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, combinatorics, string-processing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Lyndon_word
---

## Summary
A Lyndon word is a non-empty string over an ordered alphabet that is strictly smaller, in lexicographic order, than all of its circular rotations. The task asks the programmer to generate all Lyndon words of length at most n over a given ordered alphabet, listed in lexicographic order. The key insight is Duval's 1988 algorithm, which produces the words in order without testing rotations explicitly.

## Task Requirements
- Given a positive integer n and an ordered alphabet, list all Lyndon words of length at most n in lexicographic order.
- A word qualifies only if it is strictly lower than every circular rotation; a word equal to one of its rotations (e.g. 0101) is excluded.
- Implement generation efficiently, ideally via Duval's successor algorithm: repeat the current word and truncate to length exactly n, drop trailing symbols equal to the alphabet's last symbol, then increment the final remaining symbol to its successor.

## Language Coverage
23 languages implement this task, spanning systems, scripting, array, and functional styles. Representative implementations include C++, Go, Rust, Zig, Java, Python, Julia, Perl, Raku, and the array language APL.

## Connections
- [[Combinatorics]] — Lyndon words are a classic combinatorial object on strings.
- [[LexicographicOrder]] — the defining and ordering relation for the task.
- [[DuvalAlgorithm]] — efficient successor-based generation method (Duval 1988).
- [[StringRotation]] — the circular-rotation comparison central to the definition.
- [[FreeLieAlgebra]] — Lyndon words form a basis, the deeper algebraic motivation.

## Contradictions
- None — reference task page.
