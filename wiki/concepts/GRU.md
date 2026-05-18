---
title: "GRU"
type: concept
tags: [deep-learning, rnn, architectures]
sources: [d2l-recurrent-modern]
last_updated: 2026-05-16
---

# GRU

**Gated Recurrent Unit** — a streamlined gated RNN cell introduced by [[KyunghyunCho|Cho]] et al. 2014 (and empirically validated by Chung, Gulcehre, Cho et al. 2014). Designed to retain the [[LSTM|LSTM]]'s ability to mitigate [[VanishingGradient|vanishing gradients]] while reducing parameter count and computation: 2 gates instead of 3, *no separate cell state* ([[d2l-recurrent-modern]] §gru).

## Architecture (D2L formulation)

For input $\mathbf{X}_t\in\mathbb{R}^{n\times d}$ and previous hidden state $\mathbf{H}_{t-1}\in\mathbb{R}^{n\times h}$:

- **[[ResetGate|Reset gate]]** $\mathbf{R}_t = \sigma(\mathbf{X}_t\mathbf{W}_\textrm{xr} + \mathbf{H}_{t-1}\mathbf{W}_\textrm{hr} + \mathbf{b}_\textrm{r})$ — how much of the previous state to remember when computing the candidate.
- **[[UpdateGate|Update gate]]** $\mathbf{Z}_t = \sigma(\mathbf{X}_t\mathbf{W}_\textrm{xz} + \mathbf{H}_{t-1}\mathbf{W}_\textrm{hz} + \mathbf{b}_\textrm{z})$ — how much of the new candidate vs. the old state to keep.
- **Candidate hidden state** $\tilde{\mathbf{H}}_t = \tanh(\mathbf{X}_t\mathbf{W}_\textrm{xh} + (\mathbf{R}_t\odot \mathbf{H}_{t-1})\mathbf{W}_\textrm{hh} + \mathbf{b}_\textrm{h})$.
- **Final update (convex combination)** $\mathbf{H}_t = \mathbf{Z}_t\odot \mathbf{H}_{t-1} + (1-\mathbf{Z}_t)\odot \tilde{\mathbf{H}}_t$.

When $\mathbf{R}_t\!\to\!1$ the candidate reduces to a vanilla RNN update; when $\mathbf{R}_t\!\to\!0$ the candidate is a pure MLP on $\mathbf{X}_t$ (history reset). When $\mathbf{Z}_t\!\to\!1$ the unit skips time step $t$ (information from $\mathbf{X}_t$ is ignored); when $\mathbf{Z}_t\!\to\!0$ the unit fully adopts the new candidate.

## Mnemonic (D2L)

> "Reset gates help capture short-term dependencies in sequences. Update gates help capture long-term dependencies in sequences."

## GRU vs LSTM

- **Parameters / compute.** GRU has 3 weight triples (reset / update / candidate) vs LSTM's 4 (input / forget / output / candidate) — ~25% fewer parameters per cell. Faster to compute.
- **Cell state.** GRU has no separate cell state $\mathbf{C}_t$ — its hidden state $\mathbf{H}_t$ serves both roles.
- **Accuracy.** Chung et al. 2014 found GRU and LSTM "comparable" on standard sequence-modeling benchmarks; the choice is often dataset- and hyperparameter-dependent.
- **D2L's [[SeqToSeq|seq2seq]] implementation uses a GRU encoder + decoder** ([[d2l-recurrent-modern]] §seq2seq) — typical of modern textbook expositions that favor GRU's compactness.

## See also
- [[LSTM]] — the gated-RNN predecessor.
- [[RNN]] — the vanilla recurrence GRU fixes.
- [[ResetGate]] / [[UpdateGate]] — internal components.
- [[DeepRNN]] / [[BidirectionalRNN]] — composable with GRU.
- [[SeqToSeq]] / [[EncoderDecoder]] — D2L's GRU-based seq2seq MT implementation.
- [[Transformer]] — the architecture that has largely supplanted both GRU and LSTM.
