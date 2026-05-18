---
title: "N-gram"
type: concept
tags: [nlp, language-models, statistics]
sources: [d2l-recurrent-neural-networks]
last_updated: 2026-05-16
---

# N-gram

A contiguous sequence of $n$ tokens from a corpus. **$n$-gram language models** approximate $P(x_t \mid x_{<t})$ by truncating the conditioning history to the previous $n-1$ tokens ([[d2l-recurrent-neural-networks]] §language-model) — the [[MarkovModel|Markov]] assumption applied to text.

## Naming

- $n=1$ → **unigram** ($P(x_t)$).
- $n=2$ → **bigram** ($P(x_t \mid x_{t-1})$).
- $n=3$ → **trigram** ($P(x_t \mid x_{t-1}, x_{t-2})$).
- $n=4$ → **four-gram**, and so on.

## Estimation

Maximum-likelihood estimate from corpus counts:

$$\hat P(x' \mid x) = \frac{n(x, x')}{n(x)}.$$

Rare $n$-grams need [[LaplaceSmoothing|smoothing]] to avoid zero probabilities.

## Why neural LMs supplanted $n$-grams

Per [[d2l-recurrent-neural-networks]]:
- Most $n$-grams occur very rarely ([[ZipfsLaw]] — bigrams and trigrams also follow power-law).
- Storage is huge ($|\mathcal{V}|^n$ counts).
- Counting cannot encode word meaning ("cat" ≠ "feline" in $n$-gram space).
- Long sequences are almost certain to be novel.

## Empirical observation from D2L

On *The Time Machine* corpus: unigram, bigram, and trigram token-frequency curves are all approximately linear on a log-log plot (Zipf's law), with smaller exponents for higher-order grams. Most $n$-grams occur very rarely — pre-deep-learning text classifiers' bag-of-words representations filtered out [[StopWord|stop words]] but kept the rare-$n$-gram problem.

## Connections

- [[d2l-recurrent-neural-networks]] — chapter-source.
- [[LanguageModel]] — $n$-gram is the canonical baseline.
- [[MarkovModel]] — $n$-gram = $(n-1)$-order Markov assumption.
- [[ZipfsLaw]] — explains rarity of high-order $n$-grams.
- [[LaplaceSmoothing]] — additive smoothing for unseen $n$-grams.
- [[Perplexity]] — how $n$-gram LMs are evaluated.
- [[RNN]] / [[Transformer]] — neural successors.
