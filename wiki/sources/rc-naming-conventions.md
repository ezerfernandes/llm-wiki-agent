---
title: "Naming conventions (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, language-design, code-style]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Naming_conventions
---

## Summary
This is a documentation task rather than an algorithm: it asks the programmer to describe the naming conventions a language imposes on identifiers — procedures, operators, classes, instances, and built-in versus library names. The key insight is distinguishing whether each convention is de facto or de jure, implicit or explicit, mandatory or discretionary, and noting any tooling that enforces it.

## Task Requirements
- Document the evolution and current status of the language's identifier naming conventions, with simple examples.
- Cover procedure/operator names, class/subclass/instance names, and built-in versus library names.
- Indicate whether conventions are implicit, explicit, mandatory, or discretionary, and name any tools that enforce them.
- Note cases where conventions are commonly violated.
- Describe where naming is used to hint at other concerns (e.g. C's leading `_` to hide OS calls, Python's `__` to mark members private).

## Language Coverage
66 languages implement this task, spanning assembly through scripting and functional dialects, since nearly every language has stylistic identifier rules to describe. Representative entries include Ada, C, C#, Go, Haskell, Java, Python, Perl, Raku, Ruby, Rust, and Common Lisp.

## Connections
- [[NamingConvention]] — the central topic, covering prefixes, suffixes, and casing rules
- [[CamelCase]] — a common casing style discussed for class and method names
- [[SnakeCase]] — the underscore-separated style favored by languages like Python and Rust
- [[Identifier]] — the lexical token that naming conventions constrain
- [[CodingStyle]] — broader stylistic guidelines that naming conventions are part of

## Contradictions
- None — reference task page.
