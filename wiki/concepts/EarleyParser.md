---
title: "Earley Parser"
type: concept
tags: [parsing, grammar, context-free-grammar, chart-parsing, dynamic-programming, fuzzing, python]
sources: [fuzzingbook-12-parser, fuzzingbook-13-probabilistic-grammar-fuzzer, fuzzingbook-15-greybox-grammar-fuzzer, fuzzingbook-16-reducer]
last_updated: 2026-06-06
---

# Earley Parser

The **Earley parser** is a general parsing algorithm that can parse **any** [[ContextFreeGrammar|context-free grammar]] — including ambiguous, left-recursive, and right-recursive grammars that defeat simpler parsers. Invented by [[JayEarley|Jay Earley]] (1970) for computational linguistics, it uses [[DynamicProgramming|dynamic programming]] ([[ChartParsing|chart parsing]]) to build, position by position, a table of all partial parses consistent with the input so far. Its worst-case complexity is `O(n^3)` for arbitrary grammars, `O(n^2)` for unambiguous grammars, and `O(n)` for `LR(k)` grammars. It is the [[fuzzingbook-12-parser|Ch 12]] parser of choice for fuzzing because it accepts arbitrary CFGs and surfaces **all** parses of an ambiguous input.

## How it works (the three operations)
The parser fills a **chart** — one [[ChartParsing|`Column`]] per input position, each holding `State`s. A `State` is an `Item` (a grammar rule `name → expr` with a `dot` marking how much is parsed, i.e. an `LR0` item) annotated with its start column `s_col` and end column `e_col`. The main loop `fill_chart()` applies, per state:

- **`predict()`** — if the symbol at the dot is a nonterminal, add all of its alternative expansions (dot at 0) to the current column.
- **`scan()`** — if the symbol at the dot is a terminal matching the next input letter, advance the state into the next column.
- **`complete()`** — if a state is finished (dot past the end), advance every *parent* state in the start column that was waiting on this nonterminal.

`parse_prefix()` finds the furthest column where the start symbol completed; `parse_paths()`, `parse_forest()`, and `extract_trees()` then read derivation trees out of the chart (see [[ParseForest]]).

## Refinements the chapter adds
- **The Aycock epsilon fix.** Plain Earley mishandles **epsilon rules** (rules deriving the empty string). The chapter pre-computes the set of `nullable` nonterminals via a [[Fixpoint|`fixpoint`]] iteration and, after `predict()`ing a nullable nonterminal, also advances the state — letting the parser handle `nullable` symbols correctly.
- **Ambiguity / parse forests.** `extract_trees()` is enhanced to *yield* every derivation tree (via `itertools.product` over alternative paths) for [[Ambiguity|ambiguous]] grammars.
- **Lazy tree extraction.** Eager extraction recurses infinitely on self-referential grammars; `SimpleExtractor` and `EnhancedExtractor` (with `ChoiceNode`) extract one tree at a time, skipping directly-recursive nodes.
- **The Leo optimization (exercise).** Plain Earley is `O(n^2)` on right-recursive grammars; Joop Leo's *deterministic reduction path* trick (`LeoParser`, using *transitive* items) restores `O(n)`. A `FilteredLeoParser` discards infinite token-repetition chains.

The chapter's `Background` situates Earley among `LL`/`LR` traditions and other general CFG parsers (GLL, GLR, CYK, ANTLR's `ALL(*)`), and notes that arbitrary-CFG parsing reduces to boolean matrix multiplication, so sub-cubic worst case is unlikely.

## From The Fuzzing Book — Probabilistic Grammar Fuzzing
[[fuzzingbook-13-probabilistic-grammar-fuzzer|Ch 13]] is the first downstream *consumer* of the `EarleyParser`: to [[GrammarMining|learn probabilities]] from a corpus, `ExpansionCountMiner`/`ProbabilisticGrammarMiner` parse each sample input with an `EarleyParser` into a [[DerivationTree|derivation tree]] and count its expansions. The chapter is explicit that the parser needs an **explicit token set** for these grammars (e.g. `IP_ADDRESS_TOKENS = {"<octet>"}`, `URL_TOKENS = {"<scheme>", "<host>", ...}`) so that tokens are kept whole rather than split into characters. The resulting expansion counts become the `prob` annotations of a [[ProbabilisticGrammar|probabilistic grammar]] — making the Earley parser the bridge from real-world samples to a tuned [[ProbabilisticGrammarFuzzer|`ProbabilisticGrammarFuzzer`]].

