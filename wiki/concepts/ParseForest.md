---
title: "Parse Forest"
type: concept
tags: [parsing, grammar, ambiguity, derivation-tree, earley, fuzzing, python]
sources: [fuzzingbook-12-parser]
last_updated: 2026-06-06
---

# Parse Forest

A **parse forest** is the set (or compact shared representation) of *all* the [[DerivationTree|derivation trees]] that a grammar can assign to a single input string. When a grammar is [[Ambiguity|ambiguous]], one input has more than one valid parse, so a parser that wants to be complete cannot return a single tree — it returns (a structure encoding) a *forest* and lets the caller enumerate trees from it. For fuzzing this matters because each distinct parse decomposes the seed input differently, giving different subtrees to mutate and recombine.

## The Fuzzing Book's treatment
[[fuzzingbook-12-parser|Ch 12]] produces and consumes parse forests inside the [[EarleyParser|`EarleyParser`]]:

- **`parse_paths(named_expr, chart, frm, til)`** unifies an expression against the [[ChartParsing|chart]], finding all ways the symbols of a rule could span the input between two columns.
- **`parse_forest(chart, state)`** turns a completed state into a forest node — the nonterminal name plus the list of alternative path-expressions that could have produced it. Its worked example: parsing `1+2+3` against `<expr>:[<expr>,+,<expr>]` yields two groupings, `[{<expr>:1+2},+,{<expr>:3}]` and `[{<expr>:1},+,{<expr>:2+3}]`.
- **`extract_trees(forest)`** walks the forest and *yields* derivation trees. The enhanced version uses `itertools.product` over the alternative sub-paths to emit **every** tree for an ambiguous grammar.

A subtlety the chapter stresses: a parse forest can contain **infinitely many** trees when the grammar is self-referential (e.g. `<expr> ::= <expr>`). Eager extraction recurses forever, so the chapter provides lazy, one-tree-at-a-time extractors — `SimpleExtractor` (random path choice) and `EnhancedExtractor` (which uses `ChoiceNode`s to systematically enumerate finite, non-directly-recursive trees).

## Connections
- [[Ambiguity]] — the reason a single input has a forest rather than one tree.
- [[DerivationTree]] — the individual trees extracted from a forest.
- [[EarleyParser]] — the parser that builds forests (`parse_forest`, `extract_trees`).
- [[ChartParsing]] — the chart the forest is read out of (`parse_paths`).
- [[Parser]] — `parse_prefix()` returns a `(cursor, forest)` pair in the base interface.
- [[fuzzingbook-12-parser]] — the chapter that builds and extracts parse forests.

## Sources
- [[fuzzingbook-12-parser]] — *The Fuzzing Book* Ch 12, "Parsing Inputs."
