---
title: "Topic variable (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, language-features, scope]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Topic_variable
---

## Summary
This task asks the programmer to demonstrate the language's "topic" (or "current") variable — a special, very short-named variable that holds an implicit subject of operations and can often be omitted from expressions entirely. The canonical example assigns 3 to the topic variable, then computes its square and square root using the implicit reference. The key insight is that topic variables make code terser by letting operations default to a shared implicit operand, common in Perl-family languages (`$_`) and shell.

## Task Requirements
- Demonstrate the utilization and behaviour of the language's topic variable.
- Explain or demonstrate how the topic variable behaves under different levels of nesting or scope, if applicable.
- Optionally illustrate by assigning 3 to it, then computing its square and square root.

## Language Coverage
39 languages implement this task, spanning Perl-family scripting languages where the concept is native, functional languages, and many that simulate or note the absence of a built-in topic variable. Representative entries include Perl, Raku, Ruby, Python, Haskell, Clojure, Go, Java, Mathematica/Wolfram Language, UNIX Shell, and PowerShell.

## Connections
- [[SpecialVariables]] — a topic variable is a special variable with implicit defaulting behavior
- [[VariableScope]] — task asks how the topic variable behaves across nesting levels
- [[Perl]] — Perl's `$_` is the archetypal topic variable this task is modeled on
- [[ImplicitArguments]] — operations omit an explicit operand, defaulting to the topic

## Contradictions
- None — reference task page.
