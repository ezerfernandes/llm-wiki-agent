---
title: "Grammar Mining"
type: concept
tags: [fuzzing, grammar, probability, parsing, machine-learning, testing, syntactic-fuzzing, python]
sources: [fuzzingbook-13-probabilistic-grammar-fuzzer, fuzzingbook-18-grammar-miner, fuzzingbook-23-configuration-fuzzer, fuzzingbook-27-web-fuzzer]
last_updated: 2026-06-06
---

# Grammar Mining

**Grammar mining** is the practice of *learning* grammar information from a corpus of example inputs rather than writing it by hand. In *The Fuzzing Book* it appears in two forms: learning **probabilities** for an existing grammar by counting how often each expansion occurs in parsed samples (this chapter), and learning an entire **input grammar** from inputs and the program that consumes them ([[fuzzingbook-18-grammar-miner|Ch 18]]).

## From The Fuzzing Book — Probabilistic Grammar Fuzzing
[[fuzzingbook-13-probabilistic-grammar-fuzzer|Ch 13]] introduces probability mining. The key insight: parse each sample input into a [[DerivationTree|derivation tree]] (using the [[fuzzingbook-12-parser|Ch 12]] [[EarleyParser|`EarleyParser`]], which needs an explicit token set), then *count* how often each expansion is taken. The chapter implements this as a small class hierarchy:

