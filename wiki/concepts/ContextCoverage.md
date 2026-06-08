---
title: "Coverage in Context"
type: concept
tags: [fuzzing, grammar, coverage, testing, syntactic-fuzzing, python]
sources: [fuzzingbook-11-grammar-coverage-fuzzer, fuzzingbook-13-probabilistic-grammar-fuzzer, fuzzingbook-23-configuration-fuzzer]
last_updated: 2026-06-06
---

# Coverage in Context

**Coverage in context** is a refinement of [[GrammarCoverage|grammar coverage]] that covers each *occurrence* of a reused [[Grammar|grammar]] symbol independently, rather than pooling coverage across all of its uses. The motivation: a symbol like `<integer>` in `EXPR_GRAMMAR` is referenced in several places (whole integers, and the whole and fractional parts of `<integer>.<integer>` floating-point numbers). Plain grammar coverage guarantees every `<digit>` expansion appears *somewhere*, but the digits get *distributed* across occurrences — so a given occurrence (e.g. the fractional part read by a distinct code path) may see only a fraction of the digits.

## From The Fuzzing Book — Grammar Coverage
[[fuzzingbook-11-grammar-coverage-fuzzer|Ch 11]] achieves per-occurrence coverage by **duplicating** grammar rules: replace a shared expansion such as `<integer>.<integer>` with `<integer-1>.<integer-2>`, giving `<integer-1>`/`<integer-2>` (and their `<digit-1>`/`<digit-2>`) fresh copies of the original rules. Each duplicate then becomes its own coverage obligation, so [[GrammarCoverageFuzzer|`GrammarCoverageFuzzer`]] will cover all digits in each context separately. The chapter shows both a manual version (via `extend_grammar()`) and the automatic function:

```python
duplicate_context(grammar, symbol, expansion=None, depth=float('inf'))
```

`duplicate_context()` (with helper `_duplicate_context()`) clones the referenced rule subtree into new symbols using `new_symbol()` and `copy.deepcopy()`, tracks already-duplicated symbols in a `seen` dict to avoid infinite recursion on recursive grammars, and deletes `unreachable_nonterminals()` afterward. The `depth` parameter bounds how far duplication propagates (`depth=1` duplicates only the next rule; default ∞ duplicates each symbol once). Unbounded duplication can explode `EXPR_GRAMMAR` to ~292 rules / ~2000 expansions — grammars that are no longer human-maintainable but let a coverage-driven fuzzer exercise every context (e.g. multiplications nested within additions). Context coverage is also the chapter's prescribed remedy for **equivalent elements**, where structural variety alone fails to induce code-coverage variety.

## From The Fuzzing Book — Probabilistic Grammar Fuzzing
[[fuzzingbook-13-probabilistic-grammar-fuzzer|Ch 13]] reuses `duplicate_context()` for a *probabilistic* purpose. A single rule can only assign one probability distribution, so all four octets of `IP_ADDRESS_GRAMMAR`'s `<octet>` must share it. Calling `duplicate_context(grammar, "<address>")` clones `<octet>` into `<octet-1>`…`<octet-4>`, after which `set_prob()` can give each occurrence its *own* distribution (e.g. forcing `<octet-1>` → `127` and `<octet-2>` → `0`). The chapter draws the explicit parallel to coverage in context — duplicating a symbol is what unlocks per-occurrence control, here over [[ProbabilisticGrammar|probabilities]] rather than coverage — and notes the same maintenance cost of the resulting larger grammar.

## From The Fuzzing Book — Testing Configurations
[[fuzzingbook-23-configuration-fuzzer|Ch 23]] revisits coverage in context for [[ConfigurationFuzzing|configuration fuzzing]]. A mined [[OptionGrammar|option grammar]] reuses a parameter symbol across many options — e.g. `autopep8`'s `--line-range <line> <line>` and other numeric options all bottom out in the same `<int>`/`<digit>` rules — so once [[GrammarCoverageFuzzer|`GrammarCoverageFuzzer`]] has covered all digits for *one* option, it stops striving to cover them for the next. Exercise 4 ("Expansions in Context") proposes an `inline(grammar, symbol)` function that *duplicates* a symbol and its expansions into fresh copies (e.g. `<line'>`/`<int'>`/`<digit'>`), so each option's parameters are covered independently — exactly the context-duplication idea of [[fuzzingbook-11-grammar-coverage-fuzzer|Ch 11]], applied per-option.

## Connections
- [[GrammarCoverage]] — the base criterion context coverage sharpens.
- [[ConfigurationFuzzing]] / [[OptionGrammar]] — Ch 23 Exercise 4 duplicates option-parameter symbols to cover each option independently.
- [[ProbabilisticGrammar]] / [[ProbabilisticGrammarFuzzer]] — Ch 13 duplicates context to give repeated symbols distinct probability distributions.
- [[GrammarCoverageFuzzer]] — the fuzzer run over a context-duplicated grammar.
- [[Grammar]] / [[ProductionRule]] — `duplicate_context()` rewrites these by cloning rule subtrees.
- [[Coverage]] — finer per-context coverage aims at finer code-coverage distinctions.
- [[fuzzingbook-23-configuration-fuzzer|Ch 23]] — configuration coverage builds on these context ideas.
- [[fuzzingbook-11-grammar-coverage-fuzzer]] — the chapter that introduces context coverage.

## Sources
- [[fuzzingbook-11-grammar-coverage-fuzzer]] — *The Fuzzing Book* Ch 11, "Grammar Coverage."
- [[fuzzingbook-13-probabilistic-grammar-fuzzer]] — *The Fuzzing Book* Ch 13, "Probabilistic Grammar Fuzzing" (`duplicate_context()` reused for per-occurrence probabilities).
- [[fuzzingbook-23-configuration-fuzzer]] — *The Fuzzing Book* Ch 23, "Testing Configurations" (Exercise 4 `inline()` duplicates option-parameter symbols for per-option coverage).
