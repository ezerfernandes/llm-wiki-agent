---
title: "Extend your language (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, metaprogramming, control-flow, macros]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Extend_your_language
---

## Summary
This task asks the programmer to introduce a brand-new flow-control construct into their language, demonstrating the language's extensibility. The canonical example is an `if2` statement that takes two conditions and offers up to four branches (both true, only first, only second, neither). The key insight is that languages in the Lisp and Forth families erase the distinction between built-in and user-defined syntax, letting new keywords nest and behave exactly like native ones.

## Task Requirements
- Show how to add a new control-flow mechanism if the language supports it.
- Implement a four-way branch (e.g. an `if2` keyword) evaluating two conditions.
- Provide up to three `else`-style clauses (e.g. `else1`, `else2`, `else`) for the partial and none cases.
- The new construct should look, nest, and behave analogously to the built-in `if` statement.
- Pick syntax natural to the language; keyword names are illustrative only.

## Language Coverage
91 languages implement this task, spanning macro systems, fexprs, hygienic macros, and runtime metaprogramming. Lisp-family entries (Common Lisp, Scheme, Racket, Clojure, EchoLisp) and Forth show the most native extensibility, while C, C++, Rust, Tcl, Perl, Raku, Nim, and Ruby demonstrate macro- or block-based approaches.

## Connections
- [[Metaprogramming]] — extending a language with new syntactic constructs
- [[Macros]] — the primary mechanism for adding keywords in Lisp, C, and Rust
- [[ControlFlow]] — the four-way branch is a custom control structure
- [[HomoiconicLanguages]] — Lisp/Forth families treat code as data, enabling seamless extension
- [[DomainSpecificLanguages]] — language extension is a foundation for embedded DSLs

## Contradictions
- None — reference task page.
