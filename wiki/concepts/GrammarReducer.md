---
title: "Grammar-Based Reducer"
type: concept
tags: [debugging, testing, fuzzing, input-reduction, grammars, parsing, derivation-tree, algorithm]
sources: [fuzzingbook-16-reducer]
last_updated: 2026-06-06
---

# Grammar-Based Reducer

A **grammar-based reducer** minimizes a *syntactically complex* failure-inducing input by reducing its [[DerivationTree|derivation tree]] rather than its raw string — keeping every candidate syntactically valid by construction. It is the structure-aware answer to [[DeltaDebugging|delta debugging]]'s failure on structured inputs: where blind lexical cuts produce mostly invalid (`UNRESOLVED`) candidates and stall, a grammar reducer only ever produces inputs the [[Grammar|grammar]] accepts. In [[fuzzingbook-16-reducer|Ch 16]] this is the `GrammarReducer` class (also called *GRABR* in the chapter); the algorithm it instantiates is [[HierarchicalDeltaDebugging|hierarchical delta debugging]].

## How it works (Ch 16)
`GrammarReducer` is a `CachingReducer` constructed with a [[Runner|`Runner`]] *and* a [[Parser|`Parser`]] (the chapter uses an [[EarleyParser|`EarleyParser`]] over `EXPR_GRAMMAR`, reusing [[fuzzingbook-12-parser|Ch 12]]). Its `reduce()` parses the input into a tree, reduces the tree, then renders it back with `all_terminals()`. Two simplification strategies, both operating on subtrees rooted at a given [[Nonterminal|nonterminal]] symbol:

1. **Replace a subtree** (`subtrees_with_symbol()`) — substitute a symbol's subtree with a *smaller* subtree already present in the tree that has the *same root symbol* (e.g. replace the whole `<expr>` with its inner `<expr>` to turn `1 + (2 * 3)` into `(2 + 3)`). Mirrors *Generalized Tree Reduction* (Herfert 2017) and *Perses* (Sun 2018).
2. **Alternate expansions** (`alternate_reductions()`) — apply a different [[ProductionRule|grammar production]] for the symbol that has *fewer children* (e.g. `<term> ::= <factor>` instead of `<term> ::= <term> * <factor>`), filling required child symbols from existing subtrees. *Searching for alternate expansions is a contribution original to this chapter.*

`symbol_reductions()` unions both strategies (subtrees first, then alternates), deduplicated and sorted by node count. `reduce_subtree()` greedily walks each child, applies any reduction that keeps the whole tree's rendered string `FAIL`ing (restoring on `PASS`), and recurses. Helpers: `number_of_nodes()`, `max_height()`, `possible_combinations()`, `tree_list_to_string()`.

**Depth-oriented strategy** — `reduce_tree()` advances a `depth` parameter from 0 upward, preferring *large/shallow* subtrees first and only descending when no shallow reduction succeeds (resetting depth to 0 after each success). This mimics delta debugging's "cut roughly in half" intuition and converges in even fewer tests.

**Payoff:** on a long expression generated with `GrammarFuzzer(min_nonterminals=100)`, `GrammarReducer` needs only a handful of tests where `DeltaDebuggingReducer` needs orders of magnitude more (and reduces less), because no test is ever wasted on an invalid input.

## Connections
- [[HierarchicalDeltaDebugging]] — the algorithm `GrammarReducer` implements (HDD over the parse tree).
- [[DeltaDebugging]] / [[DDMin]] — the lexical baseline this replaces for structured inputs.
- [[InputReduction]] — `GrammarReducer` is a `Reducer`/`CachingReducer` subclass.
- [[DerivationTree]] — the data structure it reduces (subtree replacement + alternate expansion).
- [[Parser]] / [[EarleyParser]] — supply the tree; reused from [[fuzzingbook-12-parser|Ch 12]].
- [[Grammar]] / [[Nonterminal]] / [[ProductionRule]] — alternate expansions come from grammar productions.
- [[OneMinimality]] — typically reaches a smaller, more meaningful minimum than character-level 1-minimality.
- [[GrammarBasedFuzzing]] — the inverse direction: here the grammar *shrinks* rather than *grows* a tree.
- [[fuzzingbook-16-reducer]] — the chapter that mints `GrammarReducer`.

## Sources
- [[fuzzingbook-16-reducer]] — *The Fuzzing Book* Ch 16, "Reducing Failure-Inducing Inputs."
