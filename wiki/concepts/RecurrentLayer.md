---
title: "Recurrent Layer"
type: concept
tags: [neural-networks, sequence-models, rnn]
sources: [d2l-recurrent-neural-networks]
last_updated: 2026-05-16
---

# Recurrent Layer

A neural-network layer that performs the [[RNN]] recurrence

$$\mathbf{H}_t = \phi(\mathbf{X}_t \mathbf{W}_\textrm{xh} + \mathbf{H}_{t-1}\mathbf{W}_\textrm{hh} + \mathbf{b}_\textrm{h})$$

over the time axis of a sequential input, maintaining a [[HiddenState|hidden state]] between successive steps ([[d2l-recurrent-neural-networks]] §rnn).

## Framework implementations

- **PyTorch:** `nn.RNN(input_size, hidden_size, ...)` — returns `(outputs, h_n)`.
- **TensorFlow / Keras:** `tf.keras.layers.SimpleRNN(num_hiddens, return_sequences, return_state, time_major)`.
- **MXNet Gluon:** `rnn.RNN(num_hiddens)` with `begin_state(batch_size, ctx)`.
- **Flax (JAX):** no `RNNCell` for vanilla RNNs as of D2L's writing; `LSTMCell` / `GRUCell` are available.

All expose the same `(input, hidden) → (outputs, new_hidden)` contract. Underneath, the framework typically concatenates $[\mathbf{X}_t,\mathbf{H}_{t-1}]$ and uses a single matmul against stacked weights — algebraically equivalent to the two-matmul form, but kernel-friendlier.

## Connections

- [[d2l-recurrent-neural-networks]] — defines the layer math.
- [[RNN]] / [[HiddenState]] — what the layer computes / maintains.
- [[NeuralNetworkModule]] — generic block abstraction the layer subclasses.
- [[LSTM]] / [[GRU]] — gated variants of the same layer concept.
