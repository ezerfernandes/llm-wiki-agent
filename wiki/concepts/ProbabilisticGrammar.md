---
title: "Probabilistic Grammar"
type: concept
tags: [fuzzing, grammar, probability, context-free-grammar, testing, syntactic-fuzzing, python]
sources: [fuzzingbook-13-probabilistic-grammar-fuzzer, fuzzingbook-14-generator-grammar-fuzzer]
last_updated: 2026-06-06
---

# Probabilistic Grammar

A **probabilistic grammar** is a [[ContextFreeGrammar|context-free grammar]] in which individual [[ProductionRule|expansion alternatives]] carry an explicit **probability**, so that the relative frequency with which each alternative is chosen can be controlled rather than left uniform. It is the basis for [[ProbabilisticGrammarFuzzing|probabilistic grammar fuzzing]]: instead of expanding every alternative with equal likelihood, a fuzzer can favor some alternatives over others and thereby shape the distribution of generated inputs.

## From The Fuzzing Book — Probabilistic Grammar Fuzzing
[[fuzzingbook-13-probabilistic-grammar-fuzzer|Ch 13]] mints this concept by *reusing the [[fuzzingbook-09-grammars|Ch 9]] annotation mechanism*: an [[Grammar|`Expansion`]] may be either a plain string or a `(string, opts(prob=X))` pair, where `X` is between 0 and 1. The running example annotates `<leaddigit>` in `PROBABILISTIC_EXPR_GRAMMAR` with [[BenfordsLaw|Benford's-law]] probabilities, and the synopsis biases a phone grammar so 90% of area codes start with `9`.

The semantics for a rule `S ::= a_1 | … | a_n | u_1 | … | u_m` (with `a_i` annotated and `u_j` un-annotated) are: the **remaining** probability is distributed *equally* over the un-annotated alternatives,

```
p(u_j) = (1 − Σ_i p(a_i)) / m
```

so if no alternative is annotated the rule is uniform (exactly like earlier grammar fuzzers), and the per-rule probabilities always sum to `1.0`. The chapter supplies helpers `exp_prob()` (read an expansion's `prob`), `exp_probabilities()` / `prob_distribution()` (compute the full per-rule distribution and assert it sums to 1 within an `epsilon`), `is_valid_probabilistic_grammar()` (validate a whole grammar), and `set_prob()` / `set_opts()` (programmatically set or clear an expansion's probability). Crucially, a probabilistic grammar is *backward compatible*: ordinary fuzzers such as [[GrammarFuzzer|`GrammarFuzzer`]] and [[GrammarCoverageFuzzer|`GrammarCoverageFuzzer`]] simply **ignore** the annotations, while the [[ProbabilisticGrammarFuzzer|`ProbabilisticGrammarFuzzer`]] interprets them.

## From The Fuzzing Book — Fuzzing with Generators
[[fuzzingbook-14-generator-grammar-fuzzer|Ch 14]] shows that the `prob` annotation composes with the new `pre`/`post`/`order` function annotations on the *same* `opts()` slot: the [[PGGCFuzzer|`PGGCFuzzer`]] capstone consumes a grammar that is *simultaneously* probabilistic and a [[GeneratorGrammar|generator grammar]]. The chapter's example sets `opts(prob=0.9)` on `<word>` to bias toward long identifiers while a generator-based symbol table still enforces define-before-use — confirming that probability and computation are *independent, composable* extensions of the base [[Grammar|`Grammar`]].

## Connections
- [[ProbabilisticGrammarFuzzing]] — the technique that consumes probabilistic grammars.
- [[GeneratorGrammar]] / [[PGGCFuzzer]] — the `prob` annotation composes with `pre`/`post`/`order` functions on the same `opts()` slot.
- [[ProbabilisticGrammarFuzzer]] — the fuzzer that interprets the `prob` annotations.
- [[Grammar]] — the underlying data structure; the `opts()` annotation mechanism is from [[fuzzingbook-09-grammars|Ch 9]].
- [[ProductionRule]] — probabilities annotate expansion alternatives.
- [[BenfordsLaw]] — the motivating "natural numbers" probability distribution.
- [[DirectedFuzzing]] — tuning these probabilities to steer test generation.
- [[GrammarMining]] — learns these probabilities automatically from a corpus.
- [[ContextCoverage]] — `duplicate_context()` lets repeated symbols carry *distinct* distributions.
- [[fuzzingbook-13-probabilistic-grammar-fuzzer]] — the chapter that introduces probabilistic grammars.

## Sources
- [[fuzzingbook-13-probabilistic-grammar-fuzzer]] — *The Fuzzing Book* Ch 13, "Probabilistic Grammar Fuzzing."
- [[fuzzingbook-14-generator-grammar-fuzzer]] — *The Fuzzing Book* Ch 14, "Fuzzing with Generators" (`prob` composes with generator-function annotations in `PGGCFuzzer`).
