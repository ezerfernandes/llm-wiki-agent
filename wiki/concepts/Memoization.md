---
title: "Memoization"
type: concept
tags: [algorithm-design, optimization, caching, parsing, python]
sources: [fuzzingbook-12-parser]
last_updated: 2026-06-06
---

# Memoization

**Memoization** is the optimization of caching the result of a (pure) function call keyed on its arguments, so that repeated calls with the same arguments return the cached value instead of recomputing it. It is the core trick that converts exponential-time recomputing recursions into polynomial- or linear-time algorithms, and is closely related to (top-down) [[DynamicProgramming|dynamic programming]].

## The Fuzzing Book's treatment
[[fuzzingbook-12-parser|Ch 12]] uses memoization to make [[PackratParsing|packrat parsing]] efficient. The [[ParsingExpressionGrammar|PEG]] `unify_key()` method is mutually recursive and gets called many times with identical `(key, text, at)` arguments while exploring ordered choices; the chapter decorates it with Python's `functools.lru_cache(maxsize=None)` so each sub-parse is computed once. As the chapter puts it, *"This memoization gives the algorithm its name – Packrat"* — the parser "hoards" every result like a packrat. The same caching idea recurs in the [[EarleyParser|Earley parser]]'s chart (storing partial parses per column) and in the Leo parser's *transitive* items.

## Connections
- [[PackratParsing]] — packrat parsing *is* memoized recursive-descent PEG parsing.
- [[ParsingExpressionGrammar]] — the grammar formalism whose parser is memoized.
- [[DynamicProgramming]] — tabulation is the iterative cousin of memoized recursion.
- [[EarleyParser]] / [[ChartParsing]] — the chart memoizes partial parses per input position.
- [[fuzzingbook-12-parser]] — the chapter that applies `lru_cache` memoization to parsing.

## Sources
- [[fuzzingbook-12-parser]] — *The Fuzzing Book* Ch 12, "Parsing Inputs."
