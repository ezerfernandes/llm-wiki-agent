---
title: "Benford's Law"
type: concept
tags: [statistics, probability, fuzzing, anomaly-detection, mathematics]
sources: [fuzzingbook-13-probabilistic-grammar-fuzzer, fuzzingbook-30-when-to-stop-fuzzing]
last_updated: 2026-06-06
---

# Benford's Law

**Benford's law** (the *law of leading digits*) states that in many naturally occurring sets of numbers the **leading significant digit** is far more likely to be small: the digit `1` occurs as the leading digit about six times as often as `8` or `9`. The probability that the leading digit is `d` is

```
P(d) = log10(d + 1) − log10(d)
```

giving ≈30.1% for `1` down to ≈4.6% for `9`. It holds across electricity bills, street addresses, stock and house prices, populations, river lengths, and physical/mathematical constants. The intuition: for a number to start with digit `d`, the fractional part of its base-10 logarithm must fall in `[log10(d), log10(d+1))`, a range that shrinks as `d` grows; when those fractional parts are uniformly distributed (as they tend to be in "natural" data), small leading digits dominate. First observed by Newcomb (1881), later formalized by Benford (1938).

## From The Fuzzing Book — Probabilistic Grammar Fuzzing
[[fuzzingbook-13-probabilistic-grammar-fuzzer|Ch 13]] uses Benford's law as the *motivating example* for [[ProbabilisticGrammar|probabilistic grammars]]: numbers produced by a plain [[GrammarFuzzer|grammar fuzzer]] (uniform digits) look "unnatural" precisely because they violate it. The chapter encodes the law as `prob` annotations on `<leaddigit>` in `PROBABILISTIC_EXPR_GRAMMAR`, and shows that a [[ProbabilisticGrammarFuzzer|`ProbabilisticGrammarFuzzer`]] generating 10,000 lead digits reproduces the distribution almost exactly. It also flips the use around for **detection**: a χ²-test (`scipy.stats.chisquare`) comparing observed lead-digit counts against the Benford distribution versus a uniform distribution can statistically flag faked/randomly-generated numbers — the uniform digits from a non-probabilistic fuzzer get a `pvalue` of 0 against the "natural" distribution but ~97% against a random one.

## From The Fuzzing Book — When To Stop Fuzzing
[[fuzzingbook-30-when-to-stop-fuzzing|Ch 30]] reuses Benford's law to make its [[EnigmaMachine|Naval Enigma]] worked example realistic. Historically, some trigrams in the *Kenngruppenbuch* were chosen more often than others; the chapter models this by generalizing the law beyond base-10 digits to all `b = 26³` trigrams, assigning the `i`-th trigram probability `log_b(1 + 1/i)`. This skewed, "natural" distribution is what makes the [[GoodTuringEstimator|Good-Turing]] singleton statistics meaningful — and motivates the "boosted" strategy of trying abundant trigrams first.

## Connections
- [[EnigmaMachine]] — Ch 30 uses Benford's law to weight Kenngruppenbuch trigram probabilities.
- [[ProbabilisticGrammar]] — the law is encoded as `prob` annotations on leading-digit expansions.
- [[ProbabilisticGrammarFuzzer]] — shown to reproduce the Benford distribution.
- [[ProbabilisticGrammarFuzzing]] — the technique this is the headline example for.
- [[HypothesisTesting]] — the χ²-test used to detect unnatural distributions.
- [[fuzzingbook-13-probabilistic-grammar-fuzzer]] — the chapter that uses Benford's law.

## Sources
- [[fuzzingbook-13-probabilistic-grammar-fuzzer]] — *The Fuzzing Book* Ch 13, "Probabilistic Grammar Fuzzing."
- [[fuzzingbook-30-when-to-stop-fuzzing]] — *The Fuzzing Book* Ch 30, "When To Stop Fuzzing" (generalizes the law to `26³` trigrams for the Enigma example).
