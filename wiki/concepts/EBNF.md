---
title: "EBNF (Extended Backus–Naur Form)"
type: concept
tags: [grammar, ebnf, bnf, context-free-grammar, formal-languages, fuzzing, notation]
sources: [fuzzingbook-09-grammars]
last_updated: 2026-06-06
---

# EBNF (Extended Backus–Naur Form)

**Extended Backus–Naur Form (EBNF)** augments plain [[BNF]] with shorthand *operators* that make grammars much easier to write, without changing expressive power. The standard operators are:

- `<symbol>?` — optional: occurs 0 or 1 times.
- `<symbol>+` — non-empty repetition: occurs 1 or more times.
- `<symbol>*` — optional repetition: occurs 0 or more times.
- `(...)` — grouping, so an operator can apply to a whole sequence (e.g. `(<foo><bar>)?`).

These operators echo regular-expression syntax, and any basic regular expression can be re-expressed as a grammar using them plus character classes.

## From The Fuzzing Book — Fuzzing with Grammars
[[fuzzingbook-09-grammars|Ch 9]] introduces EBNF as part of its *grammar toolbox* and, crucially, implements `convert_ebnf_grammar()` to **desugar EBNF back into plain [[BNF]]** (the [[Grammar|`Grammar`]] structure the fuzzers actually consume). The conversion runs in two passes: `convert_ebnf_parentheses()` replaces each `(content)op` group with a fresh `new_symbol()`, then `convert_ebnf_operators()` rewrites the `?`/`+`/`*` operators into fresh recursive symbols:

- `<s>?` → `<new> ::= <empty> | <s>`
- `<s>+` → `<new> ::= <s> | <s><new>`
- `<s>*` → `<new> ::= <empty> | <s><new>`

(where `<empty>` is the epsilon/empty expansion). `EXPR_EBNF_GRAMMAR` is the worked example, and `is_valid_grammar()` accepts EBNF grammars too. EBNF is used pervasively in later chapters to keep grammar definitions compact.

## Connections
- [[BNF]] — the base notation EBNF extends and is desugared back into.
- [[ContextFreeGrammar]] / [[Grammar]] / [[ProductionRule]] — what EBNF is a notation for.
- [[GrammarBasedFuzzing]] — EBNF makes grammars practical to author for fuzzing.
- [[Nonterminal]] / [[Terminal]] — the symbols EBNF operators apply to.
- [[fuzzingbook-09-grammars]] — the chapter that defines `convert_ebnf_grammar()`.

## Sources
- [[fuzzingbook-09-grammars]] — *The Fuzzing Book* Ch 9, "Fuzzing with Grammars."
