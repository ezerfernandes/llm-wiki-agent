---
title: "Conditional structures (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, control-flow, language-features]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Conditional_structures
---

## Summary
This task asks the programmer to enumerate and demonstrate every conditional structure a given programming language offers for branching control flow. Rather than solving an algorithm, each entry is a survey of how the language expresses decisions. The key insight is that conditionals span a spectrum: nearly every language has some form of if-then-else, fewer have switch/case, and only a handful expose less common forms like arithmetic if, the ternary operator, or hash/dictionary-based dispatch.

## Task Requirements
- List the conditional structures offered by the language, referencing the Wikipedia article on conditionals for definitions.
- Cover common structures: if-then-else and switch.
- Cover less common structures where they exist: arithmetic if, the ternary operator, and hash-based conditionals.
- Note that arithmetic if allows tight control over computed gotos that optimizers struggle to reason about.

## Language Coverage
252 languages implement this task, an unusually broad set because every general-purpose language has at least one branching construct. Representative entries include C, Python, Java, JavaScript, Haskell, Rust, Ruby, Fortran, COBOL, Lisp, and low-level Assembly variants where branching reduces to compare-and-jump instructions.

## Connections
- [[ControlFlow]] — conditionals are the core branching primitive of control flow
- [[TernaryOperator]] — a compact expression-level conditional
- [[SwitchStatement]] — multi-way branching on a single value
- [[BooleanLogic]] — predicates that conditionals evaluate to choose a branch
- [[PatternMatching]] — a structural generalization of switch in functional languages

## Contradictions
- None — reference task page.
