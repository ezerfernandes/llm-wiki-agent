---
title: "Narcissist (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, self-reference, decision-problem]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Narcissist
---

## Summary
A narcissist (or Narcissus program) is the decision-problem counterpart of a quine: instead of printing its own source, it reads a string from input and decides whether that input exactly matches its own source code, emitting "accept" (1) or "reject" (0). The key insight is that a program must embed knowledge of its own text — like a quine — but use it for comparison against arbitrary input rather than for reproduction.

## Task Requirements
- Read a string of symbols (here, characters) from input.
- Produce no output except an "accept"/"1" if the input equals the program's own source code, or "reject"/"0" otherwise.
- Cope with any finite input regardless of length.
- Always halt; "accept", "reject", and "not yet finished" must be distinguishable. Any output form is allowed.

## Language Coverage
49 languages implement this task, spanning systems, scripting, functional, and esoteric languages. Representative entries include C, C#, Java, Python, Haskell, Ruby, Rust, Go, Perl, Common Lisp, and the stack-based esolang Befunge.

## Connections
- [[Quine]] — the narcissist is the decision-problem variant of a self-replicating program
- [[SelfReference]] — both rely on a program encoding its own source text
- [[DecisionProblem]] — output is a binary accept/reject classification
- [[StringMatching]] — the core operation is exact equality of input against source

## Contradictions
- None — reference task page.
