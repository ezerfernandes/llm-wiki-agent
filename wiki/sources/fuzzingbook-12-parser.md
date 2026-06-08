---
title: "The Fuzzing Book Ch 12 — Parsing Inputs"
type: source
tags: [book, fuzzingbook, fuzzing, testing, security, parsing, grammar, peg, earley, derivation-tree]
date: 2026-06-06
source_file: raw/books/fuzzingbook/fuzzingbook-12-parser.md
book: "The Fuzzing Book"
book_authors: ["Andreas Zeller", "Rahul Gopinath", "Marcel Böhme", "Gordon Fraser", "Christian Holler"]
book_publisher: "CISPA Helmholtz Center for Information Security"
book_year: 2024
book_url: "https://www.fuzzingbook.org/"
---

# Parsing Inputs

## Summary
Chapter 12 — the parsing chapter of Part III (Syntactic Fuzzing) — runs grammar-based fuzzing *in reverse*: it [[Parser|parses]] existing valid seed inputs into [[DerivationTree|derivation trees]] so their subtrees can be mutated, crossed over, and recombined into new valid, slightly-changed inputs. It builds on the [[fuzzingbook-09-grammars|Ch 9]] grammars and the [[fuzzingbook-10-grammar-fuzzer|Ch 10]] derivation-tree machinery, and motivates parsing with a CSV example where a plain `GrammarFuzzer` produces almost no valid rows because the grammar under-specifies the format. After showing why ad-hoc/regex parsing collapses on recursive formats (JSON, quoted CSV), it develops a `Parser` base class and two concrete parsers: the [[PackratParsing|`PEGParser`]] (a memoized packrat parser for [[ParsingExpressionGrammar|Parsing Expression Grammars]], fast but ordered-choice and unambiguous) and the [[EarleyParser|`EarleyParser`]] (a [[ChartParsing|chart parser]] that handles **any** [[ContextFreeGrammar|context-free grammar]], including [[Ambiguity|ambiguous]] and recursive ones). The parsed trees feed directly into the seed-recombination fuzzing of [[fuzzingbook-13-probabilistic-grammar-fuzzer|the next chapters]], the grammar miner of [[fuzzingbook-18-grammar-miner|Ch 18]], and the reducer of [[fuzzingbook-16-reducer|Ch 16]].

## Key Concepts
- **[[Parser|`Parser`]] base class** — minimal interface: `parse(text)` returns an iterable of [[DerivationTree|derivation trees]]; `parse_prefix(text)` returns `(cursor, forest)`. Converts a generation-oriented [[Grammar|`Grammar`]] into a *canonical* form (`canonical()`, `single_char_tokens()`, `CanonicalGrammar = Dict[str, List[List[str]]]`) where each symbol is a separate token. Skips a separate lexer; instead `prune_tree()`/`coalesce()` collapse token nodes into leaf strings after parsing (contrast with the lexer→[[AbstractSyntaxTree|AST]] route).
- **[[ParsingExpressionGrammar|Parsing Expression Grammars (PEG)]]** — look like CFGs but use **ordered choice**: try alternatives left-to-right, commit to the first match. Unambiguous by construction; introduced by [[BryanFord|Bryan Ford]] (2004). `PEG2 = {'<start>': ['ab','abc']}` matches `ab` but not `abc`.
- **[[PackratParsing|Packrat parsing]] (`PEGParser`)** — recursive-descent with backtracking made linear-time by [[Memoization|memoizing]] (`functools.lru_cache`) the mutually-recursive `unify_key()`/`unify_rule()`. The caching is what names the technique "packrat."
- **[[EarleyParser|Earley parser]] (`EarleyParser`)** — general CFG parser ([[JayEarley|Jay Earley]], 1970) using [[DynamicProgramming|dynamic programming]] / [[ChartParsing|chart parsing]]. `O(n^3)` arbitrary, `O(n^2)` unambiguous, `O(n)` for `LR(k)`. Operations `predict()`, `scan()`, `complete()` fill a chart of `Column`/`State`/`Item` (`LR0` items with a `dot`).
- **[[ParseForest|Parse forests]] & [[Ambiguity|ambiguity]]** — `parse_paths()`/`parse_forest()`/`extract_trees()` read all parses out of the chart; enhanced `extract_trees()` yields every tree (`itertools.product`) for ambiguous grammars. Lazy `SimpleExtractor`/`EnhancedExtractor` (with `ChoiceNode`) avoid infinite recursion on self-referential grammars.
- **[[Fixpoint|`fixpoint`]] & the Aycock epsilon fix** — `fixpoint(f)` iterates a step until stable; used to compute the `nullable` set (nonterminals deriving the empty string) so the Earley parser handles **epsilon rules** by advancing nullable predicted states.
- **The Leo optimization (exercise)** — `LeoParser` restores `O(n)` on right-recursive grammars via Joop Leo's *deterministic reduction path* and *transitive* (`TState`) items; `FilteredLeoParser` discards infinite token-repetition chains.

