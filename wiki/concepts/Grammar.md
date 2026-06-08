---
title: "Grammar (Fuzzing Data Structure)"
type: concept
tags: [fuzzing, grammar, context-free-grammar, data-structure, python, testing]
sources: [fuzzingbook-09-grammars, fuzzingbook-10-grammar-fuzzer, fuzzingbook-13-probabilistic-grammar-fuzzer, fuzzingbook-14-generator-grammar-fuzzer, fuzzingbook-18-grammar-miner, fuzzingbook-23-configuration-fuzzer]
last_updated: 2026-06-06
---

# Grammar (Fuzzing Data Structure)

In *The Fuzzing Book*, **`Grammar`** is the concrete Python data structure used to represent a [[ContextFreeGrammar|context-free grammar]] for input generation. It is a mapping from symbol names to lists of alternative expansions:

```python
Grammar = Dict[str, List[Expansion]]
```

Each key is a [[Nonterminal|nonterminal]] (a string in `<angle brackets>`); each value is a list of [[ProductionRule|expansion alternatives]]. An `Expansion` is either a plain string or a `(string, opts)` pair so individual expansions can carry annotations:

```python
Expansion = Union[str, Tuple[str, Option]]   # Option = Dict[str, Any]
```

The canonical entry point is `START_SYMBOL = "<start>"`. Every symbol is defined exactly once; expansion alternatives within a rule are written as separate list entries (the list models BNF's `|`). This string-and-dict format is chosen to make writing grammars as frictionless as possible while staying ordinary Python data that can be built programmatically.

## From The Fuzzing Book — Fuzzing with Grammars
[[fuzzingbook-09-grammars|Ch 9]] mints this `Grammar` type and uses it throughout Part III. The running examples are `EXPR_GRAMMAR` (arithmetic expressions), `CGI_GRAMMAR`, `URL_GRAMMAR`, `TITLE_GRAMMAR`, and `US_PHONE_GRAMMAR`. The chapter pairs the structure with helpers — `nonterminals()`/`is_nonterminal()` to inspect symbols, `is_valid_grammar()` to check that all nonterminals are defined, used, and reachable, `extend_grammar()` to copy-and-extend a grammar (grammar extension as a form of subclassing), `srange()`/`crange()` to build character-class expansions, `trim_grammar()` to drop unused symbols, and `opts()`/`exp_string()`/`exp_opts()` for the per-expansion annotation mechanism. The naive `simple_grammar_fuzzer()` consumes a `Grammar` by string rewriting; later chapters consume the same structure with far more efficient producers. This exact data structure is reused by the [[fuzzingbook-10-grammar-fuzzer|`GrammarFuzzer` (Ch 10)]] and every grammar-based fuzzer after it.

## From The Fuzzing Book — Efficient Grammar Fuzzing
[[fuzzingbook-10-grammar-fuzzer|Ch 10]] consumes the `Grammar` structure **unchanged** but with a far better producer: the [[GrammarFuzzer|`GrammarFuzzer`]], which turns each expansion into [[DerivationTree|derivation-tree]] children via `expansion_to_children()` (reusing `exp_string()`/`is_nonterminal()`/`RE_NONTERMINAL`) and validates the grammar with `is_valid_grammar()`. The chapter also reads the grammar to compute [[ExpansionCost|symbol/expansion costs]] — a property of the `Grammar` alone, which Exercise 2 precomputes once. That the same `Grammar` data structure feeds both the naive Ch 9 producer and the efficient Ch 10 fuzzer (and all later ones) is exactly the point: the input model is stable while the generation algorithm improves.

## From The Fuzzing Book — Probabilistic Grammar Fuzzing
[[fuzzingbook-13-probabilistic-grammar-fuzzer|Ch 13]] puts the `Grammar` structure's *annotation* slot to real use: the `(string, opts(prob=X))` expansion form carries a **probability** on an alternative, turning a `Grammar` into a [[ProbabilisticGrammar|probabilistic grammar]]. It adds reader/writer helpers around the same structure — `exp_prob()` (read an expansion's `prob`), `exp_probabilities()`/`prob_distribution()` (compute and check a rule's full distribution), `is_valid_probabilistic_grammar()`, and `set_prob()` (a `set_opts()` wrapper). Because annotations live on the existing structure, ordinary fuzzers ignore them while the [[ProbabilisticGrammarFuzzer|`ProbabilisticGrammarFuzzer`]] interprets them — the same backward-compatible extensibility that lets the `Grammar` type serve every producer in Part III. The chapter also reuses [[ContextCoverage|`duplicate_context()`]] to clone a rule (e.g. `<octet>` → `<octet-1>`…`<octet-4>`) so repeated symbols can carry *distinct* probability distributions.

## From The Fuzzing Book — Fuzzing with Generators
[[fuzzingbook-14-generator-grammar-fuzzer|Ch 14]] puts the `Grammar` structure's *annotation* slot to a second use (after Ch 13's `prob`): the `(string, opts(...))` expansion form now also carries **`pre`**, **`post`**, and **`order`** keys holding Python functions, turning a `Grammar` into a [[GeneratorGrammar|generator grammar]]. Helpers `exp_pre_expansion_function()`/`exp_post_expansion_function()`/`exp_order()` (all wrappers over the Ch 9 `exp_opt()`) read these keys, and the `<credit-card-number>`/`<float>`/`<xml-tree>` expansions of `CHARGE_GRAMMAR`/`XML_GRAMMAR` carry repair/checking functions. As with `prob`, the keys live on the existing structure so ordinary fuzzers ignore them while the [[GeneratorGrammarFuzzer|`GeneratorGrammarFuzzer`]] interprets them — the same backward-compatible extensibility that lets one `Grammar` type serve every producer in Part III, including the all-features [[PGGCFuzzer|`PGGCFuzzer`]] that consumes `prob`, `pre`/`post`, *and* coverage at once.

