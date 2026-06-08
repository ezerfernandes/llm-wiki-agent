---
title: "Nonterminal"
type: concept
tags: [grammar, context-free-grammar, formal-languages, fuzzing, parsing]
sources: [fuzzingbook-09-grammars]
last_updated: 2026-06-06
---

# Nonterminal

A **nonterminal** is a grammar symbol that stands for a *language fragment to be further expanded*, as opposed to a [[Terminal|terminal]], which is a literal character that appears verbatim in the final output. In a [[ContextFreeGrammar|context-free grammar]], every [[ProductionRule|rule]] rewrites a nonterminal into a string of terminals and nonterminals; generation finishes when no nonterminals remain.

## From The Fuzzing Book — Fuzzing with Grammars
[[fuzzingbook-09-grammars|Ch 9]] adopts the convention that **nonterminals are enclosed in angle brackets** (e.g. `<digit>`, `<expr>`, `<start>`), which keeps them visually distinct from terminals in the [[Grammar|`Grammar`]] data structure and makes them easy to detect with a regular expression. Two helpers operate on them:

```python
RE_NONTERMINAL = re.compile(r'(<[^<> ]*>)')
nonterminals("<term> * <factor>")  # -> ['<term>', '<factor>']
is_nonterminal("<abc>")            # -> truthy match
is_nonterminal("+")                # -> None
```

`simple_grammar_fuzzer()` drives generation by repeatedly calling `nonterminals()` on the current string, picking one at random, and replacing it; the `max_nonterminals` cap bounds how many may remain pending. To emit a literal `<` or `>`, the chapter wraps it in its own nonterminal (e.g. `<left-angle> ::= "<"`) so it cannot be mistaken for a symbol. `is_valid_grammar()` checks that every nonterminal is both *defined* and *used* and is *reachable* from the start symbol.

## Connections
- [[Terminal]] — the complementary symbol kind (literal output).
- [[ContextFreeGrammar]] / [[Grammar]] — nonterminals are the keys of the grammar mapping.
- [[ProductionRule]] — each rule expands one nonterminal.
- [[fuzzingbook-09-grammars]] — the chapter that establishes the `<angle-bracket>` convention.

## Sources
- [[fuzzingbook-09-grammars]] — *The Fuzzing Book* Ch 9, "Fuzzing with Grammars."
