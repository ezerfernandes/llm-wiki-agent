---
title: "Markov Model"
type: concept
tags: [probability, sequence-models, statistics]
sources: [d2l-recurrent-neural-networks]
last_updated: 2026-05-16
---

# Markov Model

A sequence model that satisfies the **Markov condition**: the future is conditionally independent of the past, given the *recent history* — i.e., we can throw away the history beyond the previous $\tau$ steps without losing predictive power ([[d2l-recurrent-neural-networks]] §sequence).

## Definition

A distribution over sequences satisfies a $k^\textrm{th}$-order Markov condition when

$$P(x_{t+1} \mid x_t, x_{t-1}, \ldots, x_1) = P(x_{t+1} \mid x_t, \ldots, x_{t-k+1}).$$

For $k=1$ (first-order Markov):

$$P(x_1, \ldots, x_T) = P(x_1) \prod_{t=2}^T P(x_t \mid x_{t-1}).$$

## Why approximate Markov is useful even when true Markov isn't

Real text *continues* to gain information as more leftwards context is added, so a true low-order Markov assumption is technically violated. But gains diminish rapidly with context length, and trading off bias for computational/statistical tractability is often worth it. Per [[d2l-recurrent-neural-networks]]: "even today's massive RNN- and Transformer-based language models seldom incorporate more than thousands of words of context."

## Discrete-data special case

With discrete tokens, a true Markov model is just relative-frequency counting of $n$-grams, and the *most likely* sequence is solvable by dynamic programming (Viterbi). This is the basis of pre-neural NLP and remains the textbook baseline.

## Related: stationarity

[[MarkovCondition|Markov]] ≠ [[StationaryProcess|stationary]]: stationary = the *dynamics* (conditional distribution given recent history) don't change over time; Markov = the *dependence range* on the past is finite. Most practical sequence models assume stationarity but not necessarily Markov.

## Connections

- [[d2l-recurrent-neural-networks]] — chapter-source.
- [[NGram]] — an $n$-gram LM is a $(n-1)$-order Markov model.
- [[AutoregressiveModel]] — Markov is the *truncated-history* autoregressive case.
- [[LanguageModel]] — Markov models are the simplest LMs.
- [[MarkovDecisionProcess]] — Markov dynamics in RL.
- [[HiddenState]] — RNNs replace the explicit-window Markov assumption with a *summary* of the past.
