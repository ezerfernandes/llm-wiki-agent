---
title: "Chart Parsing"
type: concept
tags: [parsing, grammar, dynamic-programming, chart, earley, fuzzing, python]
sources: [fuzzingbook-12-parser]
last_updated: 2026-06-06
---

# Chart Parsing

**Chart parsing** is a family of parsing algorithms that use [[DynamicProgramming|dynamic programming]] to avoid re-deriving the same sub-parses: rather than backtracking, the parser fills a **chart** (a table) of all partial parses consistent with the input read so far, then reads complete parses out of the finished chart. The [[EarleyParser|Earley parser]] is the canonical chart parser — indeed *chart parsing* is its alternative name. The chart has one column per input position, and each column accumulates the grammar rules that are partially or fully matched ending at that position.

## The Fuzzing Book's chart data structures
[[fuzzingbook-12-parser|Ch 12]] builds the chart from three classes:

- **`Column`** — created per input index `i` with its `letter`; stores a list of `states` (kept unique via an internal `dict`). `add(state)` inserts a state if not already present. The chapter exploits the fact that you can append to a Python *list* while iterating it (but not a `dict`) — `fill_chart()` adds states to the column it is currently scanning.
- **`Item`** — a *parse in progress for one rule*: a nonterminal `name`, its alternative expression `expr`, and a `dot` position. Methods `finished()` (dot past the end), `advance()` (dot + 1), and `at_dot()` (current symbol). The chapter notes an `Item` is exactly an `LR0` item from LR parsing.
- **`State`** — an `Item` plus the bookkeeping needed for chart parsing: the start column `s_col` and end column `e_col`, with `__hash__`/`__eq__` so states can be deduplicated. States are printed as e.g. `<A>:= a | <B> c (0,2)`, where `|` marks the dot and `(s,e)` the start/end columns.

The state notation `<A> : a ● <B> c` (with `●` for the dot) shows the parsed prefix on the left and the remaining symbols on the right. Worked examples walk the chart for input `adcd` column by column, showing `predict`/`scan`/`complete` populating each column until the start symbol completes in the final column — the signal of a successful parse.

## Connections
- [[EarleyParser]] — the chart parser this machinery implements.
- [[DynamicProgramming]] — the paradigm: tabulate sub-parses instead of recomputing.
- [[ParseForest]] — read out of the completed chart by `parse_forest()`.
- [[DerivationTree]] — the final per-input trees extracted from the chart.
- [[ContextFreeGrammar]] / [[Grammar]] — the rules whose `Item`s populate the chart.
- [[Parser]] — chart parsing realizes the book's `Parser` interface via `EarleyParser`.
- [[fuzzingbook-12-parser]] — the chapter that builds the `Column`/`Item`/`State` chart.

## Sources
- [[fuzzingbook-12-parser]] — *The Fuzzing Book* Ch 12, "Parsing Inputs."
