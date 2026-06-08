---
title: "Ternary logic (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, logic, type-systems]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Ternary_logic
---

## Summary
This task asks the programmer to model three-valued (trivalent) logic, in which a value can be True, False, or an indeterminate third value (often called "Maybe" or "Unknown"). Unlike classical bivalent boolean logic, the operators NOT, AND, OR, implication, and equivalence must be redefined over three truth values via their full truth tables. The key insight is that the indeterminate value propagates predictably (e.g. Maybe AND False is still False, but Maybe AND True is Maybe), which is useful where information may be missing or unknown.

## Task Requirements
- Define a new "trit" type that emulates ternary logic by storing one of three truth values.
- Reimplement the language's binary logic operators (NOT, AND, OR, IF-THEN/implication, equivalence) for the new trit type, matching the given truth tables.
- Generate a sampling of results using trit variables to demonstrate the operators.
- Kudos for devising a test case where ternary logic is intrinsically useful and preferable to binary logic.

## Language Coverage
71 languages implement this task, showing broad coverage across functional, imperative, and BASIC-family languages. Representative implementations include C, C++, C#, Java, Python, Haskell, OCaml, Rust, Go, Common Lisp, Perl, and Raku.

## Connections
- [[ManyValuedLogic]] — ternary logic is the simplest case of n-valued logic
- [[BooleanLogic]] — generalizes the bivalent true/false system
- [[TruthTable]] — operators are defined exhaustively via truth tables
- [[BalancedTernary]] — related ternary number system used by the Setun computer
- [[TypeSystems]] — task centers on defining a custom enumerated type

## Contradictions
- None — reference task page.
