---
title: "Gotchas (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, language-design, error-handling]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Gotchas
---

## Summary
This open-ended task asks each language community to document a "gotcha" — a valid construct that behaves exactly as specified yet is counter-intuitive, easy to trigger, and prone to causing bugs. Unlike most Rosetta Code entries it has no fixed algorithm; instead it surveys the surprising sharp edges of real languages. The key insight is that correctness-as-documented does not imply safety, since unexpected-but-legal behavior invites mistakes.

## Task Requirements
- Give one or more examples of common gotchas in your programming language.
- For each, explain why the behavior is counter-intuitive or surprising despite being valid.
- Describe how, if at all, a programmer can defend against the gotcha without relying on special tools (e.g. linters or static analyzers).

## Language Coverage
22 languages contribute examples, spanning assembly, mainstream high-level languages, and niche/esoteric ones. Representative entries include C, C#, Java, JavaScript, Perl, Raku, Julia, R, and jq, alongside assembly variants (6502, 68000, MIPS, X86, Z80) and esoteric languages such as LOLCODE and Quackery.

## Connections
- [[UndefinedBehavior]] — many classic gotchas stem from unspecified or implementation-defined semantics
- [[TypeCoercion]] — implicit conversions (notably in JavaScript and Perl) produce surprising results
- [[OperatorPrecedence]] — non-obvious binding order is a frequent source of counter-intuitive outcomes
- [[FloatingPointArithmetic]] — rounding and comparison surprises are a recurring gotcha theme
- [[DefensiveProgramming]] — the task's core ask is mitigation without special tooling

## Contradictions
- None — reference task page.
