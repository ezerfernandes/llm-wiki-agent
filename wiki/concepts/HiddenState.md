---
title: "Hidden State"
type: concept
tags: [neural-networks, sequence-models, rnn]
sources: [d2l-recurrent-neural-networks]
last_updated: 2026-05-16
---

# Hidden State

The persistent **memory** variable of an [[RNN]] (or any latent-variable sequence model). At time step $t$, $\mathbf{H}_t$ is a function of the current input $\mathbf{X}_t$ *and* the previous hidden state $\mathbf{H}_{t-1}$, so it captures and retains the sequence's historical information ([[d2l-recurrent-neural-networks]] §rnn).

## Definition

$$\mathbf{H}_t = \phi(\mathbf{X}_t \mathbf{W}_\textrm{xh} + \mathbf{H}_{t-1}\mathbf{W}_\textrm{hh} + \mathbf{b}_\textrm{h}).$$

The same $(\mathbf{W}_\textrm{xh},\mathbf{W}_\textrm{hh},\mathbf{b}_\textrm{h})$ are reused at every step — parameter count is independent of sequence length.

## Hidden state ≠ hidden layer

- A **hidden layer** is a fixed-shape intermediate computation in the input-to-output path of a *single* forward pass.
- A **hidden state** is technically an *input* to whatever happens at a given step; it can only be computed by looking at data at *previous* time steps. It is the network's persistent memory.

## Generalizations

- [[LSTM]] adds a *cell state* alongside the hidden state with multiplicative gates.
- [[GRU]] merges the two using reset/update gates.
- [[Transformer]] dispenses with hidden state entirely, attending to all positions in parallel.

## Connections

- [[d2l-recurrent-neural-networks]] — definitional source.
- [[RNN]] / [[RecurrentLayer]] — where hidden states live.
- [[LSTM]] / [[GRU]] — gated variants that protect $\mathbf{H}_t$ from vanishing gradients.
- [[BPTT]] — gradient flows through the chain $\mathbf{H}_T \to \mathbf{H}_{T-1} \to \ldots \to \mathbf{H}_1$.
- [[AutoregressiveModel]] — latent-autoregressive models with summary $h_t$.
