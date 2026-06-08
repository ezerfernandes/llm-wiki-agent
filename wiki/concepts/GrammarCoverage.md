---
title: "Grammar Coverage"
type: concept
tags: [fuzzing, grammar, coverage, testing, syntactic-fuzzing, test-adequacy, python]
sources: [fuzzingbook-11-grammar-coverage-fuzzer, fuzzingbook-23-configuration-fuzzer]
last_updated: 2026-06-06
---

# Grammar Coverage

**Grammar coverage** is a [[TestAdequacy|test-adequacy]] criterion for [[GrammarBasedFuzzing|grammar-based fuzzing]]: the goal is to exercise *each [[ProductionRule|expansion]] (production) of the [[Grammar|grammar]] at least once*, so that the generated inputs achieve maximum syntactic *variety* rather than repeating the same expansions by chance. The motivation is structural: program functionality is tied to input structure, so a production never produced (e.g. negative numbers, floating-point numbers in `EXPR_GRAMMAR`) means the corresponding code is never triggered. Grammar coverage is the input-side analogue of [[Coverage|code coverage]] — and *The Fuzzing Book* shows the two are strongly correlated.

## From The Fuzzing Book — Grammar Coverage
[[fuzzingbook-11-grammar-coverage-fuzzer|Ch 11]] makes the notion concrete. An expansion is identified by the string key `SYMBOL -> EXPANSION`, produced by `expansion_key()` (which also accepts a list of [[DerivationTree|derivation-tree]] children, flattening them with `all_terminals()`). The set of expansions actually produced is the `covered_expansions` set; the set of *all* reachable expansions is computed by `max_expansion_coverage(symbol, max_depth)`, a recursive grammar traversal (bounded by an optional `max_depth`, default ∞). The residual to still cover is `missing_expansion_coverage() = max_expansion_coverage() - expansion_coverage()` — pure set algebra, mirroring the `cov_max - cov_run` idiom of [[fuzzingbook-04-coverage|Ch 4]]'s [[Coverage|`Coverage`]] class.

The chapter builds three fuzzers of increasing sophistication on the [[GrammarFuzzer|`GrammarFuzzer`]] base:
1. **`TrackingGrammarCoverageFuzzer`** — only *measures*. It overloads `choose_node_expansion()` to call `add_coverage()`, recording each chosen expansion but still selecting randomly. Exposes `expansion_coverage()`, `reset_coverage()`, `missing_expansion_coverage()`.
2. **`SimpleGrammarCoverageFuzzer`** — *prefers* uncovered alternatives among a node's local `children_alternatives`, falling back to the random superclass choice only when all are covered.
3. **[[GrammarCoverageFuzzer|`GrammarCoverageFuzzer`]]** — adds *deep foresight* so it reaches full coverage fastest (see its page).

The headline empirical result is the strong correlation between grammar coverage and [[Coverage|code coverage]] (≈0.9 for `cgi_decode()`, >0.95 for `urlparse()`), so striving for grammar coverage is an effective route to code coverage. The idea of using each expansion at least once goes back to Burkhardt (1967) and Purdom (1972); the coverage↔code-coverage link is due to Nikolas Havrikov.

## From The Fuzzing Book — Testing Configurations
[[fuzzingbook-23-configuration-fuzzer|Ch 23]] applies grammar coverage to *configurations*: covering every expansion of a mined [[OptionGrammar|option grammar]] means exercising every command-line option (and every digit/letter in option values) of a program at least once — the basis of [[ConfigurationFuzzing|configuration fuzzing]]. [[CombinatorialTesting|Pairwise testing]] is likewise expressed as grammar coverage: rewriting the `<option>` rule into option *pairs* makes covering it cover all interactions. Exercise 4 surfaces a subtlety of the criterion — once `<int>`/`<digit>` is covered for one option, the fuzzer no longer strives to cover it for the next — and proposes duplicating expansions into fresh symbols so each option's parameters are covered independently (see [[ContextCoverage|coverage in context]]).

## Connections
- [[GrammarCoverageFuzzer]] — the foresighted fuzzer that *produces* (not just tracks) grammar coverage.
- [[ConfigurationFuzzing]] / [[OptionGrammar]] / [[CombinatorialTesting]] — Ch 23 applies grammar coverage to command-line options and pairs.
- [[ContextCoverage]] — refining grammar coverage so a reused symbol is covered per-occurrence.
- [[GrammarFuzzer]] — the base fuzzer whose `choose_node_expansion()` hook coverage is layered onto.
- [[DerivationTree]] — the structure whose chosen expansions are recorded as `SYMBOL -> EXPANSION` keys.
- [[Grammar]] / [[ContextFreeGrammar]] / [[ProductionRule]] — the productions being covered.
- [[Coverage]] / [[CoverageGuidedFuzzing]] — the code-coverage quantity grammar coverage correlates with and predicts.
- [[GrammarBasedFuzzing]] — the technique this criterion grades.
- [[fuzzingbook-04-coverage|Ch 4]] — supplies the `Coverage`/`cgi_decode` machinery for the correlation study.
- [[fuzzingbook-11-grammar-coverage-fuzzer]] — the chapter that defines grammar coverage.

## Sources
- [[fuzzingbook-11-grammar-coverage-fuzzer]] — *The Fuzzing Book* Ch 11, "Grammar Coverage."
- [[fuzzingbook-23-configuration-fuzzer]] — *The Fuzzing Book* Ch 23, "Testing Configurations" (grammar coverage applied to command-line options and pairs).
