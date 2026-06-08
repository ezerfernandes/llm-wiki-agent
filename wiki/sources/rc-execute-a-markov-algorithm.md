---
title: "Execute a Markov algorithm (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, interpreters, computability]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Execute_a_Markov_algorithm
---

## Summary
The task is to build an interpreter for a Markov algorithm: a string-rewriting system whose ruleset is a sequence of `pattern -> replacement` rules (plus optional `#` comments). The interpreter repeatedly scans the rules in order, applies the first rule whose pattern occurs in the working string by replacing its leftmost occurrence, and restarts the scan; rules prefixed with a leading period are terminating, halting execution once applied. The key insight is that this minimal substitution model is Turing-complete, which the supplied test rulesets demonstrate by encoding unary multiplication and a three-state busy-beaver Turing machine.

## Task Requirements
- Parse a ruleset where each line is either a comment (`#`) or a rule of the form `<pattern> -> <replacement>`, with whitespace around the arrow.
- Detect a terminating rule by a `.` immediately preceding the replacement, and halt after applying it.
- On each iteration, apply the first matching rule (in textual order) to the leftmost match, then re-scan from the top; stop when no rule matches or a terminating rule fires.
- Perform literal (non-regex) substitution so special characters in patterns are matched exactly.
- Pass the five provided test rulesets, including order-sensitive substitution, the unary multiplication engine, and the busy-beaver Turing machine.

## Language Coverage
57 languages implement this task, spanning systems, scripting, and functional families. Representative implementations include C, C++, C#, Rust, Go, Java, Haskell, OCaml, Python, Perl, Ruby, Prolog, and Tcl.

## Connections
- [[StringRewritingSystem]] — the formal model underlying the task
- [[MarkovAlgorithm]] — the named algorithm being interpreted
- [[TuringCompleteness]] — demonstrated by the multiplication and busy-beaver rulesets
- [[TuringMachine]] — encoded directly in Ruleset 5
- [[StringProcessing]] — pattern matching and substitution drive the implementation

## Contradictions
- None — reference task page.