## From The Fuzzing Book — Greybox Fuzzing with Grammars
[[fuzzingbook-15-greybox-grammar-fuzzer|Ch 15]] uses the `EarleyParser` in *two* ways for [[GrammarAwareGreyboxFuzzing|grammar-aware greybox fuzzing]]. First, `parse()` turns seeds into [[DerivationTree|derivation trees]] whose subtrees become the [[FragmentBasedFuzzing|fragment pool]] (with a 200 ms `Timeout` to keep mutation fast). Second — crucially — its `chart_parse()` exposes the raw [[ChartParsing|parse table]] so that, even for *unparsable* inputs, each finished state's `(s_col.index, e_col.index)` span labels a byte **region** with a grammar symbol ([[RegionMutation|region-based mutation]]); the number of state-bearing columns also yields the [[DegreeOfValidity|degree of validity]] (length of the longest parsable prefix). The parser is configured with an explicit token set (`XML_TOKENS = {"<id>", "<text>"}`) so tokens stay whole.

## From The Fuzzing Book — Reducing Failure-Inducing Inputs
[[fuzzingbook-16-reducer|Ch 16]] uses the `EarleyParser` (over `EXPR_GRAMMAR`) as the front end of its [[GrammarReducer|`GrammarReducer`]]: `parse()` turns a failure-inducing input into a [[DerivationTree|derivation tree]] on which [[HierarchicalDeltaDebugging|hierarchical delta debugging]] then operates. The chapter also uses Earley's strictness as a foil — an `EvalMysteryRunner` parses each candidate and returns `UNRESOLVED` for inputs that fail to parse, which is exactly why blind [[DeltaDebugging|delta debugging]] stalls on structured inputs and why parsing-then-tree-reduction wins.

## Connections
- [[GrammarReducer]] / [[HierarchicalDeltaDebugging]] — Ch 16 parses inputs with Earley, then reduces the resulting tree.
- [[ChartParsing]] — the dynamic-programming table (`Column`/`State`/`Item`) Earley fills.
- [[FragmentBasedFuzzing]] / [[RegionMutation]] / [[DegreeOfValidity]] — Ch 15 reuses `parse()` (fragments) and `chart_parse()` (regions, validity).
- [[GrammarMining]] / [[ProbabilisticGrammar]] — Ch 13 parses a corpus with the Earley parser to mine expansion probabilities.
- [[ParseForest]] — the structure `parse_forest()` produces, from which trees are extracted.
- [[Ambiguity]] — Earley returns all parses; the reason `extract_trees()` yields multiple trees.
- [[Fixpoint]] — used to compute the `nullable` set for the Aycock epsilon fix.
- [[DynamicProgramming]] — the algorithmic paradigm behind chart parsing.
- [[ContextFreeGrammar]] / [[Grammar]] — Earley parses *any* CFG, unlike a PEG parser.
- [[ParsingExpressionGrammar]] / [[PackratParsing]] — the faster but less general alternative in the same chapter.
- [[Parser]] — `EarleyParser` subclasses the book's `Parser` base.
- [[DerivationTree]] — the per-input output trees.
- [[JayEarley]] — invented the algorithm.
- [[fuzzingbook-12-parser]] — the chapter that implements the Earley parser.

## Sources
- [[fuzzingbook-12-parser]] — *The Fuzzing Book* Ch 12, "Parsing Inputs."
- [[fuzzingbook-13-probabilistic-grammar-fuzzer]] — *The Fuzzing Book* Ch 13, "Probabilistic Grammar Fuzzing" (parses a corpus to mine expansion probabilities).
- [[fuzzingbook-15-greybox-grammar-fuzzer]] — *The Fuzzing Book* Ch 15, "Greybox Fuzzing with Grammars" (`parse()` for fragments, `chart_parse()` for regions and degree of validity).
- [[fuzzingbook-16-reducer]] — *The Fuzzing Book* Ch 16, "Reducing Failure-Inducing Inputs" (front end of the `GrammarReducer`).
