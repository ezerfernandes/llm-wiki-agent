---
title: "The Fuzzing Book Ch 13 — Probabilistic Grammar Fuzzing"
type: source
tags: [book, fuzzingbook, fuzzing, testing, security, grammar, probability, directed-fuzzing, grammar-mining, syntactic-fuzzing]
date: 2026-06-06
source_file: raw/books/fuzzingbook/fuzzingbook-13-probabilistic-grammar-fuzzer.md
book: "The Fuzzing Book"
book_authors: ["Andreas Zeller", "Rahul Gopinath", "Marcel Böhme", "Gordon Fraser", "Christian Holler"]
book_publisher: "CISPA Helmholtz Center for Information Security"
book_year: 2024
book_url: "https://www.fuzzingbook.org/"
---

# Probabilistic Grammar Fuzzing

## Summary
Chapter 13 — in Part III (Syntactic Fuzzing) — gives grammars more power by attaching individual **probabilities** to expansion alternatives, so the fuzzer can *control how often each element is produced* and thereby [[DirectedFuzzing|direct]] test generation toward specific functionality. Building on the [[fuzzingbook-09-grammars|Ch 9]] grammar annotation mechanism and subclassing the [[fuzzingbook-10-grammar-fuzzer|Ch 10]] [[GrammarFuzzer|`GrammarFuzzer`]], it introduces the [[ProbabilisticGrammar|probabilistic grammar]] (`opts(prob=X)` annotations on alternatives) and the [[ProbabilisticGrammarFuzzer|`ProbabilisticGrammarFuzzer`]], which overloads a single method (`choose_node_expansion()`) to make a *weighted* random choice via `random.choices()`. The motivating example is [[BenfordsLaw|Benford's law]] — generating "natural"-looking numbers whose leading digit follows the real-world `1`-is-six-times-`9` distribution. The chapter then shows how to **learn** probabilities by counting expansion frequencies in a corpus of inputs parsed with the [[fuzzingbook-12-parser|Ch 12]] [[EarleyParser|`EarleyParser`]] ([[GrammarMining|`ProbabilisticGrammarMiner`]]), and how to bias *toward* common features, *against* them (inverting/swapping probabilities to generate uncommon inputs — useful for security testing), or toward a critical input *slice*.

## Key Concepts
- **[[ProbabilisticGrammar|Probabilistic grammar]]** — a [[Grammar|`Grammar`]] in which expansion alternatives may carry a probability via the `(string, opts(prob=X))` pair annotation (reusing the Ch 9 `opts()`/`exp_string()`/`exp_opt()`/`set_opts()` mechanism, `supported_opts={'prob'}`). The running example `PROBABILISTIC_EXPR_GRAMMAR` annotates `<leaddigit>` with Benford's-law probabilities.
- **Distributing & checking probabilities** — `exp_prob()` reads an expansion's `prob`; `exp_probabilities()`/`prob_distribution()` map every alternative of a rule to a probability, distributing the *remaining* probability **equally over un-annotated alternatives** (`p(u_j) = (1 − Σ p(a_i)) / m`), and asserting the per-rule sum is `1.0` (within `epsilon`). `is_valid_probabilistic_grammar()` validates a whole grammar this way.
- **[[ProbabilisticGrammarFuzzer|`ProbabilisticGrammarFuzzer`]]** — subclass of [[GrammarFuzzer|`GrammarFuzzer`]] that overloads `choose_node_expansion()` to make a **weighted choice** (`random.choices(..., weights=...)`) over the candidate expansions; `check_grammar()` adds the probabilistic-validity check. Non-probabilistic fuzzers simply *ignore* the annotations.
- **[[DirectedFuzzing|Directed fuzzing]]** — by raising/lowering probabilities (e.g. `set_prob()` giving the `ftps` URL scheme prob `0.8`, or `0.0` to disable an expansion) one steers tests toward critical/changed/rarely-tested code. A zero-probability expansion can still be taken in the **closing phase** when it is the only way to finish a tree at minimum cost.
- **Probabilities in context** — a single probability per rule cannot give *different* distributions to repeated symbols (e.g. the four `<octet>`s of an IP address). The remedy reuses [[ContextCoverage|Ch 11's `duplicate_context()`]]: clone `<octet>` into `<octet-1>`…`<octet-4>` so each gets its own distribution.
- **[[GrammarMining|Learning probabilities from samples]]** — `ExpansionCountMiner` parses inputs with an [[EarleyParser|`EarleyParser`]] into [[DerivationTree|derivation trees]] and counts expansions (`expansion_key()`); `ProbabilisticGrammarMiner.mine_probabilistic_grammar()` turns those counts into probabilities (`p_i = count(S→a_i) / count(S)`, *unspecified* if `S` never occurs).
- **Inverting probabilities** — `invert_expansion()` *swaps* the highest/lowest, second-highest/second-lowest… probabilities of a rule (sum-preserving, no renormalization needed; `invert_probs()` does this grammar-wide) so the fuzzer focuses on the **complement** of a sample — the uncommon features prized in security testing.
- **[[BenfordsLaw|Benford's law]]** — `P(d) = log10(d+1) − log10(d)`; the chapter both *generates* numbers obeying it and *detects* "unnatural" (uniform/random) digit distributions with a χ²-test (`scipy.stats.chisquare`).

## Key Claims
- Attaching probabilities to expansions lets a grammar fuzzer control the *distribution* of generated inputs and direct testing toward specific functionality, code, or features.
- Within a rule, any probability mass not explicitly assigned is distributed *equally* over the un-annotated alternatives; if none are annotated the rule behaves uniformly, exactly like earlier grammar fuzzers; per-rule probabilities must sum to 1.0.
- Setting an expansion's probability to 0 effectively disables it — *except* during the grammar fuzzer's minimum-cost "closing" phase, where it may still be taken if it is the only way to finish.
- A single per-rule probability cannot distinguish repeated occurrences of a symbol; duplicating the symbol *in context* (`duplicate_context()`) is what enables per-occurrence distributions — at the cost of larger, harder-to-maintain grammars.
- Probabilities can be *learned* by parsing a corpus and counting expansions; learning from all inputs reproduces common features, inverting the learned probabilities targets uncommon ones, and learning from a coverage *slice* specializes the fuzzer toward that slice (the CGI Line 25 example raises the slice-covering fraction sharply over a few re-learning rounds).
- This common-vs-uncommon-vs-slice control is the classic *exploration vs. exploitation* trade-off; high specialization improves focus but limits discovery of bugs outside the chosen scope.
- Benford's law (leading-digit distribution) can both produce "natural" numbers and statistically *detect* faked/random ones via a χ²-test.

## Key Quotes
> "Let us give grammars even more power by assigning _probabilities_ to individual expansions. This allows us to control how many of each element should be produced, and thus allows us to _target_ our generated tests towards specific functionality." — chapter intro.

> "The last shall be first, and the first last." — on inverting learned probabilities to generate uncommon inputs.

> "By specifying probabilities, one can steer fuzzing towards input features of interest." — Lessons Learned.

## Connections
- [[ProbabilisticGrammar]] — the annotated `Grammar` this chapter mints (`opts(prob=...)`).
- [[ProbabilisticGrammarFuzzing]] — the technique the chapter introduces.
- [[ProbabilisticGrammarFuzzer]] — the weighted-choice subclass of [[GrammarFuzzer]] that interprets the annotations.
- [[DirectedFuzzing]] — steering tests by tuning expansion probabilities (`set_prob()`).
- [[GrammarMining]] — learning probabilities from a parsed corpus (`ProbabilisticGrammarMiner`); foreshadows [[fuzzingbook-18-grammar-miner|Ch 18]]'s full grammar mining.
- [[BenfordsLaw]] — the motivating "natural numbers" example and the χ² detector.
- [[GrammarFuzzer]] — the base class; only `choose_node_expansion()` is overloaded.
- [[Grammar]] — the data structure the annotations live on; the annotation mechanism (`opts()`) is from Ch 9.
- [[EarleyParser]] / [[Parser]] / [[DerivationTree]] — parse the corpus into trees whose expansions are counted.
- [[ContextCoverage]] — `duplicate_context()` reused to give repeated symbols per-occurrence probabilities.
- [[GrammarCoverageFuzzer]] — Exercise 1 combines it with `ProbabilisticGrammarFuzzer` via multiple inheritance (`ProbabilisticGrammarCoverageFuzzer`).
- [[GrammarBasedFuzzing]] — the parent technique; probabilities are one more axis of control.
- [[Coverage]] — the CGI Line 25 slice example uses code coverage to select the learning corpus.
- [[AndreasZeller]] / [[CISPA]] — chapter authors / publisher.
- [[fuzzingbook-09-grammars|Ch 9]] / [[fuzzingbook-10-grammar-fuzzer|Ch 10]] / [[fuzzingbook-12-parser|Ch 12]] — prerequisites: annotation mechanism, the grammar fuzzer, the parser.
- [[fuzzingbook-11-grammar-coverage-fuzzer|Ch 11]] — supplies `duplicate_context()` and `GrammarCoverageFuzzer`.
- [[fuzzingbook-18-grammar-miner|Ch 18]] — full input-grammar mining, building on the counting-from-parses idea.

## Contradictions
- None identified.
