---
title: "BNF (Backus–Naur Form)"
type: concept
tags: [grammar, bnf, ebnf, context-free-grammar, formal-languages, notation, parsing]
sources: [fuzzingbook-09-grammars]
last_updated: 2026-06-06
---

# BNF (Backus–Naur Form)

**Backus–Naur Form (BNF)** is the classic notation for writing [[ContextFreeGrammar|context-free grammars]]. A BNF grammar is a set of [[ProductionRule|production rules]] `<symbol> ::= expansion`, where `::=` reads "is defined as," nonterminals are written in `<angle brackets>`, and the alternation operator `|` separates alternative expansions. Named after John Backus and Peter Naur (who used it to define ALGOL 60), BNF is the lingua franca for specifying programming-language and data-format syntax. Its extension with repetition/optional operators is [[EBNF]].

## From The Fuzzing Book — Fuzzing with Grammars
[[fuzzingbook-09-grammars|Ch 9]] states that "our grammars come in the so-called Backus–Naur form, or BNF for short," and the [[Grammar|`Grammar`]] Python data structure is a direct encoding of BNF (nonterminal → list of alternative expansions). The chapter writes its illustrative rules in `::=`/`|` BNF notation (digits, integers, arithmetic expressions) before translating them into the Python `dict` form. It also implements `convert_ebnf_grammar()` to reduce [[EBNF]] shorthand back down to plain BNF, since the fuzzers operate on BNF grammars. The `Background` section ties BNF to Chomsky's grammar hierarchy and the long history of using grammars to specify input and programming languages.

## Connections
- [[EBNF]] — the extended form (adds `?`/`+`/`*`/`(...)`), desugared back to BNF.
- [[ContextFreeGrammar]] / [[Grammar]] / [[ProductionRule]] — what BNF notation expresses.
- [[Nonterminal]] / [[Terminal]] — the symbols a BNF rule combines.
- [[GrammarBasedFuzzing]] — consumes BNF grammars to produce inputs.
- [[fuzzingbook-09-grammars]] — the chapter that adopts BNF for its grammars.

## Sources
- [[fuzzingbook-09-grammars]] — *The Fuzzing Book* Ch 9, "Fuzzing with Grammars."
