---
title: "Deep RNN"
type: concept
tags: [rnn, architecture, depth]
sources: [d2l-recurrent-modern]
last_updated: 2026-05-16
---

# Deep RNN

A **multi-layer recurrent neural network** — RNN cells stacked in the depth direction, with the previous layer's output sequence becoming the next layer's input sequence ([[d2l-recurrent-modern]] §deep-rnn).

## Recurrence

With $L$ hidden layers, set $\mathbf{H}_t^{(0)} = \mathbf{X}_t$ and recurse:

$$\mathbf{H}_t^{(l)} = \phi_l(\mathbf{H}_t^{(l-1)}\mathbf{W}_\textrm{xh}^{(l)} + \mathbf{H}_{t-1}^{(l)}\mathbf{W}_\textrm{hh}^{(l)} + \mathbf{b}_\textrm{h}^{(l)}), \quad l = 1,\ldots,L.$$

Output uses only the topmost hidden state:

$$\mathbf{O}_t = \mathbf{H}_t^{(L)}\mathbf{W}_\textrm{hq} + \mathbf{b}_\textrm{q}.$$

Each layer has its own weights and biases. Two distinct flavors of depth coexist in any deep RNN: depth *across time* (the unrolled $T$-step graph) and depth *across layers* (the $L$ stacked layers). Inputs from time step 1 reach the output at time step $T$ through $L\!+\!T\!-\!1$ matrix products in the cleanest cases ([[BPTT]] gradient chain length grows accordingly).

## Practical ranges (D2L)

> "Common RNN layer widths ($h$) are in the range $(64, 2056)$, and common depths ($L$) are in the range $(1, 8)$."

## Composes with gating

Deep RNNs work identically with vanilla RNN cells, [[LSTM|LSTMs]], or [[GRU|GRUs]] — just substitute the per-layer recurrence. Frameworks expose a `num_layers` argument on `nn.RNN` / `nn.LSTM` / `nn.GRU`. [[1409.3215-seq2seq]] uses 4-layer LSTMs for both encoder and decoder; [[d2l-recurrent-modern]] §seq2seq uses multi-layer GRUs.

## See also
- [[RNN]] / [[LSTM]] / [[GRU]] — composable cell types.
- [[BidirectionalRNN]] — orthogonal architectural axis (direction).
- [[BPTT]] — gradient chain length scales with $L\cdot T$.
- [[SeqToSeq]] / [[EncoderDecoder]] — primary deployment context.
