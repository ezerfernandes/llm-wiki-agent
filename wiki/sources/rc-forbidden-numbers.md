---
title: "Forbidden numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Forbidden_numbers
---

## Summary
A "forbidden number" is a positive integer that requires *at least* four nonzero squares to be expressed as a sum of squares — it cannot be written using one, two, or three squares. By Lagrange's four-square theorem every positive integer is a sum of at most four squares, so these are precisely the numbers needing the full four. They have the closed form 4^a·(8b+7), and arise in crystallography where cubic-crystal X-ray diffraction indices (length²+width²+height²) cannot reach them.

## Task Requirements
- Find and show the first fifty forbidden numbers.
- Find and show the count of forbidden numbers up to 500 and up to 5,000.
- Stretch: find and show the count of forbidden numbers up to 50,000 and up to 500,000.

## Language Coverage
51 languages implement this task, spanning systems, scripting, functional, and array languages. Representative entries include C, C++, Java, Python, Go, Julia, Raku, Perl, Wren, and J.

## Connections
- [[LagrangeFourSquareTheorem]] — the underlying theorem guaranteeing at most four squares
- [[SumOfSquares]] — decomposing integers into squared terms
- [[NumberTheory]] — the branch of mathematics this task draws on
- [[OeisSequences]] — corresponds to OEIS A004215

## Contradictions
- None — reference task page.
