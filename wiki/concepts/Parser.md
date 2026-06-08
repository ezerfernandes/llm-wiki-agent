---
title: "Parser"
type: concept
tags: [parsing, grammar, derivation-tree, fuzzing, testing, python]
sources: [fuzzingbook-12-parser, fuzzingbook-15-greybox-grammar-fuzzer, fuzzingbook-16-reducer, fuzzingbook-18-grammar-miner]
last_updated: 2026-06-06
---

# Parser

A **parser** is the component of a program that turns a (structured) input *string* into a structured representation — here, a [[DerivationTree|derivation tree]] over a [[ContextFreeGrammar|grammar]]. Parsing is the *inverse* of grammar-based generation: where a [[GrammarBasedFuzzing|grammar fuzzer]] expands a grammar to *produce* strings, a parser *decomposes* a given valid string back into the tree that the same grammar would have produced. This makes parsing the bridge that lets a fuzzer ingest real seed inputs, take them apart, and mutate/recombine their parts to generate new, structurally-valid variants.

## The Fuzzing Book's `Parser` base class
[[fuzzingbook-12-parser|Ch 12]] mints a minimal `Parser` base class that all concrete parsers subclass. The user-facing contract is two steps:

```python
parser = Parser(grammar)
trees  = parser.parse(input)   # iterable of derivation trees
```

Key design points:

- **`parse_prefix(text)`** (abstract; defined per subclass) returns `(cursor, forest)` — the index up to which parsing succeeded and the partial parse forest. **`parse(text)`** calls it, raises `SyntaxError` if the whole string wasn't consumed, and prunes each resulting tree.
- **Canonical grammar form.** The generation-oriented [[Grammar|`Grammar`]] (rules stored as strings) is converted to a *canonical* `Dict[str, List[List[str]]]` representation (`canonical()`, `single_char_tokens()`), where each symbol in an expansion is a separate token — easier to work with during parsing. A phony `<>` start rule is inserted when the start symbol has multiple alternatives.
- **No separate lexer.** The chapter deliberately skips the traditional *lexer/tokenizer* stage. Instead it parses against a grammar with full syntactic detail and then runs `prune_tree()` to collapse token nodes — `coalesce()` merges adjacent terminal characters into single leaf strings. This avoids an artificial lexing/parsing split (contrast with building an [[AbstractSyntaxTree|AST]] via a shallow lexed tree).

The chapter provides two concrete subclasses: the [[ParsingExpressionGrammar|`PEGParser`]] (fast, ordered-choice, no ambiguity) and the [[EarleyParser|`EarleyParser`]] (any CFG, all parses). Returns are always an *iterable of trees*, so ambiguous grammars can yield multiple parses.

## From The Fuzzing Book — Greybox Fuzzing with Grammars
[[fuzzingbook-15-greybox-grammar-fuzzer|Ch 15]] is a major *consumer* of the parser: it is the bridge that lets a [[GreyboxFuzzing|greybox fuzzer]] turn seed strings into structure. The [[FragmentBasedFuzzing|`FragmentMutator`]] uses `parser.parse()` to obtain a [[DerivationTree|derivation tree]] (subject to a 200 ms `Timeout`) whose subtrees it recombines; the [[RegionMutation|`RegionMutator`]] reaches past `parse()` into the [[EarleyParser|Earley]] `chart_parse()` table to recover byte regions from inputs that don't parse at all. This is exactly the "parsing is the inverse of generation, feeding seeds back into fuzzing" role this page describes, now operating inside a coverage-guided loop.

## From The Fuzzing Book — Reducing Failure-Inducing Inputs
[[fuzzingbook-16-reducer|Ch 16]] is another consumer: the [[GrammarReducer|`GrammarReducer`]] is constructed with a `Parser` (an [[EarleyParser|`EarleyParser`]] over `EXPR_GRAMMAR`) and calls `parser.parse()` to turn a failure-inducing input into a [[DerivationTree|derivation tree]]. It then performs [[HierarchicalDeltaDebugging|hierarchical delta debugging]] on that tree — replacing subtrees with smaller subtrees of the same [[Nonterminal|nonterminal]] and applying alternate grammar expansions — so that *every* reduced candidate is syntactically valid by construction. This is precisely the "parse a seed, take it apart, recombine its parts" role this page describes, here applied to *shrinking* an input rather than fuzzing it (lexical [[DeltaDebugging|delta debugging]] stalls because its blind cuts rarely parse).

## From The Fuzzing Book — Mining Input Grammars
[[fuzzingbook-18-grammar-miner|Ch 18]] inverts the relationship: instead of *running* a `Parser`, it treats the program's own hand-written parser as the thing to be reverse-engineered. By dynamically tracing how a program (its `process_inventory()` example from [[fuzzingbook-12-parser|Ch 12]], or Python's `urllib.parse`) decomposes an input into substrings held by named variables, [[GrammarMiner|`GrammarMiner`]] recovers the [[Grammar|grammar]] the parser implicitly encodes — i.e. it reconstructs a parser's grammar from observed parsing behavior. The recovered grammar can then be re-parsed/fuzzed with the book's standard machinery.

## Connections
- [[GrammarMiner]] / [[GrammarInference]] — Ch 18 recovers the grammar a hand-written parser implicitly encodes, by tracing it.
- [[GrammarReducer]] / [[HierarchicalDeltaDebugging]] — Ch 16 parses an input to a tree, then reduces the tree.
- [[ParsingExpressionGrammar]] / [[PackratParsing]] — the PEG parser subclass (`PEGParser`).
- [[FragmentBasedFuzzing]] / [[RegionMutation]] — Ch 15 mutators that parse seeds (or partial parses) into structure for fuzzing.
- [[EarleyParser]] — the general CFG parser subclass; uses [[ChartParsing]] and [[ParseForest|parse forests]].
- [[DerivationTree]] — the output data structure (`parse()` returns these).
- [[ContextFreeGrammar]] / [[Grammar]] — the input specification a parser parses *against*.
- [[GrammarBasedFuzzing]] — parsing is the inverse of grammar production; feeds seeds back into fuzzing.
- [[Ambiguity]] — why `parse()` returns an iterable of trees rather than one.
- [[AbstractSyntaxTree]] — the lexer-based alternative to the book's tree-pruning approach.
- [[fuzzingbook-12-parser]] — the chapter that mints this class.
- [[fuzzingbook-10-grammar-fuzzer|Ch 10]] — defines `DerivationTree`, the parser's output type.
- [[fuzzingbook-13-probabilistic-grammar-fuzzer|Ch 13]] — reuses this parser machinery (parses corpus inputs to count expansions); [[fuzzingbook-18-grammar-miner|Ch 18]] instead *recovers* the grammar a parser encodes.

## Sources
- [[fuzzingbook-12-parser]] — *The Fuzzing Book* Ch 12, "Parsing Inputs."
- [[fuzzingbook-15-greybox-grammar-fuzzer]] — *The Fuzzing Book* Ch 15, "Greybox Fuzzing with Grammars" (parsing seeds into fragments/regions for structure-aware mutation).
- [[fuzzingbook-16-reducer]] — *The Fuzzing Book* Ch 16, "Reducing Failure-Inducing Inputs" (the `GrammarReducer` parses inputs into trees for hierarchical reduction).
- [[fuzzingbook-18-grammar-miner]] — *The Fuzzing Book* Ch 18, "Mining Input Grammars" (recovers the grammar a hand-written parser implicitly encodes).