- **`ExpansionCountMiner`** — initialized with a [[Parser|`Parser`]]; `count_expansions(inputs)` parses each input and `add_tree()` walks the tree, tallying each expansion in `expansion_counts` keyed by `expansion_key(symbol, children)` (reused from [[fuzzingbook-11-grammar-coverage-fuzzer|Ch 11]]'s coverage machinery). `counts()` returns the tally.
- **`ProbabilisticGrammarMiner`** (subclass) — `set_expansion_probabilities()` converts counts to probabilities with `p_i = count(S→a_i) / count(S)` (leaving `S` *unspecified* if it never occurs, and skipping single-alternative rules); `mine_probabilistic_grammar(inputs)` does the whole pipeline and returns a [[ProbabilisticGrammar|probabilistic grammar]] ready for the [[ProbabilisticGrammarFuzzer|`ProbabilisticGrammarFuzzer`]].

Mined grammars enable three [[DirectedFuzzing|directed]] strategies: reproduce **common** features (learn from all inputs — e.g. the `URL_SAMPLE` corpus yields mostly `https:` schemes and multi-parameter URLs); target **uncommon** features (invert the learned probabilities via `invert_expansion()`/`invert_probs()`); or specialize toward a **slice** (learn only from inputs covering a critical line, the CGI Line 25 example). The chapter notes the lineage: corpus-driven probability learning is from Patra & Pradel's "Learning to Fuzz" (2016), and inverting/slicing from Pavese et al.'s "Inputs from Hell" (2018).

## From The Fuzzing Book — Mining Input Grammars
[[fuzzingbook-18-grammar-miner|Ch 18]] mines the *whole input grammar* (structure, not just probabilities) — the broader sense of grammar mining. Where Ch 13 counts expansions in an existing grammar, Ch 18 performs program-guided [[GrammarInference|grammar inference]]: it dynamically traces a program and observes that each variable holding a **substring of the input** marks a [[Nonterminal|nonterminal]] over that span, stitches those fragments into [[DerivationTree|derivation trees]], and abstracts them into a [[Grammar|grammar]] via the [[GrammarMiner|`GrammarMiner`]] pipeline (`recover_grammar()`). The recovered grammar feeds the same [[GrammarFuzzer|`GrammarFuzzer`]]/[[GrammarCoverageFuzzer|`GrammarCoverageFuzzer`]] used elsewhere in the book. The two senses are complementary: Ch 18 recovers the grammar's *rules*, Ch 13 learns the *weights* on them.

## From The Fuzzing Book — Testing Configurations
[[fuzzingbook-23-configuration-fuzzer|Ch 23]] adds a *third* sense of grammar mining: mining a program's **[[OptionGrammar|option grammar]]** — its valid command-line invocations — rather than its input-data grammar. The [[OptionGrammarMiner|`OptionGrammarMiner`]] traces a Python program (`sys.settrace`) up to its `argparse.parse_args()` call and intercepts the `add_argument()`/`add_mutually_exclusive_group()` calls to reconstruct the options, their parameter types, arities, and exclusion groups. Where Ch 18 mines structure from input *substrings* and Ch 13 mines *probabilities* from expansion counts, Ch 23 mines structure from a program's *option-parser configuration* — but all three feed the same [[GrammarCoverageFuzzer|`GrammarCoverageFuzzer`]], so a single fuzzing engine consumes whatever the miner recovers.

## From The Fuzzing Book — Testing Web Applications
[[fuzzingbook-27-web-fuzzer|Ch 27]] adds a *fourth* sense of grammar mining: mining an input grammar from a **user interface** rather than from program traces or option parsers. The `HTMLGrammarMiner` (with its `FormHTMLParser`, built on the stdlib `html.parser.HTMLParser`) parses a served HTML form, extracts its `action` and a `fields` map (input name → HTML type, or `<select>` → option list), and `mine_grammar()` extends a base `CGI_GRAMMAR`/`QUERY_GRAMMAR` into a [[Grammar|grammar]] of valid form-submission URLs. Where Ch 18 mines structure from input *substrings* and Ch 23 from a program's *option parser*, Ch 27 mines it from the *rendered HTML surface* — and the result again feeds a [[GrammarFuzzer|`GrammarFuzzer`]] (via [[WebFormFuzzer|`WebFormFuzzer`]]), reinforcing the book's recurring pattern: whatever the miner recovers, one fuzzing engine consumes it.

## Connections
- [[WebFormFuzzer]] / [[WebApplicationFuzzing]] — Ch 27's mining of a submission grammar from a served HTML form.
- [[OptionGrammar]] / [[OptionGrammarMiner]] / [[ConfigurationFuzzing]] — Ch 23's mining of command-line option grammars from `argparse`.
- [[GrammarInference]] / [[GrammarMiner]] — program-guided recovery of a grammar's structure (Ch 18).
- [[ProbabilisticGrammar]] — what mining produces (an annotated grammar).
- [[ProbabilisticGrammarFuzzer]] / [[ProbabilisticGrammarFuzzing]] — consume the mined probabilities.
- [[EarleyParser]] / [[Parser]] — parse corpus inputs into trees to be counted.
- [[DerivationTree]] — the per-input structure whose expansions are tallied.
- [[DirectedFuzzing]] — common/uncommon/slice strategies built on mined probabilities.
- [[GrammarCoverage]] — `expansion_key()` is reused from the coverage chapter.
- [[Coverage]] — code coverage selects the slice corpus to learn from.
- [[fuzzingbook-13-probabilistic-grammar-fuzzer]] — the chapter that introduces probability mining.
- [[fuzzingbook-18-grammar-miner|Ch 18]] — mines whole input grammars (the broader sense of grammar mining).

## Sources
- [[fuzzingbook-13-probabilistic-grammar-fuzzer]] — *The Fuzzing Book* Ch 13, "Probabilistic Grammar Fuzzing."
- [[fuzzingbook-18-grammar-miner]] — *The Fuzzing Book* Ch 18, "Mining Input Grammars" (whole-grammar inference).
- [[fuzzingbook-23-configuration-fuzzer]] — *The Fuzzing Book* Ch 23, "Testing Configurations" (mining option grammars from `argparse`).
- [[fuzzingbook-27-web-fuzzer]] — *The Fuzzing Book* Ch 27, "Testing Web Applications" (mining a form-submission grammar from served HTML via `HTMLGrammarMiner`).
