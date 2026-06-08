---
title: "Probabilistic Grammar Fuzzing"
type: concept
tags: [fuzzing, grammar, probability, testing, security, syntactic-fuzzing, directed-fuzzing]
sources: [fuzzingbook-13-probabilistic-grammar-fuzzer]
last_updated: 2026-06-06
---

# Probabilistic Grammar Fuzzing

**Probabilistic grammar fuzzing** extends [[GrammarBasedFuzzing|grammar-based fuzzing]] by attaching **probabilities** to expansion alternatives, so the generator can control *how often* each input element is produced instead of choosing uniformly at random. This turns a grammar into a tunable input *distribution*: by raising or lowering probabilities one can [[DirectedFuzzing|direct]] tests toward (or away from) particular features, generate "natural"-looking inputs, or replicate the statistics of a real-world sample.

## From The Fuzzing Book — Probabilistic Grammar Fuzzing
[[fuzzingbook-13-probabilistic-grammar-fuzzer|Ch 13]] founds this technique. It uses a [[ProbabilisticGrammar|probabilistic grammar]] (alternatives annotated with `opts(prob=X)`) and the [[ProbabilisticGrammarFuzzer|`ProbabilisticGrammarFuzzer`]], a subclass of [[GrammarFuzzer|`GrammarFuzzer`]] that overloads only `choose_node_expansion()` to make a **weighted** choice via `random.choices(..., weights=...)`. The chapter develops three layers of use:

1. **Specifying probabilities by hand** — e.g. [[BenfordsLaw|Benford's-law]] leading-digit frequencies, or `set_prob()` to favor an `ftps` URL scheme; in-context duplication ([[ContextCoverage|`duplicate_context()`]]) gives repeated symbols (the four IP `<octet>`s) independent distributions.
2. **Learning probabilities from samples** — [[GrammarMining|`ProbabilisticGrammarMiner`]] parses a corpus with the [[EarleyParser|`EarleyParser`]] and counts expansions to set probabilities (`p_i = count(S→a_i)/count(S)`). Learning from *all* inputs replicates common features; **inverting** the learned probabilities (`invert_expansion()` / `invert_probs()`, a sum-preserving swap) focuses on *uncommon* features (valuable for security testing); learning from a coverage *slice* specializes toward that slice (the CGI Line 25 example).
3. **Detecting unnatural distributions** — Benford's law plus a χ²-test (`scipy.stats.chisquare`) statistically distinguishes "natural" digit distributions from random ones.

The chapter frames the common-vs-uncommon-vs-slice spectrum as the machine-learning *exploration vs. exploitation* trade-off, and notes its lineage: mining probabilities from a corpus (Patra & Pradel 2016) and inverting/slicing them ("Inputs from Hell," Pavese et al. 2018).

## Connections
- [[ProbabilisticGrammar]] — the annotated grammar this technique consumes.
- [[ProbabilisticGrammarFuzzer]] — the weighted-choice fuzzer that realizes it.
- [[DirectedFuzzing]] — steering tests by tuning probabilities (the chief application).
- [[GrammarMining]] — learning the probabilities automatically from a parsed corpus.
- [[BenfordsLaw]] — the motivating example and the unnatural-number detector.
- [[GrammarBasedFuzzing]] — the parent technique; probabilities add a distributional control axis.
- [[GrammarCoverageFuzzer]] / [[GrammarCoverage]] — the complementary *systematic* (rather than probabilistic) selection strategy; combinable via multiple inheritance.
- [[EarleyParser]] / [[DerivationTree]] — used to turn corpus inputs into trees whose expansions are counted.
- [[fuzzingbook-13-probabilistic-grammar-fuzzer]] — the chapter that introduces the technique.
- [[fuzzingbook-18-grammar-miner|Ch 18]] — extends corpus learning to mining whole input grammars.

## Sources
- [[fuzzingbook-13-probabilistic-grammar-fuzzer]] — *The Fuzzing Book* Ch 13, "Probabilistic Grammar Fuzzing."
