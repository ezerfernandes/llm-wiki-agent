---
title: "Autoregressive Model"
type: concept
tags: [sequence-models, time-series, language-models]
sources: [d2l-recurrent-neural-networks]
last_updated: 2026-05-16
---

# Autoregressive Model

A sequence model that **regresses the value of a signal on the previous values of that same signal** — i.e., estimates $P(x_t \mid x_{t-1}, \ldots, x_1)$ or some statistic of it ([[d2l-recurrent-neural-networks]] §sequence).

## The variable-input-length problem

The number of conditioning inputs grows with $t$ — each example has a different number of features. Two recurring strategies:

1. **Truncate history** to a window of length $\tau$ → $P(x_t \mid x_{t-1}, \ldots, x_{t-\tau})$. This is the [[MarkovModel|Markov-condition]] case. Once $t > \tau$, the input length is fixed and any standard fixed-vector model (linear regression, MLP, CNN) applies.
2. **Latent autoregressive model** — maintain a learned summary $h_t = g(h_{t-1}, x_{t-1})$ that captures the past, predict $\hat x_t = f(h_t)$, and update $h_t$ at every step. The conceptual ancestor of [[RNN|RNNs]] and [[HiddenState|hidden states]].

## $k$-step-ahead extrapolation

For an observed sequence $x_1, \ldots, x_t$, the predicted output $\hat x_{t+k}$ at time step $t+k$ is the **$k$-step-ahead prediction**. Predictions errors compound: $\epsilon_{k+1} \approx \bar\epsilon + c\epsilon_k$. On D2L's synthetic sine demo, 1- and 4-step-ahead predictions track ground truth; 16- and 64-step-ahead predictions decay to a constant. Weather-forecast analogy: 24-hour forecasts are accurate, beyond-week forecasts degrade rapidly.

## Causality + factorization order

For causally-structured data ($x_{t+1} = f(x_t) + \epsilon$ with the converse not necessarily true; Hoyer / Janzing / Mooij et al. 2009), the **forward** prediction direction is easier than reverse. Left-to-right factorization of $P(x_1, \ldots, x_T)$ is preferred for LMs because (i) it matches reading order, (ii) lets a single LM score arbitrarily-long sequences via incremental multiplication, (iii) is statistically easier for adjacent-token prediction.

## Applications

- **Time-series forecasting** — FTSE 100 trader example, weather, energy demand.
- **[[LanguageModel|Language modeling]]** — autoregressive token prediction is the dominant LM formulation (GPT, LLaMA, character-level RNN LMs).
- **Speech / audio** — WaveNet, neural vocoders.
- **Image generation** — PixelCNN, autoregressive image transformers.

## Connections

- [[d2l-recurrent-neural-networks]] — chapter-source.
- [[MarkovModel]] — truncated-history autoregressive special case.
- [[NGram]] — the discrete-token Markov autoregressive baseline.
- [[LanguageModel]] — autoregressive LM is the dominant formulation.
- [[RNN]] / [[HiddenState]] — latent-autoregressive realization.
- [[TeacherForcing]] — training trick for autoregressive sequence models.
