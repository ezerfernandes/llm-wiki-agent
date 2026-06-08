---
title: "Production Rule"
type: concept
tags: [grammar, context-free-grammar, formal-languages, fuzzing, parsing]
sources: [fuzzingbook-09-grammars]
last_updated: 2026-06-06
---

# Production Rule

A **production rule** (or *expansion rule*, or simply *rule*) is the basic building block of a [[ContextFreeGrammar|context-free grammar]]. It has the form `<A> ::= <B>`, meaning the [[Nonterminal|nonterminal]] on the left-hand side may be *rewritten* (expanded) into the string on the right. The `|` operator separates **alternatives** — `<digit> ::= 0 | 1 | 2 | ... | 9` says any one of those expansions may be chosen. A grammar defines exactly one rule (set of alternatives) per nonterminal, and rules may be **recursive**, which is the source of a grammar's ability to generate unbounded nested structure.

## From The Fuzzing Book — Fuzzing with Grammars
[[fuzzingbook-09-grammars|Ch 9]] models a production rule's right-hand side as a Python *list of alternatives* inside the [[Grammar|`Grammar`]] mapping — e.g. `"<expr>": ["<term> + <expr>", "<term> - <expr>", "<term>"]` is the rule for `<expr>` with three alternatives. The chapter's producer, `simple_grammar_fuzzer()`, applies a rule by picking a random nonterminal in the current string and `str.replace()`-ing it with `random.choice(grammar[symbol])`. [[EBNF]] adds shorthand operators (`?`/`+`/`*`/`(...)`) that `convert_ebnf_grammar()` desugars into ordinary recursive production rules with fresh symbols (e.g. `<idchar>+` becomes `<new> ::= <idchar> | <idchar><new>`). `is_valid_grammar()` rejects grammars whose rules are malformed (empty alternative lists, non-string expansions) or reference undefined/unreachable nonterminals.

## Connections
- [[ContextFreeGrammar]] / [[Grammar]] — a grammar *is* a set of production rules.
- [[Nonterminal]] / [[Terminal]] — a rule expands a nonterminal into a mix of both.
- [[EBNF]] / [[BNF]] — EBNF operators desugar into plain recursive production rules.
- [[GrammarBasedFuzzing]] — generation = repeatedly applying production rules.
- [[fuzzingbook-09-grammars]] — the chapter that represents rules as lists of alternatives.

## Sources
- [[fuzzingbook-09-grammars]] — *The Fuzzing Book* Ch 9, "Fuzzing with Grammars."
