---
title: "Idiomatically determine all the characters that can be used for symbols (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, language-introspection, character-sets]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Idiomatically_determine_all_the_characters_that_can_be_used_for_symbols
---

## Summary
This Rosetta Code task asks the programmer to determine, in an idiomatic and hardware-independent way, the complete set of characters a given language permits inside symbols (identifiers): names of variables, procedures, functions, labels, and other nameable entities. The core insight is that the answer must be discovered from the language's own definition or runtime rules rather than assumed, and it should hold regardless of underlying encoding (ASCII, EBCDIC, or other). Restrictions on the first character (e.g. no leading digit) may be mentioned but are not the focus.

## Task Requirements
- Display the full set of characters that are valid within symbols/identifiers in the implementing language.
- The determination must be hardware/encoding independent (work under ASCII, EBCDIC, or otherwise).
- Optionally state which hardware architecture and operating system is being used.
- Leading-character restrictions need not be handled, but may be noted.

## Language Coverage
36 languages implement this task, spanning legacy mainframe-oriented languages, functional languages, and modern dynamic languages. Representative entries include Ada, ALGOL 68, Haskell, Java, Julia, Perl, Python, Racket, Raku, REXX, Tcl, and Wren.

## Connections
- [[CharacterEncoding]] — the task hinges on encoding-independence (ASCII vs EBCDIC vs Unicode).
- [[Identifier]] — symbols/identifiers are the entities whose legal characters are enumerated.
- [[LexicalAnalysis]] — valid identifier characters are defined by a language's lexer/grammar rules.
- [[LanguageIntrospection]] — idiomatic solutions query the language's own rules at runtime.
- [[Unicode]] — many modern languages allow Unicode letters in identifiers.

## Contradictions
- None — reference task page.