## From The Fuzzing Book — Mining Input Grammars
[[fuzzingbook-18-grammar-miner|Ch 18]] *produces* the `Grammar` structure instead of consuming a hand-written one: [[GrammarMiner|`recover_grammar()`]] performs program-guided [[GrammarInference|grammar inference]] and returns an ordinary `Grammar` dict (via `tree_to_grammar()` + `readable()`), with nonterminals named after the methods/variables that held each input span (e.g. `<urlparse@394:scheme>`). Because the output is the same data structure used everywhere else in Part III, a mined grammar drops straight into the [[GrammarFuzzer|`GrammarFuzzer`]]/[[GrammarCoverageFuzzer|`GrammarCoverageFuzzer`]] — closing the loop from program to grammar to fuzzer.

## From The Fuzzing Book — Testing Configurations
[[fuzzingbook-23-configuration-fuzzer|Ch 23]] both *produces* and *transforms* the `Grammar` structure for [[ConfigurationFuzzing|configuration fuzzing]]. The [[OptionGrammarMiner|`OptionGrammarMiner`]] builds an [[OptionGrammar|option grammar]] dict from scratch while tracing `argparse`, using `new_symbol()` to mint group symbols and `crange()`/`srange()` for `<digit>`/`<char>` rules. The grammar is then transformed with the same Ch 9 helpers: `convert_ebnf_grammar()` lowers the mined EBNF to BNF, `is_valid_grammar()` validates it, `unreachable_nonterminals()` prunes dead rules after `set_arguments()` pins the positional arguments, and `extend_grammar()` clones the grammar so the `<option>` rule can be rewritten into option *pairs* for [[CombinatorialTesting|pairwise testing]]. This reinforces the chapter-spanning theme: one stable `Grammar` data structure serves miners, transformers, and fuzzers alike.

## Connections
- [[ContextFreeGrammar]] — the formalism this structure encodes.
- [[OptionGrammar]] / [[OptionGrammarMiner]] / [[ConfigurationFuzzing]] — Ch 23 builds and rewrites a `Grammar` of command-line options.
- [[GrammarInference]] / [[GrammarMiner]] — Ch 18 recovers a `Grammar` automatically from a program + samples.
- [[GeneratorGrammar]] — a `Grammar` whose expansions carry `pre`/`post`/`order` function annotations.
- [[ProbabilisticGrammar]] — a `Grammar` whose expansions carry `prob` annotations.
- [[DerivationTree]] / [[GrammarFuzzer]] / [[ExpansionCost]] — Ch 10's tree producer and cost machinery built on this structure.
- [[Nonterminal]] / [[Terminal]] — the symbol kinds the keys/expansions are built from.
- [[ProductionRule]] — each list of expansion alternatives is the right-hand side of a rule.
- [[EBNF]] / [[BNF]] — `Grammar` literally stores BNF; EBNF grammars are converted into it via `convert_ebnf_grammar()`.
- [[GrammarBasedFuzzing]] — the technique that consumes this structure.
- [[fuzzingbook-09-grammars]] — the chapter that defines `Grammar`.
- [[fuzzingbook-10-grammar-fuzzer]] — reuses `Grammar` with a derivation-tree producer.

## Sources
- [[fuzzingbook-09-grammars]] — *The Fuzzing Book* Ch 9, "Fuzzing with Grammars."
- [[fuzzingbook-10-grammar-fuzzer]] — *The Fuzzing Book* Ch 10, "Efficient Grammar Fuzzing."
- [[fuzzingbook-13-probabilistic-grammar-fuzzer]] — *The Fuzzing Book* Ch 13, "Probabilistic Grammar Fuzzing" (the `prob` annotation on expansions).
- [[fuzzingbook-14-generator-grammar-fuzzer]] — *The Fuzzing Book* Ch 14, "Fuzzing with Generators" (the `pre`/`post`/`order` function annotations on expansions).
- [[fuzzingbook-18-grammar-miner]] — *The Fuzzing Book* Ch 18, "Mining Input Grammars" (recovers a `Grammar` automatically from a program).
- [[fuzzingbook-23-configuration-fuzzer]] — *The Fuzzing Book* Ch 23, "Testing Configurations" (builds and rewrites a `Grammar` of command-line options).
