---
title: "Packrat Parsing"
type: concept
tags: [parsing, peg, memoization, recursive-descent, packrat, fuzzing, python]
sources: [fuzzingbook-12-parser]
last_updated: 2026-06-06
---

# Packrat Parsing

**Packrat parsing** is a linear-time technique for parsing [[ParsingExpressionGrammar|Parsing Expression Grammars]]. It is, at heart, a top-down recursive-descent parser with backtracking, made efficient by **memoizing** every intermediate result: the name "packrat" comes from the fact that it greedily *hoards* the result of every sub-parse so it never recomputes the same `(symbol, position)` problem twice. This memoization is exactly what turns an exponential-in-the-worst-case backtracking recognizer into a guaranteed `O(n)` parser (at the cost of `O(n)` table space). Packrat parsing was introduced by [[BryanFord|Bryan Ford]].

## The Fuzzing Book's `PEGParser`
[[fuzzingbook-12-parser|Ch 12]] implements packrat parsing as the `PEGParser` (a [[Parser]] subclass) with two mutually-recursive methods:

- **`unify_key(key, text, at)`** — if `key` is a terminal, match it against `text` at position `at`; if it's a nonterminal, try each ordered choice via `unify_rule()` and return on the **first** that succeeds (the PEG ordered-choice semantics).
- **`unify_rule(rule, text, at)`** — match the rule's tokens in sequence by calling `unify_key()` on each; the rule succeeds only if **all** tokens unify.

Because `unify_key()` can be invoked repeatedly with identical arguments while exploring ordered choices, the chapter decorates it with Python's `functools.lru_cache(maxsize=None)`. The chapter states plainly: *"This memoization gives the algorithm its name – Packrat."* An exercise ("An Alternative Packrat") reworks the parser as `PackratParser` to track the remaining *substring* instead of an integer index.

Limitations inherited from PEGs: the parser produces a single unambiguous tree (it still returns a one-element list of trees for interface uniformity), and it cannot recognize arbitrary [[ContextFreeGrammar|CFGs]] — see the `PEG_SURPRISE` example — which is why the chapter then develops the [[EarleyParser]].

## Connections
- [[ParsingExpressionGrammar]] — the grammar formalism packrat parsing is built for.
- [[Parser]] — `PEGParser`/`PackratParser` subclass the book's `Parser` base.
- [[Memoization]] — the caching (`lru_cache`) that makes packrat parsing linear-time.
- [[EarleyParser]] — the chapter's alternative for arbitrary CFGs and ambiguity.
- [[BryanFord]] — introduced packrat parsing and PEGs.
- [[fuzzingbook-12-parser]] — the chapter that implements the packrat `PEGParser`.

## Sources
- [[fuzzingbook-12-parser]] — *The Fuzzing Book* Ch 12, "Parsing Inputs."
