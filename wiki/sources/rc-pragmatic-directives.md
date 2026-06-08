---
title: "Pragmatic directives (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, language-features, compiler-directives]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Pragmatic_directives
---

## Summary
This task asks the programmer to enumerate the pragmatic directives (pragmas) supported by a given language and to show how each one is activated and deactivated. A pragma instructs the language implementation to operate in a specific manner — for example by enabling stricter checking, toggling warnings, or loading alternative modules — without changing the program's core logic. The key insight is that pragmas affect the compiler or interpreter behavior rather than runtime data, and they typically have a defined scope (file, block, or lexical) within which the variance applies.

## Task Requirements
- List the pragmatic directives the language supports.
- Demonstrate how to activate each pragmatic directive.
- Demonstrate how to deactivate each pragmatic directive.
- Describe or demonstrate the scope of effect a pragmatic directive has within a program.

## Language Coverage
39 languages implement this task, ranging from assembly (6502, 8086) through systems and scripting languages, reflecting how widely the "pragma" concept varies. Representative entries include C (`#pragma`), Ada, Perl (`use strict`, `no strict`), Python (`from __future__ import`), Common Lisp (`declaim`/`declare`), D, Go, Lua, and Tcl.

## Connections
- [[CompilerDirectives]] — pragmas are a form of directive to the compiler or interpreter
- [[LexicalScope]] — pragma effects are commonly scoped lexically (file or block)
- [[Preprocessor]] — many languages express pragmas through preprocessing (e.g. C's `#pragma`)
- [[LanguageFeatureToggles]] — pragmas toggle optional or stricter language semantics

## Contradictions
- None — reference task page.
