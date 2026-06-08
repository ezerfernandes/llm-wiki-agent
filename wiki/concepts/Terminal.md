---
title: "Terminal (Grammar Symbol)"
type: concept
tags: [grammar, context-free-grammar, formal-languages, fuzzing, parsing]
sources: [fuzzingbook-09-grammars]
last_updated: 2026-06-06
---

# Terminal (Grammar Symbol)

A **terminal** is a grammar symbol that is a *literal* — a concrete character or string that appears verbatim in generated output and is not expanded further. Terminals are the leaves of a derivation; everything else is a [[Nonterminal|nonterminal]] awaiting expansion. In a [[ContextFreeGrammar|context-free grammar]], a string belongs to the language exactly when it can be derived from the start symbol down to a sequence consisting only of terminals.

## From The Fuzzing Book — Fuzzing with Grammars
[[fuzzingbook-09-grammars|Ch 9]] treats anything that is *not* a `<angle-bracket>` [[Nonterminal|nonterminal]] as a terminal: digits like `"0"`, operators like `"+"`, and literal text such as `"http"` or `"://"` in `URL_GRAMMAR`. Character classes are produced programmatically with `srange(characters)` (one terminal per character in a string) and `crange(start, end)` (all characters in an ASCII range), e.g. `srange(string.ascii_letters)` or `crange('0', '9')`. When visualizing grammars as railroad diagrams, the chapter draws terminals as ovals and nonterminals as rectangles (`syntax_diagram_symbol()`).

## Connections
- [[Nonterminal]] — the complementary symbol kind (expanded, not literal).
- [[ContextFreeGrammar]] / [[Grammar]] — terminals are the literal output a grammar produces.
- [[fuzzingbook-09-grammars]] — the chapter that introduces `srange()`/`crange()` for building terminal character classes.

## Sources
- [[fuzzingbook-09-grammars]] — *The Fuzzing Book* Ch 9, "Fuzzing with Grammars."
