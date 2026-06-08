---
title: "Generate Chess960 starting position (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, combinatorics, randomization]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Generate_Chess960_starting_position
---

## Summary
Write a program that randomly generates one of the 960 valid starting positions for Chess960 (Fischer Random Chess), a variant invented by Bobby Fischer. The eight back-rank pieces are shuffled subject to two placement rules, and the key insight is that exactly 960 arrangements satisfy these constraints — hence the variant's name.

## Task Requirements
- Place pieces on the first rank only (pawns and the mirrored black rank are fixed).
- The two bishops must occupy opposite-color squares (an odd number of squares apart).
- The king must be positioned between the two rooks.
- Randomly produce any one of the 960 legal arrangements with uniform validity.
- Display the resulting rank using Unicode chess glyphs, the letters KQRBN, or equivalent letters in another language.

## Language Coverage
59 languages implement this task, giving broad mainstream and esoteric coverage. Representative entries include C, C++, C#, Java, Python, Haskell, Rust, Go, Ruby, Perl, and Common Lisp.

## Connections
- [[Combinatorics]] — the constrained count of exactly 960 valid back-rank permutations.
- [[RandomNumberGeneration]] — uniformly selecting one valid position.
- [[Permutations]] — arranging the eight distinct piece types under placement rules.
- [[ConstraintSatisfaction]] — bishop-color and king-between-rooks conditions.
- [[Chess960]] — the Fischer Random Chess variant being generated.

## Contradictions
- None — reference task page.
