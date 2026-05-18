---
title: "Truncated BPTT"
type: concept
tags: [optimization, rnn, training]
sources: [d2l-recurrent-neural-networks]
last_updated: 2026-05-16
---

# Truncated BPTT

Practical variants of [[BPTT|backpropagation through time]] that **terminate the chain rule after a finite number of steps** rather than computing the full $\mathcal{O}(T)$-deep gradient ([[d2l-recurrent-neural-networks]] §bptt). What every deep-learning framework actually implements.

## Three strategies

D2L distinguishes:

1. **Full computation** — sum *every* term in the BPTT expansion. Computationally infeasible for long sequences and unstable: subtle changes in initial conditions lead to disproportionate gradient changes (butterfly effect). "Almost never used in practice."

2. **Regular truncation** — terminate the sum at $\partial h_{t-\tau}/\partial w_\textrm{h}$. The standard textbook approach (Jaeger 2002). Biases the model toward short-range interactions, which is *desirable*: it acts as a regularizer that yields simpler and more stable models.

3. **Randomized truncation** (Tallec & Ollivier 2017) — replace $\partial h_t/\partial w_\textrm{h}$ with a random variable that is unbiased in expectation but truncates with probability $1-\pi_t$. Theoretically appealing (unbiased estimator), but empirically does **no better** than regular truncation — the increased variance counteracts the gradient-accuracy gains, and short-range models are what we want anyway.

## Practical realization

In framework code, truncated BPTT is typically implemented by:
- Partitioning training data into length-$n$ subsequences (`num_steps=32` in D2L's example).
- Detaching the hidden state between minibatches so gradients don't flow across boundaries.
- Running standard backprop on the unrolled $n$-step graph.

## Connections

- [[d2l-recurrent-neural-networks]] — exposition + comparison figure (§bptt).
- [[BPTT]] — the general algorithm being truncated.
- [[GradientClipping]] — companion stabilization technique.
- [[RNN]] / [[LSTM]] / [[GRU]] — architectures trained with truncated BPTT.
