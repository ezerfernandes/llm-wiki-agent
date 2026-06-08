---
title: "Scope/Function names and labels (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, scope, language-semantics]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Scope/Function_names_and_labels
---

## Summary
This task asks the programmer to explain or demonstrate the rules governing the visibility (scope) of function names and labels in their chosen language. Rather than computing a result, it documents where a function or label can be referenced from — for example whether functions are global, file-local, module-scoped, or nested, and whether labels used by goto/jump statements are visible only within their enclosing block or the whole routine. The key insight is that name visibility for callable code and jump targets often follows different rules than visibility for ordinary variables.

## Task Requirements
- Explain or demonstrate the levels of visibility of function names within the language.
- Explain or demonstrate the levels of visibility of labels (e.g. goto/jump targets) within the language.
- Companion to the related tasks on variable scope and general scope modifiers.

## Language Coverage
48 languages implement this task, spanning assembly, BASIC dialects, functional, scripting, and systems languages — reflecting how universal yet language-specific scoping rules are. Representative entries include 6502 Assembly, C, Go, Haskell, Python, Perl, Ruby, Racket, Tcl, and REXX.

## Connections
- [[Scope]] — the central language concept this task documents
- [[NameResolution]] — how identifiers for functions and labels are bound and looked up
- [[LexicalScope]] — block- and file-level visibility rules common to many implementations
- [[ControlFlow]] — labels exist to serve goto/jump-based control transfer

## Contradictions
- None — reference task page.
