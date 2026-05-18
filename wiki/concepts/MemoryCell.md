---
title: "Memory Cell"
type: concept
tags: [rnn, lstm, gating, memory]
sources: [d2l-recurrent-modern]
last_updated: 2026-05-16
---

# Memory Cell

The unit of computation introduced by [[SeppHochreiter|Hochreiter]] & [[JurgenSchmidhuber|Schmidhuber]] 1997 to replace traditional nodes in the hidden layer of an [[LSTM|LSTM]] ([[d2l-recurrent-modern]] §lstm). A memory cell is a composite node:

- An **internal state** $\mathbf{C}_t \in \mathbb{R}^{n\times h}$ with a self-connected recurrent edge of **fixed weight 1**.
- A set of **multiplicative gates** ([[InputGate]] / [[ForgetGate]] / [[OutputGate]]) that decide what to write, what to keep, and what to expose.

## Why it works

The weight-1 recurrent edge means $\partial \mathbf{C}_t / \partial \mathbf{C}_{t-1}$ contains no shrinking factor — gradients pass across many time steps without [[VanishingGradient|vanishing]]. The gates then *learn* when to flush, write, or expose the cell. From D2L: "if the forget gate is always 1 and the input gate is always 0, the memory cell internal state $\mathbf{C}_{t-1}$ will remain constant forever, passing unchanged to each subsequent time step."

## Long short-term memory

The cell is the *intermediate* memory tier in D2L's three-tier framing: weights are long-term, activations are short-term, and the cell is the *long short-term* in between — controllable persistence that defeats vanishing gradients without sacrificing learnability.

## Internal vs. visible

The cell state $\mathbf{C}_t$ is *entirely internal* to the LSTM. Only the hidden state $\mathbf{H}_t = \mathbf{O}_t \odot \tanh(\mathbf{C}_t)$ is visible to other layers. This separation lets the cell accumulate information silently and reveal it later when the output gate opens.

## See also
- [[LSTM]] — the architecture built around memory cells.
- [[InputGate]] / [[ForgetGate]] / [[OutputGate]] — the gates that regulate the cell.
- [[VanishingGradient]] — the problem the weight-1 recurrent edge solves.
- [[GRU]] — has no separate cell state; the hidden state plays both roles.
