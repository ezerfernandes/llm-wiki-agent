---
title: "Zipf's Law"
type: concept
tags: [statistics, nlp, language-models, power-laws]
sources: [d2l-recurrent-neural-networks]
last_updated: 2026-05-16
---

# Zipf's Law

The empirical observation that **word frequencies in natural-language corpora follow a power-law distribution**: the frequency $n_i$ of the $i^\textrm{th}$ most frequent word is

$$n_i \propto \frac{1}{i^\alpha},$$

equivalently $\log n_i = -\alpha \log i + c$ — a nearly straight line on a log-log frequency-rank plot ([[d2l-recurrent-neural-networks]] §text-sequence).

## D2L's empirical demonstration

On H. G. Wells' *The Time Machine* corpus (~30K words):
- The 10th most frequent word occurs <1/5 as often as the most popular.
- The log-log frequency-rank plot is approximately linear (after the first few outlier articles).
- **Bigrams and trigrams also follow Zipf's law**, with smaller exponents $\alpha$.
- Many $n$-grams occur very rarely.

## Why it matters for language modeling

Zipf's law is the structural reason pure-counting $n$-gram language models break down:
- High-order $n$-grams ($n \geq 3$) are dominated by rare combinations.
- [[LaplaceSmoothing|Laplace smoothing]] cannot rescue the long tail.
- Storing all $|\mathcal{V}|^n$ counts is infeasible.
- → Motivates **neural language models** that learn distributed representations and can generalize across word combinations they never saw.

Per [[d2l-recurrent-neural-networks]]: "this makes certain methods unsuitable for language modeling and motivates the use of deep learning models."

## Beyond words

Power-law distributions appear in many domains — city populations, income distributions, web hyperlinks, scientific citations. Zipf's law for natural language was named after linguist George Kingsley Zipf (1949).

## Connections

- [[d2l-recurrent-neural-networks]] — empirical demonstration on *The Time Machine* (§text-sequence).
- [[NGram]] — Zipf's law explains why $n$-gram counts have heavy tails.
- [[LanguageModel]] / [[LaplaceSmoothing]] — Zipf's law breaks counting-based LMs.
- [[Tokenization]] — vocabulary-size choices are influenced by the frequency tail.
- [[StopWord|Stop words]] — the head of the Zipfian distribution.