## Key Claims
- Parsing seed inputs into derivation trees lets a fuzzer mutate/recombine real structure that a hand-written grammar alone misses (the CSV `process_vehicle` motivation).
- Ad-hoc and regex-based parsers fall apart on recursive/quoted formats; formal grammar-based parsers compose cleanly.
- A PEG can denote a *different* language than the same rules read as a CFG; only `LL(1)` grammars are guaranteed equivalent under both. The PEG parser recognizes `PEG_SURPRISE`'s `a`-strings of length `2^n`, not the `2n` a CFG generator yields.
- The Earley parser parses *any* CFG; arbitrary-CFG parsing is `O(n^3)` worst case and reduces to boolean matrix multiplication, so sub-cubic is unlikely.
- Some context-free *languages* are inherently ambiguous and have no `LR(1)` grammar.
- The set of trees in a parse forest can be infinite (self-reference), so trees must be extracted lazily, one at a time.

## Key Quotes
> "given a string, one can decompose the string into its constituent parts that correspond to the parts of grammar used to generate it – the derivation tree of that string." — chapter intro, on parsing as the inverse of generation.

> "This memoization gives the algorithm its name – Packrat." — on caching `unify_key()` with `lru_cache`.

> "The parser uses dynamic programming to generate a table containing a forest of possible parses at each letter index." — on Earley chart parsing.

## Connections
- [[Parser]] — the base class the chapter mints; parent of both concrete parsers.
- [[ParsingExpressionGrammar]] / [[PackratParsing]] — the fast, ordered-choice, unambiguous PEG path.
- [[EarleyParser]] / [[ChartParsing]] / [[ParseForest]] — the general any-CFG path with all parses.
- [[Ambiguity]] — multiple parses per string; PEG resolves it, Earley enumerates it.
- [[Fixpoint]] / [[Memoization]] — algorithmic building blocks (nullable set; packrat caching).
- [[DynamicProgramming]] — the paradigm behind chart parsing.
- [[DerivationTree]] — the shared output type; a parse tree *is* a derivation tree.
- [[ContextFreeGrammar]] / [[Grammar]] / [[Nonterminal]] / [[Terminal]] — the grammar formalism parsed against.
- [[GrammarBasedFuzzing]] — parsing is the inverse of grammar production; parsed trees feed recombination fuzzing.
- [[AbstractSyntaxTree]] — the lexer-based alternative to the chapter's tree-pruning approach.
- [[JayEarley]] — invented the Earley parser; [[BryanFord]] — introduced PEGs and packrat parsing.
- [[fuzzingbook-09-grammars|Ch 9]] / [[fuzzingbook-10-grammar-fuzzer|Ch 10]] — prerequisite grammars and derivation trees.
- [[fuzzingbook-13-probabilistic-grammar-fuzzer|Ch 13]] / [[fuzzingbook-16-reducer|Ch 16]] / [[fuzzingbook-18-grammar-miner|Ch 18]] — reuse this parser machinery.

## Contradictions
- None identified.
