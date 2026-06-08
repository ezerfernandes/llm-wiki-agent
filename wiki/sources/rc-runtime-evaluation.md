---
title: "Runtime evaluation (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, metaprogramming, interpreters]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Runtime_evaluation
---

## Summary
This task asks the programmer to demonstrate a language's ability to execute code, written in that same language, that is supplied at runtime — the classic "eval" capability. The key dimensions to show are what kind of fragments are accepted (expressions versus full statements), how data flows in and out (environments, arguments, return values), the lexical/static scope in which the supplied code runs, and any facilities for restricting (sandboxes, resource limits) or customizing (debugging hooks) the execution. The point is that for many dynamic languages this is a built-in feature, while for compiled languages it requires invoking a built-in interpreter or compiler exposed by the platform itself.

## Task Requirements
- Execute code, provided at runtime, written in the host language.
- Show which program fragments are permitted (e.g. expressions vs. statements).
- Show how to pass values in and out (environments, arguments, return values).
- Note the lexical/static environment in which the code is evaluated, if applicable.
- Describe any facilities for restricting (sandboxes, resource limits) or customizing (debugging) execution.
- Do not invoke a separate standalone evaluator program unless that program's interface is itself considered part of the language/library/platform.

## Language Coverage
75 languages implement this task, spanning dynamic scripting languages where eval is trivial, Lisp dialects with first-class code-as-data, and compiled languages that must surface an embedded interpreter or compiler. Representative implementations include Python, Ruby, Perl, JavaScript, Common Lisp, Scheme, Racket, Lua, Tcl, Java, and Go.

## Connections
- [[Eval]] — the core mechanism this task demonstrates
- [[Metaprogramming]] — programs treating code as data they manipulate at runtime
- [[Homoiconicity]] — why Lisp-family languages make this especially natural
- [[Sandboxing]] — the restriction facility the task asks about
- [[Eval In Environment]] — the more constrained sibling task

## Contradictions
- None — reference task page.
