---
title: "Laplace Smoothing"
type: concept
tags: [statistics, nlp, language-models]
sources: [d2l-recurrent-neural-networks]
last_updated: 2026-05-16
---

# Laplace Smoothing

A simple technique for handling **unseen events** in count-based probability estimation: add a small constant $\epsilon$ to all counts before normalizing, so zero counts become small-but-nonzero probabilities ([[d2l-recurrent-neural-networks]] §language-model).

## Formula (for [[NGram|$n$-gram]] language models)

$$\hat P(x) = \frac{n(x) + \epsilon_1/m}{n + \epsilon_1}, \quad \hat P(x' \mid x) = \frac{n(x, x') + \epsilon_2 \hat P(x')}{n(x) + \epsilon_2}, \quad \ldots$$

where $n$ is the total token count, $m$ is the vocabulary size, $\epsilon_i$ are smoothing hyperparameters.

## Limiting behavior

- $\epsilon_1 = 0$ → no smoothing (MLE).
- $\epsilon_1 \to \infty$ → uniform distribution $1/m$.

## Why it isn't enough

[[ZipfsLaw|Zipf's law]] guarantees that most $n$-grams (especially high-order ones) occur very rarely or not at all. Per [[d2l-recurrent-neural-networks]]:

- Laplace smoothing is **rather unsuitable for language modeling** because so many $n$-grams are infrequent.
- Need to store all counts (large memory footprint).
- Ignores word **meaning** — "cat" and "feline" remain separate count cells despite identical contexts.
- Long sequences are almost certain to be novel, hence pure counting performs poorly.

→ Neural language models ([[RNN]], [[Transformer]]) supplant the count-based approach.

## More sophisticated variants

D2L cites Wood / Gasthaus / Archambeau et al. 2011 for more advanced smoothing (Kneser-Ney, Good-Turing, etc.). All address the same fundamental tail-rarity problem; none rescue counting-based LMs at scale.

## Connections

- [[d2l-recurrent-neural-networks]] — exposition + critique (§language-model).
- [[NGram]] — what gets smoothed.
- [[ZipfsLaw]] — why smoothing isn't enough.
- [[LanguageModel]] — what Laplace smoothing was historically used for.
- [[RNN]] / [[Transformer]] — neural successors that learn distributed representations.
