---
title: "Idoneal numbers (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, number-theory]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Idoneal_numbers
---

## Summary
Idoneal (also "suitable" or "convenient") numbers are positive integers D for which any integer expressible in only one way as x² ± Dy² (with x² coprime to Dy²) is a prime power or twice a prime power. The practical computational characterization is simpler: a positive integer n is idoneal if and only if it cannot be written as ab + bc + ac for distinct positive integers 0 < a < b < c. Only 65 such numbers are known, and at most two more could exist (none below 1,000,000).

## Task Requirements
- Find and display at least the first 50 idoneal numbers, which lie between 1 and 255.
- Stretch goal: find and display all 65 known idoneal numbers.

## Language Coverage
46 languages implement this task, spanning low-level systems languages to math-oriented and scripting environments. Representative implementations include C, C++, Java, Python, Go, Julia, Perl, Raku, Wren, and Mathematica/Wolfram Language.

## Connections
- [[NumberTheory]] — the task is rooted in classical number theory.
- [[PrimePower]] — the defining property references prime powers and twice prime powers.
- [[QuadraticForms]] — idoneal numbers arise from the theory of binary quadratic forms x² ± Dy².
- [[BruteForceSearch]] — the common implementation strategy tests the ab+bc+ac decomposition exhaustively.
- [[LeonhardEuler]] — Euler studied these as "numerus idoneus."

## Contradictions
- None — reference task page.
