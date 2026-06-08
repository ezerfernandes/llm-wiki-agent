---
title: "Metaprogramming (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, metaprogramming, macros]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Metaprogramming
---

## Summary
This task asks the programmer to name and briefly demonstrate whatever support their language offers for metaprogramming, ideally with links to documentation or cross-references to related tasks. The key insight is the task's working definition: metaprogramming means any built-in or conventional way for the user to effectively modify the language's syntax, such as Lisp macros, the C preprocessor, or user-defined infix operators. It is deliberately a judgment call — and notably, plain operator overloading and `eval` generally do not qualify.

## Task Requirements
- Identify and name any metaprogramming facilities the language provides.
- Briefly demonstrate them, optionally via cross-references to other Rosetta Code tasks.
- Provide links to relevant documentation when possible.
- Focus on facilities that let the user alter syntax (macros, preprocessor, custom infix operators); exclude mere operator overloading and `eval`.

## Language Coverage
55 languages implement this task, spanning Lisp-family languages with rich macro systems and others relying on preprocessors or operator definitions. Representative entries include Common Lisp, Clojure, Racket, Scheme-like PicoLisp, Haskell, Rust, Perl, Raku, Python, Ruby, Tcl, and C.

## Connections
- [[Macro]] — compile-time code transformation, the canonical metaprogramming mechanism
- [[Lisp]] — homoiconic languages whose macros define this task's reference example
- [[Preprocessor]] — text-substitution metaprogramming as in C
- [[DomainSpecificLanguage]] — DSLs are a common end-goal of syntax extension
- [[Reflection]] — runtime introspection often paired with metaprogramming

## Contradictions
- None — reference task page.
