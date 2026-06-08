---
title: "Directed Fuzzing"
type: concept
tags: [fuzzing, grammar, probability, testing, security, syntactic-fuzzing]
sources: [fuzzingbook-13-probabilistic-grammar-fuzzer]
last_updated: 2026-06-06
---

# Directed Fuzzing

**Directed fuzzing** steers test generation toward (or away from) particular program features, code paths, or input shapes, rather than exploring the input space uniformly. The goal is to spend the testing budget where it matters most — on recently changed code, failure-prone or security-critical functionality, or features that are rarely exercised in practice and therefore harbor undiscovered bugs.

## From The Fuzzing Book — Probabilistic Grammar Fuzzing
[[fuzzingbook-13-probabilistic-grammar-fuzzer|Ch 13]] realizes directed fuzzing through [[ProbabilisticGrammar|probabilistic grammars]]: by raising the probabilities of the expansions associated with a feature, the [[ProbabilisticGrammarFuzzer|`ProbabilisticGrammarFuzzer`]] generates proportionally more inputs that exercise it. The helper `set_prob(grammar, symbol, expansion, prob)` sets an expansion's probability — e.g. giving the `ftps` URL scheme probability `0.8` to test a freshly changed secure-FTP implementation, or `0.0` to *disable* an expansion (with the caveat that the grammar fuzzer's minimum-cost **closing phase** may still take a zero-probability expansion when it is the only way to finish a tree).

The chapter then shows that the probabilities need not be set by hand — [[GrammarMining|`ProbabilisticGrammarMiner`]] can *learn* them from a corpus, and the direction can be tuned three ways: learn from all inputs to favor **common** features; **invert** the learned probabilities (`invert_expansion()`) to focus on **uncommon** features (the security-testing case — "fewer users means fewer bugs reported, and thus more bugs left to be found"); or learn from a coverage **slice** to specialize toward a critical code region (the CGI Line 25 example, where re-learning sharply raises the fraction of inputs hitting the target line). The chapter frames this as the classic *exploration vs. exploitation* trade-off: deep specialization improves focus but limits discovery of bugs outside the chosen scope.

## Connections
- [[ProbabilisticGrammar]] / [[ProbabilisticGrammarFuzzer]] — the mechanism (tunable expansion probabilities) directed fuzzing uses.
- [[ProbabilisticGrammarFuzzing]] — the technique directed fuzzing is the chief application of.
- [[GrammarMining]] — learns probabilities to direct toward common/uncommon/sliced features.
- [[Coverage]] — code coverage selects the input slice to learn from.
- [[ContextCoverage]] — per-occurrence duplication adds finer directional control.
- [[GrammarBasedFuzzing]] — the parent technique being directed.
- [[fuzzingbook-13-probabilistic-grammar-fuzzer]] — the chapter that introduces directed (probabilistic) fuzzing.

## Sources
- [[fuzzingbook-13-probabilistic-grammar-fuzzer]] — *The Fuzzing Book* Ch 13, "Probabilistic Grammar Fuzzing."
